import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset
from torch.nn.utils.rnn import pad_sequence
from tqdm.auto import tqdm
from utils import BOS_TOKEN, EOS_TOKEN, PAD_TOKEN
from utils import load_reuters, save_pretrained, get_loader, init_weights


class Skip_Gram_Dataset(Dataset):
    def __init__(self, corpus, vocab, context_size=2):
        self.data = []
        self.bos = vocab[BOS_TOKEN]
        self.eos = vocab[EOS_TOKEN]
        for sentence in tqdm(corpus, desc="Dataset Construction"):
            sentence = [self.bos] + sentence + [self.eos]
            # 如句子长度不足以构建（当前词、目标上下文）训练样本，则跳过
            if len(sentence) < context_size * 2 + 1:
                continue
            for i in range(context_size, len(sentence) - context_size):
                # 模型输入：当前词
                current_word = sentence[i]
                # 模型输出：左右分别取context_size长度的上下文
                for j in range(i - context_size, i + context_size + 1):
                    if j == i:
                        continue
                    target = sentence[j]
                    self.data.append((current_word, target))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, i):
        return self.data[i]

    def collate_fn(self, examples):
        inputs = torch.tensor([ex[0] for ex in examples])
        targets = torch.tensor([ex[1] for ex in examples])
        return (inputs, targets)


class Skip_Gram_Model(nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super(Skip_Gram_Model, self).__init__()
        # 词嵌入层 提示：nn.Embedding
        self.embeddings = nn.Embedding(vocab_size, embedding_dim)
        # 线性变换：隐含层->输出层 提示：nn.Linear
        self.output = nn.Linear(embedding_dim, vocab_size)
        init_weights(self)

    def forward(self, inputs):
        embeds = self.embeddings(inputs)
        output = self.output(embeds)
        log_probs = F.log_softmax(output, dim=1)
        return log_probs  # log_probs是概率分布


embedding_dim = 64
context_size = 2
batch_size = 1024
num_epoch = 10

# 读取文本数据，构建Skip_Gram模型训练数据集
corpus, vocab = load_reuters()
dataset = Skip_Gram_Dataset(corpus, vocab, context_size=context_size)
data_loader = get_loader(dataset, batch_size)

nll_loss = nn.NLLLoss()
# 构建Skip_Gram模型，并加载至device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = Skip_Gram_Model(len(vocab), embedding_dim)
model.to(device)
optimizer = optim.Adam(model.parameters(), lr=0.02)

model.train()
for epoch in range(1, num_epoch + 1):
    total_loss = 0
    for batch in tqdm(data_loader, desc=f"Training Epoch {epoch}"):
        inputs, targets = [x.to(device) for x in batch]
        optimizer.zero_grad()
        log_probs = model(inputs)
        loss = nll_loss(log_probs, targets)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    if epoch % 1 == 0:
        # 保存词向量（model.embeddings）
        save_pretrained(
            vocab, model.embeddings.weight.data, "data/skip_gram.vec" + str(epoch)
        )
    print(f"Loss: {total_loss:.2f}")
