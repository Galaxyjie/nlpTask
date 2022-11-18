```python
!python 1_layer_lstmlm_with_penn_assignment.py
```

    The size of the dictionary is: 7613
    The number of the train batch is: 134
    
    Train the LSTMLM……………………
    TextLSTM(
      (embedding): Embedding(7613, 128)
      (W_xi): Linear(in_features=128, out_features=5, bias=False)
      (W_hi): Linear(in_features=5, out_features=5, bias=False)
      (W_xf): Linear(in_features=128, out_features=5, bias=False)
      (W_hf): Linear(in_features=5, out_features=5, bias=False)
      (W_xo): Linear(in_features=128, out_features=5, bias=False)
      (W_ho): Linear(in_features=5, out_features=5, bias=False)
      (W_xc): Linear(in_features=128, out_features=5, bias=False)
      (W_hc): Linear(in_features=5, out_features=5, bias=False)
      (W_hq): Linear(in_features=5, out_features=7613, bias=False)
      (sigmoid): Sigmoid()
      (tanh): Tanh()
    )
    Epoch: 0001 Batch: 50 /134 lost = 8.824258 ppl = 6797.14
    Epoch: 0001 Batch: 100 /134 lost = 8.656797 ppl = 5749.09
    Valid 4864 samples after epoch: 0001 lost = 8.540380 ppl = 5117.29
    Epoch: 0002 Batch: 50 /134 lost = 8.245525 ppl = 3810.54
    Epoch: 0002 Batch: 100 /134 lost = 7.993659 ppl = 2962.12
    Valid 4864 samples after epoch: 0002 lost = 7.880550 ppl = 2645.33
    Epoch: 0003 Batch: 50 /134 lost = 7.591721 ppl = 1981.72
    Epoch: 0003 Batch: 100 /134 lost = 7.421226 ppl = 1671.08
    Valid 4864 samples after epoch: 0003 lost = 7.387445 ppl = 1615.57
    Epoch: 0004 Batch: 50 /134 lost = 7.145610 ppl = 1268.52
    Epoch: 0004 Batch: 100 /134 lost = 7.033770 ppl = 1134.3
    Valid 4864 samples after epoch: 0004 lost = 7.067046 ppl = 1172.68
    Epoch: 0005 Batch: 50 /134 lost = 6.852508 ppl = 946.251
    Epoch: 0005 Batch: 100 /134 lost = 6.776700 ppl = 877.169
    Valid 4864 samples after epoch: 0005 lost = 6.863941 ppl = 957.132
    Epoch: 0006 Batch: 50 /134 lost = 6.664553 ppl = 784.113
    Epoch: 0006 Batch: 100 /134 lost = 6.611402 ppl = 743.525
    Valid 4864 samples after epoch: 0006 lost = 6.742559 ppl = 847.727
    Epoch: 0007 Batch: 50 /134 lost = 6.550802 ppl = 699.805
    Epoch: 0007 Batch: 100 /134 lost = 6.513348 ppl = 674.079
    Valid 4864 samples after epoch: 0007 lost = 6.673801 ppl = 791.398
    Epoch: 0008 Batch: 50 /134 lost = 6.483765 ppl = 654.43
    Epoch: 0008 Batch: 100 /134 lost = 6.453996 ppl = 635.236
    Valid 4864 samples after epoch: 0008 lost = 6.638171 ppl = 763.697
    Epoch: 0009 Batch: 50 /134 lost = 6.442491 ppl = 627.969
    Epoch: 0009 Batch: 100 /134 lost = 6.414435 ppl = 610.596
    Valid 4864 samples after epoch: 0009 lost = 6.621698 ppl = 751.22
    Epoch: 0010 Batch: 50 /134 lost = 6.417836 ppl = 612.676
    Epoch: 0010 Batch: 100 /134 lost = 6.390572 ppl = 596.197
    Valid 4864 samples after epoch: 0010 lost = 6.613657 ppl = 745.203
    Epoch: 0011 Batch: 50 /134 lost = 6.398376 ppl = 600.868
    Epoch: 0011 Batch: 100 /134 lost = 6.374703 ppl = 586.811
    Valid 4864 samples after epoch: 0011 lost = 6.608922 ppl = 741.683
    Epoch: 0012 Batch: 50 /134 lost = 6.379189 ppl = 589.45
    Epoch: 0012 Batch: 100 /134 lost = 6.358181 ppl = 577.195
    Valid 4864 samples after epoch: 0012 lost = 6.603852 ppl = 737.932
    Epoch: 0013 Batch: 50 /134 lost = 6.362583 ppl = 579.742
    Epoch: 0013 Batch: 100 /134 lost = 6.346332 ppl = 570.397
    Valid 4864 samples after epoch: 0013 lost = 6.602245 ppl = 736.747
    Epoch: 0014 Batch: 50 /134 lost = 6.346906 ppl = 570.724
    Epoch: 0014 Batch: 100 /134 lost = 6.336334 ppl = 564.722
    Valid 4864 samples after epoch: 0014 lost = 6.599161 ppl = 734.479
    Epoch: 0015 Batch: 50 /134 lost = 6.333001 ppl = 562.843
    Epoch: 0015 Batch: 100 /134 lost = 6.324838 ppl = 558.267
    Valid 4864 samples after epoch: 0015 lost = 6.596893 ppl = 732.815
    Epoch: 0016 Batch: 50 /134 lost = 6.319150 ppl = 555.101
    Epoch: 0016 Batch: 100 /134 lost = 6.312155 ppl = 551.232
    Valid 4864 samples after epoch: 0016 lost = 6.595447 ppl = 731.756
    Epoch: 0017 Batch: 50 /134 lost = 6.306520 ppl = 548.134
    Epoch: 0017 Batch: 100 /134 lost = 6.302832 ppl = 546.116
    Valid 4864 samples after epoch: 0017 lost = 6.594765 ppl = 731.257
    Epoch: 0018 Batch: 50 /134 lost = 6.296320 ppl = 542.572
    Epoch: 0018 Batch: 100 /134 lost = 6.294282 ppl = 541.467
    Valid 4864 samples after epoch: 0018 lost = 6.593688 ppl = 730.47
    Epoch: 0019 Batch: 50 /134 lost = 6.287590 ppl = 537.855
    Epoch: 0019 Batch: 100 /134 lost = 6.285176 ppl = 536.559
    Valid 4864 samples after epoch: 0019 lost = 6.593664 ppl = 730.452
    Epoch: 0020 Batch: 50 /134 lost = 6.278728 ppl = 533.11
    Epoch: 0020 Batch: 100 /134 lost = 6.267052 ppl = 526.922
    Valid 4864 samples after epoch: 0020 lost = 6.587524 ppl = 725.981
    Epoch: 0021 Batch: 50 /134 lost = 6.266686 ppl = 526.729
    Epoch: 0021 Batch: 100 /134 lost = 6.251970 ppl = 519.034
    Valid 4864 samples after epoch: 0021 lost = 6.581628 ppl = 721.714
    Epoch: 0022 Batch: 50 /134 lost = 6.253738 ppl = 519.953
    Epoch: 0022 Batch: 100 /134 lost = 6.239814 ppl = 512.763
    Valid 4864 samples after epoch: 0022 lost = 6.578639 ppl = 719.56
    Epoch: 0023 Batch: 50 /134 lost = 6.243494 ppl = 514.654
    Epoch: 0023 Batch: 100 /134 lost = 6.227950 ppl = 506.715
    Valid 4864 samples after epoch: 0023 lost = 6.575007 ppl = 716.951
    Epoch: 0024 Batch: 50 /134 lost = 6.232740 ppl = 509.149
    Epoch: 0024 Batch: 100 /134 lost = 6.214324 ppl = 499.858
    Valid 4864 samples after epoch: 0024 lost = 6.571562 ppl = 714.485
    Epoch: 0025 Batch: 50 /134 lost = 6.221824 ppl = 503.621
    Epoch: 0025 Batch: 100 /134 lost = 6.200539 ppl = 493.015
    Valid 4864 samples after epoch: 0025 lost = 6.564885 ppl = 709.73
    Epoch: 0026 Batch: 50 /134 lost = 6.207530 ppl = 496.473
    Epoch: 0026 Batch: 100 /134 lost = 6.185026 ppl = 485.426
    Valid 4864 samples after epoch: 0026 lost = 6.558913 ppl = 705.504
    Epoch: 0027 Batch: 50 /134 lost = 6.194526 ppl = 490.059
    Epoch: 0027 Batch: 100 /134 lost = 6.169537 ppl = 477.965
    Valid 4864 samples after epoch: 0027 lost = 6.553832 ppl = 701.928
    Epoch: 0028 Batch: 50 /134 lost = 6.181470 ppl = 483.703
    Epoch: 0028 Batch: 100 /134 lost = 6.154232 ppl = 470.705
    Valid 4864 samples after epoch: 0028 lost = 6.547965 ppl = 697.823
    Epoch: 0029 Batch: 50 /134 lost = 6.166596 ppl = 476.561
    Epoch: 0029 Batch: 100 /134 lost = 6.138452 ppl = 463.336
    Valid 4864 samples after epoch: 0029 lost = 6.541824 ppl = 693.551
    Epoch: 0030 Batch: 50 /134 lost = 6.151744 ppl = 469.536
    Epoch: 0030 Batch: 100 /134 lost = 6.121571 ppl = 455.58
    Valid 4864 samples after epoch: 0030 lost = 6.537017 ppl = 690.225
    Epoch: 0031 Batch: 50 /134 lost = 6.137289 ppl = 462.797
    Epoch: 0031 Batch: 100 /134 lost = 6.103675 ppl = 447.499
    Valid 4864 samples after epoch: 0031 lost = 6.531952 ppl = 686.737
    Epoch: 0032 Batch: 50 /134 lost = 6.123753 ppl = 456.575
    Epoch: 0032 Batch: 100 /134 lost = 6.085927 ppl = 439.627
    Valid 4864 samples after epoch: 0032 lost = 6.528068 ppl = 684.075
    Epoch: 0033 Batch: 50 /134 lost = 6.110109 ppl = 450.388
    Epoch: 0033 Batch: 100 /134 lost = 6.067183 ppl = 431.463
    Valid 4864 samples after epoch: 0033 lost = 6.524169 ppl = 681.413
    Epoch: 0034 Batch: 50 /134 lost = 6.094755 ppl = 443.525
    Epoch: 0034 Batch: 100 /134 lost = 6.045041 ppl = 422.015
    Valid 4864 samples after epoch: 0034 lost = 6.520373 ppl = 678.832
    Epoch: 0035 Batch: 50 /134 lost = 6.079645 ppl = 436.874
    Epoch: 0035 Batch: 100 /134 lost = 6.021378 ppl = 412.146
    Valid 4864 samples after epoch: 0035 lost = 6.513931 ppl = 674.473
    Epoch: 0036 Batch: 50 /134 lost = 6.064476 ppl = 430.297
    Epoch: 0036 Batch: 100 /134 lost = 6.002356 ppl = 404.38
    Valid 4864 samples after epoch: 0036 lost = 6.507225 ppl = 669.965
    Epoch: 0037 Batch: 50 /134 lost = 6.050610 ppl = 424.372
    Epoch: 0037 Batch: 100 /134 lost = 5.985642 ppl = 397.678
    Valid 4864 samples after epoch: 0037 lost = 6.503178 ppl = 667.259
    Epoch: 0038 Batch: 50 /134 lost = 6.035222 ppl = 417.892
    Epoch: 0038 Batch: 100 /134 lost = 5.967712 ppl = 390.611
    Valid 4864 samples after epoch: 0038 lost = 6.499513 ppl = 664.818
    Epoch: 0039 Batch: 50 /134 lost = 6.021108 ppl = 412.035
    Epoch: 0039 Batch: 100 /134 lost = 5.950723 ppl = 384.031
    Valid 4864 samples after epoch: 0039 lost = 6.496366 ppl = 662.729
    Epoch: 0040 Batch: 50 /134 lost = 6.006785 ppl = 406.175
    Epoch: 0040 Batch: 100 /134 lost = 5.934714 ppl = 377.932
    Valid 4864 samples after epoch: 0040 lost = 6.494744 ppl = 661.655
    Epoch: 0041 Batch: 50 /134 lost = 5.991971 ppl = 400.203
    Epoch: 0041 Batch: 100 /134 lost = 5.919763 ppl = 372.323
    Valid 4864 samples after epoch: 0041 lost = 6.492823 ppl = 660.385
    Epoch: 0042 Batch: 50 /134 lost = 5.977656 ppl = 394.515
    Epoch: 0042 Batch: 100 /134 lost = 5.904053 ppl = 366.52
    Valid 4864 samples after epoch: 0042 lost = 6.490290 ppl = 658.714
    Epoch: 0043 Batch: 50 /134 lost = 5.961344 ppl = 388.131
    Epoch: 0043 Batch: 100 /134 lost = 5.887821 ppl = 360.619
    Valid 4864 samples after epoch: 0043 lost = 6.488092 ppl = 657.268
    Epoch: 0044 Batch: 50 /134 lost = 5.946574 ppl = 382.441
    Epoch: 0044 Batch: 100 /134 lost = 5.872280 ppl = 355.058
    Valid 4864 samples after epoch: 0044 lost = 6.486173 ppl = 656.008
    Epoch: 0045 Batch: 50 /134 lost = 5.931784 ppl = 376.826
    Epoch: 0045 Batch: 100 /134 lost = 5.857608 ppl = 349.886
    Valid 4864 samples after epoch: 0045 lost = 6.485707 ppl = 655.702
    Epoch: 0046 Batch: 50 /134 lost = 5.919557 ppl = 372.247
    Epoch: 0046 Batch: 100 /134 lost = 5.843998 ppl = 345.157
    Valid 4864 samples after epoch: 0046 lost = 6.484150 ppl = 654.682
    Epoch: 0047 Batch: 50 /134 lost = 5.905225 ppl = 366.95
    Epoch: 0047 Batch: 100 /134 lost = 5.830599 ppl = 340.563
    Valid 4864 samples after epoch: 0047 lost = 6.482784 ppl = 653.788
    Epoch: 0048 Batch: 50 /134 lost = 5.892150 ppl = 362.183
    Epoch: 0048 Batch: 100 /134 lost = 5.817906 ppl = 336.267
    Valid 4864 samples after epoch: 0048 lost = 6.483300 ppl = 654.126
    Epoch: 0049 Batch: 50 /134 lost = 5.880178 ppl = 357.873
    Epoch: 0049 Batch: 100 /134 lost = 5.805678 ppl = 332.18
    Valid 4864 samples after epoch: 0049 lost = 6.482679 ppl = 653.72
    Epoch: 0050 Batch: 50 /134 lost = 5.867099 ppl = 353.223
    Epoch: 0050 Batch: 100 /134 lost = 5.793255 ppl = 328.079
    Valid 4864 samples after epoch: 0050 lost = 6.482539 ppl = 653.628
    Epoch: 0051 Batch: 50 /134 lost = 5.853512 ppl = 348.456
    Epoch: 0051 Batch: 100 /134 lost = 5.780609 ppl = 323.956
    Valid 4864 samples after epoch: 0051 lost = 6.483889 ppl = 654.512
    Epoch: 0052 Batch: 50 /134 lost = 5.839657 ppl = 343.661
    Epoch: 0052 Batch: 100 /134 lost = 5.768507 ppl = 320.059
    Valid 4864 samples after epoch: 0052 lost = 6.483797 ppl = 654.451
    Epoch: 0053 Batch: 50 /134 lost = 5.827950 ppl = 339.661
    Epoch: 0053 Batch: 100 /134 lost = 5.755715 ppl = 315.991
    Valid 4864 samples after epoch: 0053 lost = 6.485705 ppl = 655.701
    Epoch: 0054 Batch: 50 /134 lost = 5.816690 ppl = 335.859
    Epoch: 0054 Batch: 100 /134 lost = 5.744796 ppl = 312.56
    Valid 4864 samples after epoch: 0054 lost = 6.486537 ppl = 656.247
    Epoch: 0055 Batch: 50 /134 lost = 5.805280 ppl = 332.048
    Epoch: 0055 Batch: 100 /134 lost = 5.730616 ppl = 308.159
    Valid 4864 samples after epoch: 0055 lost = 6.487991 ppl = 657.201
    Epoch: 0056 Batch: 50 /134 lost = 5.789485 ppl = 326.845
    Epoch: 0056 Batch: 100 /134 lost = 5.714815 ppl = 303.328
    Valid 4864 samples after epoch: 0056 lost = 6.485968 ppl = 655.873
    Epoch: 0057 Batch: 50 /134 lost = 5.776824 ppl = 322.733
    Epoch: 0057 Batch: 100 /134 lost = 5.701885 ppl = 299.431
    Valid 4864 samples after epoch: 0057 lost = 6.488261 ppl = 657.379
    Epoch: 0058 Batch: 50 /134 lost = 5.766714 ppl = 319.486
    Epoch: 0058 Batch: 100 /134 lost = 5.691379 ppl = 296.302
    Valid 4864 samples after epoch: 0058 lost = 6.491610 ppl = 659.584
    Epoch: 0059 Batch: 50 /134 lost = 5.753949 ppl = 315.434
    Epoch: 0059 Batch: 100 /134 lost = 5.678743 ppl = 292.582
    Valid 4864 samples after epoch: 0059 lost = 6.492377 ppl = 660.091
    Epoch: 0060 Batch: 50 /134 lost = 5.743008 ppl = 312.001
    Epoch: 0060 Batch: 100 /134 lost = 5.667742 ppl = 289.38
    Valid 4864 samples after epoch: 0060 lost = 6.498382 ppl = 664.066
    
    Test the LSTMLM……………………
    Test 5760 samples with models/1_layer_lstmlm_model_epoch60.ckpt……………………
    lost = 6.443443 ppl = 628.567
    
