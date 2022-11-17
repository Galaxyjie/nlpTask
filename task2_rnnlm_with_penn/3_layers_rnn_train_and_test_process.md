```python
!python rnnlm_with_penn_assignment_n.py
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
    Epoch: 0001 Batch: 50 /134 lost = 8.818153 ppl = 6755.78
    Epoch: 0001 Batch: 100 /134 lost = 8.624718 ppl = 5567.59
    Valid 4864 samples after epoch: 0001 lost = 8.525762 ppl = 5043.03
    Epoch: 0002 Batch: 50 /134 lost = 8.312224 ppl = 4073.36
    Epoch: 0002 Batch: 100 /134 lost = 8.151650 ppl = 3469.1
    Valid 4864 samples after epoch: 0002 lost = 8.088107 ppl = 3255.52
    Epoch: 0003 Batch: 50 /134 lost = 7.866869 ppl = 2609.38
    Epoch: 0003 Batch: 100 /134 lost = 7.730049 ppl = 2275.71
    Valid 4864 samples after epoch: 0003 lost = 7.706932 ppl = 2223.71
    Epoch: 0004 Batch: 50 /134 lost = 7.483504 ppl = 1778.46
    Epoch: 0004 Batch: 100 /134 lost = 7.373992 ppl = 1593.98
    Valid 4864 samples after epoch: 0004 lost = 7.389862 ppl = 1619.48
    Epoch: 0005 Batch: 50 /134 lost = 7.168510 ppl = 1297.91
    Epoch: 0005 Batch: 100 /134 lost = 7.082194 ppl = 1190.58
    Valid 4864 samples after epoch: 0005 lost = 7.136387 ppl = 1256.88
    Epoch: 0006 Batch: 50 /134 lost = 6.917021 ppl = 1009.31
    Epoch: 0006 Batch: 100 /134 lost = 6.854408 ppl = 948.051
    Valid 4864 samples after epoch: 0006 lost = 6.945073 ppl = 1038.02
    Epoch: 0007 Batch: 50 /134 lost = 6.728641 ppl = 836.01
    Epoch: 0007 Batch: 100 /134 lost = 6.684035 ppl = 799.539
    Valid 4864 samples after epoch: 0007 lost = 6.808964 ppl = 905.932
    Epoch: 0008 Batch: 50 /134 lost = 6.596781 ppl = 732.733
    Epoch: 0008 Batch: 100 /134 lost = 6.564649 ppl = 709.563
    Valid 4864 samples after epoch: 0008 lost = 6.721280 ppl = 829.879
    Epoch: 0009 Batch: 50 /134 lost = 6.511981 ppl = 673.158
    Epoch: 0009 Batch: 100 /134 lost = 6.486513 ppl = 656.231
    Valid 4864 samples after epoch: 0009 lost = 6.669348 ppl = 787.882
    Epoch: 0010 Batch: 50 /134 lost = 6.459300 ppl = 638.614
    Epoch: 0010 Batch: 100 /134 lost = 6.438751 ppl = 625.625
    Valid 4864 samples after epoch: 0010 lost = 6.640194 ppl = 765.243
    Epoch: 0011 Batch: 50 /134 lost = 6.427270 ppl = 618.483
    Epoch: 0011 Batch: 100 /134 lost = 6.410254 ppl = 608.048
    Valid 4864 samples after epoch: 0011 lost = 6.622895 ppl = 752.119
    Epoch: 0012 Batch: 50 /134 lost = 6.407966 ppl = 606.658
    Epoch: 0012 Batch: 100 /134 lost = 6.391109 ppl = 596.518
    Valid 4864 samples after epoch: 0012 lost = 6.613763 ppl = 745.282
    Epoch: 0013 Batch: 50 /134 lost = 6.393796 ppl = 598.123
    Epoch: 0013 Batch: 100 /134 lost = 6.378375 ppl = 588.97
    Valid 4864 samples after epoch: 0013 lost = 6.607864 ppl = 740.899
    Epoch: 0014 Batch: 50 /134 lost = 6.384687 ppl = 592.699
    Epoch: 0014 Batch: 100 /134 lost = 6.369670 ppl = 583.865
    Valid 4864 samples after epoch: 0014 lost = 6.605038 ppl = 738.808
    Epoch: 0015 Batch: 50 /134 lost = 6.377046 ppl = 588.188
    Epoch: 0015 Batch: 100 /134 lost = 6.363439 ppl = 580.238
    Valid 4864 samples after epoch: 0015 lost = 6.603204 ppl = 737.454
    Epoch: 0016 Batch: 50 /134 lost = 6.370286 ppl = 584.225
    Epoch: 0016 Batch: 100 /134 lost = 6.357937 ppl = 577.055
    Valid 4864 samples after epoch: 0016 lost = 6.601801 ppl = 736.42
    Epoch: 0017 Batch: 50 /134 lost = 6.364867 ppl = 581.067
    Epoch: 0017 Batch: 100 /134 lost = 6.352642 ppl = 574.007
    Valid 4864 samples after epoch: 0017 lost = 6.601370 ppl = 736.103
    Epoch: 0018 Batch: 50 /134 lost = 6.360063 ppl = 578.283
    Epoch: 0018 Batch: 100 /134 lost = 6.347593 ppl = 571.117
    Valid 4864 samples after epoch: 0018 lost = 6.601296 ppl = 736.049
    Epoch: 0019 Batch: 50 /134 lost = 6.356003 ppl = 575.94
    Epoch: 0019 Batch: 100 /134 lost = 6.342551 ppl = 568.244
    Valid 4864 samples after epoch: 0019 lost = 6.601535 ppl = 736.225
    Epoch: 0020 Batch: 50 /134 lost = 6.352307 ppl = 573.815
    Epoch: 0020 Batch: 100 /134 lost = 6.336815 ppl = 564.994
    Valid 4864 samples after epoch: 0020 lost = 6.602181 ppl = 736.7
    Epoch: 0021 Batch: 50 /134 lost = 6.348691 ppl = 571.744
    Epoch: 0021 Batch: 100 /134 lost = 6.331873 ppl = 562.209
    Valid 4864 samples after epoch: 0021 lost = 6.602853 ppl = 737.195
    Epoch: 0022 Batch: 50 /134 lost = 6.344996 ppl = 569.635
    Epoch: 0022 Batch: 100 /134 lost = 6.327706 ppl = 559.871
    Valid 4864 samples after epoch: 0022 lost = 6.603633 ppl = 737.771
    Epoch: 0023 Batch: 50 /134 lost = 6.341453 ppl = 567.62
    Epoch: 0023 Batch: 100 /134 lost = 6.323501 ppl = 557.521
    Valid 4864 samples after epoch: 0023 lost = 6.604483 ppl = 738.398
    Epoch: 0024 Batch: 50 /134 lost = 6.338296 ppl = 565.831
    Epoch: 0024 Batch: 100 /134 lost = 6.320283 ppl = 555.73
    Valid 4864 samples after epoch: 0024 lost = 6.605441 ppl = 739.106
    Epoch: 0025 Batch: 50 /134 lost = 6.335039 ppl = 563.991
    Epoch: 0025 Batch: 100 /134 lost = 6.317266 ppl = 554.056
    Valid 4864 samples after epoch: 0025 lost = 6.606536 ppl = 739.916
    Epoch: 0026 Batch: 50 /134 lost = 6.332065 ppl = 562.316
    Epoch: 0026 Batch: 100 /134 lost = 6.313512 ppl = 551.98
    Valid 4864 samples after epoch: 0026 lost = 6.607472 ppl = 740.608
    Epoch: 0027 Batch: 50 /134 lost = 6.328990 ppl = 560.59
    Epoch: 0027 Batch: 100 /134 lost = 6.309805 ppl = 549.938
    Valid 4864 samples after epoch: 0027 lost = 6.608240 ppl = 741.177
    Epoch: 0028 Batch: 50 /134 lost = 6.326642 ppl = 559.275
    Epoch: 0028 Batch: 100 /134 lost = 6.306227 ppl = 547.974
    Valid 4864 samples after epoch: 0028 lost = 6.609331 ppl = 741.986
    Epoch: 0029 Batch: 50 /134 lost = 6.323596 ppl = 557.574
    Epoch: 0029 Batch: 100 /134 lost = 6.303023 ppl = 546.221
    Valid 4864 samples after epoch: 0029 lost = 6.610307 ppl = 742.711
    Epoch: 0030 Batch: 50 /134 lost = 6.320647 ppl = 555.932
    Epoch: 0030 Batch: 100 /134 lost = 6.299832 ppl = 544.48
    Valid 4864 samples after epoch: 0030 lost = 6.611410 ppl = 743.531
    Epoch: 0031 Batch: 50 /134 lost = 6.317164 ppl = 554.0
    Epoch: 0031 Batch: 100 /134 lost = 6.296632 ppl = 542.741
    Valid 4864 samples after epoch: 0031 lost = 6.612444 ppl = 744.3
    Epoch: 0032 Batch: 50 /134 lost = 6.314398 ppl = 552.47
    Epoch: 0032 Batch: 100 /134 lost = 6.293064 ppl = 540.808
    Valid 4864 samples after epoch: 0032 lost = 6.613536 ppl = 745.113
    Epoch: 0033 Batch: 50 /134 lost = 6.311464 ppl = 550.851
    Epoch: 0033 Batch: 100 /134 lost = 6.290201 ppl = 539.262
    Valid 4864 samples after epoch: 0033 lost = 6.614880 ppl = 746.115
    Epoch: 0034 Batch: 50 /134 lost = 6.308498 ppl = 549.219
    Epoch: 0034 Batch: 100 /134 lost = 6.287425 ppl = 537.767
    Valid 4864 samples after epoch: 0034 lost = 6.615853 ppl = 746.841
    Epoch: 0035 Batch: 50 /134 lost = 6.305247 ppl = 547.437
    Epoch: 0035 Batch: 100 /134 lost = 6.284243 ppl = 536.058
    Valid 4864 samples after epoch: 0035 lost = 6.617268 ppl = 747.899
    Epoch: 0036 Batch: 50 /134 lost = 6.301968 ppl = 545.644
    Epoch: 0036 Batch: 100 /134 lost = 6.280966 ppl = 534.304
    Valid 4864 samples after epoch: 0036 lost = 6.618742 ppl = 749.002
    Epoch: 0037 Batch: 50 /134 lost = 6.298927 ppl = 543.988
    Epoch: 0037 Batch: 100 /134 lost = 6.277718 ppl = 532.572
    Valid 4864 samples after epoch: 0037 lost = 6.620178 ppl = 750.078
    Epoch: 0038 Batch: 50 /134 lost = 6.296072 ppl = 542.437
    Epoch: 0038 Batch: 100 /134 lost = 6.274546 ppl = 530.885
    Valid 4864 samples after epoch: 0038 lost = 6.621555 ppl = 751.112
    Epoch: 0039 Batch: 50 /134 lost = 6.293497 ppl = 541.042
    Epoch: 0039 Batch: 100 /134 lost = 6.271255 ppl = 529.141
    Valid 4864 samples after epoch: 0039 lost = 6.622866 ppl = 752.097
    Epoch: 0040 Batch: 50 /134 lost = 6.290533 ppl = 539.441
    Epoch: 0040 Batch: 100 /134 lost = 6.268215 ppl = 527.535
    Valid 4864 samples after epoch: 0040 lost = 6.624309 ppl = 753.183
    Epoch: 0041 Batch: 50 /134 lost = 6.287798 ppl = 537.967
    Epoch: 0041 Batch: 100 /134 lost = 6.265397 ppl = 526.05
    Valid 4864 samples after epoch: 0041 lost = 6.625895 ppl = 754.379
    Epoch: 0042 Batch: 50 /134 lost = 6.285479 ppl = 536.721
    Epoch: 0042 Batch: 100 /134 lost = 6.262718 ppl = 524.643
    Valid 4864 samples after epoch: 0042 lost = 6.627451 ppl = 755.554
    Epoch: 0043 Batch: 50 /134 lost = 6.283142 ppl = 535.468
    Epoch: 0043 Batch: 100 /134 lost = 6.260131 ppl = 523.288
    Valid 4864 samples after epoch: 0043 lost = 6.628845 ppl = 756.607
    Epoch: 0044 Batch: 50 /134 lost = 6.280317 ppl = 533.958
    Epoch: 0044 Batch: 100 /134 lost = 6.257592 ppl = 521.961
    Valid 4864 samples after epoch: 0044 lost = 6.630383 ppl = 757.772
    Epoch: 0045 Batch: 50 /134 lost = 6.277311 ppl = 532.355
    Epoch: 0045 Batch: 100 /134 lost = 6.255009 ppl = 520.614
    Valid 4864 samples after epoch: 0045 lost = 6.631797 ppl = 758.844
    Epoch: 0046 Batch: 50 /134 lost = 6.273536 ppl = 530.349
    Epoch: 0046 Batch: 100 /134 lost = 6.252729 ppl = 519.428
    Valid 4864 samples after epoch: 0046 lost = 6.633408 ppl = 760.068
    Epoch: 0047 Batch: 50 /134 lost = 6.270664 ppl = 528.828
    Epoch: 0047 Batch: 100 /134 lost = 6.250381 ppl = 518.21
    Valid 4864 samples after epoch: 0047 lost = 6.634904 ppl = 761.206
    Epoch: 0048 Batch: 50 /134 lost = 6.268119 ppl = 527.484
    Epoch: 0048 Batch: 100 /134 lost = 6.247804 ppl = 516.877
    Valid 4864 samples after epoch: 0048 lost = 6.636493 ppl = 762.417
    Epoch: 0049 Batch: 50 /134 lost = 6.265748 ppl = 526.235
    Epoch: 0049 Batch: 100 /134 lost = 6.245315 ppl = 515.591
    Valid 4864 samples after epoch: 0049 lost = 6.637919 ppl = 763.504
    Epoch: 0050 Batch: 50 /134 lost = 6.263356 ppl = 524.978
    Epoch: 0050 Batch: 100 /134 lost = 6.242847 ppl = 514.321
    Valid 4864 samples after epoch: 0050 lost = 6.639596 ppl = 764.786
    Epoch: 0051 Batch: 50 /134 lost = 6.261098 ppl = 523.794
    Epoch: 0051 Batch: 100 /134 lost = 6.240479 ppl = 513.104
    Valid 4864 samples after epoch: 0051 lost = 6.641205 ppl = 766.018
    Epoch: 0052 Batch: 50 /134 lost = 6.258683 ppl = 522.53
    Epoch: 0052 Batch: 100 /134 lost = 6.238147 ppl = 511.909
    Valid 4864 samples after epoch: 0052 lost = 6.643014 ppl = 767.405
    Epoch: 0053 Batch: 50 /134 lost = 6.256307 ppl = 521.29
    Epoch: 0053 Batch: 100 /134 lost = 6.235886 ppl = 510.753
    Valid 4864 samples after epoch: 0053 lost = 6.644802 ppl = 768.778
    Epoch: 0054 Batch: 50 /134 lost = 6.253850 ppl = 520.011
    Epoch: 0054 Batch: 100 /134 lost = 6.233845 ppl = 509.712
    Valid 4864 samples after epoch: 0054 lost = 6.646039 ppl = 769.729
    Epoch: 0055 Batch: 50 /134 lost = 6.251179 ppl = 518.624
    Epoch: 0055 Batch: 100 /134 lost = 6.231658 ppl = 508.598
    Valid 4864 samples after epoch: 0055 lost = 6.647466 ppl = 770.828
    Epoch: 0056 Batch: 50 /134 lost = 6.248863 ppl = 517.424
    Epoch: 0056 Batch: 100 /134 lost = 6.229501 ppl = 507.502
    Valid 4864 samples after epoch: 0056 lost = 6.649231 ppl = 772.191
    Epoch: 0057 Batch: 50 /134 lost = 6.246872 ppl = 516.395
    Epoch: 0057 Batch: 100 /134 lost = 6.227240 ppl = 506.356
    Valid 4864 samples after epoch: 0057 lost = 6.650991 ppl = 773.55
    Epoch: 0058 Batch: 50 /134 lost = 6.244936 ppl = 515.396
    Epoch: 0058 Batch: 100 /134 lost = 6.224961 ppl = 505.203
    Valid 4864 samples after epoch: 0058 lost = 6.652743 ppl = 774.907
    Epoch: 0059 Batch: 50 /134 lost = 6.243027 ppl = 514.413
    Epoch: 0059 Batch: 100 /134 lost = 6.222753 ppl = 504.089
    Valid 4864 samples after epoch: 0059 lost = 6.654636 ppl = 776.376
    Epoch: 0060 Batch: 50 /134 lost = 6.241138 ppl = 513.443
    Epoch: 0060 Batch: 100 /134 lost = 6.220540 ppl = 502.975
    Valid 4864 samples after epoch: 0060 lost = 6.656594 ppl = 777.897
    
    Test the RNNLM……………………
    Test 5760 samples with models/rnnlm_3_layers_model_epoch60.ckpt……………………
    lost = 6.572121 ppl = 714.885
    
