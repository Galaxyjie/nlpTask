# NEU自然语言处理课程任务

## 任务一、Skip_Gram

把cbow.py修改为Skip_Gram模型

## 任务二、RNN、DRNN

### 单层RNN

利用nn.Linear、nn.Parameter实现了单层RNN

### DRNN

利用nn.Linear、nn.Parameter实现了一个自定义层数的DRNN，默认为3

### 文件结构

#### code

1_layer_rnnlm_with_penn_assignment.py为RNN模型定义及训练测试方法

n_layers_rnnlm_with_penn_assignment(default_n=3).py为DRNN模型定义及训练测试方法，默认3层

#### 训练及测试过程

每份代码均对应jupyter和markdown版本的训练及测试过程，内容完全相同

*_layer(s)_rnnlm_train_and_test_process.ipynb利用jupyter记录训练及测试过程，共150epoch，每50个epoch生成一个checkpoint

*_layer(s)_rnnlm_train_and_test_process.mb转jupyter训练及测试过程为markdown版

#### best_model及checkpoints

训练部分添加了根据valid_loss保存best_model，最后测试的时候用best_model进行测试

best_model保存在models文件夹中，格式为*_layer(s)_rnnlm_model_best.ckpt

checkpoint保存在models文件夹中，格式为*_layer(s)_rnnlm_model_epoch*.ckpt

## 任务三、LSTM

### 单层LSTM

1、利用nn.Linear、nn.Parameter实现了单层RNN，

2、一并实现了pytorch_api版本作对比，发现除训练速度有差距外，其余差距不大

### 多层LSTM

1、利用nn.Linear、nn.Parameter实现了一个自定义层数的LSTM，默认为2

2、一并实现了pytorch_api版本作对比，发现除训练速度有差距外，其余差距不大

3、将自己实现的多层LSTM，每层hidden_size由固定5改为input_size/2，本例中， 第0层hidden_size=emb_size/2=64， 第1层hidden_size=64/2=32

## 文件结构

#### code

1_layer_lstmlm_with_penn_assignment.py为单层lstm模型定义及训练测试方法

(pytorch_api)1_layer_lstmlm_with_penn_assignment.py为使用pytorch api实现的单层lstm模型定义及训练测试方法

n_layers_lstmlm_with_penn_assignment(default_n=2_hidden=5).py为自定义n层lstm模型定义及训练测试方法，默认2层

(pytorch_api)n_layers_lstmlm_with_penn_assignment(default_n=2).py为使用pytorch api实现的自定义n层lstm模型定义及训练测试方法，默认2层

n_layers_lstmlm_with_penn_assignment(default_n=2_hidden=0.5input).py为自定义n层lstm模型定义及训练测试方法，默认2层，其中隐状态的size为该层输入的一半

#### 训练及测试过程

每份代码均对应jupyter和markdown版本的训练及测试过程，内容完全相同

*_layer(s)_lstmlm_train_and_test_process.ipynb利用jupyter记录训练及测试过程，共150epoch，每50个epoch生成一个checkpoint

*_layer(s)_lstmlm_train_and_test_process.mb转jupyter训练及测试过程为markdown版

#### best_model及checkpoints

训练部分添加了根据valid_loss保存best_model，最后测试的时候用best_model进行测试

best_model保存在models文件夹中，格式为*_layer(s)_lstmlm_model_best.ckpt

checkpoint保存在models文件夹中，格式为*_layer(s)_lstmlm_model_epoch*.ckpt
