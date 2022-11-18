```python
!python (pytorch_api)1_layer_lstmlm_with_penn_assignment.py
```

    The size of the dictionary is: 7613
    The number of the train batch is: 134
    
    Train the LSTMLM……………………
    TextLSTM(
      (C): Embedding(7613, 128)
      (LSTM): LSTM(128, 5)
      (W): Linear(in_features=5, out_features=7613, bias=False)
    )
    Epoch: 0001 Batch: 50 /134 lost = 8.850698 ppl = 6979.26
    Epoch: 0001 Batch: 100 /134 lost = 8.738298 ppl = 6237.27
    Valid 4864 samples after epoch: 0001 lost = 8.630463 ppl = 5599.67
    ------Saving best model------
    Epoch: 0002 Batch: 50 /134 lost = 8.386159 ppl = 4385.94
    Epoch: 0002 Batch: 100 /134 lost = 8.081698 ppl = 3234.72
    Valid 4864 samples after epoch: 0002 lost = 7.869183 ppl = 2615.43
    ------Saving best model------
    Epoch: 0003 Batch: 50 /134 lost = 7.481357 ppl = 1774.65
    Epoch: 0003 Batch: 100 /134 lost = 7.211497 ppl = 1354.92
    Valid 4864 samples after epoch: 0003 lost = 7.150842 ppl = 1275.18
    ------Saving best model------
    Epoch: 0004 Batch: 50 /134 lost = 6.889605 ppl = 982.013
    Epoch: 0004 Batch: 100 /134 lost = 6.773870 ppl = 874.69
    Valid 4864 samples after epoch: 0004 lost = 6.830767 ppl = 925.901
    ------Saving best model------
    Epoch: 0005 Batch: 50 /134 lost = 6.625990 ppl = 754.451
    Epoch: 0005 Batch: 100 /134 lost = 6.575320 ppl = 717.175
    Valid 4864 samples after epoch: 0005 lost = 6.698331 ppl = 811.051
    ------Saving best model------
    Epoch: 0006 Batch: 50 /134 lost = 6.510991 ppl = 672.493
    Epoch: 0006 Batch: 100 /134 lost = 6.489727 ppl = 658.343
    Valid 4864 samples after epoch: 0006 lost = 6.650346 ppl = 773.052
    ------Saving best model------
    Epoch: 0007 Batch: 50 /134 lost = 6.462870 ppl = 640.898
    Epoch: 0007 Batch: 100 /134 lost = 6.454201 ppl = 635.366
    Valid 4864 samples after epoch: 0007 lost = 6.635275 ppl = 761.489
    ------Saving best model------
    Epoch: 0008 Batch: 50 /134 lost = 6.441171 ppl = 627.141
    Epoch: 0008 Batch: 100 /134 lost = 6.437612 ppl = 624.912
    Valid 4864 samples after epoch: 0008 lost = 6.630403 ppl = 757.787
    ------Saving best model------
    Epoch: 0009 Batch: 50 /134 lost = 6.428076 ppl = 618.982
    Epoch: 0009 Batch: 100 /134 lost = 6.427327 ppl = 618.519
    Valid 4864 samples after epoch: 0009 lost = 6.628306 ppl = 756.2
    ------Saving best model------
    Epoch: 0010 Batch: 50 /134 lost = 6.412630 ppl = 609.495
    Epoch: 0010 Batch: 100 /134 lost = 6.410269 ppl = 608.057
    Valid 4864 samples after epoch: 0010 lost = 6.617990 ppl = 748.439
    ------Saving best model------
    Epoch: 0011 Batch: 50 /134 lost = 6.401886 ppl = 602.981
    Epoch: 0011 Batch: 100 /134 lost = 6.390450 ppl = 596.124
    Valid 4864 samples after epoch: 0011 lost = 6.615250 ppl = 746.391
    ------Saving best model------
    Epoch: 0012 Batch: 50 /134 lost = 6.388057 ppl = 594.7
    Epoch: 0012 Batch: 100 /134 lost = 6.373861 ppl = 586.317
    Valid 4864 samples after epoch: 0012 lost = 6.611072 ppl = 743.279
    ------Saving best model------
    Epoch: 0013 Batch: 50 /134 lost = 6.376472 ppl = 587.85
    Epoch: 0013 Batch: 100 /134 lost = 6.356793 ppl = 576.395
    Valid 4864 samples after epoch: 0013 lost = 6.609445 ppl = 742.071
    ------Saving best model------
    Epoch: 0014 Batch: 50 /134 lost = 6.362729 ppl = 579.826
    Epoch: 0014 Batch: 100 /134 lost = 6.343434 ppl = 568.746
    Valid 4864 samples after epoch: 0014 lost = 6.609463 ppl = 742.084
    Epoch: 0015 Batch: 50 /134 lost = 6.349783 ppl = 572.369
    Epoch: 0015 Batch: 100 /134 lost = 6.333492 ppl = 563.119
    Valid 4864 samples after epoch: 0015 lost = 6.608949 ppl = 741.703
    ------Saving best model------
    Epoch: 0016 Batch: 50 /134 lost = 6.337322 ppl = 565.281
    Epoch: 0016 Batch: 100 /134 lost = 6.320380 ppl = 555.784
    Valid 4864 samples after epoch: 0016 lost = 6.606170 ppl = 739.645
    ------Saving best model------
    Epoch: 0017 Batch: 50 /134 lost = 6.327425 ppl = 559.713
    Epoch: 0017 Batch: 100 /134 lost = 6.310722 ppl = 550.442
    Valid 4864 samples after epoch: 0017 lost = 6.603147 ppl = 737.412
    ------Saving best model------
    Epoch: 0018 Batch: 50 /134 lost = 6.316120 ppl = 553.422
    Epoch: 0018 Batch: 100 /134 lost = 6.299114 ppl = 544.09
    Valid 4864 samples after epoch: 0018 lost = 6.599154 ppl = 734.474
    ------Saving best model------
    Epoch: 0019 Batch: 50 /134 lost = 6.303101 ppl = 546.263
    Epoch: 0019 Batch: 100 /134 lost = 6.285310 ppl = 536.631
    Valid 4864 samples after epoch: 0019 lost = 6.596287 ppl = 732.371
    ------Saving best model------
    Epoch: 0020 Batch: 50 /134 lost = 6.290509 ppl = 539.428
    Epoch: 0020 Batch: 100 /134 lost = 6.272221 ppl = 529.652
    Valid 4864 samples after epoch: 0020 lost = 6.594147 ppl = 730.806
    ------Saving best model------
    Epoch: 0021 Batch: 50 /134 lost = 6.275855 ppl = 531.58
    Epoch: 0021 Batch: 100 /134 lost = 6.254719 ppl = 520.463
    Valid 4864 samples after epoch: 0021 lost = 6.587487 ppl = 725.954
    ------Saving best model------
    Epoch: 0022 Batch: 50 /134 lost = 6.259650 ppl = 523.036
    Epoch: 0022 Batch: 100 /134 lost = 6.235593 ppl = 510.603
    Valid 4864 samples after epoch: 0022 lost = 6.583257 ppl = 722.89
    ------Saving best model------
    Epoch: 0023 Batch: 50 /134 lost = 6.244421 ppl = 515.131
    Epoch: 0023 Batch: 100 /134 lost = 6.218212 ppl = 501.805
    Valid 4864 samples after epoch: 0023 lost = 6.580397 ppl = 720.826
    ------Saving best model------
    Epoch: 0024 Batch: 50 /134 lost = 6.229331 ppl = 507.416
    Epoch: 0024 Batch: 100 /134 lost = 6.201122 ppl = 493.302
    Valid 4864 samples after epoch: 0024 lost = 6.576664 ppl = 718.14
    ------Saving best model------
    Epoch: 0025 Batch: 50 /134 lost = 6.213788 ppl = 499.59
    Epoch: 0025 Batch: 100 /134 lost = 6.180987 ppl = 483.469
    Valid 4864 samples after epoch: 0025 lost = 6.570986 ppl = 714.074
    ------Saving best model------
    Epoch: 0026 Batch: 50 /134 lost = 6.194365 ppl = 489.98
    Epoch: 0026 Batch: 100 /134 lost = 6.161218 ppl = 474.005
    Valid 4864 samples after epoch: 0026 lost = 6.565230 ppl = 709.975
    ------Saving best model------
    Epoch: 0027 Batch: 50 /134 lost = 6.177396 ppl = 481.736
    Epoch: 0027 Batch: 100 /134 lost = 6.143312 ppl = 465.593
    Valid 4864 samples after epoch: 0027 lost = 6.558723 ppl = 705.371
    ------Saving best model------
    Epoch: 0028 Batch: 50 /134 lost = 6.160506 ppl = 473.668
    Epoch: 0028 Batch: 100 /134 lost = 6.124416 ppl = 456.878
    Valid 4864 samples after epoch: 0028 lost = 6.553314 ppl = 701.565
    ------Saving best model------
    Epoch: 0029 Batch: 50 /134 lost = 6.145772 ppl = 466.74
    Epoch: 0029 Batch: 100 /134 lost = 6.106885 ppl = 448.938
    Valid 4864 samples after epoch: 0029 lost = 6.547598 ppl = 697.567
    ------Saving best model------
    Epoch: 0030 Batch: 50 /134 lost = 6.129242 ppl = 459.088
    Epoch: 0030 Batch: 100 /134 lost = 6.091740 ppl = 442.19
    Valid 4864 samples after epoch: 0030 lost = 6.541594 ppl = 693.391
    ------Saving best model------
    Epoch: 0031 Batch: 50 /134 lost = 6.112310 ppl = 451.38
    Epoch: 0031 Batch: 100 /134 lost = 6.075436 ppl = 435.039
    Valid 4864 samples after epoch: 0031 lost = 6.535635 ppl = 689.271
    ------Saving best model------
    Epoch: 0032 Batch: 50 /134 lost = 6.096963 ppl = 444.506
    Epoch: 0032 Batch: 100 /134 lost = 6.058256 ppl = 427.629
    Valid 4864 samples after epoch: 0032 lost = 6.531891 ppl = 686.695
    ------Saving best model------
    Epoch: 0033 Batch: 50 /134 lost = 6.084839 ppl = 439.149
    Epoch: 0033 Batch: 100 /134 lost = 6.041947 ppl = 420.712
    Valid 4864 samples after epoch: 0033 lost = 6.529337 ppl = 684.944
    ------Saving best model------
    Epoch: 0034 Batch: 50 /134 lost = 6.069464 ppl = 432.449
    Epoch: 0034 Batch: 100 /134 lost = 6.026278 ppl = 414.17
    Valid 4864 samples after epoch: 0034 lost = 6.528577 ppl = 684.423
    ------Saving best model------
    Epoch: 0035 Batch: 50 /134 lost = 6.059412 ppl = 428.124
    Epoch: 0035 Batch: 100 /134 lost = 6.012435 ppl = 408.477
    Valid 4864 samples after epoch: 0035 lost = 6.527236 ppl = 683.506
    ------Saving best model------
    Epoch: 0036 Batch: 50 /134 lost = 6.041071 ppl = 420.343
    Epoch: 0036 Batch: 100 /134 lost = 5.993114 ppl = 400.66
    Valid 4864 samples after epoch: 0036 lost = 6.526140 ppl = 682.758
    ------Saving best model------
    Epoch: 0037 Batch: 50 /134 lost = 6.029830 ppl = 415.645
    Epoch: 0037 Batch: 100 /134 lost = 5.978106 ppl = 394.692
    Valid 4864 samples after epoch: 0037 lost = 6.526049 ppl = 682.696
    ------Saving best model------
    Epoch: 0038 Batch: 50 /134 lost = 6.015990 ppl = 409.931
    Epoch: 0038 Batch: 100 /134 lost = 5.965052 ppl = 389.573
    Valid 4864 samples after epoch: 0038 lost = 6.525896 ppl = 682.591
    ------Saving best model------
    Epoch: 0039 Batch: 50 /134 lost = 6.002532 ppl = 404.452
    Epoch: 0039 Batch: 100 /134 lost = 5.950418 ppl = 383.914
    Valid 4864 samples after epoch: 0039 lost = 6.526688 ppl = 683.132
    Epoch: 0040 Batch: 50 /134 lost = 5.988401 ppl = 398.776
    Epoch: 0040 Batch: 100 /134 lost = 5.936747 ppl = 378.701
    Valid 4864 samples after epoch: 0040 lost = 6.526498 ppl = 683.002
    Epoch: 0041 Batch: 50 /134 lost = 5.976420 ppl = 394.027
    Epoch: 0041 Batch: 100 /134 lost = 5.923652 ppl = 373.774
    Valid 4864 samples after epoch: 0041 lost = 6.527845 ppl = 683.923
    Epoch: 0042 Batch: 50 /134 lost = 5.963865 ppl = 389.111
    Epoch: 0042 Batch: 100 /134 lost = 5.910876 ppl = 369.029
    Valid 4864 samples after epoch: 0042 lost = 6.528775 ppl = 684.559
    Epoch: 0043 Batch: 50 /134 lost = 5.951908 ppl = 384.486
    Epoch: 0043 Batch: 100 /134 lost = 5.897268 ppl = 364.042
    Valid 4864 samples after epoch: 0043 lost = 6.530298 ppl = 685.602
    Epoch: 0044 Batch: 50 /134 lost = 5.940265 ppl = 380.036
    Epoch: 0044 Batch: 100 /134 lost = 5.886415 ppl = 360.112
    Valid 4864 samples after epoch: 0044 lost = 6.532786 ppl = 687.31
    Epoch: 0045 Batch: 50 /134 lost = 5.932638 ppl = 377.148
    Epoch: 0045 Batch: 100 /134 lost = 5.874922 ppl = 355.997
    Valid 4864 samples after epoch: 0045 lost = 6.534653 ppl = 688.594
    Epoch: 0046 Batch: 50 /134 lost = 5.925174 ppl = 374.343
    Epoch: 0046 Batch: 100 /134 lost = 5.863554 ppl = 351.973
    Valid 4864 samples after epoch: 0046 lost = 6.538009 ppl = 690.91
    Epoch: 0047 Batch: 50 /134 lost = 5.912949 ppl = 369.795
    Epoch: 0047 Batch: 100 /134 lost = 5.849167 ppl = 346.945
    Valid 4864 samples after epoch: 0047 lost = 6.535372 ppl = 689.09
    Epoch: 0048 Batch: 50 /134 lost = 5.902872 ppl = 366.087
    Epoch: 0048 Batch: 100 /134 lost = 5.839842 ppl = 343.725
    Valid 4864 samples after epoch: 0048 lost = 6.538792 ppl = 691.451
    Epoch: 0049 Batch: 50 /134 lost = 5.893795 ppl = 362.78
    Epoch: 0049 Batch: 100 /134 lost = 5.830866 ppl = 340.654
    Valid 4864 samples after epoch: 0049 lost = 6.540362 ppl = 692.537
    Epoch: 0050 Batch: 50 /134 lost = 5.885963 ppl = 359.949
    Epoch: 0050 Batch: 100 /134 lost = 5.820601 ppl = 337.175
    Valid 4864 samples after epoch: 0050 lost = 6.544889 ppl = 695.679
    Epoch: 0051 Batch: 50 /134 lost = 5.876634 ppl = 356.607
    Epoch: 0051 Batch: 100 /134 lost = 5.810722 ppl = 333.86
    Valid 4864 samples after epoch: 0051 lost = 6.547203 ppl = 697.291
    Epoch: 0052 Batch: 50 /134 lost = 5.869237 ppl = 353.979
    Epoch: 0052 Batch: 100 /134 lost = 5.801808 ppl = 330.897
    Valid 4864 samples after epoch: 0052 lost = 6.550913 ppl = 699.883
    Epoch: 0053 Batch: 50 /134 lost = 5.861948 ppl = 351.408
    Epoch: 0053 Batch: 100 /134 lost = 5.792412 ppl = 327.803
    Valid 4864 samples after epoch: 0053 lost = 6.554808 ppl = 702.614
    Epoch: 0054 Batch: 50 /134 lost = 5.856957 ppl = 349.659
    Epoch: 0054 Batch: 100 /134 lost = 5.782725 ppl = 324.643
    Valid 4864 samples after epoch: 0054 lost = 6.558849 ppl = 705.46
    Epoch: 0055 Batch: 50 /134 lost = 5.850240 ppl = 347.318
    Epoch: 0055 Batch: 100 /134 lost = 5.774463 ppl = 321.972
    Valid 4864 samples after epoch: 0055 lost = 6.559896 ppl = 706.198
    Epoch: 0056 Batch: 50 /134 lost = 5.845062 ppl = 345.524
    Epoch: 0056 Batch: 100 /134 lost = 5.765787 ppl = 319.19
    Valid 4864 samples after epoch: 0056 lost = 6.565612 ppl = 710.247
    Epoch: 0057 Batch: 50 /134 lost = 5.837958 ppl = 343.078
    Epoch: 0057 Batch: 100 /134 lost = 5.758301 ppl = 316.81
    Valid 4864 samples after epoch: 0057 lost = 6.570758 ppl = 713.911
    Epoch: 0058 Batch: 50 /134 lost = 5.828923 ppl = 339.992
    Epoch: 0058 Batch: 100 /134 lost = 5.748642 ppl = 313.764
    Valid 4864 samples after epoch: 0058 lost = 6.571710 ppl = 714.591
    Epoch: 0059 Batch: 50 /134 lost = 5.820384 ppl = 337.101
    Epoch: 0059 Batch: 100 /134 lost = 5.741356 ppl = 311.486
    Valid 4864 samples after epoch: 0059 lost = 6.572393 ppl = 715.079
    Epoch: 0060 Batch: 50 /134 lost = 5.811657 ppl = 334.173
    Epoch: 0060 Batch: 100 /134 lost = 5.736628 ppl = 310.017
    Valid 4864 samples after epoch: 0060 lost = 6.575064 ppl = 716.992
    Epoch: 0061 Batch: 50 /134 lost = 5.802029 ppl = 330.97
    Epoch: 0061 Batch: 100 /134 lost = 5.729665 ppl = 307.866
    Valid 4864 samples after epoch: 0061 lost = 6.577415 ppl = 718.679
    Epoch: 0062 Batch: 50 /134 lost = 5.794467 ppl = 328.477
    Epoch: 0062 Batch: 100 /134 lost = 5.723306 ppl = 305.915
    Valid 4864 samples after epoch: 0062 lost = 6.580700 ppl = 721.044
    Epoch: 0063 Batch: 50 /134 lost = 5.788190 ppl = 326.422
    Epoch: 0063 Batch: 100 /134 lost = 5.718095 ppl = 304.325
    Valid 4864 samples after epoch: 0063 lost = 6.584888 ppl = 724.07
    Epoch: 0064 Batch: 50 /134 lost = 5.777824 ppl = 323.055
    Epoch: 0064 Batch: 100 /134 lost = 5.708221 ppl = 301.335
    Valid 4864 samples after epoch: 0064 lost = 6.587304 ppl = 725.821
    Epoch: 0065 Batch: 50 /134 lost = 5.771317 ppl = 320.96
    Epoch: 0065 Batch: 100 /134 lost = 5.700749 ppl = 299.091
    Valid 4864 samples after epoch: 0065 lost = 6.590825 ppl = 728.381
    Epoch: 0066 Batch: 50 /134 lost = 5.761464 ppl = 317.813
    Epoch: 0066 Batch: 100 /134 lost = 5.692882 ppl = 296.748
    Valid 4864 samples after epoch: 0066 lost = 6.596059 ppl = 732.204
    Epoch: 0067 Batch: 50 /134 lost = 5.751817 ppl = 314.762
    Epoch: 0067 Batch: 100 /134 lost = 5.686329 ppl = 294.809
    Valid 4864 samples after epoch: 0067 lost = 6.598680 ppl = 734.126
    Epoch: 0068 Batch: 50 /134 lost = 5.745711 ppl = 312.846
    Epoch: 0068 Batch: 100 /134 lost = 5.680383 ppl = 293.062
    Valid 4864 samples after epoch: 0068 lost = 6.604486 ppl = 738.4
    Epoch: 0069 Batch: 50 /134 lost = 5.738355 ppl = 310.553
    Epoch: 0069 Batch: 100 /134 lost = 5.673652 ppl = 291.096
    Valid 4864 samples after epoch: 0069 lost = 6.608468 ppl = 741.347
    Epoch: 0070 Batch: 50 /134 lost = 5.732303 ppl = 308.679
    Epoch: 0070 Batch: 100 /134 lost = 5.669883 ppl = 290.001
    Valid 4864 samples after epoch: 0070 lost = 6.610574 ppl = 742.909
    Epoch: 0071 Batch: 50 /134 lost = 5.722721 ppl = 305.736
    Epoch: 0071 Batch: 100 /134 lost = 5.659079 ppl = 286.884
    Valid 4864 samples after epoch: 0071 lost = 6.617020 ppl = 747.714
    Epoch: 0072 Batch: 50 /134 lost = 5.718213 ppl = 304.36
    Epoch: 0072 Batch: 100 /134 lost = 5.655289 ppl = 285.799
    Valid 4864 samples after epoch: 0072 lost = 6.618594 ppl = 748.891
    Epoch: 0073 Batch: 50 /134 lost = 5.709037 ppl = 301.58
    Epoch: 0073 Batch: 100 /134 lost = 5.648552 ppl = 283.88
    Valid 4864 samples after epoch: 0073 lost = 6.623851 ppl = 752.839
    Epoch: 0074 Batch: 50 /134 lost = 5.701883 ppl = 299.431
    Epoch: 0074 Batch: 100 /134 lost = 5.642900 ppl = 282.28
    Valid 4864 samples after epoch: 0074 lost = 6.629340 ppl = 756.982
    Epoch: 0075 Batch: 50 /134 lost = 5.697348 ppl = 298.076
    Epoch: 0075 Batch: 100 /134 lost = 5.637333 ppl = 280.713
    Valid 4864 samples after epoch: 0075 lost = 6.632624 ppl = 759.472
    Epoch: 0076 Batch: 50 /134 lost = 5.690535 ppl = 296.052
    Epoch: 0076 Batch: 100 /134 lost = 5.630487 ppl = 278.798
    Valid 4864 samples after epoch: 0076 lost = 6.638154 ppl = 763.684
    Epoch: 0077 Batch: 50 /134 lost = 5.683468 ppl = 293.967
    Epoch: 0077 Batch: 100 /134 lost = 5.624956 ppl = 277.26
    Valid 4864 samples after epoch: 0077 lost = 6.643793 ppl = 768.003
    Epoch: 0078 Batch: 50 /134 lost = 5.678069 ppl = 292.384
    Epoch: 0078 Batch: 100 /134 lost = 5.618418 ppl = 275.453
    Valid 4864 samples after epoch: 0078 lost = 6.646395 ppl = 770.003
    Epoch: 0079 Batch: 50 /134 lost = 5.672251 ppl = 290.688
    Epoch: 0079 Batch: 100 /134 lost = 5.612846 ppl = 273.923
    Valid 4864 samples after epoch: 0079 lost = 6.650727 ppl = 773.346
    Epoch: 0080 Batch: 50 /134 lost = 5.664543 ppl = 288.456
    Epoch: 0080 Batch: 100 /134 lost = 5.609095 ppl = 272.897
    Valid 4864 samples after epoch: 0080 lost = 6.654490 ppl = 776.262
    Epoch: 0081 Batch: 50 /134 lost = 5.658976 ppl = 286.855
    Epoch: 0081 Batch: 100 /134 lost = 5.603068 ppl = 271.257
    Valid 4864 samples after epoch: 0081 lost = 6.658694 ppl = 779.532
    Epoch: 0082 Batch: 50 /134 lost = 5.662236 ppl = 287.791
    Epoch: 0082 Batch: 100 /134 lost = 5.598522 ppl = 270.027
    Valid 4864 samples after epoch: 0082 lost = 6.663882 ppl = 783.587
    Epoch: 0083 Batch: 50 /134 lost = 5.646886 ppl = 283.408
    Epoch: 0083 Batch: 100 /134 lost = 5.591645 ppl = 268.176
    Valid 4864 samples after epoch: 0083 lost = 6.667993 ppl = 786.815
    Epoch: 0084 Batch: 50 /134 lost = 5.642204 ppl = 282.084
    Epoch: 0084 Batch: 100 /134 lost = 5.590231 ppl = 267.798
    Valid 4864 samples after epoch: 0084 lost = 6.673443 ppl = 791.115
    Epoch: 0085 Batch: 50 /134 lost = 5.635573 ppl = 280.219
    Epoch: 0085 Batch: 100 /134 lost = 5.582592 ppl = 265.76
    Valid 4864 samples after epoch: 0085 lost = 6.678561 ppl = 795.174
    Epoch: 0086 Batch: 50 /134 lost = 5.631193 ppl = 278.995
    Epoch: 0086 Batch: 100 /134 lost = 5.575193 ppl = 263.801
    Valid 4864 samples after epoch: 0086 lost = 6.682218 ppl = 798.087
    Epoch: 0087 Batch: 50 /134 lost = 5.625697 ppl = 277.466
    Epoch: 0087 Batch: 100 /134 lost = 5.571279 ppl = 262.77
    Valid 4864 samples after epoch: 0087 lost = 6.689477 ppl = 803.902
    Epoch: 0088 Batch: 50 /134 lost = 5.628462 ppl = 278.234
    Epoch: 0088 Batch: 100 /134 lost = 5.567883 ppl = 261.879
    Valid 4864 samples after epoch: 0088 lost = 6.692632 ppl = 806.442
    Epoch: 0089 Batch: 50 /134 lost = 5.612480 ppl = 273.823
    Epoch: 0089 Batch: 100 /134 lost = 5.562325 ppl = 260.428
    Valid 4864 samples after epoch: 0089 lost = 6.696252 ppl = 809.367
    Epoch: 0090 Batch: 50 /134 lost = 5.607959 ppl = 272.587
    Epoch: 0090 Batch: 100 /134 lost = 5.555902 ppl = 258.76
    Valid 4864 samples after epoch: 0090 lost = 6.702594 ppl = 814.516
    Epoch: 0091 Batch: 50 /134 lost = 5.604068 ppl = 271.529
    Epoch: 0091 Batch: 100 /134 lost = 5.555830 ppl = 258.742
    Valid 4864 samples after epoch: 0091 lost = 6.706570 ppl = 817.761
    Epoch: 0092 Batch: 50 /134 lost = 5.603107 ppl = 271.268
    Epoch: 0092 Batch: 100 /134 lost = 5.548122 ppl = 256.755
    Valid 4864 samples after epoch: 0092 lost = 6.707327 ppl = 818.38
    Epoch: 0093 Batch: 50 /134 lost = 5.596536 ppl = 269.491
    Epoch: 0093 Batch: 100 /134 lost = 5.544293 ppl = 255.774
    Valid 4864 samples after epoch: 0093 lost = 6.713945 ppl = 823.814
    Epoch: 0094 Batch: 50 /134 lost = 5.594147 ppl = 268.848
    Epoch: 0094 Batch: 100 /134 lost = 5.542672 ppl = 255.359
    Valid 4864 samples after epoch: 0094 lost = 6.719085 ppl = 828.059
    Epoch: 0095 Batch: 50 /134 lost = 5.588509 ppl = 267.337
    Epoch: 0095 Batch: 100 /134 lost = 5.535192 ppl = 253.456
    Valid 4864 samples after epoch: 0095 lost = 6.721343 ppl = 829.931
    Epoch: 0096 Batch: 50 /134 lost = 5.585382 ppl = 266.502
    Epoch: 0096 Batch: 100 /134 lost = 5.533434 ppl = 253.011
    Valid 4864 samples after epoch: 0096 lost = 6.730104 ppl = 837.235
    Epoch: 0097 Batch: 50 /134 lost = 5.582497 ppl = 265.734
    Epoch: 0097 Batch: 100 /134 lost = 5.531109 ppl = 252.424
    Valid 4864 samples after epoch: 0097 lost = 6.730214 ppl = 837.326
    Epoch: 0098 Batch: 50 /134 lost = 5.579361 ppl = 264.902
    Epoch: 0098 Batch: 100 /134 lost = 5.527757 ppl = 251.579
    Valid 4864 samples after epoch: 0098 lost = 6.734760 ppl = 841.142
    Epoch: 0099 Batch: 50 /134 lost = 5.573514 ppl = 263.358
    Epoch: 0099 Batch: 100 /134 lost = 5.524683 ppl = 250.807
    Valid 4864 samples after epoch: 0099 lost = 6.739151 ppl = 844.843
    Epoch: 0100 Batch: 50 /134 lost = 5.570263 ppl = 262.503
    Epoch: 0100 Batch: 100 /134 lost = 5.523971 ppl = 250.628
    Valid 4864 samples after epoch: 0100 lost = 6.742946 ppl = 848.055
    Epoch: 0101 Batch: 50 /134 lost = 5.564821 ppl = 261.079
    Epoch: 0101 Batch: 100 /134 lost = 5.519664 ppl = 249.551
    Valid 4864 samples after epoch: 0101 lost = 6.746530 ppl = 851.1
    Epoch: 0102 Batch: 50 /134 lost = 5.560958 ppl = 260.072
    Epoch: 0102 Batch: 100 /134 lost = 5.514766 ppl = 248.332
    Valid 4864 samples after epoch: 0102 lost = 6.748504 ppl = 852.782
    Epoch: 0103 Batch: 50 /134 lost = 5.558336 ppl = 259.391
    Epoch: 0103 Batch: 100 /134 lost = 5.515629 ppl = 248.546
    Valid 4864 samples after epoch: 0103 lost = 6.752589 ppl = 856.273
    Epoch: 0104 Batch: 50 /134 lost = 5.555253 ppl = 258.592
    Epoch: 0104 Batch: 100 /134 lost = 5.510290 ppl = 247.223
    Valid 4864 samples after epoch: 0104 lost = 6.756944 ppl = 860.01
    Epoch: 0105 Batch: 50 /134 lost = 5.551366 ppl = 257.589
    Epoch: 0105 Batch: 100 /134 lost = 5.504577 ppl = 245.814
    Valid 4864 samples after epoch: 0105 lost = 6.758952 ppl = 861.738
    Epoch: 0106 Batch: 50 /134 lost = 5.548397 ppl = 256.826
    Epoch: 0106 Batch: 100 /134 lost = 5.500866 ppl = 244.904
    Valid 4864 samples after epoch: 0106 lost = 6.763351 ppl = 865.538
    Epoch: 0107 Batch: 50 /134 lost = 5.547339 ppl = 256.554
    Epoch: 0107 Batch: 100 /134 lost = 5.502327 ppl = 245.262
    Valid 4864 samples after epoch: 0107 lost = 6.769986 ppl = 871.3
    Epoch: 0108 Batch: 50 /134 lost = 5.542034 ppl = 255.196
    Epoch: 0108 Batch: 100 /134 lost = 5.494353 ppl = 243.314
    Valid 4864 samples after epoch: 0108 lost = 6.773698 ppl = 874.54
    Epoch: 0109 Batch: 50 /134 lost = 5.538827 ppl = 254.38
    Epoch: 0109 Batch: 100 /134 lost = 5.491054 ppl = 242.513
    Valid 4864 samples after epoch: 0109 lost = 6.778270 ppl = 878.548
    Epoch: 0110 Batch: 50 /134 lost = 5.535790 ppl = 253.608
    Epoch: 0110 Batch: 100 /134 lost = 5.486816 ppl = 241.487
    Valid 4864 samples after epoch: 0110 lost = 6.779778 ppl = 879.873
    Epoch: 0111 Batch: 50 /134 lost = 5.548174 ppl = 256.768
    Epoch: 0111 Batch: 100 /134 lost = 5.489634 ppl = 242.168
    Valid 4864 samples after epoch: 0111 lost = 6.787449 ppl = 886.649
    Epoch: 0112 Batch: 50 /134 lost = 5.533995 ppl = 253.153
    Epoch: 0112 Batch: 100 /134 lost = 5.483225 ppl = 240.621
    Valid 4864 samples after epoch: 0112 lost = 6.787254 ppl = 886.476
    Epoch: 0113 Batch: 50 /134 lost = 5.527868 ppl = 251.607
    Epoch: 0113 Batch: 100 /134 lost = 5.477304 ppl = 239.201
    Valid 4864 samples after epoch: 0113 lost = 6.795111 ppl = 893.468
    Epoch: 0114 Batch: 50 /134 lost = 5.524411 ppl = 250.739
    Epoch: 0114 Batch: 100 /134 lost = 5.474809 ppl = 238.605
    Valid 4864 samples after epoch: 0114 lost = 6.797998 ppl = 896.052
    Epoch: 0115 Batch: 50 /134 lost = 5.522417 ppl = 250.239
    Epoch: 0115 Batch: 100 /134 lost = 5.474164 ppl = 238.451
    Valid 4864 samples after epoch: 0115 lost = 6.803396 ppl = 900.902
    Epoch: 0116 Batch: 50 /134 lost = 5.520910 ppl = 249.862
    Epoch: 0116 Batch: 100 /134 lost = 5.471118 ppl = 237.726
    Valid 4864 samples after epoch: 0116 lost = 6.807177 ppl = 904.315
    Epoch: 0117 Batch: 50 /134 lost = 5.518847 ppl = 249.347
    Epoch: 0117 Batch: 100 /134 lost = 5.466412 ppl = 236.61
    Valid 4864 samples after epoch: 0117 lost = 6.811106 ppl = 907.875
    Epoch: 0118 Batch: 50 /134 lost = 5.514682 ppl = 248.311
    Epoch: 0118 Batch: 100 /134 lost = 5.465050 ppl = 236.288
    Valid 4864 samples after epoch: 0118 lost = 6.817940 ppl = 914.1
    Epoch: 0119 Batch: 50 /134 lost = 5.512525 ppl = 247.776
    Epoch: 0119 Batch: 100 /134 lost = 5.458877 ppl = 234.833
    Valid 4864 samples after epoch: 0119 lost = 6.823854 ppl = 919.522
    Epoch: 0120 Batch: 50 /134 lost = 5.513165 ppl = 247.935
    Epoch: 0120 Batch: 100 /134 lost = 5.458862 ppl = 234.83
    Valid 4864 samples after epoch: 0120 lost = 6.825136 ppl = 920.701
    Epoch: 0121 Batch: 50 /134 lost = 5.508547 ppl = 246.792
    Epoch: 0121 Batch: 100 /134 lost = 5.452186 ppl = 233.268
    Valid 4864 samples after epoch: 0121 lost = 6.833524 ppl = 928.457
    Epoch: 0122 Batch: 50 /134 lost = 5.502888 ppl = 245.4
    Epoch: 0122 Batch: 100 /134 lost = 5.453557 ppl = 233.587
    Valid 4864 samples after epoch: 0122 lost = 6.837987 ppl = 932.61
    Epoch: 0123 Batch: 50 /134 lost = 5.499147 ppl = 244.483
    Epoch: 0123 Batch: 100 /134 lost = 5.449455 ppl = 232.631
    Valid 4864 samples after epoch: 0123 lost = 6.842930 ppl = 937.231
    Epoch: 0124 Batch: 50 /134 lost = 5.495465 ppl = 243.585
    Epoch: 0124 Batch: 100 /134 lost = 5.443827 ppl = 231.326
    Valid 4864 samples after epoch: 0124 lost = 6.847711 ppl = 941.723
    Epoch: 0125 Batch: 50 /134 lost = 5.496659 ppl = 243.876
    Epoch: 0125 Batch: 100 /134 lost = 5.439887 ppl = 230.416
    Valid 4864 samples after epoch: 0125 lost = 6.850019 ppl = 943.899
    Epoch: 0126 Batch: 50 /134 lost = 5.494706 ppl = 243.4
    Epoch: 0126 Batch: 100 /134 lost = 5.435842 ppl = 229.486
    Valid 4864 samples after epoch: 0126 lost = 6.857815 ppl = 951.286
    Epoch: 0127 Batch: 50 /134 lost = 5.492219 ppl = 242.795
    Epoch: 0127 Batch: 100 /134 lost = 5.432896 ppl = 228.811
    Valid 4864 samples after epoch: 0127 lost = 6.860477 ppl = 953.822
    Epoch: 0128 Batch: 50 /134 lost = 5.491840 ppl = 242.703
    Epoch: 0128 Batch: 100 /134 lost = 5.431963 ppl = 228.598
    Valid 4864 samples after epoch: 0128 lost = 6.863689 ppl = 956.891
    Epoch: 0129 Batch: 50 /134 lost = 5.487919 ppl = 241.754
    Epoch: 0129 Batch: 100 /134 lost = 5.424504 ppl = 226.899
    Valid 4864 samples after epoch: 0129 lost = 6.867708 ppl = 960.744
    Epoch: 0130 Batch: 50 /134 lost = 5.483914 ppl = 240.787
    Epoch: 0130 Batch: 100 /134 lost = 5.423192 ppl = 226.601
    Valid 4864 samples after epoch: 0130 lost = 6.872011 ppl = 964.887
    Epoch: 0131 Batch: 50 /134 lost = 5.483213 ppl = 240.619
    Epoch: 0131 Batch: 100 /134 lost = 5.416938 ppl = 225.188
    Valid 4864 samples after epoch: 0131 lost = 6.873600 ppl = 966.421
    Epoch: 0132 Batch: 50 /134 lost = 5.478416 ppl = 239.467
    Epoch: 0132 Batch: 100 /134 lost = 5.414811 ppl = 224.71
    Valid 4864 samples after epoch: 0132 lost = 6.879302 ppl = 971.947
    Epoch: 0133 Batch: 50 /134 lost = 5.472281 ppl = 238.003
    Epoch: 0133 Batch: 100 /134 lost = 5.412837 ppl = 224.267
    Valid 4864 samples after epoch: 0133 lost = 6.880401 ppl = 973.016
    Epoch: 0134 Batch: 50 /134 lost = 5.470618 ppl = 237.607
    Epoch: 0134 Batch: 100 /134 lost = 5.411393 ppl = 223.943
    Valid 4864 samples after epoch: 0134 lost = 6.884521 ppl = 977.033
    Epoch: 0135 Batch: 50 /134 lost = 5.465664 ppl = 236.433
    Epoch: 0135 Batch: 100 /134 lost = 5.409595 ppl = 223.541
    Valid 4864 samples after epoch: 0135 lost = 6.892312 ppl = 984.675
    Epoch: 0136 Batch: 50 /134 lost = 5.462638 ppl = 235.719
    Epoch: 0136 Batch: 100 /134 lost = 5.407292 ppl = 223.027
    Valid 4864 samples after epoch: 0136 lost = 6.892495 ppl = 984.856
    Epoch: 0137 Batch: 50 /134 lost = 5.463321 ppl = 235.879
    Epoch: 0137 Batch: 100 /134 lost = 5.404630 ppl = 222.434
    Valid 4864 samples after epoch: 0137 lost = 6.895221 ppl = 987.544
    Epoch: 0138 Batch: 50 /134 lost = 5.461926 ppl = 235.551
    Epoch: 0138 Batch: 100 /134 lost = 5.403162 ppl = 222.108
    Valid 4864 samples after epoch: 0138 lost = 6.899115 ppl = 991.397
    Epoch: 0139 Batch: 50 /134 lost = 5.457008 ppl = 234.395
    Epoch: 0139 Batch: 100 /134 lost = 5.401733 ppl = 221.791
    Valid 4864 samples after epoch: 0139 lost = 6.901627 ppl = 993.89
    Epoch: 0140 Batch: 50 /134 lost = 5.455798 ppl = 234.112
    Epoch: 0140 Batch: 100 /134 lost = 5.395806 ppl = 220.48
    Valid 4864 samples after epoch: 0140 lost = 6.905707 ppl = 997.954
    Epoch: 0141 Batch: 50 /134 lost = 5.453952 ppl = 233.68
    Epoch: 0141 Batch: 100 /134 lost = 5.397491 ppl = 220.852
    Valid 4864 samples after epoch: 0141 lost = 6.910189 ppl = 1002.44
    Epoch: 0142 Batch: 50 /134 lost = 5.451932 ppl = 233.208
    Epoch: 0142 Batch: 100 /134 lost = 5.393089 ppl = 219.882
    Valid 4864 samples after epoch: 0142 lost = 6.911763 ppl = 1004.02
    Epoch: 0143 Batch: 50 /134 lost = 5.447602 ppl = 232.201
    Epoch: 0143 Batch: 100 /134 lost = 5.387901 ppl = 218.744
    Valid 4864 samples after epoch: 0143 lost = 6.914671 ppl = 1006.94
    Epoch: 0144 Batch: 50 /134 lost = 5.443541 ppl = 231.26
    Epoch: 0144 Batch: 100 /134 lost = 5.387043 ppl = 218.556
    Valid 4864 samples after epoch: 0144 lost = 6.918516 ppl = 1010.82
    Epoch: 0145 Batch: 50 /134 lost = 5.436114 ppl = 229.548
    Epoch: 0145 Batch: 100 /134 lost = 5.387687 ppl = 218.697
    Valid 4864 samples after epoch: 0145 lost = 6.920179 ppl = 1012.5
    Epoch: 0146 Batch: 50 /134 lost = 5.439134 ppl = 230.243
    Epoch: 0146 Batch: 100 /134 lost = 5.382716 ppl = 217.612
    Valid 4864 samples after epoch: 0146 lost = 6.926800 ppl = 1019.23
    Epoch: 0147 Batch: 50 /134 lost = 5.434354 ppl = 229.145
    Epoch: 0147 Batch: 100 /134 lost = 5.397890 ppl = 220.94
    Valid 4864 samples after epoch: 0147 lost = 6.929781 ppl = 1022.27
    Epoch: 0148 Batch: 50 /134 lost = 5.434877 ppl = 229.265
    Epoch: 0148 Batch: 100 /134 lost = 5.384409 ppl = 217.981
    Valid 4864 samples after epoch: 0148 lost = 6.932597 ppl = 1025.15
    Epoch: 0149 Batch: 50 /134 lost = 5.428943 ppl = 227.908
    Epoch: 0149 Batch: 100 /134 lost = 5.378254 ppl = 216.644
    Valid 4864 samples after epoch: 0149 lost = 6.936402 ppl = 1029.06
    Epoch: 0150 Batch: 50 /134 lost = 5.424268 ppl = 226.845
    Epoch: 0150 Batch: 100 /134 lost = 5.371623 ppl = 215.212
    Valid 4864 samples after epoch: 0150 lost = 6.939618 ppl = 1032.38
    
    Test the LSTMLM……………………
    Test 5760 samples with models/(pytorch_api)1_layer_lstmlm_model_best.ckpt……………………
    lost = 6.448031 ppl = 631.458
    
