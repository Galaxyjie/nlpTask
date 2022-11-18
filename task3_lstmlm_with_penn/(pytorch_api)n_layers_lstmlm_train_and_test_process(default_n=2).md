```python
!python (pytorch_api)n_layers_lstmlm_with_penn_assignment(default_n=2).py
```

    The size of the dictionary is: 7613
    The number of the train batch is: 134
    
    Train the LSTMLM……………………
    TextLSTM(
      (C): Embedding(7613, 128)
      (LSTM): LSTM(128, 5, num_layers=2)
      (W): Linear(in_features=5, out_features=7613, bias=False)
    )
    Epoch: 0001 Batch: 50 /134 lost = 8.853827 ppl = 7001.13
    Epoch: 0001 Batch: 100 /134 lost = 8.688534 ppl = 5934.47
    Valid 4864 samples after epoch: 0001 lost = 8.523166 ppl = 5029.95
    Epoch: 0002 Batch: 50 /134 lost = 8.120270 ppl = 3361.93
    Epoch: 0002 Batch: 100 /134 lost = 7.781338 ppl = 2395.48
    Valid 4864 samples after epoch: 0002 lost = 7.639598 ppl = 2078.91
    Epoch: 0003 Batch: 50 /134 lost = 7.320689 ppl = 1511.25
    Epoch: 0003 Batch: 100 /134 lost = 7.170103 ppl = 1299.98
    Valid 4864 samples after epoch: 0003 lost = 7.168303 ppl = 1297.64
    Epoch: 0004 Batch: 50 /134 lost = 6.915230 ppl = 1007.5
    Epoch: 0004 Batch: 100 /134 lost = 6.832931 ppl = 927.907
    Valid 4864 samples after epoch: 0004 lost = 6.911205 ppl = 1003.46
    Epoch: 0005 Batch: 50 /134 lost = 6.684272 ppl = 799.728
    Epoch: 0005 Batch: 100 /134 lost = 6.633992 ppl = 760.512
    Valid 4864 samples after epoch: 0005 lost = 6.771512 ppl = 872.63
    Epoch: 0006 Batch: 50 /134 lost = 6.558464 ppl = 705.188
    Epoch: 0006 Batch: 100 /134 lost = 6.526266 ppl = 682.843
    Valid 4864 samples after epoch: 0006 lost = 6.705291 ppl = 816.716
    Epoch: 0007 Batch: 50 /134 lost = 6.495162 ppl = 661.932
    Epoch: 0007 Batch: 100 /134 lost = 6.473726 ppl = 647.893
    Valid 4864 samples after epoch: 0007 lost = 6.679165 ppl = 795.654
    Epoch: 0008 Batch: 50 /134 lost = 6.465087 ppl = 642.321
    Epoch: 0008 Batch: 100 /134 lost = 6.450098 ppl = 632.764
    Valid 4864 samples after epoch: 0008 lost = 6.671582 ppl = 789.644
    Epoch: 0009 Batch: 50 /134 lost = 6.451503 ppl = 633.654
    Epoch: 0009 Batch: 100 /134 lost = 6.439612 ppl = 626.164
    Valid 4864 samples after epoch: 0009 lost = 6.671037 ppl = 789.213
    Epoch: 0010 Batch: 50 /134 lost = 6.445230 ppl = 629.692
    Epoch: 0010 Batch: 100 /134 lost = 6.434365 ppl = 622.887
    Valid 4864 samples after epoch: 0010 lost = 6.672807 ppl = 790.612
    Epoch: 0011 Batch: 50 /134 lost = 6.441932 ppl = 627.618
    Epoch: 0011 Batch: 100 /134 lost = 6.431125 ppl = 620.872
    Valid 4864 samples after epoch: 0011 lost = 6.675311 ppl = 792.594
    Epoch: 0012 Batch: 50 /134 lost = 6.439713 ppl = 626.227
    Epoch: 0012 Batch: 100 /134 lost = 6.428267 ppl = 619.1
    Valid 4864 samples after epoch: 0012 lost = 6.677762 ppl = 794.539
    Epoch: 0013 Batch: 50 /134 lost = 6.437515 ppl = 624.852
    Epoch: 0013 Batch: 100 /134 lost = 6.424540 ppl = 616.797
    Valid 4864 samples after epoch: 0013 lost = 6.679537 ppl = 795.951
    Epoch: 0014 Batch: 50 /134 lost = 6.434882 ppl = 623.209
    Epoch: 0014 Batch: 100 /134 lost = 6.419114 ppl = 613.459
    Valid 4864 samples after epoch: 0014 lost = 6.679178 ppl = 795.665
    Epoch: 0015 Batch: 50 /134 lost = 6.428773 ppl = 619.413
    Epoch: 0015 Batch: 100 /134 lost = 6.400453 ppl = 602.118
    Valid 4864 samples after epoch: 0015 lost = 6.661433 ppl = 781.67
    Epoch: 0016 Batch: 50 /134 lost = 6.419050 ppl = 613.42
    Epoch: 0016 Batch: 100 /134 lost = 6.383695 ppl = 592.112
    Valid 4864 samples after epoch: 0016 lost = 6.654607 ppl = 776.353
    Epoch: 0017 Batch: 50 /134 lost = 6.406932 ppl = 606.031
    Epoch: 0017 Batch: 100 /134 lost = 6.369037 ppl = 583.495
    Valid 4864 samples after epoch: 0017 lost = 6.651626 ppl = 774.042
    Epoch: 0018 Batch: 50 /134 lost = 6.396557 ppl = 599.777
    Epoch: 0018 Batch: 100 /134 lost = 6.356931 ppl = 576.475
    Valid 4864 samples after epoch: 0018 lost = 6.651138 ppl = 773.665
    Epoch: 0019 Batch: 50 /134 lost = 6.387088 ppl = 594.124
    Epoch: 0019 Batch: 100 /134 lost = 6.345855 ppl = 570.125
    Valid 4864 samples after epoch: 0019 lost = 6.652702 ppl = 774.875
    Epoch: 0020 Batch: 50 /134 lost = 6.374506 ppl = 586.696
    Epoch: 0020 Batch: 100 /134 lost = 6.336066 ppl = 564.571
    Valid 4864 samples after epoch: 0020 lost = 6.655397 ppl = 776.966
    Epoch: 0021 Batch: 50 /134 lost = 6.361974 ppl = 579.389
    Epoch: 0021 Batch: 100 /134 lost = 6.326306 ppl = 559.087
    Valid 4864 samples after epoch: 0021 lost = 6.659273 ppl = 779.984
    Epoch: 0022 Batch: 50 /134 lost = 6.348553 ppl = 571.665
    Epoch: 0022 Batch: 100 /134 lost = 6.316976 ppl = 553.896
    Valid 4864 samples after epoch: 0022 lost = 6.662426 ppl = 782.447
    Epoch: 0023 Batch: 50 /134 lost = 6.334474 ppl = 563.673
    Epoch: 0023 Batch: 100 /134 lost = 6.309054 ppl = 549.525
    Valid 4864 samples after epoch: 0023 lost = 6.666261 ppl = 785.453
    Epoch: 0024 Batch: 50 /134 lost = 6.325992 ppl = 558.912
    Epoch: 0024 Batch: 100 /134 lost = 6.299595 ppl = 544.352
    Valid 4864 samples after epoch: 0024 lost = 6.669174 ppl = 787.744
    Epoch: 0025 Batch: 50 /134 lost = 6.313002 ppl = 551.699
    Epoch: 0025 Batch: 100 /134 lost = 6.289768 ppl = 539.028
    Valid 4864 samples after epoch: 0025 lost = 6.674283 ppl = 791.779
    Epoch: 0026 Batch: 50 /134 lost = 6.299757 ppl = 544.44
    Epoch: 0026 Batch: 100 /134 lost = 6.281118 ppl = 534.386
    Valid 4864 samples after epoch: 0026 lost = 6.677177 ppl = 794.075
    Epoch: 0027 Batch: 50 /134 lost = 6.287438 ppl = 537.774
    Epoch: 0027 Batch: 100 /134 lost = 6.270850 ppl = 528.927
    Valid 4864 samples after epoch: 0027 lost = 6.681371 ppl = 797.412
    Epoch: 0028 Batch: 50 /134 lost = 6.274910 ppl = 531.079
    Epoch: 0028 Batch: 100 /134 lost = 6.261266 ppl = 523.882
    Valid 4864 samples after epoch: 0028 lost = 6.684851 ppl = 800.192
    Epoch: 0029 Batch: 50 /134 lost = 6.264755 ppl = 525.713
    Epoch: 0029 Batch: 100 /134 lost = 6.251849 ppl = 518.972
    Valid 4864 samples after epoch: 0029 lost = 6.689099 ppl = 803.598
    Epoch: 0030 Batch: 50 /134 lost = 6.252850 ppl = 519.491
    Epoch: 0030 Batch: 100 /134 lost = 6.243554 ppl = 514.685
    Valid 4864 samples after epoch: 0030 lost = 6.694212 ppl = 807.717
    Epoch: 0031 Batch: 50 /134 lost = 6.243676 ppl = 514.747
    Epoch: 0031 Batch: 100 /134 lost = 6.235243 ppl = 510.425
    Valid 4864 samples after epoch: 0031 lost = 6.698833 ppl = 811.458
    Epoch: 0032 Batch: 50 /134 lost = 6.231846 ppl = 508.694
    Epoch: 0032 Batch: 100 /134 lost = 6.228718 ppl = 507.105
    Valid 4864 samples after epoch: 0032 lost = 6.703191 ppl = 815.002
    Epoch: 0033 Batch: 50 /134 lost = 6.219371 ppl = 502.387
    Epoch: 0033 Batch: 100 /134 lost = 6.220100 ppl = 502.753
    Valid 4864 samples after epoch: 0033 lost = 6.707455 ppl = 818.485
    Epoch: 0034 Batch: 50 /134 lost = 6.211210 ppl = 498.304
    Epoch: 0034 Batch: 100 /134 lost = 6.211961 ppl = 498.678
    Valid 4864 samples after epoch: 0034 lost = 6.711136 ppl = 821.504
    Epoch: 0035 Batch: 50 /134 lost = 6.198931 ppl = 492.223
    Epoch: 0035 Batch: 100 /134 lost = 6.205688 ppl = 495.56
    Valid 4864 samples after epoch: 0035 lost = 6.715232 ppl = 824.875
    Epoch: 0036 Batch: 50 /134 lost = 6.192276 ppl = 488.958
    Epoch: 0036 Batch: 100 /134 lost = 6.200420 ppl = 492.956
    Valid 4864 samples after epoch: 0036 lost = 6.721437 ppl = 830.009
    Epoch: 0037 Batch: 50 /134 lost = 6.183806 ppl = 484.834
    Epoch: 0037 Batch: 100 /134 lost = 6.193396 ppl = 489.505
    Valid 4864 samples after epoch: 0037 lost = 6.728454 ppl = 835.854
    Epoch: 0038 Batch: 50 /134 lost = 6.173839 ppl = 480.025
    Epoch: 0038 Batch: 100 /134 lost = 6.181683 ppl = 483.805
    Valid 4864 samples after epoch: 0038 lost = 6.732622 ppl = 839.345
    Epoch: 0039 Batch: 50 /134 lost = 6.162306 ppl = 474.521
    Epoch: 0039 Batch: 100 /134 lost = 6.175233 ppl = 480.695
    Valid 4864 samples after epoch: 0039 lost = 6.741191 ppl = 846.568
    Epoch: 0040 Batch: 50 /134 lost = 6.153006 ppl = 470.129
    Epoch: 0040 Batch: 100 /134 lost = 6.167548 ppl = 477.015
    Valid 4864 samples after epoch: 0040 lost = 6.746223 ppl = 850.839
    Epoch: 0041 Batch: 50 /134 lost = 6.144093 ppl = 465.957
    Epoch: 0041 Batch: 100 /134 lost = 6.157865 ppl = 472.418
    Valid 4864 samples after epoch: 0041 lost = 6.752772 ppl = 856.43
    Epoch: 0042 Batch: 50 /134 lost = 6.137353 ppl = 462.827
    Epoch: 0042 Batch: 100 /134 lost = 6.151331 ppl = 469.342
    Valid 4864 samples after epoch: 0042 lost = 6.760309 ppl = 862.909
    Epoch: 0043 Batch: 50 /134 lost = 6.128848 ppl = 458.907
    Epoch: 0043 Batch: 100 /134 lost = 6.144875 ppl = 466.321
    Valid 4864 samples after epoch: 0043 lost = 6.766918 ppl = 868.63
    Epoch: 0044 Batch: 50 /134 lost = 6.120333 ppl = 455.016
    Epoch: 0044 Batch: 100 /134 lost = 6.139443 ppl = 463.795
    Valid 4864 samples after epoch: 0044 lost = 6.772409 ppl = 873.413
    Epoch: 0045 Batch: 50 /134 lost = 6.111994 ppl = 451.237
    Epoch: 0045 Batch: 100 /134 lost = 6.130813 ppl = 459.81
    Valid 4864 samples after epoch: 0045 lost = 6.778535 ppl = 878.781
    Epoch: 0046 Batch: 50 /134 lost = 6.104007 ppl = 447.648
    Epoch: 0046 Batch: 100 /134 lost = 6.123403 ppl = 456.415
    Valid 4864 samples after epoch: 0046 lost = 6.786024 ppl = 885.386
    Epoch: 0047 Batch: 50 /134 lost = 6.097380 ppl = 444.691
    Epoch: 0047 Batch: 100 /134 lost = 6.120418 ppl = 455.055
    Valid 4864 samples after epoch: 0047 lost = 6.791186 ppl = 889.969
    Epoch: 0048 Batch: 50 /134 lost = 6.089028 ppl = 440.993
    Epoch: 0048 Batch: 100 /134 lost = 6.111374 ppl = 450.958
    Valid 4864 samples after epoch: 0048 lost = 6.797850 ppl = 895.919
    Epoch: 0049 Batch: 50 /134 lost = 6.082368 ppl = 438.065
    Epoch: 0049 Batch: 100 /134 lost = 6.109532 ppl = 450.128
    Valid 4864 samples after epoch: 0049 lost = 6.805203 ppl = 902.531
    Epoch: 0050 Batch: 50 /134 lost = 6.074555 ppl = 434.656
    Epoch: 0050 Batch: 100 /134 lost = 6.102276 ppl = 446.874
    Valid 4864 samples after epoch: 0050 lost = 6.808159 ppl = 905.202
    Epoch: 0051 Batch: 50 /134 lost = 6.068032 ppl = 431.83
    Epoch: 0051 Batch: 100 /134 lost = 6.093409 ppl = 442.929
    Valid 4864 samples after epoch: 0051 lost = 6.815271 ppl = 911.663
    Epoch: 0052 Batch: 50 /134 lost = 6.061585 ppl = 429.055
    Epoch: 0052 Batch: 100 /134 lost = 6.085169 ppl = 439.294
    Valid 4864 samples after epoch: 0052 lost = 6.821824 ppl = 917.658
    Epoch: 0053 Batch: 50 /134 lost = 6.055660 ppl = 426.52
    Epoch: 0053 Batch: 100 /134 lost = 6.084840 ppl = 439.15
    Valid 4864 samples after epoch: 0053 lost = 6.829436 ppl = 924.669
    Epoch: 0054 Batch: 50 /134 lost = 6.051291 ppl = 424.661
    Epoch: 0054 Batch: 100 /134 lost = 6.074716 ppl = 434.726
    Valid 4864 samples after epoch: 0054 lost = 6.834567 ppl = 929.426
    Epoch: 0055 Batch: 50 /134 lost = 6.047716 ppl = 423.145
    Epoch: 0055 Batch: 100 /134 lost = 6.068833 ppl = 432.176
    Valid 4864 samples after epoch: 0055 lost = 6.839769 ppl = 934.273
    Epoch: 0056 Batch: 50 /134 lost = 6.039555 ppl = 419.706
    Epoch: 0056 Batch: 100 /134 lost = 6.064886 ppl = 430.474
    Valid 4864 samples after epoch: 0056 lost = 6.844299 ppl = 938.515
    Epoch: 0057 Batch: 50 /134 lost = 6.031453 ppl = 416.32
    Epoch: 0057 Batch: 100 /134 lost = 6.059992 ppl = 428.372
    Valid 4864 samples after epoch: 0057 lost = 6.851431 ppl = 945.233
    Epoch: 0058 Batch: 50 /134 lost = 6.024360 ppl = 413.377
    Epoch: 0058 Batch: 100 /134 lost = 6.053123 ppl = 425.44
    Valid 4864 samples after epoch: 0058 lost = 6.856071 ppl = 949.629
    Epoch: 0059 Batch: 50 /134 lost = 6.022131 ppl = 412.457
    Epoch: 0059 Batch: 100 /134 lost = 6.050346 ppl = 424.26
    Valid 4864 samples after epoch: 0059 lost = 6.862073 ppl = 955.346
    Epoch: 0060 Batch: 50 /134 lost = 6.013578 ppl = 408.944
    Epoch: 0060 Batch: 100 /134 lost = 6.043959 ppl = 421.559
    Valid 4864 samples after epoch: 0060 lost = 6.868440 ppl = 961.447
    Epoch: 0061 Batch: 50 /134 lost = 6.013056 ppl = 408.73
    Epoch: 0061 Batch: 100 /134 lost = 6.036979 ppl = 418.627
    Valid 4864 samples after epoch: 0061 lost = 6.873619 ppl = 966.44
    Epoch: 0062 Batch: 50 /134 lost = 6.000854 ppl = 403.773
    Epoch: 0062 Batch: 100 /134 lost = 6.036247 ppl = 418.32
    Valid 4864 samples after epoch: 0062 lost = 6.879909 ppl = 972.538
    Epoch: 0063 Batch: 50 /134 lost = 6.000845 ppl = 403.77
    Epoch: 0063 Batch: 100 /134 lost = 6.024889 ppl = 413.596
    Valid 4864 samples after epoch: 0063 lost = 6.886130 ppl = 978.607
    Epoch: 0064 Batch: 50 /134 lost = 6.008169 ppl = 406.738
    Epoch: 0064 Batch: 100 /134 lost = 6.025193 ppl = 413.722
    Valid 4864 samples after epoch: 0064 lost = 6.887586 ppl = 980.033
    Epoch: 0065 Batch: 50 /134 lost = 5.987059 ppl = 398.242
    Epoch: 0065 Batch: 100 /134 lost = 6.014064 ppl = 409.143
    Valid 4864 samples after epoch: 0065 lost = 6.895359 ppl = 987.68
    Epoch: 0066 Batch: 50 /134 lost = 5.981164 ppl = 395.901
    Epoch: 0066 Batch: 100 /134 lost = 6.008307 ppl = 406.794
    Valid 4864 samples after epoch: 0066 lost = 6.898525 ppl = 990.812
    Epoch: 0067 Batch: 50 /134 lost = 5.975319 ppl = 393.594
    Epoch: 0067 Batch: 100 /134 lost = 6.001648 ppl = 404.094
    Valid 4864 samples after epoch: 0067 lost = 6.904012 ppl = 996.263
    Epoch: 0068 Batch: 50 /134 lost = 5.970799 ppl = 391.819
    Epoch: 0068 Batch: 100 /134 lost = 5.994011 ppl = 401.02
    Valid 4864 samples after epoch: 0068 lost = 6.907685 ppl = 999.93
    Epoch: 0069 Batch: 50 /134 lost = 5.965472 ppl = 389.737
    Epoch: 0069 Batch: 100 /134 lost = 5.987823 ppl = 398.546
    Valid 4864 samples after epoch: 0069 lost = 6.912242 ppl = 1004.5
    Epoch: 0070 Batch: 50 /134 lost = 5.961347 ppl = 388.133
    Epoch: 0070 Batch: 100 /134 lost = 5.988038 ppl = 398.632
    Valid 4864 samples after epoch: 0070 lost = 6.919409 ppl = 1011.72
    Epoch: 0071 Batch: 50 /134 lost = 5.958632 ppl = 387.08
    Epoch: 0071 Batch: 100 /134 lost = 5.976923 ppl = 394.225
    Valid 4864 samples after epoch: 0071 lost = 6.926060 ppl = 1018.47
    Epoch: 0072 Batch: 50 /134 lost = 5.950277 ppl = 383.86
    Epoch: 0072 Batch: 100 /134 lost = 5.974737 ppl = 393.365
    Valid 4864 samples after epoch: 0072 lost = 6.926019 ppl = 1018.43
    Epoch: 0073 Batch: 50 /134 lost = 5.944599 ppl = 381.686
    Epoch: 0073 Batch: 100 /134 lost = 5.964543 ppl = 389.375
    Valid 4864 samples after epoch: 0073 lost = 6.935140 ppl = 1027.76
    Epoch: 0074 Batch: 50 /134 lost = 5.937744 ppl = 379.079
    Epoch: 0074 Batch: 100 /134 lost = 5.960586 ppl = 387.837
    Valid 4864 samples after epoch: 0074 lost = 6.942261 ppl = 1035.11
    Epoch: 0075 Batch: 50 /134 lost = 5.930207 ppl = 376.232
    Epoch: 0075 Batch: 100 /134 lost = 5.955641 ppl = 385.924
    Valid 4864 samples after epoch: 0075 lost = 6.948110 ppl = 1041.18
    Epoch: 0076 Batch: 50 /134 lost = 5.927581 ppl = 375.246
    Epoch: 0076 Batch: 100 /134 lost = 5.953806 ppl = 385.217
    Valid 4864 samples after epoch: 0076 lost = 6.950797 ppl = 1043.98
    Epoch: 0077 Batch: 50 /134 lost = 5.922920 ppl = 373.501
    Epoch: 0077 Batch: 100 /134 lost = 5.946633 ppl = 382.464
    Valid 4864 samples after epoch: 0077 lost = 6.956483 ppl = 1049.93
    Epoch: 0078 Batch: 50 /134 lost = 5.918194 ppl = 371.74
    Epoch: 0078 Batch: 100 /134 lost = 5.940596 ppl = 380.161
    Valid 4864 samples after epoch: 0078 lost = 6.961458 ppl = 1055.17
    Epoch: 0079 Batch: 50 /134 lost = 5.909424 ppl = 368.494
    Epoch: 0079 Batch: 100 /134 lost = 5.937534 ppl = 378.999
    Valid 4864 samples after epoch: 0079 lost = 6.967217 ppl = 1061.27
    Epoch: 0080 Batch: 50 /134 lost = 5.903700 ppl = 366.391
    Epoch: 0080 Batch: 100 /134 lost = 5.930169 ppl = 376.218
    Valid 4864 samples after epoch: 0080 lost = 6.975494 ppl = 1070.09
    Epoch: 0081 Batch: 50 /134 lost = 5.898625 ppl = 364.536
    Epoch: 0081 Batch: 100 /134 lost = 5.926027 ppl = 374.663
    Valid 4864 samples after epoch: 0081 lost = 6.977837 ppl = 1072.6
    Epoch: 0082 Batch: 50 /134 lost = 5.890972 ppl = 361.757
    Epoch: 0082 Batch: 100 /134 lost = 5.919846 ppl = 372.354
    Valid 4864 samples after epoch: 0082 lost = 6.987677 ppl = 1083.2
    Epoch: 0083 Batch: 50 /134 lost = 5.886285 ppl = 360.065
    Epoch: 0083 Batch: 100 /134 lost = 5.913159 ppl = 369.873
    Valid 4864 samples after epoch: 0083 lost = 6.987787 ppl = 1083.32
    Epoch: 0084 Batch: 50 /134 lost = 5.882788 ppl = 358.808
    Epoch: 0084 Batch: 100 /134 lost = 5.911679 ppl = 369.326
    Valid 4864 samples after epoch: 0084 lost = 6.993909 ppl = 1089.97
    Epoch: 0085 Batch: 50 /134 lost = 5.876077 ppl = 356.408
    Epoch: 0085 Batch: 100 /134 lost = 5.903263 ppl = 366.231
    Valid 4864 samples after epoch: 0085 lost = 7.004875 ppl = 1101.99
    Epoch: 0086 Batch: 50 /134 lost = 5.875689 ppl = 356.27
    Epoch: 0086 Batch: 100 /134 lost = 5.902569 ppl = 365.977
    Valid 4864 samples after epoch: 0086 lost = 7.007947 ppl = 1105.38
    Epoch: 0087 Batch: 50 /134 lost = 5.868105 ppl = 353.578
    Epoch: 0087 Batch: 100 /134 lost = 5.899069 ppl = 364.698
    Valid 4864 samples after epoch: 0087 lost = 7.014567 ppl = 1112.73
    Epoch: 0088 Batch: 50 /134 lost = 5.868683 ppl = 353.783
    Epoch: 0088 Batch: 100 /134 lost = 5.892945 ppl = 362.471
    Valid 4864 samples after epoch: 0088 lost = 7.020656 ppl = 1119.52
    Epoch: 0089 Batch: 50 /134 lost = 5.859198 ppl = 350.443
    Epoch: 0089 Batch: 100 /134 lost = 5.886217 ppl = 360.041
    Valid 4864 samples after epoch: 0089 lost = 7.023899 ppl = 1123.16
    Epoch: 0090 Batch: 50 /134 lost = 5.859133 ppl = 350.42
    Epoch: 0090 Batch: 100 /134 lost = 5.882999 ppl = 358.884
    Valid 4864 samples after epoch: 0090 lost = 7.031926 ppl = 1132.21
    Epoch: 0091 Batch: 50 /134 lost = 5.850577 ppl = 347.435
    Epoch: 0091 Batch: 100 /134 lost = 5.877688 ppl = 356.983
    Valid 4864 samples after epoch: 0091 lost = 7.036684 ppl = 1137.61
    Epoch: 0092 Batch: 50 /134 lost = 5.854243 ppl = 348.711
    Epoch: 0092 Batch: 100 /134 lost = 5.874691 ppl = 355.915
    Valid 4864 samples after epoch: 0092 lost = 7.044147 ppl = 1146.13
    Epoch: 0093 Batch: 50 /134 lost = 5.844785 ppl = 345.428
    Epoch: 0093 Batch: 100 /134 lost = 5.877782 ppl = 357.017
    Valid 4864 samples after epoch: 0093 lost = 7.048855 ppl = 1151.54
    Epoch: 0094 Batch: 50 /134 lost = 5.843340 ppl = 344.929
    Epoch: 0094 Batch: 100 /134 lost = 5.864892 ppl = 352.444
    Valid 4864 samples after epoch: 0094 lost = 7.057554 ppl = 1161.6
    Epoch: 0095 Batch: 50 /134 lost = 5.836949 ppl = 342.732
    Epoch: 0095 Batch: 100 /134 lost = 5.861639 ppl = 351.299
    Valid 4864 samples after epoch: 0095 lost = 7.067950 ppl = 1173.74
    Epoch: 0096 Batch: 50 /134 lost = 5.839621 ppl = 343.649
    Epoch: 0096 Batch: 100 /134 lost = 5.856459 ppl = 349.484
    Valid 4864 samples after epoch: 0096 lost = 7.072243 ppl = 1178.79
    Epoch: 0097 Batch: 50 /134 lost = 5.829932 ppl = 340.336
    Epoch: 0097 Batch: 100 /134 lost = 5.855381 ppl = 349.108
    Valid 4864 samples after epoch: 0097 lost = 7.079755 ppl = 1187.68
    Epoch: 0098 Batch: 50 /134 lost = 5.821404 ppl = 337.446
    Epoch: 0098 Batch: 100 /134 lost = 5.850596 ppl = 347.442
    Valid 4864 samples after epoch: 0098 lost = 7.086959 ppl = 1196.26
    Epoch: 0099 Batch: 50 /134 lost = 5.822605 ppl = 337.851
    Epoch: 0099 Batch: 100 /134 lost = 5.848646 ppl = 346.764
    Valid 4864 samples after epoch: 0099 lost = 7.094290 ppl = 1205.07
    Epoch: 0100 Batch: 50 /134 lost = 5.814219 ppl = 335.029
    Epoch: 0100 Batch: 100 /134 lost = 5.842525 ppl = 344.649
    Valid 4864 samples after epoch: 0100 lost = 7.100419 ppl = 1212.48
    
    Test the LSTMLM……………………
    Test 5760 samples with models/(pytorch_api)2_layers_lstmlm_model_epoch100.ckpt……………………
    lost = 6.977028 ppl = 1071.73
    