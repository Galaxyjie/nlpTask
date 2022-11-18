import math
import torch
import torch.nn as nn
import torch.optim as optim
import give_valid_test

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# device = torch.device("cpu")


def make_batch(train_path, word2number_dict, batch_size, n_step):
    all_input_batch = []
    all_target_batch = []

    text = open(train_path, "r", encoding="utf-8")  # open the file

    input_batch = []
    target_batch = []
    for sen in text:
        word = sen.strip().split(" ")  # space tokenizer

        if len(word) <= n_step:  # pad the sentence
            word = ["<pad>"] * (n_step + 1 - len(word)) + word

        for word_index in range(len(word) - n_step):
            input = [
                word2number_dict[n] for n in word[word_index : word_index + n_step]
            ]  # create (1~n-1) as input
            target = word2number_dict[
                word[word_index + n_step]
            ]  # create (n) as target, We usually call this 'casual language model'
            input_batch.append(input)
            target_batch.append(target)

            if len(input_batch) == batch_size:
                all_input_batch.append(input_batch)
                all_target_batch.append(target_batch)
                input_batch = []
                target_batch = []

    return all_input_batch, all_target_batch


def make_dict(train_path):
    text = open(train_path, "r", encoding="utf-8")  # open the train file
    word_list = set()  # a set for making dict

    for line in text:
        line = line.strip().split(" ")
        word_list = word_list.union(set(line))

    word_list = list(sorted(word_list))  # set to list

    word2number_dict = {w: i + 2 for i, w in enumerate(word_list)}
    number2word_dict = {i + 2: w for i, w in enumerate(word_list)}

    # add the <pad> and <unk_word>
    word2number_dict["<pad>"] = 0
    number2word_dict[0] = "<pad>"
    word2number_dict["<unk_word>"] = 1
    number2word_dict[1] = "<unk_word>"

    return word2number_dict, number2word_dict


class TextLSTM(nn.Module):
    def __init__(self):
        super().__init__()
        self.C = nn.Embedding(n_class, embedding_dim=emb_size)
        self.LSTM = nn.LSTM(
            input_size=emb_size, hidden_size=n_hidden, num_layers=num_layer
        )
        self.W = nn.Linear(n_hidden, n_class, bias=False)
        self.b = nn.Parameter(torch.ones([n_class]))

    def forward(self, X):
        X = self.C(X)
        X = X.transpose(0, 1)  # X : [n_step, batch_size, embeding size]
        outputs, (_, _) = self.LSTM(X)
        outputs = outputs[-1]  # [batch_size, num_directions(=1) * n_hidden]
        model = self.W(outputs) + self.b  # model : [batch_size, n_class]
        return model


def train_lstmlm():
    model = TextLSTM()
    model.to(device)
    print(model)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learn_rate)

    # Training
    best_loss = 100
    batch_number = len(all_input_batch)
    for epoch in range(all_epoch):
        count_batch = 0
        for input_batch, target_batch in zip(all_input_batch, all_target_batch):
            optimizer.zero_grad()

            # input_batch : [batch_size, n_step, n_class]
            output = model(input_batch)

            # output : [batch_size, n_class], target_batch : [batch_size] (LongTensor, not one-hot)
            loss = criterion(output, target_batch)
            ppl = math.exp(loss.item())
            if (count_batch + 1) % 50 == 0:
                print(
                    "Epoch:",
                    "%04d" % (epoch + 1),
                    "Batch:",
                    "%02d" % (count_batch + 1),
                    f"/{batch_number}",
                    "lost =",
                    "{:.6f}".format(loss),
                    "ppl =",
                    "{:.6}".format(ppl),
                )

            loss.backward()
            optimizer.step()

            count_batch += 1

        # valid after training one epoch
        all_valid_batch, all_valid_target = give_valid_test.give_valid(
            word2number_dict, n_step
        )
        all_valid_batch = torch.LongTensor(all_valid_batch).to(device)  # list to tensor
        all_valid_target = torch.LongTensor(all_valid_target).to(device)

        total_valid = len(all_valid_target) * 128
        with torch.no_grad():
            total_loss = 0
            count_loss = 0
            for valid_batch, valid_target in zip(all_valid_batch, all_valid_target):
                valid_output = model(valid_batch)
                valid_loss = criterion(valid_output, valid_target)
                total_loss += valid_loss.item()
                count_loss += 1

            print(
                f"Valid {total_valid} samples after epoch:",
                "%04d" % (epoch + 1),
                "lost =",
                "{:.6f}".format(total_loss / count_loss),
                "ppl =",
                "{:.6}".format(math.exp(total_loss / count_loss)),
            )
        if total_loss / count_loss < best_loss:
            best_loss = total_loss / count_loss
            print("Saving best model")
            torch.save(
                model, f"models/(pytorch_api){num_layer}_layers_lstmlm_model_best.ckpt"
            )
        if (epoch + 1) % save_checkpoint_epoch == 0:
            torch.save(
                model,
                f"models/(pytorch_api){num_layer}_layers_lstmlm_model_epoch{epoch+1}.ckpt",
            )


def test_lstmlm(select_model_path):
    model = torch.load(select_model_path)  # load the selected model
    model.to(device)

    # load the test data
    all_test_batch, all_test_target = give_valid_test.give_test(
        word2number_dict, n_step
    )
    all_test_batch = torch.LongTensor(all_test_batch).to(device)  # list to tensor
    all_test_target = torch.LongTensor(all_test_target).to(device)

    total_test = len(all_test_target) * 128
    model.eval()
    criterion = nn.CrossEntropyLoss()
    total_loss = 0
    count_loss = 0
    for test_batch, test_target in zip(all_test_batch, all_test_target):
        test_output = model(test_batch)
        test_loss = criterion(test_output, test_target)
        total_loss += test_loss.item()
        count_loss += 1

    print(f"Test {total_test} samples with {select_model_path}……………………")
    print(
        "lost =",
        "{:.6f}".format(total_loss / count_loss),
        "ppl =",
        "{:.6}".format(math.exp(total_loss / count_loss)),
    )


if __name__ == "__main__":
    num_layer = 2
    n_step = 5  # number of cells(= number of Step)
    n_hidden = 5  # number of hidden units in one cell
    batch_size = 512  # batch size
    learn_rate = 0.001
    all_epoch = 100  # the all epoch for training
    emb_size = 128  # embeding size
    save_checkpoint_epoch = 20  # save a checkpoint per save_checkpoint_epoch epochs
    train_path = "data/train.txt"  # the path of train dataset

    word2number_dict, number2word_dict = make_dict(
        train_path
    )  # use the make_dict function to make the dict
    print("The size of the dictionary is:", len(word2number_dict))

    n_class = len(word2number_dict)  # n_class (= dict size)

    all_input_batch, all_target_batch = make_batch(
        train_path, word2number_dict, batch_size, n_step
    )  # make the batch
    print("The number of the train batch is:", len(all_input_batch))

    all_input_batch = torch.LongTensor(all_input_batch).to(device)  # list to tensor
    all_target_batch = torch.LongTensor(all_target_batch).to(device)

    print("\nTrain the LSTMLM……………………")
    train_lstmlm()

    print("\nTest the LSTMLM……………………")
    select_model_path = f"models/(pytorch_api){num_layer}_layers_lstmlm_model_best.ckpt"
    test_lstmlm(select_model_path)
