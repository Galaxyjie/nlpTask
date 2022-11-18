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
    Epoch: 0001 Batch: 50 /134 lost = 8.743100 ppl = 6267.3
    Epoch: 0001 Batch: 100 /134 lost = 8.511660 ppl = 4972.41
    Valid 4864 samples after epoch: 0001 lost = 8.402018 ppl = 4456.05
    Saving best model
    Epoch: 0002 Batch: 50 /134 lost = 8.220428 ppl = 3716.09
    Epoch: 0002 Batch: 100 /134 lost = 8.034413 ppl = 3085.33
    Valid 4864 samples after epoch: 0002 lost = 7.968390 ppl = 2888.2
    Saving best model
    Epoch: 0003 Batch: 50 /134 lost = 7.781535 ppl = 2395.95
    Epoch: 0003 Batch: 100 /134 lost = 7.627457 ppl = 2053.82
    Valid 4864 samples after epoch: 0003 lost = 7.601090 ppl = 2000.38
    Saving best model
    Epoch: 0004 Batch: 50 /134 lost = 7.409705 ppl = 1651.94
    Epoch: 0004 Batch: 100 /134 lost = 7.285444 ppl = 1458.91
    Valid 4864 samples after epoch: 0004 lost = 7.298408 ppl = 1477.95
    Saving best model
    Epoch: 0005 Batch: 50 /134 lost = 7.105134 ppl = 1218.2
    Epoch: 0005 Batch: 100 /134 lost = 7.009287 ppl = 1106.86
    Valid 4864 samples after epoch: 0005 lost = 7.061211 ppl = 1165.86
    Saving best model
    Epoch: 0006 Batch: 50 /134 lost = 6.869011 ppl = 961.997
    Epoch: 0006 Batch: 100 /134 lost = 6.798272 ppl = 896.297
    Valid 4864 samples after epoch: 0006 lost = 6.887660 ppl = 980.106
    Saving best model
    Epoch: 0007 Batch: 50 /134 lost = 6.697928 ppl = 810.724
    Epoch: 0007 Batch: 100 /134 lost = 6.647139 ppl = 770.576
    Valid 4864 samples after epoch: 0007 lost = 6.770490 ppl = 871.739
    Saving best model
    Epoch: 0008 Batch: 50 /134 lost = 6.582237 ppl = 722.153
    Epoch: 0008 Batch: 100 /134 lost = 6.545303 ppl = 695.968
    Valid 4864 samples after epoch: 0008 lost = 6.697174 ppl = 810.113
    Saving best model
    Epoch: 0009 Batch: 50 /134 lost = 6.508231 ppl = 670.639
    Epoch: 0009 Batch: 100 /134 lost = 6.478887 ppl = 651.245
    Valid 4864 samples after epoch: 0009 lost = 6.654727 ppl = 776.446
    Saving best model
    Epoch: 0010 Batch: 50 /134 lost = 6.461661 ppl = 640.124
    Epoch: 0010 Batch: 100 /134 lost = 6.437152 ppl = 624.625
    Valid 4864 samples after epoch: 0010 lost = 6.632589 ppl = 759.446
    Saving best model
    Epoch: 0011 Batch: 50 /134 lost = 6.432090 ppl = 621.472
    Epoch: 0011 Batch: 100 /134 lost = 6.410519 ppl = 608.209
    Valid 4864 samples after epoch: 0011 lost = 6.619017 ppl = 749.209
    Saving best model
    Epoch: 0012 Batch: 50 /134 lost = 6.412543 ppl = 609.441
    Epoch: 0012 Batch: 100 /134 lost = 6.392587 ppl = 597.4
    Valid 4864 samples after epoch: 0012 lost = 6.610909 ppl = 743.158
    Saving best model
    Epoch: 0013 Batch: 50 /134 lost = 6.398379 ppl = 600.87
    Epoch: 0013 Batch: 100 /134 lost = 6.380026 ppl = 589.943
    Valid 4864 samples after epoch: 0013 lost = 6.605794 ppl = 739.367
    Saving best model
    Epoch: 0014 Batch: 50 /134 lost = 6.386550 ppl = 593.804
    Epoch: 0014 Batch: 100 /134 lost = 6.370865 ppl = 584.563
    Valid 4864 samples after epoch: 0014 lost = 6.602754 ppl = 737.123
    Saving best model
    Epoch: 0015 Batch: 50 /134 lost = 6.377925 ppl = 588.705
    Epoch: 0015 Batch: 100 /134 lost = 6.363747 ppl = 580.417
    Valid 4864 samples after epoch: 0015 lost = 6.601145 ppl = 735.937
    Saving best model
    Epoch: 0016 Batch: 50 /134 lost = 6.370894 ppl = 584.58
    Epoch: 0016 Batch: 100 /134 lost = 6.357690 ppl = 576.912
    Valid 4864 samples after epoch: 0016 lost = 6.600374 ppl = 735.37
    Saving best model
    Epoch: 0017 Batch: 50 /134 lost = 6.365123 ppl = 581.216
    Epoch: 0017 Batch: 100 /134 lost = 6.351918 ppl = 573.592
    Valid 4864 samples after epoch: 0017 lost = 6.600010 ppl = 735.103
    Saving best model
    Epoch: 0018 Batch: 50 /134 lost = 6.360180 ppl = 578.351
    Epoch: 0018 Batch: 100 /134 lost = 6.346192 ppl = 570.317
    Valid 4864 samples after epoch: 0018 lost = 6.599931 ppl = 735.045
    Saving best model
    Epoch: 0019 Batch: 50 /134 lost = 6.355754 ppl = 575.797
    Epoch: 0019 Batch: 100 /134 lost = 6.340687 ppl = 567.186
    Valid 4864 samples after epoch: 0019 lost = 6.600012 ppl = 735.104
    Saving best model
    Epoch: 0020 Batch: 50 /134 lost = 6.351603 ppl = 573.411
    Epoch: 0020 Batch: 100 /134 lost = 6.335546 ppl = 564.278
    Valid 4864 samples after epoch: 0020 lost = 6.600218 ppl = 735.255
    Saving best model
    Epoch: 0021 Batch: 50 /134 lost = 6.347516 ppl = 571.072
    Epoch: 0021 Batch: 100 /134 lost = 6.330695 ppl = 561.547
    Valid 4864 samples after epoch: 0021 lost = 6.600596 ppl = 735.534
    Saving best model
    Epoch: 0022 Batch: 50 /134 lost = 6.343289 ppl = 568.664
    Epoch: 0022 Batch: 100 /134 lost = 6.325997 ppl = 558.915
    Valid 4864 samples after epoch: 0022 lost = 6.600997 ppl = 735.828
    Saving best model
    Epoch: 0023 Batch: 50 /134 lost = 6.339330 ppl = 566.417
    Epoch: 0023 Batch: 100 /134 lost = 6.321408 ppl = 556.356
    Valid 4864 samples after epoch: 0023 lost = 6.601423 ppl = 736.142
    Saving best model
    Epoch: 0024 Batch: 50 /134 lost = 6.335553 ppl = 564.281
    Epoch: 0024 Batch: 100 /134 lost = 6.316940 ppl = 553.875
    Valid 4864 samples after epoch: 0024 lost = 6.601870 ppl = 736.471
    Saving best model
    Epoch: 0025 Batch: 50 /134 lost = 6.331964 ppl = 562.26
    Epoch: 0025 Batch: 100 /134 lost = 6.312580 ppl = 551.466
    Valid 4864 samples after epoch: 0025 lost = 6.602393 ppl = 736.856
    Saving best model
    Epoch: 0026 Batch: 50 /134 lost = 6.328563 ppl = 560.351
    Epoch: 0026 Batch: 100 /134 lost = 6.308315 ppl = 549.119
    Valid 4864 samples after epoch: 0026 lost = 6.603017 ppl = 737.316
    Saving best model
    Epoch: 0027 Batch: 50 /134 lost = 6.325371 ppl = 558.565
    Epoch: 0027 Batch: 100 /134 lost = 6.304222 ppl = 546.876
    Valid 4864 samples after epoch: 0027 lost = 6.603654 ppl = 737.786
    Saving best model
    Epoch: 0028 Batch: 50 /134 lost = 6.322243 ppl = 556.82
    Epoch: 0028 Batch: 100 /134 lost = 6.300214 ppl = 544.689
    Valid 4864 samples after epoch: 0028 lost = 6.604328 ppl = 738.284
    Saving best model
    Epoch: 0029 Batch: 50 /134 lost = 6.319184 ppl = 555.12
    Epoch: 0029 Batch: 100 /134 lost = 6.296332 ppl = 542.578
    Valid 4864 samples after epoch: 0029 lost = 6.605067 ppl = 738.829
    Saving best model
    Epoch: 0030 Batch: 50 /134 lost = 6.316295 ppl = 553.518
    Epoch: 0030 Batch: 100 /134 lost = 6.290699 ppl = 539.53
    Valid 4864 samples after epoch: 0030 lost = 6.604473 ppl = 738.391
    Saving best model
    Epoch: 0031 Batch: 50 /134 lost = 6.312382 ppl = 551.357
    Epoch: 0031 Batch: 100 /134 lost = 6.286723 ppl = 537.389
    Valid 4864 samples after epoch: 0031 lost = 6.604904 ppl = 738.709
    Saving best model
    Epoch: 0032 Batch: 50 /134 lost = 6.309933 ppl = 550.008
    Epoch: 0032 Batch: 100 /134 lost = 6.282979 ppl = 535.381
    Valid 4864 samples after epoch: 0032 lost = 6.605711 ppl = 739.305
    Saving best model
    Epoch: 0033 Batch: 50 /134 lost = 6.306998 ppl = 548.396
    Epoch: 0033 Batch: 100 /134 lost = 6.279305 ppl = 533.418
    Valid 4864 samples after epoch: 0033 lost = 6.606589 ppl = 739.955
    Saving best model
    Epoch: 0034 Batch: 50 /134 lost = 6.304029 ppl = 546.77
    Epoch: 0034 Batch: 100 /134 lost = 6.275805 ppl = 531.554
    Valid 4864 samples after epoch: 0034 lost = 6.607591 ppl = 740.697
    Saving best model
    Epoch: 0035 Batch: 50 /134 lost = 6.301175 ppl = 545.212
    Epoch: 0035 Batch: 100 /134 lost = 6.272398 ppl = 529.746
    Valid 4864 samples after epoch: 0035 lost = 6.608626 ppl = 741.464
    Saving best model
    Epoch: 0036 Batch: 50 /134 lost = 6.298427 ppl = 543.716
    Epoch: 0036 Batch: 100 /134 lost = 6.269041 ppl = 527.971
    Valid 4864 samples after epoch: 0036 lost = 6.609792 ppl = 742.329
    Saving best model
    Epoch: 0037 Batch: 50 /134 lost = 6.295786 ppl = 542.282
    Epoch: 0037 Batch: 100 /134 lost = 6.265570 ppl = 526.141
    Valid 4864 samples after epoch: 0037 lost = 6.610907 ppl = 743.157
    Saving best model
    Epoch: 0038 Batch: 50 /134 lost = 6.293225 ppl = 540.895
    Epoch: 0038 Batch: 100 /134 lost = 6.262036 ppl = 524.285
    Valid 4864 samples after epoch: 0038 lost = 6.612088 ppl = 744.035
    Saving best model
    Epoch: 0039 Batch: 50 /134 lost = 6.290748 ppl = 539.557
    Epoch: 0039 Batch: 100 /134 lost = 6.258647 ppl = 522.511
    Valid 4864 samples after epoch: 0039 lost = 6.613333 ppl = 744.962
    Saving best model
    Epoch: 0040 Batch: 50 /134 lost = 6.288329 ppl = 538.253
    Epoch: 0040 Batch: 100 /134 lost = 6.255280 ppl = 520.755
    Valid 4864 samples after epoch: 0040 lost = 6.614647 ppl = 745.941
    Saving best model
    Epoch: 0041 Batch: 50 /134 lost = 6.285957 ppl = 536.978
    Epoch: 0041 Batch: 100 /134 lost = 6.252092 ppl = 519.098
    Valid 4864 samples after epoch: 0041 lost = 6.616121 ppl = 747.042
    Saving best model
    Epoch: 0042 Batch: 50 /134 lost = 6.283644 ppl = 535.737
    Epoch: 0042 Batch: 100 /134 lost = 6.249147 ppl = 517.571
    Valid 4864 samples after epoch: 0042 lost = 6.617699 ppl = 748.222
    Saving best model
    Epoch: 0043 Batch: 50 /134 lost = 6.281417 ppl = 534.546
    Epoch: 0043 Batch: 100 /134 lost = 6.245893 ppl = 515.89
    Valid 4864 samples after epoch: 0043 lost = 6.619299 ppl = 749.419
    Saving best model
    Epoch: 0044 Batch: 50 /134 lost = 6.279278 ppl = 533.404
    Epoch: 0044 Batch: 100 /134 lost = 6.242978 ppl = 514.388
    Valid 4864 samples after epoch: 0044 lost = 6.620900 ppl = 750.62
    Saving best model
    Epoch: 0045 Batch: 50 /134 lost = 6.277143 ppl = 532.266
    Epoch: 0045 Batch: 100 /134 lost = 6.240066 ppl = 512.892
    Valid 4864 samples after epoch: 0045 lost = 6.622673 ppl = 751.952
    Saving best model
    Epoch: 0046 Batch: 50 /134 lost = 6.275028 ppl = 531.141
    Epoch: 0046 Batch: 100 /134 lost = 6.237269 ppl = 511.46
    Valid 4864 samples after epoch: 0046 lost = 6.624490 ppl = 753.32
    Saving best model
    Epoch: 0047 Batch: 50 /134 lost = 6.272930 ppl = 530.028
    Epoch: 0047 Batch: 100 /134 lost = 6.234459 ppl = 510.025
    Valid 4864 samples after epoch: 0047 lost = 6.626406 ppl = 754.764
    Saving best model
    Epoch: 0048 Batch: 50 /134 lost = 6.270840 ppl = 528.921
    Epoch: 0048 Batch: 100 /134 lost = 6.231751 ppl = 508.645
    Valid 4864 samples after epoch: 0048 lost = 6.628375 ppl = 756.253
    Saving best model
    Epoch: 0049 Batch: 50 /134 lost = 6.268721 ppl = 527.802
    Epoch: 0049 Batch: 100 /134 lost = 6.229173 ppl = 507.336
    Valid 4864 samples after epoch: 0049 lost = 6.630354 ppl = 757.751
    Saving best model
    Epoch: 0050 Batch: 50 /134 lost = 6.266644 ppl = 526.707
    Epoch: 0050 Batch: 100 /134 lost = 6.226707 ppl = 506.086
    Valid 4864 samples after epoch: 0050 lost = 6.632268 ppl = 759.202
    Saving best model
    Epoch: 0051 Batch: 50 /134 lost = 6.264775 ppl = 525.723
    Epoch: 0051 Batch: 100 /134 lost = 6.224430 ppl = 504.935
    Valid 4864 samples after epoch: 0051 lost = 6.634138 ppl = 760.623
    Saving best model
    Epoch: 0052 Batch: 50 /134 lost = 6.262993 ppl = 524.787
    Epoch: 0052 Batch: 100 /134 lost = 6.222206 ppl = 503.813
    Valid 4864 samples after epoch: 0052 lost = 6.636049 ppl = 762.078
    Saving best model
    Epoch: 0053 Batch: 50 /134 lost = 6.261136 ppl = 523.813
    Epoch: 0053 Batch: 100 /134 lost = 6.219855 ppl = 502.63
    Valid 4864 samples after epoch: 0053 lost = 6.638035 ppl = 763.593
    Saving best model
    Epoch: 0054 Batch: 50 /134 lost = 6.259079 ppl = 522.738
    Epoch: 0054 Batch: 100 /134 lost = 6.217584 ppl = 501.49
    Valid 4864 samples after epoch: 0054 lost = 6.639627 ppl = 764.81
    Saving best model
    Epoch: 0055 Batch: 50 /134 lost = 6.257339 ppl = 521.829
    Epoch: 0055 Batch: 100 /134 lost = 6.214946 ppl = 500.169
    Valid 4864 samples after epoch: 0055 lost = 6.641460 ppl = 766.213
    Saving best model
    Epoch: 0056 Batch: 50 /134 lost = 6.255640 ppl = 520.942
    Epoch: 0056 Batch: 100 /134 lost = 6.212418 ppl = 498.906
    Valid 4864 samples after epoch: 0056 lost = 6.643480 ppl = 767.762
    Saving best model
    Epoch: 0057 Batch: 50 /134 lost = 6.253509 ppl = 519.834
    Epoch: 0057 Batch: 100 /134 lost = 6.210182 ppl = 497.792
    Valid 4864 samples after epoch: 0057 lost = 6.645400 ppl = 769.237
    Saving best model
    Epoch: 0058 Batch: 50 /134 lost = 6.251482 ppl = 518.781
    Epoch: 0058 Batch: 100 /134 lost = 6.208089 ppl = 496.751
    Valid 4864 samples after epoch: 0058 lost = 6.647293 ppl = 770.696
    Saving best model
    Epoch: 0059 Batch: 50 /134 lost = 6.249368 ppl = 517.686
    Epoch: 0059 Batch: 100 /134 lost = 6.205700 ppl = 495.566
    Valid 4864 samples after epoch: 0059 lost = 6.649370 ppl = 772.298
    Saving best model
    Epoch: 0060 Batch: 50 /134 lost = 6.247674 ppl = 516.809
    Epoch: 0060 Batch: 100 /134 lost = 6.203348 ppl = 494.401
    Valid 4864 samples after epoch: 0060 lost = 6.651466 ppl = 773.918
    Saving best model
    
    Test the RNNLM……………………
    Test 5760 samples with models/3_layers_rnnlm_model_best.ckpt……………………
    lost = 6.543356 ppl = 694.614
    
