from utils import load_reuters

corpus, vocab = load_reuters()

if corpus is not None and vocab is not None:
    print("success!")
else:
    print("failed~")