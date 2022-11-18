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
    Epoch: 0001 Batch: 50 /134 lost = 8.812283 ppl = 6716.23
    Epoch: 0001 Batch: 100 /134 lost = 8.650175 ppl = 5711.15
    Valid 4864 samples after epoch: 0001 lost = 8.516849 ppl = 4998.28
    ------Saving best model------
    Epoch: 0002 Batch: 50 /134 lost = 8.198701 ppl = 3636.22
    Epoch: 0002 Batch: 100 /134 lost = 7.954762 ppl = 2849.11
    Valid 4864 samples after epoch: 0002 lost = 7.842837 ppl = 2547.42
    ------Saving best model------
    Epoch: 0003 Batch: 50 /134 lost = 7.528488 ppl = 1860.29
    Epoch: 0003 Batch: 100 /134 lost = 7.360157 ppl = 1572.08
    Valid 4864 samples after epoch: 0003 lost = 7.341655 ppl = 1543.26
    ------Saving best model------
    Epoch: 0004 Batch: 50 /134 lost = 7.073092 ppl = 1179.79
    Epoch: 0004 Batch: 100 /134 lost = 6.969148 ppl = 1063.32
    Valid 4864 samples after epoch: 0004 lost = 7.021153 ppl = 1120.08
    ------Saving best model------
    Epoch: 0005 Batch: 50 /134 lost = 6.783267 ppl = 882.949
    Epoch: 0005 Batch: 100 /134 lost = 6.720392 ppl = 829.143
    Valid 4864 samples after epoch: 0005 lost = 6.825861 ppl = 921.37
    ------Saving best model------
    Epoch: 0006 Batch: 50 /134 lost = 6.609062 ppl = 741.787
    Epoch: 0006 Batch: 100 /134 lost = 6.571811 ppl = 714.663
    Valid 4864 samples after epoch: 0006 lost = 6.717365 ppl = 826.636
    ------Saving best model------
    Epoch: 0007 Batch: 50 /134 lost = 6.514904 ppl = 675.129
    Epoch: 0007 Batch: 100 /134 lost = 6.493043 ppl = 660.53
    Valid 4864 samples after epoch: 0007 lost = 6.666263 ppl = 785.455
    ------Saving best model------
    Epoch: 0008 Batch: 50 /134 lost = 6.470883 ppl = 646.054
    Epoch: 0008 Batch: 100 /134 lost = 6.455513 ppl = 636.2
    Valid 4864 samples after epoch: 0008 lost = 6.644381 ppl = 768.454
    ------Saving best model------
    Epoch: 0009 Batch: 50 /134 lost = 6.450776 ppl = 633.194
    Epoch: 0009 Batch: 100 /134 lost = 6.436868 ppl = 624.448
    Valid 4864 samples after epoch: 0009 lost = 6.635519 ppl = 761.675
    ------Saving best model------
    Epoch: 0010 Batch: 50 /134 lost = 6.431498 ppl = 621.104
    Epoch: 0010 Batch: 100 /134 lost = 6.423871 ppl = 616.384
    Valid 4864 samples after epoch: 0010 lost = 6.629860 ppl = 757.376
    ------Saving best model------
    Epoch: 0011 Batch: 50 /134 lost = 6.416981 ppl = 612.152
    Epoch: 0011 Batch: 100 /134 lost = 6.401540 ppl = 602.773
    Valid 4864 samples after epoch: 0011 lost = 6.613362 ppl = 744.984
    ------Saving best model------
    Epoch: 0012 Batch: 50 /134 lost = 6.394017 ppl = 598.255
    Epoch: 0012 Batch: 100 /134 lost = 6.384700 ppl = 592.707
    Valid 4864 samples after epoch: 0012 lost = 6.608156 ppl = 741.115
    ------Saving best model------
    Epoch: 0013 Batch: 50 /134 lost = 6.382066 ppl = 591.148
    Epoch: 0013 Batch: 100 /134 lost = 6.372152 ppl = 585.316
    Valid 4864 samples after epoch: 0013 lost = 6.601922 ppl = 736.509
    ------Saving best model------
    Epoch: 0014 Batch: 50 /134 lost = 6.368805 ppl = 583.36
    Epoch: 0014 Batch: 100 /134 lost = 6.355274 ppl = 575.52
    Valid 4864 samples after epoch: 0014 lost = 6.599347 ppl = 734.616
    ------Saving best model------
    Epoch: 0015 Batch: 50 /134 lost = 6.356365 ppl = 576.148
    Epoch: 0015 Batch: 100 /134 lost = 6.343156 ppl = 568.588
    Valid 4864 samples after epoch: 0015 lost = 6.596319 ppl = 732.394
    ------Saving best model------
    Epoch: 0016 Batch: 50 /134 lost = 6.344574 ppl = 569.395
    Epoch: 0016 Batch: 100 /134 lost = 6.329951 ppl = 561.129
    Valid 4864 samples after epoch: 0016 lost = 6.593086 ppl = 730.03
    ------Saving best model------
    Epoch: 0017 Batch: 50 /134 lost = 6.333538 ppl = 563.146
    Epoch: 0017 Batch: 100 /134 lost = 6.316594 ppl = 553.684
    Valid 4864 samples after epoch: 0017 lost = 6.591428 ppl = 728.821
    ------Saving best model------
    Epoch: 0018 Batch: 50 /134 lost = 6.322688 ppl = 557.068
    Epoch: 0018 Batch: 100 /134 lost = 6.307190 ppl = 548.502
    Valid 4864 samples after epoch: 0018 lost = 6.590257 ppl = 727.968
    ------Saving best model------
    Epoch: 0019 Batch: 50 /134 lost = 6.312998 ppl = 551.696
    Epoch: 0019 Batch: 100 /134 lost = 6.298943 ppl = 543.997
    Valid 4864 samples after epoch: 0019 lost = 6.586802 ppl = 725.457
    ------Saving best model------
    Epoch: 0020 Batch: 50 /134 lost = 6.300490 ppl = 544.839
    Epoch: 0020 Batch: 100 /134 lost = 6.288359 ppl = 538.269
    Valid 4864 samples after epoch: 0020 lost = 6.584994 ppl = 724.147
    ------Saving best model------
    Epoch: 0021 Batch: 50 /134 lost = 6.291209 ppl = 539.805
    Epoch: 0021 Batch: 100 /134 lost = 6.278048 ppl = 532.747
    Valid 4864 samples after epoch: 0021 lost = 6.584067 ppl = 723.475
    ------Saving best model------
    Epoch: 0022 Batch: 50 /134 lost = 6.282089 ppl = 534.905
    Epoch: 0022 Batch: 100 /134 lost = 6.267308 ppl = 527.057
    Valid 4864 samples after epoch: 0022 lost = 6.582924 ppl = 722.649
    ------Saving best model------
    Epoch: 0023 Batch: 50 /134 lost = 6.273036 ppl = 530.084
    Epoch: 0023 Batch: 100 /134 lost = 6.256366 ppl = 521.321
    Valid 4864 samples after epoch: 0023 lost = 6.581436 ppl = 721.575
    ------Saving best model------
    Epoch: 0024 Batch: 50 /134 lost = 6.263908 ppl = 525.268
    Epoch: 0024 Batch: 100 /134 lost = 6.244411 ppl = 515.126
    Valid 4864 samples after epoch: 0024 lost = 6.579777 ppl = 720.379
    ------Saving best model------
    Epoch: 0025 Batch: 50 /134 lost = 6.250039 ppl = 518.033
    Epoch: 0025 Batch: 100 /134 lost = 6.225839 ppl = 505.647
    Valid 4864 samples after epoch: 0025 lost = 6.571774 ppl = 714.636
    ------Saving best model------
    Epoch: 0026 Batch: 50 /134 lost = 6.236869 ppl = 511.255
    Epoch: 0026 Batch: 100 /134 lost = 6.211078 ppl = 498.238
    Valid 4864 samples after epoch: 0026 lost = 6.568376 ppl = 712.212
    ------Saving best model------
    Epoch: 0027 Batch: 50 /134 lost = 6.225946 ppl = 505.701
    Epoch: 0027 Batch: 100 /134 lost = 6.195669 ppl = 490.62
    Valid 4864 samples after epoch: 0027 lost = 6.561524 ppl = 707.349
    ------Saving best model------
    Epoch: 0028 Batch: 50 /134 lost = 6.214007 ppl = 499.7
    Epoch: 0028 Batch: 100 /134 lost = 6.174484 ppl = 480.335
    Valid 4864 samples after epoch: 0028 lost = 6.558180 ppl = 704.987
    ------Saving best model------
    Epoch: 0029 Batch: 50 /134 lost = 6.201715 ppl = 493.595
    Epoch: 0029 Batch: 100 /134 lost = 6.160696 ppl = 473.758
    Valid 4864 samples after epoch: 0029 lost = 6.556325 ppl = 703.681
    ------Saving best model------
    Epoch: 0030 Batch: 50 /134 lost = 6.190311 ppl = 487.998
    Epoch: 0030 Batch: 100 /134 lost = 6.148389 ppl = 467.963
    Valid 4864 samples after epoch: 0030 lost = 6.554527 ppl = 702.417
    ------Saving best model------
    Epoch: 0031 Batch: 50 /134 lost = 6.179561 ppl = 482.78
    Epoch: 0031 Batch: 100 /134 lost = 6.136710 ppl = 462.529
    Valid 4864 samples after epoch: 0031 lost = 6.552911 ppl = 701.283
    ------Saving best model------
    Epoch: 0032 Batch: 50 /134 lost = 6.168876 ppl = 477.649
    Epoch: 0032 Batch: 100 /134 lost = 6.125063 ppl = 457.174
    Valid 4864 samples after epoch: 0032 lost = 6.552728 ppl = 701.154
    ------Saving best model------
    Epoch: 0033 Batch: 50 /134 lost = 6.158082 ppl = 472.521
    Epoch: 0033 Batch: 100 /134 lost = 6.112932 ppl = 451.661
    Valid 4864 samples after epoch: 0033 lost = 6.551268 ppl = 700.131
    ------Saving best model------
    Epoch: 0034 Batch: 50 /134 lost = 6.146140 ppl = 466.911
    Epoch: 0034 Batch: 100 /134 lost = 6.099442 ppl = 445.609
    Valid 4864 samples after epoch: 0034 lost = 6.550533 ppl = 699.617
    ------Saving best model------
    Epoch: 0035 Batch: 50 /134 lost = 6.133675 ppl = 461.128
    Epoch: 0035 Batch: 100 /134 lost = 6.086758 ppl = 439.992
    Valid 4864 samples after epoch: 0035 lost = 6.548674 ppl = 698.318
    ------Saving best model------
    Epoch: 0036 Batch: 50 /134 lost = 6.120771 ppl = 455.216
    Epoch: 0036 Batch: 100 /134 lost = 6.074016 ppl = 434.422
    Valid 4864 samples after epoch: 0036 lost = 6.547703 ppl = 697.64
    ------Saving best model------
    Epoch: 0037 Batch: 50 /134 lost = 6.105171 ppl = 448.169
    Epoch: 0037 Batch: 100 /134 lost = 6.062070 ppl = 429.263
    Valid 4864 samples after epoch: 0037 lost = 6.548403 ppl = 698.128
    Epoch: 0038 Batch: 50 /134 lost = 6.091967 ppl = 442.29
    Epoch: 0038 Batch: 100 /134 lost = 6.050548 ppl = 424.346
    Valid 4864 samples after epoch: 0038 lost = 6.549145 ppl = 698.647
    Epoch: 0039 Batch: 50 /134 lost = 6.078521 ppl = 436.383
    Epoch: 0039 Batch: 100 /134 lost = 6.037763 ppl = 418.955
    Valid 4864 samples after epoch: 0039 lost = 6.549671 ppl = 699.014
    Epoch: 0040 Batch: 50 /134 lost = 6.066729 ppl = 431.268
    Epoch: 0040 Batch: 100 /134 lost = 6.025865 ppl = 413.999
    Valid 4864 samples after epoch: 0040 lost = 6.549843 ppl = 699.135
    Epoch: 0041 Batch: 50 /134 lost = 6.055368 ppl = 426.396
    Epoch: 0041 Batch: 100 /134 lost = 6.014186 ppl = 409.193
    Valid 4864 samples after epoch: 0041 lost = 6.550379 ppl = 699.509
    Epoch: 0042 Batch: 50 /134 lost = 6.043771 ppl = 421.48
    Epoch: 0042 Batch: 100 /134 lost = 6.001202 ppl = 403.914
    Valid 4864 samples after epoch: 0042 lost = 6.551041 ppl = 699.972
    Epoch: 0043 Batch: 50 /134 lost = 6.032842 ppl = 416.898
    Epoch: 0043 Batch: 100 /134 lost = 5.990015 ppl = 399.421
    Valid 4864 samples after epoch: 0043 lost = 6.552102 ppl = 700.716
    Epoch: 0044 Batch: 50 /134 lost = 6.021598 ppl = 412.237
    Epoch: 0044 Batch: 100 /134 lost = 5.979633 ppl = 395.295
    Valid 4864 samples after epoch: 0044 lost = 6.552779 ppl = 701.19
    Epoch: 0045 Batch: 50 /134 lost = 6.011256 ppl = 407.995
    Epoch: 0045 Batch: 100 /134 lost = 5.969278 ppl = 391.223
    Valid 4864 samples after epoch: 0045 lost = 6.554710 ppl = 702.545
    Epoch: 0046 Batch: 50 /134 lost = 5.998841 ppl = 402.962
    Epoch: 0046 Batch: 100 /134 lost = 5.957082 ppl = 386.481
    Valid 4864 samples after epoch: 0046 lost = 6.553918 ppl = 701.989
    Epoch: 0047 Batch: 50 /134 lost = 5.988635 ppl = 398.87
    Epoch: 0047 Batch: 100 /134 lost = 5.946934 ppl = 382.578
    Valid 4864 samples after epoch: 0047 lost = 6.555613 ppl = 703.18
    Epoch: 0048 Batch: 50 /134 lost = 5.978486 ppl = 394.842
    Epoch: 0048 Batch: 100 /134 lost = 5.936076 ppl = 378.447
    Valid 4864 samples after epoch: 0048 lost = 6.557662 ppl = 704.623
    Epoch: 0049 Batch: 50 /134 lost = 5.968976 ppl = 391.105
    Epoch: 0049 Batch: 100 /134 lost = 5.923936 ppl = 373.88
    Valid 4864 samples after epoch: 0049 lost = 6.559202 ppl = 705.708
    Epoch: 0050 Batch: 50 /134 lost = 5.961243 ppl = 388.092
    Epoch: 0050 Batch: 100 /134 lost = 5.912728 ppl = 369.713
    Valid 4864 samples after epoch: 0050 lost = 6.561847 ppl = 707.577
    Epoch: 0051 Batch: 50 /134 lost = 5.951820 ppl = 384.453
    Epoch: 0051 Batch: 100 /134 lost = 5.899714 ppl = 364.933
    Valid 4864 samples after epoch: 0051 lost = 6.564990 ppl = 709.805
    Epoch: 0052 Batch: 50 /134 lost = 5.942722 ppl = 380.97
    Epoch: 0052 Batch: 100 /134 lost = 5.889561 ppl = 361.247
    Valid 4864 samples after epoch: 0052 lost = 6.568275 ppl = 712.14
    Epoch: 0053 Batch: 50 /134 lost = 5.935256 ppl = 378.137
    Epoch: 0053 Batch: 100 /134 lost = 5.878239 ppl = 357.18
    Valid 4864 samples after epoch: 0053 lost = 6.570719 ppl = 713.883
    Epoch: 0054 Batch: 50 /134 lost = 5.927466 ppl = 375.203
    Epoch: 0054 Batch: 100 /134 lost = 5.868577 ppl = 353.745
    Valid 4864 samples after epoch: 0054 lost = 6.573905 ppl = 716.161
    Epoch: 0055 Batch: 50 /134 lost = 5.920458 ppl = 372.582
    Epoch: 0055 Batch: 100 /134 lost = 5.857138 ppl = 349.722
    Valid 4864 samples after epoch: 0055 lost = 6.576258 ppl = 717.848
    Epoch: 0056 Batch: 50 /134 lost = 5.913455 ppl = 369.982
    Epoch: 0056 Batch: 100 /134 lost = 5.846891 ppl = 346.156
    Valid 4864 samples after epoch: 0056 lost = 6.579778 ppl = 720.379
    Epoch: 0057 Batch: 50 /134 lost = 5.907498 ppl = 367.785
    Epoch: 0057 Batch: 100 /134 lost = 5.837893 ppl = 343.056
    Valid 4864 samples after epoch: 0057 lost = 6.583685 ppl = 723.199
    Epoch: 0058 Batch: 50 /134 lost = 5.900129 ppl = 365.085
    Epoch: 0058 Batch: 100 /134 lost = 5.829264 ppl = 340.108
    Valid 4864 samples after epoch: 0058 lost = 6.585727 ppl = 724.678
    Epoch: 0059 Batch: 50 /134 lost = 5.892782 ppl = 362.412
    Epoch: 0059 Batch: 100 /134 lost = 5.819965 ppl = 336.96
    Valid 4864 samples after epoch: 0059 lost = 6.588072 ppl = 726.379
    Epoch: 0060 Batch: 50 /134 lost = 5.885667 ppl = 359.843
    Epoch: 0060 Batch: 100 /134 lost = 5.812032 ppl = 334.298
    Valid 4864 samples after epoch: 0060 lost = 6.590740 ppl = 728.32
    Epoch: 0061 Batch: 50 /134 lost = 5.877072 ppl = 356.763
    Epoch: 0061 Batch: 100 /134 lost = 5.805105 ppl = 331.99
    Valid 4864 samples after epoch: 0061 lost = 6.592646 ppl = 729.709
    Epoch: 0062 Batch: 50 /134 lost = 5.868900 ppl = 353.86
    Epoch: 0062 Batch: 100 /134 lost = 5.795965 ppl = 328.969
    Valid 4864 samples after epoch: 0062 lost = 6.596225 ppl = 732.326
    Epoch: 0063 Batch: 50 /134 lost = 5.858674 ppl = 350.259
    Epoch: 0063 Batch: 100 /134 lost = 5.786627 ppl = 325.912
    Valid 4864 samples after epoch: 0063 lost = 6.599616 ppl = 734.813
    Epoch: 0064 Batch: 50 /134 lost = 5.851032 ppl = 347.593
    Epoch: 0064 Batch: 100 /134 lost = 5.778102 ppl = 323.145
    Valid 4864 samples after epoch: 0064 lost = 6.603271 ppl = 737.503
    Epoch: 0065 Batch: 50 /134 lost = 5.843980 ppl = 345.15
    Epoch: 0065 Batch: 100 /134 lost = 5.769000 ppl = 320.217
    Valid 4864 samples after epoch: 0065 lost = 6.605219 ppl = 738.942
    Epoch: 0066 Batch: 50 /134 lost = 5.833253 ppl = 341.468
    Epoch: 0066 Batch: 100 /134 lost = 5.762200 ppl = 318.047
    Valid 4864 samples after epoch: 0066 lost = 6.607996 ppl = 740.997
    Epoch: 0067 Batch: 50 /134 lost = 5.826310 ppl = 339.105
    Epoch: 0067 Batch: 100 /134 lost = 5.756042 ppl = 316.095
    Valid 4864 samples after epoch: 0067 lost = 6.612295 ppl = 744.189
    Epoch: 0068 Batch: 50 /134 lost = 5.817933 ppl = 336.276
    Epoch: 0068 Batch: 100 /134 lost = 5.749992 ppl = 314.188
    Valid 4864 samples after epoch: 0068 lost = 6.615431 ppl = 746.526
    Epoch: 0069 Batch: 50 /134 lost = 5.813612 ppl = 334.826
    Epoch: 0069 Batch: 100 /134 lost = 5.742684 ppl = 311.9
    Valid 4864 samples after epoch: 0069 lost = 6.621448 ppl = 751.032
    Epoch: 0070 Batch: 50 /134 lost = 5.803634 ppl = 331.502
    Epoch: 0070 Batch: 100 /134 lost = 5.735035 ppl = 309.524
    Valid 4864 samples after epoch: 0070 lost = 6.626693 ppl = 754.982
    Epoch: 0071 Batch: 50 /134 lost = 5.797584 ppl = 329.503
    Epoch: 0071 Batch: 100 /134 lost = 5.728180 ppl = 307.409
    Valid 4864 samples after epoch: 0071 lost = 6.628788 ppl = 756.565
    Epoch: 0072 Batch: 50 /134 lost = 5.791737 ppl = 327.581
    Epoch: 0072 Batch: 100 /134 lost = 5.722507 ppl = 305.67
    Valid 4864 samples after epoch: 0072 lost = 6.633118 ppl = 759.848
    Epoch: 0073 Batch: 50 /134 lost = 5.784766 ppl = 325.306
    Epoch: 0073 Batch: 100 /134 lost = 5.713629 ppl = 302.968
    Valid 4864 samples after epoch: 0073 lost = 6.640277 ppl = 765.307
    Epoch: 0074 Batch: 50 /134 lost = 5.779545 ppl = 323.612
    Epoch: 0074 Batch: 100 /134 lost = 5.706135 ppl = 300.707
    Valid 4864 samples after epoch: 0074 lost = 6.642397 ppl = 766.931
    Epoch: 0075 Batch: 50 /134 lost = 5.773120 ppl = 321.539
    Epoch: 0075 Batch: 100 /134 lost = 5.698071 ppl = 298.292
    Valid 4864 samples after epoch: 0075 lost = 6.646879 ppl = 770.377
    Epoch: 0076 Batch: 50 /134 lost = 5.766969 ppl = 319.568
    Epoch: 0076 Batch: 100 /134 lost = 5.690235 ppl = 295.963
    Valid 4864 samples after epoch: 0076 lost = 6.651503 ppl = 773.946
    Epoch: 0077 Batch: 50 /134 lost = 5.759387 ppl = 317.154
    Epoch: 0077 Batch: 100 /134 lost = 5.683550 ppl = 293.991
    Valid 4864 samples after epoch: 0077 lost = 6.657654 ppl = 778.722
    Epoch: 0078 Batch: 50 /134 lost = 5.752581 ppl = 315.003
    Epoch: 0078 Batch: 100 /134 lost = 5.677758 ppl = 292.293
    Valid 4864 samples after epoch: 0078 lost = 6.661725 ppl = 781.898
    Epoch: 0079 Batch: 50 /134 lost = 5.745976 ppl = 312.929
    Epoch: 0079 Batch: 100 /134 lost = 5.670431 ppl = 290.159
    Valid 4864 samples after epoch: 0079 lost = 6.667838 ppl = 786.693
    Epoch: 0080 Batch: 50 /134 lost = 5.737033 ppl = 310.143
    Epoch: 0080 Batch: 100 /134 lost = 5.659912 ppl = 287.123
    Valid 4864 samples after epoch: 0080 lost = 6.670435 ppl = 788.739
    Epoch: 0081 Batch: 50 /134 lost = 5.730896 ppl = 308.245
    Epoch: 0081 Batch: 100 /134 lost = 5.656200 ppl = 286.06
    Valid 4864 samples after epoch: 0081 lost = 6.675430 ppl = 792.688
    Epoch: 0082 Batch: 50 /134 lost = 5.722935 ppl = 305.801
    Epoch: 0082 Batch: 100 /134 lost = 5.647586 ppl = 283.606
    Valid 4864 samples after epoch: 0082 lost = 6.679200 ppl = 795.682
    Epoch: 0083 Batch: 50 /134 lost = 5.718326 ppl = 304.395
    Epoch: 0083 Batch: 100 /134 lost = 5.641108 ppl = 281.775
    Valid 4864 samples after epoch: 0083 lost = 6.684102 ppl = 799.592
    Epoch: 0084 Batch: 50 /134 lost = 5.710007 ppl = 301.873
    Epoch: 0084 Batch: 100 /134 lost = 5.634390 ppl = 279.888
    Valid 4864 samples after epoch: 0084 lost = 6.688630 ppl = 803.221
    Epoch: 0085 Batch: 50 /134 lost = 5.705458 ppl = 300.503
    Epoch: 0085 Batch: 100 /134 lost = 5.628482 ppl = 278.239
    Valid 4864 samples after epoch: 0085 lost = 6.691815 ppl = 805.784
    Epoch: 0086 Batch: 50 /134 lost = 5.699589 ppl = 298.745
    Epoch: 0086 Batch: 100 /134 lost = 5.623566 ppl = 276.875
    Valid 4864 samples after epoch: 0086 lost = 6.698302 ppl = 811.027
    Epoch: 0087 Batch: 50 /134 lost = 5.694690 ppl = 297.285
    Epoch: 0087 Batch: 100 /134 lost = 5.617603 ppl = 275.229
    Valid 4864 samples after epoch: 0087 lost = 6.704663 ppl = 816.203
    Epoch: 0088 Batch: 50 /134 lost = 5.692130 ppl = 296.525
    Epoch: 0088 Batch: 100 /134 lost = 5.611846 ppl = 273.649
    Valid 4864 samples after epoch: 0088 lost = 6.708964 ppl = 819.721
    Epoch: 0089 Batch: 50 /134 lost = 5.687026 ppl = 295.015
    Epoch: 0089 Batch: 100 /134 lost = 5.608547 ppl = 272.748
    Valid 4864 samples after epoch: 0089 lost = 6.710906 ppl = 821.314
    Epoch: 0090 Batch: 50 /134 lost = 5.683772 ppl = 294.056
    Epoch: 0090 Batch: 100 /134 lost = 5.603617 ppl = 271.406
    Valid 4864 samples after epoch: 0090 lost = 6.718172 ppl = 827.304
    Epoch: 0091 Batch: 50 /134 lost = 5.676915 ppl = 292.047
    Epoch: 0091 Batch: 100 /134 lost = 5.598188 ppl = 269.937
    Valid 4864 samples after epoch: 0091 lost = 6.723466 ppl = 831.695
    Epoch: 0092 Batch: 50 /134 lost = 5.672748 ppl = 290.833
    Epoch: 0092 Batch: 100 /134 lost = 5.592316 ppl = 268.356
    Valid 4864 samples after epoch: 0092 lost = 6.726304 ppl = 834.058
    Epoch: 0093 Batch: 50 /134 lost = 5.667978 ppl = 289.449
    Epoch: 0093 Batch: 100 /134 lost = 5.584597 ppl = 266.293
    Valid 4864 samples after epoch: 0093 lost = 6.733447 ppl = 840.038
    Epoch: 0094 Batch: 50 /134 lost = 5.665511 ppl = 288.735
    Epoch: 0094 Batch: 100 /134 lost = 5.577740 ppl = 264.473
    Valid 4864 samples after epoch: 0094 lost = 6.734561 ppl = 840.975
    Epoch: 0095 Batch: 50 /134 lost = 5.657521 ppl = 286.438
    Epoch: 0095 Batch: 100 /134 lost = 5.577341 ppl = 264.368
    Valid 4864 samples after epoch: 0095 lost = 6.742573 ppl = 847.739
    Epoch: 0096 Batch: 50 /134 lost = 5.653534 ppl = 285.298
    Epoch: 0096 Batch: 100 /134 lost = 5.573241 ppl = 263.286
    Valid 4864 samples after epoch: 0096 lost = 6.744858 ppl = 849.678
    Epoch: 0097 Batch: 50 /134 lost = 5.649545 ppl = 284.162
    Epoch: 0097 Batch: 100 /134 lost = 5.565804 ppl = 261.335
    Valid 4864 samples after epoch: 0097 lost = 6.751567 ppl = 855.398
    Epoch: 0098 Batch: 50 /134 lost = 5.645398 ppl = 282.986
    Epoch: 0098 Batch: 100 /134 lost = 5.563011 ppl = 260.606
    Valid 4864 samples after epoch: 0098 lost = 6.757465 ppl = 860.458
    Epoch: 0099 Batch: 50 /134 lost = 5.642667 ppl = 282.214
    Epoch: 0099 Batch: 100 /134 lost = 5.557284 ppl = 259.118
    Valid 4864 samples after epoch: 0099 lost = 6.761133 ppl = 863.62
    Epoch: 0100 Batch: 50 /134 lost = 5.637765 ppl = 280.834
    Epoch: 0100 Batch: 100 /134 lost = 5.553286 ppl = 258.084
    Valid 4864 samples after epoch: 0100 lost = 6.763367 ppl = 865.552
    Epoch: 0101 Batch: 50 /134 lost = 5.632312 ppl = 279.307
    Epoch: 0101 Batch: 100 /134 lost = 5.548252 ppl = 256.788
    Valid 4864 samples after epoch: 0101 lost = 6.770189 ppl = 871.476
    Epoch: 0102 Batch: 50 /134 lost = 5.630624 ppl = 278.836
    Epoch: 0102 Batch: 100 /134 lost = 5.543935 ppl = 255.682
    Valid 4864 samples after epoch: 0102 lost = 6.776321 ppl = 876.837
    Epoch: 0103 Batch: 50 /134 lost = 5.625388 ppl = 277.38
    Epoch: 0103 Batch: 100 /134 lost = 5.538609 ppl = 254.324
    Valid 4864 samples after epoch: 0103 lost = 6.781515 ppl = 881.403
    Epoch: 0104 Batch: 50 /134 lost = 5.623271 ppl = 276.793
    Epoch: 0104 Batch: 100 /134 lost = 5.534435 ppl = 253.265
    Valid 4864 samples after epoch: 0104 lost = 6.785582 ppl = 884.995
    Epoch: 0105 Batch: 50 /134 lost = 5.618246 ppl = 275.406
    Epoch: 0105 Batch: 100 /134 lost = 5.529438 ppl = 252.002
    Valid 4864 samples after epoch: 0105 lost = 6.790774 ppl = 889.602
    Epoch: 0106 Batch: 50 /134 lost = 5.614316 ppl = 274.326
    Epoch: 0106 Batch: 100 /134 lost = 5.523080 ppl = 250.405
    Valid 4864 samples after epoch: 0106 lost = 6.795303 ppl = 893.64
    Epoch: 0107 Batch: 50 /134 lost = 5.611170 ppl = 273.464
    Epoch: 0107 Batch: 100 /134 lost = 5.518829 ppl = 249.343
    Valid 4864 samples after epoch: 0107 lost = 6.798966 ppl = 896.919
    Epoch: 0108 Batch: 50 /134 lost = 5.612027 ppl = 273.699
    Epoch: 0108 Batch: 100 /134 lost = 5.513244 ppl = 247.954
    Valid 4864 samples after epoch: 0108 lost = 6.806286 ppl = 903.509
    Epoch: 0109 Batch: 50 /134 lost = 5.604743 ppl = 271.712
    Epoch: 0109 Batch: 100 /134 lost = 5.508521 ppl = 246.786
    Valid 4864 samples after epoch: 0109 lost = 6.810915 ppl = 907.701
    Epoch: 0110 Batch: 50 /134 lost = 5.605194 ppl = 271.835
    Epoch: 0110 Batch: 100 /134 lost = 5.502114 ppl = 245.21
    Valid 4864 samples after epoch: 0110 lost = 6.813916 ppl = 910.429
    Epoch: 0111 Batch: 50 /134 lost = 5.597598 ppl = 269.778
    Epoch: 0111 Batch: 100 /134 lost = 5.497210 ppl = 244.01
    Valid 4864 samples after epoch: 0111 lost = 6.819669 ppl = 915.682
    Epoch: 0112 Batch: 50 /134 lost = 5.589906 ppl = 267.711
    Epoch: 0112 Batch: 100 /134 lost = 5.494880 ppl = 243.442
    Valid 4864 samples after epoch: 0112 lost = 6.826810 ppl = 922.244
    Epoch: 0113 Batch: 50 /134 lost = 5.591428 ppl = 268.118
    Epoch: 0113 Batch: 100 /134 lost = 5.490898 ppl = 242.475
    Valid 4864 samples after epoch: 0113 lost = 6.829622 ppl = 924.841
    Epoch: 0114 Batch: 50 /134 lost = 5.581453 ppl = 265.457
    Epoch: 0114 Batch: 100 /134 lost = 5.487094 ppl = 241.554
    Valid 4864 samples after epoch: 0114 lost = 6.836434 ppl = 931.163
    Epoch: 0115 Batch: 50 /134 lost = 5.579149 ppl = 264.846
    Epoch: 0115 Batch: 100 /134 lost = 5.481088 ppl = 240.108
    Valid 4864 samples after epoch: 0115 lost = 6.838933 ppl = 933.492
    Epoch: 0116 Batch: 50 /134 lost = 5.575275 ppl = 263.822
    Epoch: 0116 Batch: 100 /134 lost = 5.480049 ppl = 239.858
    Valid 4864 samples after epoch: 0116 lost = 6.846325 ppl = 940.418
    Epoch: 0117 Batch: 50 /134 lost = 5.571023 ppl = 262.703
    Epoch: 0117 Batch: 100 /134 lost = 5.474511 ppl = 238.534
    Valid 4864 samples after epoch: 0117 lost = 6.847520 ppl = 941.543
    Epoch: 0118 Batch: 50 /134 lost = 5.562499 ppl = 260.473
    Epoch: 0118 Batch: 100 /134 lost = 5.466644 ppl = 236.665
    Valid 4864 samples after epoch: 0118 lost = 6.852519 ppl = 946.262
    Epoch: 0119 Batch: 50 /134 lost = 5.560115 ppl = 259.853
    Epoch: 0119 Batch: 100 /134 lost = 5.465180 ppl = 236.318
    Valid 4864 samples after epoch: 0119 lost = 6.858297 ppl = 951.745
    Epoch: 0120 Batch: 50 /134 lost = 5.556585 ppl = 258.937
    Epoch: 0120 Batch: 100 /134 lost = 5.461543 ppl = 235.46
    Valid 4864 samples after epoch: 0120 lost = 6.863125 ppl = 956.351
    Epoch: 0121 Batch: 50 /134 lost = 5.551363 ppl = 257.588
    Epoch: 0121 Batch: 100 /134 lost = 5.457255 ppl = 234.453
    Valid 4864 samples after epoch: 0121 lost = 6.865474 ppl = 958.6
    Epoch: 0122 Batch: 50 /134 lost = 5.547323 ppl = 256.55
    Epoch: 0122 Batch: 100 /134 lost = 5.453962 ppl = 233.682
    Valid 4864 samples after epoch: 0122 lost = 6.873480 ppl = 966.305
    Epoch: 0123 Batch: 50 /134 lost = 5.544957 ppl = 255.943
    Epoch: 0123 Batch: 100 /134 lost = 5.449018 ppl = 232.53
    Valid 4864 samples after epoch: 0123 lost = 6.877429 ppl = 970.129
    Epoch: 0124 Batch: 50 /134 lost = 5.543646 ppl = 255.608
    Epoch: 0124 Batch: 100 /134 lost = 5.444999 ppl = 231.597
    Valid 4864 samples after epoch: 0124 lost = 6.878344 ppl = 971.017
    Epoch: 0125 Batch: 50 /134 lost = 5.538178 ppl = 254.215
    Epoch: 0125 Batch: 100 /134 lost = 5.438640 ppl = 230.129
    Valid 4864 samples after epoch: 0125 lost = 6.880268 ppl = 972.887
    Epoch: 0126 Batch: 50 /134 lost = 5.535400 ppl = 253.509
    Epoch: 0126 Batch: 100 /134 lost = 5.428390 ppl = 227.782
    Valid 4864 samples after epoch: 0126 lost = 6.882913 ppl = 975.464
    Epoch: 0127 Batch: 50 /134 lost = 5.531725 ppl = 252.579
    Epoch: 0127 Batch: 100 /134 lost = 5.425819 ppl = 227.197
    Valid 4864 samples after epoch: 0127 lost = 6.892406 ppl = 984.768
    Epoch: 0128 Batch: 50 /134 lost = 5.533845 ppl = 253.115
    Epoch: 0128 Batch: 100 /134 lost = 5.420887 ppl = 226.079
    Valid 4864 samples after epoch: 0128 lost = 6.892751 ppl = 985.108
    Epoch: 0129 Batch: 50 /134 lost = 5.524819 ppl = 250.841
    Epoch: 0129 Batch: 100 /134 lost = 5.416111 ppl = 225.002
    Valid 4864 samples after epoch: 0129 lost = 6.898131 ppl = 990.421
    Epoch: 0130 Batch: 50 /134 lost = 5.526858 ppl = 251.353
    Epoch: 0130 Batch: 100 /134 lost = 5.415014 ppl = 224.756
    Valid 4864 samples after epoch: 0130 lost = 6.901589 ppl = 993.852
    Epoch: 0131 Batch: 50 /134 lost = 5.520128 ppl = 249.667
    Epoch: 0131 Batch: 100 /134 lost = 5.411249 ppl = 223.911
    Valid 4864 samples after epoch: 0131 lost = 6.905312 ppl = 997.56
    Epoch: 0132 Batch: 50 /134 lost = 5.519287 ppl = 249.457
    Epoch: 0132 Batch: 100 /134 lost = 5.409041 ppl = 223.417
    Valid 4864 samples after epoch: 0132 lost = 6.910359 ppl = 1002.61
    Epoch: 0133 Batch: 50 /134 lost = 5.514374 ppl = 248.234
    Epoch: 0133 Batch: 100 /134 lost = 5.405200 ppl = 222.561
    Valid 4864 samples after epoch: 0133 lost = 6.913405 ppl = 1005.67
    Epoch: 0134 Batch: 50 /134 lost = 5.508940 ppl = 246.889
    Epoch: 0134 Batch: 100 /134 lost = 5.401336 ppl = 221.702
    Valid 4864 samples after epoch: 0134 lost = 6.914114 ppl = 1006.38
    Epoch: 0135 Batch: 50 /134 lost = 5.503878 ppl = 245.643
    Epoch: 0135 Batch: 100 /134 lost = 5.395259 ppl = 220.359
    Valid 4864 samples after epoch: 0135 lost = 6.926473 ppl = 1018.89
    Epoch: 0136 Batch: 50 /134 lost = 5.500089 ppl = 244.714
    Epoch: 0136 Batch: 100 /134 lost = 5.393580 ppl = 219.99
    Valid 4864 samples after epoch: 0136 lost = 6.928466 ppl = 1020.93
    Epoch: 0137 Batch: 50 /134 lost = 5.499912 ppl = 244.67
    Epoch: 0137 Batch: 100 /134 lost = 5.390642 ppl = 219.344
    Valid 4864 samples after epoch: 0137 lost = 6.933846 ppl = 1026.43
    Epoch: 0138 Batch: 50 /134 lost = 5.502525 ppl = 245.311
    Epoch: 0138 Batch: 100 /134 lost = 5.385440 ppl = 218.206
    Valid 4864 samples after epoch: 0138 lost = 6.935257 ppl = 1027.88
    Epoch: 0139 Batch: 50 /134 lost = 5.495837 ppl = 243.675
    Epoch: 0139 Batch: 100 /134 lost = 5.381032 ppl = 217.246
    Valid 4864 samples after epoch: 0139 lost = 6.946181 ppl = 1039.17
    Epoch: 0140 Batch: 50 /134 lost = 5.493551 ppl = 243.119
    Epoch: 0140 Batch: 100 /134 lost = 5.379447 ppl = 216.902
    Valid 4864 samples after epoch: 0140 lost = 6.946581 ppl = 1039.59
    Epoch: 0141 Batch: 50 /134 lost = 5.486751 ppl = 241.471
    Epoch: 0141 Batch: 100 /134 lost = 5.377097 ppl = 216.393
    Valid 4864 samples after epoch: 0141 lost = 6.950026 ppl = 1043.18
    Epoch: 0142 Batch: 50 /134 lost = 5.484798 ppl = 241.0
    Epoch: 0142 Batch: 100 /134 lost = 5.371692 ppl = 215.227
    Valid 4864 samples after epoch: 0142 lost = 6.954896 ppl = 1048.27
    Epoch: 0143 Batch: 50 /134 lost = 5.479867 ppl = 239.815
    Epoch: 0143 Batch: 100 /134 lost = 5.368142 ppl = 214.464
    Valid 4864 samples after epoch: 0143 lost = 6.957283 ppl = 1050.78
    Epoch: 0144 Batch: 50 /134 lost = 5.476815 ppl = 239.084
    Epoch: 0144 Batch: 100 /134 lost = 5.367106 ppl = 214.242
    Valid 4864 samples after epoch: 0144 lost = 6.958334 ppl = 1051.88
    Epoch: 0145 Batch: 50 /134 lost = 5.472766 ppl = 238.118
    Epoch: 0145 Batch: 100 /134 lost = 5.364511 ppl = 213.687
    Valid 4864 samples after epoch: 0145 lost = 6.965115 ppl = 1059.04
    Epoch: 0146 Batch: 50 /134 lost = 5.470482 ppl = 237.575
    Epoch: 0146 Batch: 100 /134 lost = 5.362886 ppl = 213.34
    Valid 4864 samples after epoch: 0146 lost = 6.968579 ppl = 1062.71
    Epoch: 0147 Batch: 50 /134 lost = 5.468905 ppl = 237.2
    Epoch: 0147 Batch: 100 /134 lost = 5.357729 ppl = 212.242
    Valid 4864 samples after epoch: 0147 lost = 6.970868 ppl = 1065.15
    Epoch: 0148 Batch: 50 /134 lost = 5.471777 ppl = 237.883
    Epoch: 0148 Batch: 100 /134 lost = 5.356575 ppl = 211.998
    Valid 4864 samples after epoch: 0148 lost = 6.969799 ppl = 1064.01
    Epoch: 0149 Batch: 50 /134 lost = 5.464375 ppl = 236.128
    Epoch: 0149 Batch: 100 /134 lost = 5.356590 ppl = 212.001
    Valid 4864 samples after epoch: 0149 lost = 6.976628 ppl = 1071.3
    Epoch: 0150 Batch: 50 /134 lost = 5.459842 ppl = 235.06
    Epoch: 0150 Batch: 100 /134 lost = 5.349992 ppl = 210.607
    Valid 4864 samples after epoch: 0150 lost = 6.979243 ppl = 1074.11
    
    Test the LSTMLM……………………
    Test 5760 samples with models/1_layer_lstmlm_model_best.ckpt……………………
    lost = 6.480314 ppl = 652.176
    
