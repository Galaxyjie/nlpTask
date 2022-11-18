import torch.nn as nn
import torch

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


def get_three_weight(input_size, hidden_size):
    return [
        nn.Linear(input_size, hidden_size, bias=False).to(device),
        nn.Linear(hidden_size, hidden_size, bias=False).to(device),
    ]


a = get_three_weight(2, 1)
print(a)


w_i = [None] * 10

w_i[0] = a
print(w_i)
