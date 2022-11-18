# NEU自然语言处理课程任务

## 任务一、Skip_Gram

## 任务二、RNN、DRNN

### 单层RNN

利用nn.Linear、nn.Parameter实现了单层RNN

1_layer_rnnlm_with_penn_assignment.py为code

1_layer_rnnlm_train_and_test_process.ipynb利用jupyter记录训练及测试过程，共60epoch，每20个epoch生成一个checkpoint

1_layer_rnnlm_train_and_test_process.mb转jupyter训练及测试过程为markdown版

checkpoint保存在models中，格式为1_layer_rnnlm_model_epoch*.ckpt

### DRNN

利用nn.Linear、nn.Parameter实现了一个自定义层数的DRNN，默认为3

n_layers_rnnlm_with_penn_assignment(default_n=3).py为code

n_layers_rnnlm_train_and_test_process(default_n=3).ipynb利用jupyter记录训练及测试过程，共60epoch，每20个epoch生成一个checkpoint

n_layers_rnnlm_train_and_test_process(default_n=3).mb转jupyter训练及测试过程为markdown版

checkpoint保存在models中，格式为3_layers_rnnlm_model_epoch*.ckpt

## 任务三、LSTM

### 单层LSTM

1、利用nn.Linear、nn.Parameter实现了单层RNN，

2、一并实现了pytorch_api版本作对比，发现除训练速度有差距外，其余差距不大

1_layer_lstmlm_with_penn_assignment.py为code

1_layer_lstmlm_train_and_test_process.ipynb利用jupyter记录训练及测试过程，共60epoch，每20个epoch生成一个checkpoint

1_layer_lstmlm_train_and_test_process.mb转jupyter训练及测试过程为markdown版

checkpoint保存在models中，格式为1_layer_lstmlm_model_epoch*.ckpt

### 多层LSTM

1、利用nn.Linear、nn.Parameter实现了一个自定义层数的LSTM，默认为2

2、一并实现了pytorch_api版本作对比，发现除训练速度有差距外，其余差距不大

3、将自己实现的多层LSTM，每层hidden_size由固定5改为input_size/2，本例中， 第0层hidden_size=emb_size/2=64， 第1层hidden_size=64/2=32

共三份代码：

n_layers_lstmlm_with_penn_assignment(default_n=2_hidden=5).py

n_layers_lstmlm_with_penn_assignment(default_n=2).py

n_layers_lstmlm_with_penn_assignment(default_n=2_hidden=0.5input).py

均利用jupyter记录训练及测试过程，并生成markdown版，共100epoch，每20个epoch生成一个checkpoint
