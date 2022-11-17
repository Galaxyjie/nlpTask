```python
!python n_layers_rnnlm_with_penn_assignment(default_n=3).py
```

    The size of the dictionary is: 7613
    The number of the train batch is: 134
    
    Train the RNNLM……………………
    TextRNN(
      (C): Embedding(7613, 128)
      (W_ax): Linear(in_features=128, out_features=5, bias=False)
      (tanh): Tanh()
      (W): Linear(in_features=5, out_features=7613, bias=False)
    )
    Epoch: 0001 Batch: 50 /134 lost = 8.890069 ppl = 7259.52
    Epoch: 0001 Batch: 100 /134 lost = 8.728570 ppl = 6176.89
    Valid 4864 samples after epoch: 0001 lost = 8.628473 ppl = 5588.54
    Epoch: 0002 Batch: 50 /134 lost = 8.458631 ppl = 4715.6
    Epoch: 0002 Batch: 100 /134 lost = 8.323507 ppl = 4119.58
    Valid 4864 samples after epoch: 0002 lost = 8.253741 ppl = 3841.97
    Epoch: 0003 Batch: 50 /134 lost = 8.076215 ppl = 3217.03
    Epoch: 0003 Batch: 100 /134 lost = 7.960410 ppl = 2865.25
    Valid 4864 samples after epoch: 0003 lost = 7.920611 ppl = 2753.45
    Epoch: 0004 Batch: 50 /134 lost = 7.736794 ppl = 2291.12
    Epoch: 0004 Batch: 100 /134 lost = 7.639929 ppl = 2079.6
    Valid 4864 samples after epoch: 0004 lost = 7.629718 ppl = 2058.47
    Epoch: 0005 Batch: 50 /134 lost = 7.440331 ppl = 1703.31
    Epoch: 0005 Batch: 100 /134 lost = 7.362144 ppl = 1575.21
    Valid 4864 samples after epoch: 0005 lost = 7.381701 ppl = 1606.32
    Epoch: 0006 Batch: 50 /134 lost = 7.186556 ppl = 1321.54
    Epoch: 0006 Batch: 100 /134 lost = 7.126275 ppl = 1244.23
    Valid 4864 samples after epoch: 0006 lost = 7.176740 ppl = 1308.64
    Epoch: 0007 Batch: 50 /134 lost = 6.975061 ppl = 1069.62
    Epoch: 0007 Batch: 100 /134 lost = 6.931140 ppl = 1023.66
    Valid 4864 samples after epoch: 0007 lost = 7.012778 ppl = 1110.74
    Epoch: 0008 Batch: 50 /134 lost = 6.804623 ppl = 902.007
    Epoch: 0008 Batch: 100 /134 lost = 6.774589 ppl = 875.32
    Valid 4864 samples after epoch: 0008 lost = 6.886306 ppl = 978.779
    Epoch: 0009 Batch: 50 /134 lost = 6.671809 ppl = 789.823
    Epoch: 0009 Batch: 100 /134 lost = 6.653140 ppl = 775.214
    Valid 4864 samples after epoch: 0009 lost = 6.793121 ppl = 891.692
    Epoch: 0010 Batch: 50 /134 lost = 6.571737 ppl = 714.61
    Epoch: 0010 Batch: 100 /134 lost = 6.561410 ppl = 707.268
    Valid 4864 samples after epoch: 0010 lost = 6.728425 ppl = 835.83
    Epoch: 0011 Batch: 50 /134 lost = 6.499657 ppl = 664.913
    Epoch: 0011 Batch: 100 /134 lost = 6.497492 ppl = 663.475
    Valid 4864 samples after epoch: 0011 lost = 6.686813 ppl = 801.763
    Epoch: 0012 Batch: 50 /134 lost = 6.450122 ppl = 632.779
    Epoch: 0012 Batch: 100 /134 lost = 6.454648 ppl = 635.65
    Valid 4864 samples after epoch: 0012 lost = 6.662271 ppl = 782.326
    Epoch: 0013 Batch: 50 /134 lost = 6.417079 ppl = 612.212
    Epoch: 0013 Batch: 100 /134 lost = 6.426748 ppl = 618.161
    Valid 4864 samples after epoch: 0013 lost = 6.648808 ppl = 771.864
    Epoch: 0014 Batch: 50 /134 lost = 6.394945 ppl = 598.81
    Epoch: 0014 Batch: 100 /134 lost = 6.408037 ppl = 606.701
    Valid 4864 samples after epoch: 0014 lost = 6.641528 ppl = 766.265
    Epoch: 0015 Batch: 50 /134 lost = 6.380021 ppl = 589.94
    Epoch: 0015 Batch: 100 /134 lost = 6.394638 ppl = 598.627
    Valid 4864 samples after epoch: 0015 lost = 6.636977 ppl = 762.786
    Epoch: 0016 Batch: 50 /134 lost = 6.368372 ppl = 583.108
    Epoch: 0016 Batch: 100 /134 lost = 6.383503 ppl = 591.998
    Valid 4864 samples after epoch: 0016 lost = 6.634753 ppl = 761.091
    Epoch: 0017 Batch: 50 /134 lost = 6.359276 ppl = 577.828
    Epoch: 0017 Batch: 100 /134 lost = 6.371679 ppl = 585.039
    Valid 4864 samples after epoch: 0017 lost = 6.633683 ppl = 760.277
    Epoch: 0018 Batch: 50 /134 lost = 6.351992 ppl = 573.634
    Epoch: 0018 Batch: 100 /134 lost = 6.364805 ppl = 581.031
    Valid 4864 samples after epoch: 0018 lost = 6.632811 ppl = 759.615
    Epoch: 0019 Batch: 50 /134 lost = 6.346019 ppl = 570.218
    Epoch: 0019 Batch: 100 /134 lost = 6.359251 ppl = 577.813
    Valid 4864 samples after epoch: 0019 lost = 6.632488 ppl = 759.369
    Epoch: 0020 Batch: 50 /134 lost = 6.341145 ppl = 567.445
    Epoch: 0020 Batch: 100 /134 lost = 6.356186 ppl = 576.045
    Valid 4864 samples after epoch: 0020 lost = 6.630906 ppl = 758.169
    Epoch: 0021 Batch: 50 /134 lost = 6.337045 ppl = 565.124
    Epoch: 0021 Batch: 100 /134 lost = 6.352043 ppl = 573.663
    Valid 4864 samples after epoch: 0021 lost = 6.630904 ppl = 758.167
    Epoch: 0022 Batch: 50 /134 lost = 6.333256 ppl = 562.987
    Epoch: 0022 Batch: 100 /134 lost = 6.344674 ppl = 569.452
    Valid 4864 samples after epoch: 0022 lost = 6.630133 ppl = 757.583
    Epoch: 0023 Batch: 50 /134 lost = 6.329078 ppl = 560.64
    Epoch: 0023 Batch: 100 /134 lost = 6.339786 ppl = 566.675
    Valid 4864 samples after epoch: 0023 lost = 6.630687 ppl = 758.003
    Epoch: 0024 Batch: 50 /134 lost = 6.325871 ppl = 558.845
    Epoch: 0024 Batch: 100 /134 lost = 6.335758 ppl = 564.397
    Valid 4864 samples after epoch: 0024 lost = 6.631490 ppl = 758.612
    Epoch: 0025 Batch: 50 /134 lost = 6.322885 ppl = 557.178
    Epoch: 0025 Batch: 100 /134 lost = 6.332178 ppl = 562.38
    Valid 4864 samples after epoch: 0025 lost = 6.632335 ppl = 759.253
    Epoch: 0026 Batch: 50 /134 lost = 6.319812 ppl = 555.468
    Epoch: 0026 Batch: 100 /134 lost = 6.329164 ppl = 560.687
    Valid 4864 samples after epoch: 0026 lost = 6.633067 ppl = 759.809
    Epoch: 0027 Batch: 50 /134 lost = 6.317629 ppl = 554.257
    Epoch: 0027 Batch: 100 /134 lost = 6.326645 ppl = 559.277
    Valid 4864 samples after epoch: 0027 lost = 6.633585 ppl = 760.203
    Epoch: 0028 Batch: 50 /134 lost = 6.315311 ppl = 552.974
    Epoch: 0028 Batch: 100 /134 lost = 6.323217 ppl = 557.363
    Valid 4864 samples after epoch: 0028 lost = 6.634554 ppl = 760.94
    Epoch: 0029 Batch: 50 /134 lost = 6.312559 ppl = 551.454
    Epoch: 0029 Batch: 100 /134 lost = 6.319603 ppl = 555.353
    Valid 4864 samples after epoch: 0029 lost = 6.635946 ppl = 761.999
    Epoch: 0030 Batch: 50 /134 lost = 6.310190 ppl = 550.149
    Epoch: 0030 Batch: 100 /134 lost = 6.315882 ppl = 553.29
    Valid 4864 samples after epoch: 0030 lost = 6.637286 ppl = 763.021
    Epoch: 0031 Batch: 50 /134 lost = 6.307794 ppl = 548.833
    Epoch: 0031 Batch: 100 /134 lost = 6.309447 ppl = 549.741
    Valid 4864 samples after epoch: 0031 lost = 6.637709 ppl = 763.344
    Epoch: 0032 Batch: 50 /134 lost = 6.305589 ppl = 547.624
    Epoch: 0032 Batch: 100 /134 lost = 6.304878 ppl = 547.235
    Valid 4864 samples after epoch: 0032 lost = 6.638955 ppl = 764.296
    Epoch: 0033 Batch: 50 /134 lost = 6.303473 ppl = 546.466
    Epoch: 0033 Batch: 100 /134 lost = 6.301524 ppl = 545.403
    Valid 4864 samples after epoch: 0033 lost = 6.640111 ppl = 765.18
    Epoch: 0034 Batch: 50 /134 lost = 6.301379 ppl = 545.323
    Epoch: 0034 Batch: 100 /134 lost = 6.298595 ppl = 543.807
    Valid 4864 samples after epoch: 0034 lost = 6.641345 ppl = 766.125
    Epoch: 0035 Batch: 50 /134 lost = 6.299623 ppl = 544.367
    Epoch: 0035 Batch: 100 /134 lost = 6.295933 ppl = 542.362
    Valid 4864 samples after epoch: 0035 lost = 6.642740 ppl = 767.194
    Epoch: 0036 Batch: 50 /134 lost = 6.298037 ppl = 543.504
    Epoch: 0036 Batch: 100 /134 lost = 6.293421 ppl = 541.001
    Valid 4864 samples after epoch: 0036 lost = 6.644153 ppl = 768.279
    Epoch: 0037 Batch: 50 /134 lost = 6.296558 ppl = 542.701
    Epoch: 0037 Batch: 100 /134 lost = 6.290870 ppl = 539.623
    Valid 4864 samples after epoch: 0037 lost = 6.645691 ppl = 769.462
    Epoch: 0038 Batch: 50 /134 lost = 6.295126 ppl = 541.924
    Epoch: 0038 Batch: 100 /134 lost = 6.288243 ppl = 538.207
    Valid 4864 samples after epoch: 0038 lost = 6.647042 ppl = 770.502
    Epoch: 0039 Batch: 50 /134 lost = 6.293553 ppl = 541.072
    Epoch: 0039 Batch: 100 /134 lost = 6.285664 ppl = 536.82
    Valid 4864 samples after epoch: 0039 lost = 6.648617 ppl = 771.716
    Epoch: 0040 Batch: 50 /134 lost = 6.291708 ppl = 540.075
    Epoch: 0040 Batch: 100 /134 lost = 6.283063 ppl = 535.426
    Valid 4864 samples after epoch: 0040 lost = 6.650101 ppl = 772.862
    Epoch: 0041 Batch: 50 /134 lost = 6.290104 ppl = 539.209
    Epoch: 0041 Batch: 100 /134 lost = 6.280505 ppl = 534.058
    Valid 4864 samples after epoch: 0041 lost = 6.651597 ppl = 774.02
    Epoch: 0042 Batch: 50 /134 lost = 6.288339 ppl = 538.258
    Epoch: 0042 Batch: 100 /134 lost = 6.278054 ppl = 532.751
    Valid 4864 samples after epoch: 0042 lost = 6.653100 ppl = 775.184
    Epoch: 0043 Batch: 50 /134 lost = 6.286566 ppl = 537.305
    Epoch: 0043 Batch: 100 /134 lost = 6.275602 ppl = 531.446
    Valid 4864 samples after epoch: 0043 lost = 6.654688 ppl = 776.415
    Epoch: 0044 Batch: 50 /134 lost = 6.284810 ppl = 536.362
    Epoch: 0044 Batch: 100 /134 lost = 6.273506 ppl = 530.334
    Valid 4864 samples after epoch: 0044 lost = 6.656127 ppl = 777.533
    Epoch: 0045 Batch: 50 /134 lost = 6.283283 ppl = 535.544
    Epoch: 0045 Batch: 100 /134 lost = 6.271264 ppl = 529.146
    Valid 4864 samples after epoch: 0045 lost = 6.657769 ppl = 778.812
    Epoch: 0046 Batch: 50 /134 lost = 6.281610 ppl = 534.649
    Epoch: 0046 Batch: 100 /134 lost = 6.268825 ppl = 527.857
    Valid 4864 samples after epoch: 0046 lost = 6.659464 ppl = 780.133
    Epoch: 0047 Batch: 50 /134 lost = 6.279938 ppl = 533.755
    Epoch: 0047 Batch: 100 /134 lost = 6.266237 ppl = 526.492
    Valid 4864 samples after epoch: 0047 lost = 6.661113 ppl = 781.42
    Epoch: 0048 Batch: 50 /134 lost = 6.278368 ppl = 532.918
    Epoch: 0048 Batch: 100 /134 lost = 6.263587 ppl = 525.099
    Valid 4864 samples after epoch: 0048 lost = 6.662976 ppl = 782.877
    Epoch: 0049 Batch: 50 /134 lost = 6.276840 ppl = 532.105
    Epoch: 0049 Batch: 100 /134 lost = 6.260987 ppl = 523.736
    Valid 4864 samples after epoch: 0049 lost = 6.664839 ppl = 784.337
    Epoch: 0050 Batch: 50 /134 lost = 6.275414 ppl = 531.347
    Epoch: 0050 Batch: 100 /134 lost = 6.258554 ppl = 522.463
    Valid 4864 samples after epoch: 0050 lost = 6.666715 ppl = 785.81
    Epoch: 0051 Batch: 50 /134 lost = 6.273910 ppl = 530.548
    Epoch: 0051 Batch: 100 /134 lost = 6.256122 ppl = 521.194
    Valid 4864 samples after epoch: 0051 lost = 6.668520 ppl = 787.23
    Epoch: 0052 Batch: 50 /134 lost = 6.271993 ppl = 529.532
    Epoch: 0052 Batch: 100 /134 lost = 6.252660 ppl = 519.393
    Valid 4864 samples after epoch: 0052 lost = 6.669753 ppl = 788.201
    Epoch: 0053 Batch: 50 /134 lost = 6.269995 ppl = 528.475
    Epoch: 0053 Batch: 100 /134 lost = 6.249944 ppl = 517.984
    Valid 4864 samples after epoch: 0053 lost = 6.671046 ppl = 789.221
    Epoch: 0054 Batch: 50 /134 lost = 6.268463 ppl = 527.666
    Epoch: 0054 Batch: 100 /134 lost = 6.247764 ppl = 516.856
    Valid 4864 samples after epoch: 0054 lost = 6.672450 ppl = 790.329
    Epoch: 0055 Batch: 50 /134 lost = 6.267008 ppl = 526.898
    Epoch: 0055 Batch: 100 /134 lost = 6.245606 ppl = 515.742
    Valid 4864 samples after epoch: 0055 lost = 6.674057 ppl = 791.601
    Epoch: 0056 Batch: 50 /134 lost = 6.265627 ppl = 526.171
    Epoch: 0056 Batch: 100 /134 lost = 6.243777 ppl = 514.799
    Valid 4864 samples after epoch: 0056 lost = 6.675358 ppl = 792.631
    Epoch: 0057 Batch: 50 /134 lost = 6.263482 ppl = 525.044
    Epoch: 0057 Batch: 100 /134 lost = 6.242086 ppl = 513.93
    Valid 4864 samples after epoch: 0057 lost = 6.677351 ppl = 794.213
    Epoch: 0058 Batch: 50 /134 lost = 6.262290 ppl = 524.419
    Epoch: 0058 Batch: 100 /134 lost = 6.240127 ppl = 512.923
    Valid 4864 samples after epoch: 0058 lost = 6.679491 ppl = 795.914
    Epoch: 0059 Batch: 50 /134 lost = 6.260988 ppl = 523.736
    Epoch: 0059 Batch: 100 /134 lost = 6.238196 ppl = 511.934
    Valid 4864 samples after epoch: 0059 lost = 6.681578 ppl = 797.577
    Epoch: 0060 Batch: 50 /134 lost = 6.259620 ppl = 523.02
    Epoch: 0060 Batch: 100 /134 lost = 6.236147 ppl = 510.886
    Valid 4864 samples after epoch: 0060 lost = 6.683533 ppl = 799.138
    
    Test the RNNLM……………………
    Test 5760 samples with models/3_layers_rnnlm_model_epoch60.ckpt……………………
    lost = 6.585613 ppl = 724.595
    
