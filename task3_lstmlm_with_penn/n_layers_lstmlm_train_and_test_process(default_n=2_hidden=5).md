两层hidden_size均为5, 与pytorch_api版保持一致, 用于对比


```python
!python n_layers_lstmlm_with_penn_assignment(default_n=2_hidden=5).py
```

    The size of the dictionary is: 7613
    The number of the train batch is: 134
    
    Train the LSTMLM……………………
    TextLSTM(
      (embedding): Embedding(7613, 128)
      (W_hq): Linear(in_features=5, out_features=7613, bias=False)
      (sigmoid): Sigmoid()
      (tanh): Tanh()
    )
    Epoch: 0001 Batch: 50 /134 lost = 8.709603 ppl = 6060.84
    Epoch: 0001 Batch: 100 /134 lost = 8.522346 ppl = 5025.83
    Valid 4864 samples after epoch: 0001 lost = 8.432871 ppl = 4595.68
    ------Saving best model------
    Epoch: 0002 Batch: 50 /134 lost = 8.231876 ppl = 3758.88
    Epoch: 0002 Batch: 100 /134 lost = 8.066978 ppl = 3187.45
    Valid 4864 samples after epoch: 0002 lost = 8.010111 ppl = 3011.25
    ------Saving best model------
    Epoch: 0003 Batch: 50 /134 lost = 7.798029 ppl = 2435.8
    Epoch: 0003 Batch: 100 /134 lost = 7.652133 ppl = 2105.13
    Valid 4864 samples after epoch: 0003 lost = 7.632338 ppl = 2063.87
    ------Saving best model------
    Epoch: 0004 Batch: 50 /134 lost = 7.418480 ppl = 1666.5
    Epoch: 0004 Batch: 100 /134 lost = 7.296938 ppl = 1475.77
    Valid 4864 samples after epoch: 0004 lost = 7.316333 ppl = 1504.68
    ------Saving best model------
    Epoch: 0005 Batch: 50 /134 lost = 7.106471 ppl = 1219.83
    Epoch: 0005 Batch: 100 /134 lost = 7.010948 ppl = 1108.7
    Valid 4864 samples after epoch: 0005 lost = 7.069025 ppl = 1175.0
    ------Saving best model------
    Epoch: 0006 Batch: 50 /134 lost = 6.866439 ppl = 959.525
    Epoch: 0006 Batch: 100 /134 lost = 6.794885 ppl = 893.266
    Valid 4864 samples after epoch: 0006 lost = 6.889503 ppl = 981.913
    ------Saving best model------
    Epoch: 0007 Batch: 50 /134 lost = 6.695063 ppl = 808.405
    Epoch: 0007 Batch: 100 /134 lost = 6.643113 ppl = 767.48
    Valid 4864 samples after epoch: 0007 lost = 6.770536 ppl = 871.779
    ------Saving best model------
    Epoch: 0008 Batch: 50 /134 lost = 6.582972 ppl = 722.684
    Epoch: 0008 Batch: 100 /134 lost = 6.545589 ppl = 696.167
    Valid 4864 samples after epoch: 0008 lost = 6.699981 ppl = 812.391
    ------Saving best model------
    Epoch: 0009 Batch: 50 /134 lost = 6.516256 ppl = 676.042
    Epoch: 0009 Batch: 100 /134 lost = 6.488365 ppl = 657.447
    Valid 4864 samples after epoch: 0009 lost = 6.662604 ppl = 782.586
    ------Saving best model------
    Epoch: 0010 Batch: 50 /134 lost = 6.479196 ppl = 651.447
    Epoch: 0010 Batch: 100 /134 lost = 6.456403 ppl = 636.767
    Valid 4864 samples after epoch: 0010 lost = 6.643998 ppl = 768.16
    ------Saving best model------
    Epoch: 0011 Batch: 50 /134 lost = 6.458308 ppl = 637.981
    Epoch: 0011 Batch: 100 /134 lost = 6.437273 ppl = 624.701
    Valid 4864 samples after epoch: 0011 lost = 6.633454 ppl = 760.103
    ------Saving best model------
    Epoch: 0012 Batch: 50 /134 lost = 6.445112 ppl = 629.617
    Epoch: 0012 Batch: 100 /134 lost = 6.424195 ppl = 616.584
    Valid 4864 samples after epoch: 0012 lost = 6.626924 ppl = 755.156
    ------Saving best model------
    Epoch: 0013 Batch: 50 /134 lost = 6.435891 ppl = 623.838
    Epoch: 0013 Batch: 100 /134 lost = 6.414939 ppl = 610.903
    Valid 4864 samples after epoch: 0013 lost = 6.623353 ppl = 752.464
    ------Saving best model------
    Epoch: 0014 Batch: 50 /134 lost = 6.428771 ppl = 619.413
    Epoch: 0014 Batch: 100 /134 lost = 6.407713 ppl = 606.505
    Valid 4864 samples after epoch: 0014 lost = 6.621277 ppl = 750.903
    ------Saving best model------
    Epoch: 0015 Batch: 50 /134 lost = 6.422805 ppl = 615.728
    Epoch: 0015 Batch: 100 /134 lost = 6.401524 ppl = 602.763
    Valid 4864 samples after epoch: 0015 lost = 6.619871 ppl = 749.848
    ------Saving best model------
    Epoch: 0016 Batch: 50 /134 lost = 6.417499 ppl = 612.469
    Epoch: 0016 Batch: 100 /134 lost = 6.395757 ppl = 599.297
    Valid 4864 samples after epoch: 0016 lost = 6.618832 ppl = 749.069
    ------Saving best model------
    Epoch: 0017 Batch: 50 /134 lost = 6.412631 ppl = 609.495
    Epoch: 0017 Batch: 100 /134 lost = 6.390257 ppl = 596.01
    Valid 4864 samples after epoch: 0017 lost = 6.618285 ppl = 748.66
    ------Saving best model------
    Epoch: 0018 Batch: 50 /134 lost = 6.408450 ppl = 606.952
    Epoch: 0018 Batch: 100 /134 lost = 6.385542 ppl = 593.206
    Valid 4864 samples after epoch: 0018 lost = 6.618260 ppl = 748.641
    ------Saving best model------
    Epoch: 0019 Batch: 50 /134 lost = 6.404824 ppl = 604.755
    Epoch: 0019 Batch: 100 /134 lost = 6.381361 ppl = 590.731
    Valid 4864 samples after epoch: 0019 lost = 6.618459 ppl = 748.79
    Epoch: 0020 Batch: 50 /134 lost = 6.401467 ppl = 602.729
    Epoch: 0020 Batch: 100 /134 lost = 6.377381 ppl = 588.385
    Valid 4864 samples after epoch: 0020 lost = 6.618709 ppl = 748.977
    Epoch: 0021 Batch: 50 /134 lost = 6.398191 ppl = 600.757
    Epoch: 0021 Batch: 100 /134 lost = 6.373597 ppl = 586.163
    Valid 4864 samples after epoch: 0021 lost = 6.619141 ppl = 749.301
    Epoch: 0022 Batch: 50 /134 lost = 6.394880 ppl = 598.771
    Epoch: 0022 Batch: 100 /134 lost = 6.369931 ppl = 584.018
    Valid 4864 samples after epoch: 0022 lost = 6.619606 ppl = 749.649
    Epoch: 0023 Batch: 50 /134 lost = 6.391491 ppl = 596.746
    Epoch: 0023 Batch: 100 /134 lost = 6.366179 ppl = 581.83
    Valid 4864 samples after epoch: 0023 lost = 6.620039 ppl = 749.975
    Epoch: 0024 Batch: 50 /134 lost = 6.388181 ppl = 594.774
    Epoch: 0024 Batch: 100 /134 lost = 6.362529 ppl = 579.711
    Valid 4864 samples after epoch: 0024 lost = 6.620563 ppl = 750.367
    Epoch: 0025 Batch: 50 /134 lost = 6.385061 ppl = 592.921
    Epoch: 0025 Batch: 100 /134 lost = 6.359101 ppl = 577.727
    Valid 4864 samples after epoch: 0025 lost = 6.621197 ppl = 750.843
    Epoch: 0026 Batch: 50 /134 lost = 6.382098 ppl = 591.167
    Epoch: 0026 Batch: 100 /134 lost = 6.355851 ppl = 575.852
    Valid 4864 samples after epoch: 0026 lost = 6.621920 ppl = 751.387
    Epoch: 0027 Batch: 50 /134 lost = 6.379224 ppl = 589.47
    Epoch: 0027 Batch: 100 /134 lost = 6.352701 ppl = 574.041
    Valid 4864 samples after epoch: 0027 lost = 6.622717 ppl = 751.986
    Epoch: 0028 Batch: 50 /134 lost = 6.376431 ppl = 587.826
    Epoch: 0028 Batch: 100 /134 lost = 6.349616 ppl = 572.273
    Valid 4864 samples after epoch: 0028 lost = 6.623590 ppl = 752.642
    Epoch: 0029 Batch: 50 /134 lost = 6.373730 ppl = 586.241
    Epoch: 0029 Batch: 100 /134 lost = 6.346625 ppl = 570.564
    Valid 4864 samples after epoch: 0029 lost = 6.624544 ppl = 753.361
    Epoch: 0030 Batch: 50 /134 lost = 6.371126 ppl = 584.716
    Epoch: 0030 Batch: 100 /134 lost = 6.343763 ppl = 568.933
    Valid 4864 samples after epoch: 0030 lost = 6.625577 ppl = 754.139
    Epoch: 0031 Batch: 50 /134 lost = 6.368604 ppl = 583.243
    Epoch: 0031 Batch: 100 /134 lost = 6.341015 ppl = 567.372
    Valid 4864 samples after epoch: 0031 lost = 6.626674 ppl = 754.967
    Epoch: 0032 Batch: 50 /134 lost = 6.366147 ppl = 581.812
    Epoch: 0032 Batch: 100 /134 lost = 6.338338 ppl = 565.855
    Valid 4864 samples after epoch: 0032 lost = 6.627825 ppl = 755.837
    Epoch: 0033 Batch: 50 /134 lost = 6.363737 ppl = 580.411
    Epoch: 0033 Batch: 100 /134 lost = 6.335705 ppl = 564.367
    Valid 4864 samples after epoch: 0033 lost = 6.629017 ppl = 756.738
    Epoch: 0034 Batch: 50 /134 lost = 6.361335 ppl = 579.019
    Epoch: 0034 Batch: 100 /134 lost = 6.333098 ppl = 562.898
    Valid 4864 samples after epoch: 0034 lost = 6.630236 ppl = 757.661
    Epoch: 0035 Batch: 50 /134 lost = 6.358916 ppl = 577.62
    Epoch: 0035 Batch: 100 /134 lost = 6.330515 ppl = 561.446
    Valid 4864 samples after epoch: 0035 lost = 6.631477 ppl = 758.602
    Epoch: 0036 Batch: 50 /134 lost = 6.356503 ppl = 576.228
    Epoch: 0036 Batch: 100 /134 lost = 6.327957 ppl = 560.011
    Valid 4864 samples after epoch: 0036 lost = 6.632728 ppl = 759.552
    Epoch: 0037 Batch: 50 /134 lost = 6.354124 ppl = 574.858
    Epoch: 0037 Batch: 100 /134 lost = 6.325420 ppl = 558.593
    Valid 4864 samples after epoch: 0037 lost = 6.633975 ppl = 760.499
    Epoch: 0038 Batch: 50 /134 lost = 6.351788 ppl = 573.517
    Epoch: 0038 Batch: 100 /134 lost = 6.322890 ppl = 557.181
    Valid 4864 samples after epoch: 0038 lost = 6.635213 ppl = 761.441
    Epoch: 0039 Batch: 50 /134 lost = 6.349478 ppl = 572.194
    Epoch: 0039 Batch: 100 /134 lost = 6.320341 ppl = 555.763
    Valid 4864 samples after epoch: 0039 lost = 6.636459 ppl = 762.39
    Epoch: 0040 Batch: 50 /134 lost = 6.347160 ppl = 570.869
    Epoch: 0040 Batch: 100 /134 lost = 6.317752 ppl = 554.326
    Valid 4864 samples after epoch: 0040 lost = 6.637709 ppl = 763.344
    Epoch: 0041 Batch: 50 /134 lost = 6.344813 ppl = 569.531
    Epoch: 0041 Batch: 100 /134 lost = 6.315091 ppl = 552.852
    Valid 4864 samples after epoch: 0041 lost = 6.638928 ppl = 764.275
    Epoch: 0042 Batch: 50 /134 lost = 6.342391 ppl = 568.153
    Epoch: 0042 Batch: 100 /134 lost = 6.312198 ppl = 551.255
    Valid 4864 samples after epoch: 0042 lost = 6.640012 ppl = 765.104
    Epoch: 0043 Batch: 50 /134 lost = 6.339849 ppl = 566.71
    Epoch: 0043 Batch: 100 /134 lost = 6.309086 ppl = 549.542
    Valid 4864 samples after epoch: 0043 lost = 6.641154 ppl = 765.979
    Epoch: 0044 Batch: 50 /134 lost = 6.337345 ppl = 565.294
    Epoch: 0044 Batch: 100 /134 lost = 6.306265 ppl = 547.994
    Valid 4864 samples after epoch: 0044 lost = 6.642391 ppl = 766.927
    Epoch: 0045 Batch: 50 /134 lost = 6.334907 ppl = 563.917
    Epoch: 0045 Batch: 100 /134 lost = 6.303487 ppl = 546.474
    Valid 4864 samples after epoch: 0045 lost = 6.643621 ppl = 767.871
    Epoch: 0046 Batch: 50 /134 lost = 6.332467 ppl = 562.542
    Epoch: 0046 Batch: 100 /134 lost = 6.300687 ppl = 544.946
    Valid 4864 samples after epoch: 0046 lost = 6.644845 ppl = 768.811
    Epoch: 0047 Batch: 50 /134 lost = 6.330054 ppl = 561.187
    Epoch: 0047 Batch: 100 /134 lost = 6.297972 ppl = 543.468
    Valid 4864 samples after epoch: 0047 lost = 6.646096 ppl = 769.773
    Epoch: 0048 Batch: 50 /134 lost = 6.327735 ppl = 559.887
    Epoch: 0048 Batch: 100 /134 lost = 6.295314 ppl = 542.026
    Valid 4864 samples after epoch: 0048 lost = 6.647358 ppl = 770.745
    Epoch: 0049 Batch: 50 /134 lost = 6.325460 ppl = 558.615
    Epoch: 0049 Batch: 100 /134 lost = 6.292688 ppl = 540.604
    Valid 4864 samples after epoch: 0049 lost = 6.648637 ppl = 771.731
    Epoch: 0050 Batch: 50 /134 lost = 6.323213 ppl = 557.361
    Epoch: 0050 Batch: 100 /134 lost = 6.290086 ppl = 539.2
    Valid 4864 samples after epoch: 0050 lost = 6.649934 ppl = 772.733
    Epoch: 0051 Batch: 50 /134 lost = 6.320989 ppl = 556.123
    Epoch: 0051 Batch: 100 /134 lost = 6.287507 ppl = 537.811
    Valid 4864 samples after epoch: 0051 lost = 6.651248 ppl = 773.749
    Epoch: 0052 Batch: 50 /134 lost = 6.318786 ppl = 554.899
    Epoch: 0052 Batch: 100 /134 lost = 6.284945 ppl = 536.435
    Valid 4864 samples after epoch: 0052 lost = 6.652578 ppl = 774.779
    Epoch: 0053 Batch: 50 /134 lost = 6.316600 ppl = 553.687
    Epoch: 0053 Batch: 100 /134 lost = 6.282405 ppl = 535.074
    Valid 4864 samples after epoch: 0053 lost = 6.653923 ppl = 775.822
    Epoch: 0054 Batch: 50 /134 lost = 6.314422 ppl = 552.482
    Epoch: 0054 Batch: 100 /134 lost = 6.279883 ppl = 533.726
    Valid 4864 samples after epoch: 0054 lost = 6.655280 ppl = 776.876
    Epoch: 0055 Batch: 50 /134 lost = 6.312244 ppl = 551.281
    Epoch: 0055 Batch: 100 /134 lost = 6.277390 ppl = 532.398
    Valid 4864 samples after epoch: 0055 lost = 6.656649 ppl = 777.939
    Epoch: 0056 Batch: 50 /134 lost = 6.310067 ppl = 550.082
    Epoch: 0056 Batch: 100 /134 lost = 6.274928 ppl = 531.088
    Valid 4864 samples after epoch: 0056 lost = 6.658031 ppl = 779.016
    Epoch: 0057 Batch: 50 /134 lost = 6.307907 ppl = 548.895
    Epoch: 0057 Batch: 100 /134 lost = 6.272501 ppl = 529.801
    Valid 4864 samples after epoch: 0057 lost = 6.659432 ppl = 780.108
    Epoch: 0058 Batch: 50 /134 lost = 6.305794 ppl = 547.736
    Epoch: 0058 Batch: 100 /134 lost = 6.270102 ppl = 528.531
    Valid 4864 samples after epoch: 0058 lost = 6.660854 ppl = 781.218
    Epoch: 0059 Batch: 50 /134 lost = 6.303735 ppl = 546.61
    Epoch: 0059 Batch: 100 /134 lost = 6.267719 ppl = 527.273
    Valid 4864 samples after epoch: 0059 lost = 6.662295 ppl = 782.345
    Epoch: 0060 Batch: 50 /134 lost = 6.301730 ppl = 545.515
    Epoch: 0060 Batch: 100 /134 lost = 6.265346 ppl = 526.024
    Valid 4864 samples after epoch: 0060 lost = 6.663756 ppl = 783.488
    Epoch: 0061 Batch: 50 /134 lost = 6.299768 ppl = 544.446
    Epoch: 0061 Batch: 100 /134 lost = 6.262997 ppl = 524.789
    Valid 4864 samples after epoch: 0061 lost = 6.665235 ppl = 784.648
    Epoch: 0062 Batch: 50 /134 lost = 6.297842 ppl = 543.398
    Epoch: 0062 Batch: 100 /134 lost = 6.260685 ppl = 523.578
    Valid 4864 samples after epoch: 0062 lost = 6.666732 ppl = 785.823
    Epoch: 0063 Batch: 50 /134 lost = 6.295948 ppl = 542.37
    Epoch: 0063 Batch: 100 /134 lost = 6.258415 ppl = 522.39
    Valid 4864 samples after epoch: 0063 lost = 6.668245 ppl = 787.013
    Epoch: 0064 Batch: 50 /134 lost = 6.294079 ppl = 541.357
    Epoch: 0064 Batch: 100 /134 lost = 6.256183 ppl = 521.225
    Valid 4864 samples after epoch: 0064 lost = 6.669774 ppl = 788.217
    Epoch: 0065 Batch: 50 /134 lost = 6.292238 ppl = 540.361
    Epoch: 0065 Batch: 100 /134 lost = 6.253985 ppl = 520.081
    Valid 4864 samples after epoch: 0065 lost = 6.671319 ppl = 789.436
    Epoch: 0066 Batch: 50 /134 lost = 6.290420 ppl = 539.38
    Epoch: 0066 Batch: 100 /134 lost = 6.251817 ppl = 518.955
    Valid 4864 samples after epoch: 0066 lost = 6.672878 ppl = 790.668
    Epoch: 0067 Batch: 50 /134 lost = 6.288625 ppl = 538.413
    Epoch: 0067 Batch: 100 /134 lost = 6.249673 ppl = 517.843
    Valid 4864 samples after epoch: 0067 lost = 6.674452 ppl = 791.913
    Epoch: 0068 Batch: 50 /134 lost = 6.286856 ppl = 537.461
    Epoch: 0068 Batch: 100 /134 lost = 6.247554 ppl = 516.747
    Valid 4864 samples after epoch: 0068 lost = 6.676039 ppl = 793.171
    Epoch: 0069 Batch: 50 /134 lost = 6.285106 ppl = 536.521
    Epoch: 0069 Batch: 100 /134 lost = 6.245457 ppl = 515.665
    Valid 4864 samples after epoch: 0069 lost = 6.677640 ppl = 794.442
    Epoch: 0070 Batch: 50 /134 lost = 6.283379 ppl = 535.595
    Epoch: 0070 Batch: 100 /134 lost = 6.243383 ppl = 514.596
    Valid 4864 samples after epoch: 0070 lost = 6.679254 ppl = 795.725
    Epoch: 0071 Batch: 50 /134 lost = 6.281671 ppl = 534.681
    Epoch: 0071 Batch: 100 /134 lost = 6.241328 ppl = 513.54
    Valid 4864 samples after epoch: 0071 lost = 6.680881 ppl = 797.021
    Epoch: 0072 Batch: 50 /134 lost = 6.279985 ppl = 533.781
    Epoch: 0072 Batch: 100 /134 lost = 6.239296 ppl = 512.498
    Valid 4864 samples after epoch: 0072 lost = 6.682522 ppl = 798.33
    Epoch: 0073 Batch: 50 /134 lost = 6.278315 ppl = 532.89
    Epoch: 0073 Batch: 100 /134 lost = 6.237284 ppl = 511.467
    Valid 4864 samples after epoch: 0073 lost = 6.684174 ppl = 799.65
    Epoch: 0074 Batch: 50 /134 lost = 6.276665 ppl = 532.011
    Epoch: 0074 Batch: 100 /134 lost = 6.235291 ppl = 510.449
    Valid 4864 samples after epoch: 0074 lost = 6.685837 ppl = 800.98
    Epoch: 0075 Batch: 50 /134 lost = 6.275032 ppl = 531.143
    Epoch: 0075 Batch: 100 /134 lost = 6.233318 ppl = 509.443
    Valid 4864 samples after epoch: 0075 lost = 6.687509 ppl = 802.321
    Epoch: 0076 Batch: 50 /134 lost = 6.273417 ppl = 530.286
    Epoch: 0076 Batch: 100 /134 lost = 6.231366 ppl = 508.45
    Valid 4864 samples after epoch: 0076 lost = 6.689189 ppl = 803.67
    Epoch: 0077 Batch: 50 /134 lost = 6.271816 ppl = 529.438
    Epoch: 0077 Batch: 100 /134 lost = 6.229434 ppl = 507.468
    Valid 4864 samples after epoch: 0077 lost = 6.690878 ppl = 805.029
    Epoch: 0078 Batch: 50 /134 lost = 6.270232 ppl = 528.6
    Epoch: 0078 Batch: 100 /134 lost = 6.227524 ppl = 506.5
    Valid 4864 samples after epoch: 0078 lost = 6.692575 ppl = 806.396
    Epoch: 0079 Batch: 50 /134 lost = 6.268664 ppl = 527.772
    Epoch: 0079 Batch: 100 /134 lost = 6.225634 ppl = 505.544
    Valid 4864 samples after epoch: 0079 lost = 6.694281 ppl = 807.773
    Epoch: 0080 Batch: 50 /134 lost = 6.267111 ppl = 526.953
    Epoch: 0080 Batch: 100 /134 lost = 6.223768 ppl = 504.601
    Valid 4864 samples after epoch: 0080 lost = 6.695997 ppl = 809.16
    Epoch: 0081 Batch: 50 /134 lost = 6.265574 ppl = 526.144
    Epoch: 0081 Batch: 100 /134 lost = 6.221924 ppl = 503.671
    Valid 4864 samples after epoch: 0081 lost = 6.697725 ppl = 810.56
    Epoch: 0082 Batch: 50 /134 lost = 6.264056 ppl = 525.345
    Epoch: 0082 Batch: 100 /134 lost = 6.220107 ppl = 502.757
    Valid 4864 samples after epoch: 0082 lost = 6.699465 ppl = 811.971
    Epoch: 0083 Batch: 50 /134 lost = 6.262554 ppl = 524.557
    Epoch: 0083 Batch: 100 /134 lost = 6.218314 ppl = 501.856
    Valid 4864 samples after epoch: 0083 lost = 6.701217 ppl = 813.395
    Epoch: 0084 Batch: 50 /134 lost = 6.261070 ppl = 523.779
    Epoch: 0084 Batch: 100 /134 lost = 6.216547 ppl = 500.97
    Valid 4864 samples after epoch: 0084 lost = 6.702981 ppl = 814.831
    Epoch: 0085 Batch: 50 /134 lost = 6.259606 ppl = 523.013
    Epoch: 0085 Batch: 100 /134 lost = 6.214807 ppl = 500.099
    Valid 4864 samples after epoch: 0085 lost = 6.704756 ppl = 816.279
    Epoch: 0086 Batch: 50 /134 lost = 6.258164 ppl = 522.259
    Epoch: 0086 Batch: 100 /134 lost = 6.213088 ppl = 499.241
    Valid 4864 samples after epoch: 0086 lost = 6.706542 ppl = 817.738
    Epoch: 0087 Batch: 50 /134 lost = 6.256742 ppl = 521.517
    Epoch: 0087 Batch: 100 /134 lost = 6.211393 ppl = 498.395
    Valid 4864 samples after epoch: 0087 lost = 6.708338 ppl = 819.208
    Epoch: 0088 Batch: 50 /134 lost = 6.255343 ppl = 520.788
    Epoch: 0088 Batch: 100 /134 lost = 6.209716 ppl = 497.56
    Valid 4864 samples after epoch: 0088 lost = 6.710143 ppl = 820.688
    Epoch: 0089 Batch: 50 /134 lost = 6.253967 ppl = 520.072
    Epoch: 0089 Batch: 100 /134 lost = 6.208058 ppl = 496.736
    Valid 4864 samples after epoch: 0089 lost = 6.711955 ppl = 822.176
    Epoch: 0090 Batch: 50 /134 lost = 6.252610 ppl = 519.367
    Epoch: 0090 Batch: 100 /134 lost = 6.206419 ppl = 495.922
    Valid 4864 samples after epoch: 0090 lost = 6.713773 ppl = 823.673
    Epoch: 0091 Batch: 50 /134 lost = 6.251273 ppl = 518.673
    Epoch: 0091 Batch: 100 /134 lost = 6.204795 ppl = 495.118
    Valid 4864 samples after epoch: 0091 lost = 6.715597 ppl = 825.176
    Epoch: 0092 Batch: 50 /134 lost = 6.249956 ppl = 517.99
    Epoch: 0092 Batch: 100 /134 lost = 6.203189 ppl = 494.323
    Valid 4864 samples after epoch: 0092 lost = 6.717424 ppl = 826.685
    Epoch: 0093 Batch: 50 /134 lost = 6.248659 ppl = 517.318
    Epoch: 0093 Batch: 100 /134 lost = 6.201598 ppl = 493.537
    Valid 4864 samples after epoch: 0093 lost = 6.719254 ppl = 828.2
    Epoch: 0094 Batch: 50 /134 lost = 6.247376 ppl = 516.655
    Epoch: 0094 Batch: 100 /134 lost = 6.200026 ppl = 492.762
    Valid 4864 samples after epoch: 0094 lost = 6.721085 ppl = 829.717
    Epoch: 0095 Batch: 50 /134 lost = 6.246113 ppl = 516.003
    Epoch: 0095 Batch: 100 /134 lost = 6.198470 ppl = 491.996
    Valid 4864 samples after epoch: 0095 lost = 6.722916 ppl = 831.238
    Epoch: 0096 Batch: 50 /134 lost = 6.244867 ppl = 515.361
    Epoch: 0096 Batch: 100 /134 lost = 6.196929 ppl = 491.238
    Valid 4864 samples after epoch: 0096 lost = 6.724746 ppl = 832.761
    Epoch: 0097 Batch: 50 /134 lost = 6.243638 ppl = 514.728
    Epoch: 0097 Batch: 100 /134 lost = 6.195404 ppl = 490.489
    Valid 4864 samples after epoch: 0097 lost = 6.726575 ppl = 834.285
    Epoch: 0098 Batch: 50 /134 lost = 6.242424 ppl = 514.103
    Epoch: 0098 Batch: 100 /134 lost = 6.193891 ppl = 489.748
    Valid 4864 samples after epoch: 0098 lost = 6.728401 ppl = 835.81
    Epoch: 0099 Batch: 50 /134 lost = 6.241224 ppl = 513.487
    Epoch: 0099 Batch: 100 /134 lost = 6.192390 ppl = 489.014
    Valid 4864 samples after epoch: 0099 lost = 6.730225 ppl = 837.336
    Epoch: 0100 Batch: 50 /134 lost = 6.240041 ppl = 512.879
    Epoch: 0100 Batch: 100 /134 lost = 6.190899 ppl = 488.285
    Valid 4864 samples after epoch: 0100 lost = 6.732045 ppl = 838.861
    Epoch: 0101 Batch: 50 /134 lost = 6.238869 ppl = 512.279
    Epoch: 0101 Batch: 100 /134 lost = 6.189419 ppl = 487.563
    Valid 4864 samples after epoch: 0101 lost = 6.733860 ppl = 840.385
    Epoch: 0102 Batch: 50 /134 lost = 6.237711 ppl = 511.686
    Epoch: 0102 Batch: 100 /134 lost = 6.187948 ppl = 486.846
    Valid 4864 samples after epoch: 0102 lost = 6.735668 ppl = 841.906
    Epoch: 0103 Batch: 50 /134 lost = 6.236564 ppl = 511.099
    Epoch: 0103 Batch: 100 /134 lost = 6.186490 ppl = 486.137
    Valid 4864 samples after epoch: 0103 lost = 6.737471 ppl = 843.425
    Epoch: 0104 Batch: 50 /134 lost = 6.235429 ppl = 510.52
    Epoch: 0104 Batch: 100 /134 lost = 6.185046 ppl = 485.435
    Valid 4864 samples after epoch: 0104 lost = 6.739265 ppl = 844.939
    Epoch: 0105 Batch: 50 /134 lost = 6.234305 ppl = 509.946
    Epoch: 0105 Batch: 100 /134 lost = 6.183616 ppl = 484.742
    Valid 4864 samples after epoch: 0105 lost = 6.741051 ppl = 846.45
    Epoch: 0106 Batch: 50 /134 lost = 6.233191 ppl = 509.378
    Epoch: 0106 Batch: 100 /134 lost = 6.182203 ppl = 484.057
    Valid 4864 samples after epoch: 0106 lost = 6.742829 ppl = 847.956
    Epoch: 0107 Batch: 50 /134 lost = 6.232088 ppl = 508.817
    Epoch: 0107 Batch: 100 /134 lost = 6.180805 ppl = 483.381
    Valid 4864 samples after epoch: 0107 lost = 6.744596 ppl = 849.456
    Epoch: 0108 Batch: 50 /134 lost = 6.230992 ppl = 508.26
    Epoch: 0108 Batch: 100 /134 lost = 6.179425 ppl = 482.714
    Valid 4864 samples after epoch: 0108 lost = 6.746353 ppl = 850.95
    Epoch: 0109 Batch: 50 /134 lost = 6.229904 ppl = 507.707
    Epoch: 0109 Batch: 100 /134 lost = 6.178061 ppl = 482.056
    Valid 4864 samples after epoch: 0109 lost = 6.748099 ppl = 852.436
    Epoch: 0110 Batch: 50 /134 lost = 6.228825 ppl = 507.159
    Epoch: 0110 Batch: 100 /134 lost = 6.176711 ppl = 481.406
    Valid 4864 samples after epoch: 0110 lost = 6.749832 ppl = 853.915
    Epoch: 0111 Batch: 50 /134 lost = 6.227752 ppl = 506.615
    Epoch: 0111 Batch: 100 /134 lost = 6.175376 ppl = 480.764
    Valid 4864 samples after epoch: 0111 lost = 6.751553 ppl = 855.386
    Epoch: 0112 Batch: 50 /134 lost = 6.226686 ppl = 506.075
    Epoch: 0112 Batch: 100 /134 lost = 6.174056 ppl = 480.129
    Valid 4864 samples after epoch: 0112 lost = 6.753261 ppl = 856.849
    Epoch: 0113 Batch: 50 /134 lost = 6.225624 ppl = 505.538
    Epoch: 0113 Batch: 100 /134 lost = 6.172748 ppl = 479.502
    Valid 4864 samples after epoch: 0113 lost = 6.754955 ppl = 858.301
    Epoch: 0114 Batch: 50 /134 lost = 6.224570 ppl = 505.006
    Epoch: 0114 Batch: 100 /134 lost = 6.171453 ppl = 478.881
    Valid 4864 samples after epoch: 0114 lost = 6.756635 ppl = 859.744
    Epoch: 0115 Batch: 50 /134 lost = 6.223521 ppl = 504.476
    Epoch: 0115 Batch: 100 /134 lost = 6.170169 ppl = 478.267
    Valid 4864 samples after epoch: 0115 lost = 6.758300 ppl = 861.177
    Epoch: 0116 Batch: 50 /134 lost = 6.222476 ppl = 503.949
    Epoch: 0116 Batch: 100 /134 lost = 6.168895 ppl = 477.658
    Valid 4864 samples after epoch: 0116 lost = 6.759949 ppl = 862.599
    Epoch: 0117 Batch: 50 /134 lost = 6.221437 ppl = 503.426
    Epoch: 0117 Batch: 100 /134 lost = 6.167632 ppl = 477.055
    Valid 4864 samples after epoch: 0117 lost = 6.761582 ppl = 864.008
    Epoch: 0118 Batch: 50 /134 lost = 6.220402 ppl = 502.905
    Epoch: 0118 Batch: 100 /134 lost = 6.166381 ppl = 476.459
    Valid 4864 samples after epoch: 0118 lost = 6.763198 ppl = 865.406
    Epoch: 0119 Batch: 50 /134 lost = 6.219373 ppl = 502.388
    Epoch: 0119 Batch: 100 /134 lost = 6.165138 ppl = 475.867
    Valid 4864 samples after epoch: 0119 lost = 6.764797 ppl = 866.79
    Epoch: 0120 Batch: 50 /134 lost = 6.218349 ppl = 501.874
    Epoch: 0120 Batch: 100 /134 lost = 6.163907 ppl = 475.281
    Valid 4864 samples after epoch: 0120 lost = 6.766377 ppl = 868.161
    Epoch: 0121 Batch: 50 /134 lost = 6.217330 ppl = 501.363
    Epoch: 0121 Batch: 100 /134 lost = 6.162683 ppl = 474.7
    Valid 4864 samples after epoch: 0121 lost = 6.767938 ppl = 869.517
    Epoch: 0122 Batch: 50 /134 lost = 6.216313 ppl = 500.853
    Epoch: 0122 Batch: 100 /134 lost = 6.161470 ppl = 474.125
    Valid 4864 samples after epoch: 0122 lost = 6.769479 ppl = 870.858
    Epoch: 0123 Batch: 50 /134 lost = 6.215301 ppl = 500.346
    Epoch: 0123 Batch: 100 /134 lost = 6.160264 ppl = 473.553
    Valid 4864 samples after epoch: 0123 lost = 6.771000 ppl = 872.184
    Epoch: 0124 Batch: 50 /134 lost = 6.214293 ppl = 499.842
    Epoch: 0124 Batch: 100 /134 lost = 6.159070 ppl = 472.988
    Valid 4864 samples after epoch: 0124 lost = 6.772500 ppl = 873.493
    Epoch: 0125 Batch: 50 /134 lost = 6.213289 ppl = 499.341
    Epoch: 0125 Batch: 100 /134 lost = 6.157885 ppl = 472.428
    Valid 4864 samples after epoch: 0125 lost = 6.773978 ppl = 874.785
    Epoch: 0126 Batch: 50 /134 lost = 6.212288 ppl = 498.841
    Epoch: 0126 Batch: 100 /134 lost = 6.156709 ppl = 471.872
    Valid 4864 samples after epoch: 0126 lost = 6.775434 ppl = 876.059
    Epoch: 0127 Batch: 50 /134 lost = 6.211289 ppl = 498.343
    Epoch: 0127 Batch: 100 /134 lost = 6.155542 ppl = 471.322
    Valid 4864 samples after epoch: 0127 lost = 6.776867 ppl = 877.316
    Epoch: 0128 Batch: 50 /134 lost = 6.210294 ppl = 497.847
    Epoch: 0128 Batch: 100 /134 lost = 6.154387 ppl = 470.778
    Valid 4864 samples after epoch: 0128 lost = 6.778276 ppl = 878.552
    Epoch: 0129 Batch: 50 /134 lost = 6.209301 ppl = 497.353
    Epoch: 0129 Batch: 100 /134 lost = 6.153244 ppl = 470.24
    Valid 4864 samples after epoch: 0129 lost = 6.779661 ppl = 879.77
    Epoch: 0130 Batch: 50 /134 lost = 6.208308 ppl = 496.86
    Epoch: 0130 Batch: 100 /134 lost = 6.152111 ppl = 469.708
    Valid 4864 samples after epoch: 0130 lost = 6.781019 ppl = 880.966
    Epoch: 0131 Batch: 50 /134 lost = 6.207318 ppl = 496.368
    Epoch: 0131 Batch: 100 /134 lost = 6.150990 ppl = 469.181
    Valid 4864 samples after epoch: 0131 lost = 6.782353 ppl = 882.142
    Epoch: 0132 Batch: 50 /134 lost = 6.206328 ppl = 495.877
    Epoch: 0132 Batch: 100 /134 lost = 6.149880 ppl = 468.661
    Valid 4864 samples after epoch: 0132 lost = 6.783658 ppl = 883.294
    Epoch: 0133 Batch: 50 /134 lost = 6.205339 ppl = 495.387
    Epoch: 0133 Batch: 100 /134 lost = 6.148782 ppl = 468.147
    Valid 4864 samples after epoch: 0133 lost = 6.784938 ppl = 884.425
    Epoch: 0134 Batch: 50 /134 lost = 6.204348 ppl = 494.896
    Epoch: 0134 Batch: 100 /134 lost = 6.147696 ppl = 467.639
    Valid 4864 samples after epoch: 0134 lost = 6.786187 ppl = 885.53
    Epoch: 0135 Batch: 50 /134 lost = 6.203357 ppl = 494.406
    Epoch: 0135 Batch: 100 /134 lost = 6.146622 ppl = 467.137
    Valid 4864 samples after epoch: 0135 lost = 6.787408 ppl = 886.613
    Epoch: 0136 Batch: 50 /134 lost = 6.202366 ppl = 493.916
    Epoch: 0136 Batch: 100 /134 lost = 6.145558 ppl = 466.64
    Valid 4864 samples after epoch: 0136 lost = 6.788599 ppl = 887.669
    Epoch: 0137 Batch: 50 /134 lost = 6.201373 ppl = 493.426
    Epoch: 0137 Batch: 100 /134 lost = 6.144503 ppl = 466.148
    Valid 4864 samples after epoch: 0137 lost = 6.789763 ppl = 888.703
    Epoch: 0138 Batch: 50 /134 lost = 6.200381 ppl = 492.937
    Epoch: 0138 Batch: 100 /134 lost = 6.143460 ppl = 465.662
    Valid 4864 samples after epoch: 0138 lost = 6.790898 ppl = 889.712
    Epoch: 0139 Batch: 50 /134 lost = 6.199391 ppl = 492.449
    Epoch: 0139 Batch: 100 /134 lost = 6.142424 ppl = 465.18
    Valid 4864 samples after epoch: 0139 lost = 6.792006 ppl = 890.698
    Epoch: 0140 Batch: 50 /134 lost = 6.198404 ppl = 491.963
    Epoch: 0140 Batch: 100 /134 lost = 6.141394 ppl = 464.701
    Valid 4864 samples after epoch: 0140 lost = 6.793087 ppl = 891.662
    Epoch: 0141 Batch: 50 /134 lost = 6.197423 ppl = 491.481
    Epoch: 0141 Batch: 100 /134 lost = 6.140368 ppl = 464.224
    Valid 4864 samples after epoch: 0141 lost = 6.794144 ppl = 892.604
    Epoch: 0142 Batch: 50 /134 lost = 6.196453 ppl = 491.004
    Epoch: 0142 Batch: 100 /134 lost = 6.139347 ppl = 463.751
    Valid 4864 samples after epoch: 0142 lost = 6.795174 ppl = 893.525
    Epoch: 0143 Batch: 50 /134 lost = 6.195488 ppl = 490.531
    Epoch: 0143 Batch: 100 /134 lost = 6.138330 ppl = 463.279
    Valid 4864 samples after epoch: 0143 lost = 6.796183 ppl = 894.426
    Epoch: 0144 Batch: 50 /134 lost = 6.194535 ppl = 490.064
    Epoch: 0144 Batch: 100 /134 lost = 6.137316 ppl = 462.81
    Valid 4864 samples after epoch: 0144 lost = 6.797164 ppl = 895.305
    Epoch: 0145 Batch: 50 /134 lost = 6.193594 ppl = 489.603
    Epoch: 0145 Batch: 100 /134 lost = 6.136306 ppl = 462.342
    Valid 4864 samples after epoch: 0145 lost = 6.798125 ppl = 896.166
    Epoch: 0146 Batch: 50 /134 lost = 6.192663 ppl = 489.147
    Epoch: 0146 Batch: 100 /134 lost = 6.135299 ppl = 461.877
    Valid 4864 samples after epoch: 0146 lost = 6.799057 ppl = 897.001
    Epoch: 0147 Batch: 50 /134 lost = 6.191741 ppl = 488.696
    Epoch: 0147 Batch: 100 /134 lost = 6.134296 ppl = 461.414
    Valid 4864 samples after epoch: 0147 lost = 6.799971 ppl = 897.821
    Epoch: 0148 Batch: 50 /134 lost = 6.190830 ppl = 488.251
    Epoch: 0148 Batch: 100 /134 lost = 6.133297 ppl = 460.954
    Valid 4864 samples after epoch: 0148 lost = 6.800853 ppl = 898.613
    Epoch: 0149 Batch: 50 /134 lost = 6.189927 ppl = 487.81
    Epoch: 0149 Batch: 100 /134 lost = 6.132305 ppl = 460.496
    Valid 4864 samples after epoch: 0149 lost = 6.801718 ppl = 899.391
    Epoch: 0150 Batch: 50 /134 lost = 6.189030 ppl = 487.373
    Epoch: 0150 Batch: 100 /134 lost = 6.131316 ppl = 460.041
    Valid 4864 samples after epoch: 0150 lost = 6.802551 ppl = 900.141
    
    Test the LSTMLM……………………
    Test 5760 samples with models/2_layers_lstmlm_model_(hidden=5)_best.ckpt……………………
    lost = 6.567145 ppl = 711.336
    
