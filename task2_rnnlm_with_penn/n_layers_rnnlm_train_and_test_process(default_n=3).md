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
    Epoch: 0001 Batch: 50 /134 lost = 8.820600 ppl = 6772.32
    Epoch: 0001 Batch: 100 /134 lost = 8.653352 ppl = 5729.32
    Valid 4864 samples after epoch: 0001 lost = 8.529416 ppl = 5061.49
    ------Saving best model------
    Epoch: 0002 Batch: 50 /134 lost = 8.336817 ppl = 4174.78
    Epoch: 0002 Batch: 100 /134 lost = 8.190594 ppl = 3606.86
    Valid 4864 samples after epoch: 0002 lost = 8.095963 ppl = 3281.19
    ------Saving best model------
    Epoch: 0003 Batch: 50 /134 lost = 7.900846 ppl = 2699.57
    Epoch: 0003 Batch: 100 /134 lost = 7.775221 ppl = 2380.87
    Valid 4864 samples after epoch: 0003 lost = 7.715477 ppl = 2242.79
    ------Saving best model------
    Epoch: 0004 Batch: 50 /134 lost = 7.520903 ppl = 1846.23
    Epoch: 0004 Batch: 100 /134 lost = 7.419019 ppl = 1667.4
    Valid 4864 samples after epoch: 0004 lost = 7.399774 ppl = 1635.62
    ------Saving best model------
    Epoch: 0005 Batch: 50 /134 lost = 7.202779 ppl = 1343.16
    Epoch: 0005 Batch: 100 /134 lost = 7.124298 ppl = 1241.78
    Valid 4864 samples after epoch: 0005 lost = 7.146825 ppl = 1270.07
    ------Saving best model------
    Epoch: 0006 Batch: 50 /134 lost = 6.951413 ppl = 1044.62
    Epoch: 0006 Batch: 100 /134 lost = 6.891466 ppl = 983.842
    Valid 4864 samples after epoch: 0006 lost = 6.955034 ppl = 1048.41
    ------Saving best model------
    Epoch: 0007 Batch: 50 /134 lost = 6.762118 ppl = 864.471
    Epoch: 0007 Batch: 100 /134 lost = 6.718598 ppl = 827.657
    Valid 4864 samples after epoch: 0007 lost = 6.818985 ppl = 915.055
    ------Saving best model------
    Epoch: 0008 Batch: 50 /134 lost = 6.627956 ppl = 755.936
    Epoch: 0008 Batch: 100 /134 lost = 6.598228 ppl = 733.794
    Valid 4864 samples after epoch: 0008 lost = 6.730625 ppl = 837.67
    ------Saving best model------
    Epoch: 0009 Batch: 50 /134 lost = 6.539236 ppl = 691.758
    Epoch: 0009 Batch: 100 /134 lost = 6.520950 ppl = 679.224
    Valid 4864 samples after epoch: 0009 lost = 6.678583 ppl = 795.192
    ------Saving best model------
    Epoch: 0010 Batch: 50 /134 lost = 6.486004 ppl = 655.897
    Epoch: 0010 Batch: 100 /134 lost = 6.475406 ppl = 648.983
    Valid 4864 samples after epoch: 0010 lost = 6.650608 ppl = 773.254
    ------Saving best model------
    Epoch: 0011 Batch: 50 /134 lost = 6.454514 ppl = 635.564
    Epoch: 0011 Batch: 100 /134 lost = 6.449154 ppl = 632.167
    Valid 4864 samples after epoch: 0011 lost = 6.635588 ppl = 761.727
    ------Saving best model------
    Epoch: 0012 Batch: 50 /134 lost = 6.436854 ppl = 624.439
    Epoch: 0012 Batch: 100 /134 lost = 6.432652 ppl = 621.821
    Valid 4864 samples after epoch: 0012 lost = 6.627399 ppl = 755.514
    ------Saving best model------
    Epoch: 0013 Batch: 50 /134 lost = 6.425820 ppl = 617.587
    Epoch: 0013 Batch: 100 /134 lost = 6.420884 ppl = 614.546
    Valid 4864 samples after epoch: 0013 lost = 6.623941 ppl = 752.906
    ------Saving best model------
    Epoch: 0014 Batch: 50 /134 lost = 6.417737 ppl = 612.615
    Epoch: 0014 Batch: 100 /134 lost = 6.412913 ppl = 609.667
    Valid 4864 samples after epoch: 0014 lost = 6.621390 ppl = 750.988
    ------Saving best model------
    Epoch: 0015 Batch: 50 /134 lost = 6.409235 ppl = 607.429
    Epoch: 0015 Batch: 100 /134 lost = 6.404340 ppl = 604.463
    Valid 4864 samples after epoch: 0015 lost = 6.620282 ppl = 750.156
    ------Saving best model------
    Epoch: 0016 Batch: 50 /134 lost = 6.402124 ppl = 603.125
    Epoch: 0016 Batch: 100 /134 lost = 6.397797 ppl = 600.52
    Valid 4864 samples after epoch: 0016 lost = 6.619381 ppl = 749.481
    ------Saving best model------
    Epoch: 0017 Batch: 50 /134 lost = 6.398095 ppl = 600.7
    Epoch: 0017 Batch: 100 /134 lost = 6.392832 ppl = 597.546
    Valid 4864 samples after epoch: 0017 lost = 6.619693 ppl = 749.715
    Epoch: 0018 Batch: 50 /134 lost = 6.394389 ppl = 598.478
    Epoch: 0018 Batch: 100 /134 lost = 6.388141 ppl = 594.75
    Valid 4864 samples after epoch: 0018 lost = 6.620014 ppl = 749.955
    Epoch: 0019 Batch: 50 /134 lost = 6.391193 ppl = 596.568
    Epoch: 0019 Batch: 100 /134 lost = 6.382832 ppl = 591.6
    Valid 4864 samples after epoch: 0019 lost = 6.620729 ppl = 750.492
    Epoch: 0020 Batch: 50 /134 lost = 6.388607 ppl = 595.027
    Epoch: 0020 Batch: 100 /134 lost = 6.376812 ppl = 588.05
    Valid 4864 samples after epoch: 0020 lost = 6.621596 ppl = 751.143
    Epoch: 0021 Batch: 50 /134 lost = 6.384116 ppl = 592.361
    Epoch: 0021 Batch: 100 /134 lost = 6.371406 ppl = 584.879
    Valid 4864 samples after epoch: 0021 lost = 6.621567 ppl = 751.121
    Epoch: 0022 Batch: 50 /134 lost = 6.379173 ppl = 589.44
    Epoch: 0022 Batch: 100 /134 lost = 6.368134 ppl = 582.969
    Valid 4864 samples after epoch: 0022 lost = 6.621868 ppl = 751.348
    Epoch: 0023 Batch: 50 /134 lost = 6.373458 ppl = 586.081
    Epoch: 0023 Batch: 100 /134 lost = 6.363953 ppl = 580.537
    Valid 4864 samples after epoch: 0023 lost = 6.620805 ppl = 750.549
    Epoch: 0024 Batch: 50 /134 lost = 6.370037 ppl = 584.079
    Epoch: 0024 Batch: 100 /134 lost = 6.359857 ppl = 578.164
    Valid 4864 samples after epoch: 0024 lost = 6.621684 ppl = 751.209
    Epoch: 0025 Batch: 50 /134 lost = 6.365312 ppl = 581.326
    Epoch: 0025 Batch: 100 /134 lost = 6.355546 ppl = 575.676
    Valid 4864 samples after epoch: 0025 lost = 6.622859 ppl = 752.092
    Epoch: 0026 Batch: 50 /134 lost = 6.362241 ppl = 579.544
    Epoch: 0026 Batch: 100 /134 lost = 6.351879 ppl = 573.57
    Valid 4864 samples after epoch: 0026 lost = 6.623874 ppl = 752.856
    Epoch: 0027 Batch: 50 /134 lost = 6.359139 ppl = 577.749
    Epoch: 0027 Batch: 100 /134 lost = 6.348844 ppl = 571.831
    Valid 4864 samples after epoch: 0027 lost = 6.623600 ppl = 752.65
    Epoch: 0028 Batch: 50 /134 lost = 6.355187 ppl = 575.47
    Epoch: 0028 Batch: 100 /134 lost = 6.345378 ppl = 569.853
    Valid 4864 samples after epoch: 0028 lost = 6.622302 ppl = 751.673
    Epoch: 0029 Batch: 50 /134 lost = 6.351308 ppl = 573.242
    Epoch: 0029 Batch: 100 /134 lost = 6.340318 ppl = 566.976
    Valid 4864 samples after epoch: 0029 lost = 6.619423 ppl = 749.513
    Epoch: 0030 Batch: 50 /134 lost = 6.346092 ppl = 570.26
    Epoch: 0030 Batch: 100 /134 lost = 6.328350 ppl = 560.231
    Valid 4864 samples after epoch: 0030 lost = 6.606843 ppl = 740.143
    ------Saving best model------
    Epoch: 0031 Batch: 50 /134 lost = 6.337146 ppl = 565.181
    Epoch: 0031 Batch: 100 /134 lost = 6.320468 ppl = 555.833
    Valid 4864 samples after epoch: 0031 lost = 6.605765 ppl = 739.345
    ------Saving best model------
    Epoch: 0032 Batch: 50 /134 lost = 6.330908 ppl = 561.667
    Epoch: 0032 Batch: 100 /134 lost = 6.314496 ppl = 552.523
    Valid 4864 samples after epoch: 0032 lost = 6.604525 ppl = 738.429
    ------Saving best model------
    Epoch: 0033 Batch: 50 /134 lost = 6.325742 ppl = 558.772
    Epoch: 0033 Batch: 100 /134 lost = 6.309359 ppl = 549.692
    Valid 4864 samples after epoch: 0033 lost = 6.603554 ppl = 737.712
    ------Saving best model------
    Epoch: 0034 Batch: 50 /134 lost = 6.320560 ppl = 555.884
    Epoch: 0034 Batch: 100 /134 lost = 6.304439 ppl = 546.994
    Valid 4864 samples after epoch: 0034 lost = 6.603161 ppl = 737.422
    ------Saving best model------
    Epoch: 0035 Batch: 50 /134 lost = 6.315536 ppl = 553.098
    Epoch: 0035 Batch: 100 /134 lost = 6.299138 ppl = 544.103
    Valid 4864 samples after epoch: 0035 lost = 6.602899 ppl = 737.229
    ------Saving best model------
    Epoch: 0036 Batch: 50 /134 lost = 6.311227 ppl = 550.72
    Epoch: 0036 Batch: 100 /134 lost = 6.294276 ppl = 541.464
    Valid 4864 samples after epoch: 0036 lost = 6.602971 ppl = 737.282
    Epoch: 0037 Batch: 50 /134 lost = 6.306599 ppl = 548.178
    Epoch: 0037 Batch: 100 /134 lost = 6.288992 ppl = 538.61
    Valid 4864 samples after epoch: 0037 lost = 6.602952 ppl = 737.268
    Epoch: 0038 Batch: 50 /134 lost = 6.302850 ppl = 546.126
    Epoch: 0038 Batch: 100 /134 lost = 6.284401 ppl = 536.143
    Valid 4864 samples after epoch: 0038 lost = 6.602970 ppl = 737.282
    Epoch: 0039 Batch: 50 /134 lost = 6.299078 ppl = 544.07
    Epoch: 0039 Batch: 100 /134 lost = 6.280575 ppl = 534.096
    Valid 4864 samples after epoch: 0039 lost = 6.603382 ppl = 737.585
    Epoch: 0040 Batch: 50 /134 lost = 6.295904 ppl = 542.346
    Epoch: 0040 Batch: 100 /134 lost = 6.275306 ppl = 531.289
    Valid 4864 samples after epoch: 0040 lost = 6.602332 ppl = 736.811
    ------Saving best model------
    Epoch: 0041 Batch: 50 /134 lost = 6.291101 ppl = 539.748
    Epoch: 0041 Batch: 100 /134 lost = 6.268178 ppl = 527.515
    Valid 4864 samples after epoch: 0041 lost = 6.602831 ppl = 737.179
    Epoch: 0042 Batch: 50 /134 lost = 6.287640 ppl = 537.882
    Epoch: 0042 Batch: 100 /134 lost = 6.263552 ppl = 525.081
    Valid 4864 samples after epoch: 0042 lost = 6.603520 ppl = 737.687
    Epoch: 0043 Batch: 50 /134 lost = 6.283894 ppl = 535.871
    Epoch: 0043 Batch: 100 /134 lost = 6.259047 ppl = 522.72
    Valid 4864 samples after epoch: 0043 lost = 6.604218 ppl = 738.202
    Epoch: 0044 Batch: 50 /134 lost = 6.279668 ppl = 533.612
    Epoch: 0044 Batch: 100 /134 lost = 6.254131 ppl = 520.157
    Valid 4864 samples after epoch: 0044 lost = 6.605199 ppl = 738.927
    Epoch: 0045 Batch: 50 /134 lost = 6.276248 ppl = 531.79
    Epoch: 0045 Batch: 100 /134 lost = 6.249437 ppl = 517.721
    Valid 4864 samples after epoch: 0045 lost = 6.606160 ppl = 739.637
    Epoch: 0046 Batch: 50 /134 lost = 6.273233 ppl = 530.189
    Epoch: 0046 Batch: 100 /134 lost = 6.245829 ppl = 515.857
    Valid 4864 samples after epoch: 0046 lost = 6.607214 ppl = 740.417
    Epoch: 0047 Batch: 50 /134 lost = 6.269819 ppl = 528.382
    Epoch: 0047 Batch: 100 /134 lost = 6.242171 ppl = 513.973
    Valid 4864 samples after epoch: 0047 lost = 6.608498 ppl = 741.369
    Epoch: 0048 Batch: 50 /134 lost = 6.266502 ppl = 526.632
    Epoch: 0048 Batch: 100 /134 lost = 6.237950 ppl = 511.808
    Valid 4864 samples after epoch: 0048 lost = 6.609767 ppl = 742.31
    Epoch: 0049 Batch: 50 /134 lost = 6.263639 ppl = 525.127
    Epoch: 0049 Batch: 100 /134 lost = 6.234691 ppl = 510.143
    Valid 4864 samples after epoch: 0049 lost = 6.610729 ppl = 743.025
    Epoch: 0050 Batch: 50 /134 lost = 6.261181 ppl = 523.837
    Epoch: 0050 Batch: 100 /134 lost = 6.231692 ppl = 508.615
    Valid 4864 samples after epoch: 0050 lost = 6.611641 ppl = 743.703
    Epoch: 0051 Batch: 50 /134 lost = 6.258203 ppl = 522.28
    Epoch: 0051 Batch: 100 /134 lost = 6.228672 ppl = 507.081
    Valid 4864 samples after epoch: 0051 lost = 6.612837 ppl = 744.592
    Epoch: 0052 Batch: 50 /134 lost = 6.255457 ppl = 520.847
    Epoch: 0052 Batch: 100 /134 lost = 6.225865 ppl = 505.66
    Valid 4864 samples after epoch: 0052 lost = 6.614236 ppl = 745.635
    Epoch: 0053 Batch: 50 /134 lost = 6.252882 ppl = 519.508
    Epoch: 0053 Batch: 100 /134 lost = 6.223119 ppl = 504.274
    Valid 4864 samples after epoch: 0053 lost = 6.615775 ppl = 746.783
    Epoch: 0054 Batch: 50 /134 lost = 6.249893 ppl = 517.957
    Epoch: 0054 Batch: 100 /134 lost = 6.220511 ppl = 502.96
    Valid 4864 samples after epoch: 0054 lost = 6.617161 ppl = 747.819
    Epoch: 0055 Batch: 50 /134 lost = 6.246551 ppl = 516.229
    Epoch: 0055 Batch: 100 /134 lost = 6.217864 ppl = 501.631
    Valid 4864 samples after epoch: 0055 lost = 6.618996 ppl = 749.192
    Epoch: 0056 Batch: 50 /134 lost = 6.243854 ppl = 514.839
    Epoch: 0056 Batch: 100 /134 lost = 6.215404 ppl = 500.398
    Valid 4864 samples after epoch: 0056 lost = 6.620777 ppl = 750.528
    Epoch: 0057 Batch: 50 /134 lost = 6.241431 ppl = 513.593
    Epoch: 0057 Batch: 100 /134 lost = 6.212792 ppl = 499.093
    Valid 4864 samples after epoch: 0057 lost = 6.622477 ppl = 751.805
    Epoch: 0058 Batch: 50 /134 lost = 6.239100 ppl = 512.397
    Epoch: 0058 Batch: 100 /134 lost = 6.209868 ppl = 497.636
    Valid 4864 samples after epoch: 0058 lost = 6.624065 ppl = 753.0
    Epoch: 0059 Batch: 50 /134 lost = 6.237016 ppl = 511.33
    Epoch: 0059 Batch: 100 /134 lost = 6.206861 ppl = 496.142
    Valid 4864 samples after epoch: 0059 lost = 6.625844 ppl = 754.341
    Epoch: 0060 Batch: 50 /134 lost = 6.235084 ppl = 510.343
    Epoch: 0060 Batch: 100 /134 lost = 6.204520 ppl = 494.981
    Valid 4864 samples after epoch: 0060 lost = 6.627642 ppl = 755.698
    Epoch: 0061 Batch: 50 /134 lost = 6.233086 ppl = 509.325
    Epoch: 0061 Batch: 100 /134 lost = 6.202109 ppl = 493.79
    Valid 4864 samples after epoch: 0061 lost = 6.629376 ppl = 757.009
    Epoch: 0062 Batch: 50 /134 lost = 6.231078 ppl = 508.303
    Epoch: 0062 Batch: 100 /134 lost = 6.200109 ppl = 492.803
    Valid 4864 samples after epoch: 0062 lost = 6.630896 ppl = 758.161
    Epoch: 0063 Batch: 50 /134 lost = 6.228917 ppl = 507.206
    Epoch: 0063 Batch: 100 /134 lost = 6.196557 ppl = 491.055
    Valid 4864 samples after epoch: 0063 lost = 6.631911 ppl = 758.931
    Epoch: 0064 Batch: 50 /134 lost = 6.224981 ppl = 505.214
    Epoch: 0064 Batch: 100 /134 lost = 6.194089 ppl = 489.845
    Valid 4864 samples after epoch: 0064 lost = 6.633595 ppl = 760.21
    Epoch: 0065 Batch: 50 /134 lost = 6.222937 ppl = 504.182
    Epoch: 0065 Batch: 100 /134 lost = 6.191842 ppl = 488.745
    Valid 4864 samples after epoch: 0065 lost = 6.635431 ppl = 761.607
    Epoch: 0066 Batch: 50 /134 lost = 6.220832 ppl = 503.122
    Epoch: 0066 Batch: 100 /134 lost = 6.189699 ppl = 487.699
    Valid 4864 samples after epoch: 0066 lost = 6.637142 ppl = 762.911
    Epoch: 0067 Batch: 50 /134 lost = 6.219507 ppl = 502.456
    Epoch: 0067 Batch: 100 /134 lost = 6.187349 ppl = 486.554
    Valid 4864 samples after epoch: 0067 lost = 6.638933 ppl = 764.279
    Epoch: 0068 Batch: 50 /134 lost = 6.215214 ppl = 500.303
    Epoch: 0068 Batch: 100 /134 lost = 6.180236 ppl = 483.106
    Valid 4864 samples after epoch: 0068 lost = 6.639863 ppl = 764.99
    Epoch: 0069 Batch: 50 /134 lost = 6.213010 ppl = 499.202
    Epoch: 0069 Batch: 100 /134 lost = 6.177594 ppl = 481.831
    Valid 4864 samples after epoch: 0069 lost = 6.641377 ppl = 766.15
    Epoch: 0070 Batch: 50 /134 lost = 6.210564 ppl = 497.982
    Epoch: 0070 Batch: 100 /134 lost = 6.175228 ppl = 480.693
    Valid 4864 samples after epoch: 0070 lost = 6.642690 ppl = 767.156
    Epoch: 0071 Batch: 50 /134 lost = 6.208648 ppl = 497.029
    Epoch: 0071 Batch: 100 /134 lost = 6.173010 ppl = 479.628
    Valid 4864 samples after epoch: 0071 lost = 6.644557 ppl = 768.589
    Epoch: 0072 Batch: 50 /134 lost = 6.206798 ppl = 496.11
    Epoch: 0072 Batch: 100 /134 lost = 6.170365 ppl = 478.361
    Valid 4864 samples after epoch: 0072 lost = 6.646478 ppl = 770.068
    Epoch: 0073 Batch: 50 /134 lost = 6.205077 ppl = 495.257
    Epoch: 0073 Batch: 100 /134 lost = 6.168335 ppl = 477.391
    Valid 4864 samples after epoch: 0073 lost = 6.648298 ppl = 771.47
    Epoch: 0074 Batch: 50 /134 lost = 6.203434 ppl = 494.444
    Epoch: 0074 Batch: 100 /134 lost = 6.166340 ppl = 476.439
    Valid 4864 samples after epoch: 0074 lost = 6.650171 ppl = 772.916
    Epoch: 0075 Batch: 50 /134 lost = 6.201930 ppl = 493.701
    Epoch: 0075 Batch: 100 /134 lost = 6.164289 ppl = 475.463
    Valid 4864 samples after epoch: 0075 lost = 6.652172 ppl = 774.465
    Epoch: 0076 Batch: 50 /134 lost = 6.200503 ppl = 492.997
    Epoch: 0076 Batch: 100 /134 lost = 6.162388 ppl = 474.56
    Valid 4864 samples after epoch: 0076 lost = 6.654030 ppl = 775.905
    Epoch: 0077 Batch: 50 /134 lost = 6.199046 ppl = 492.279
    Epoch: 0077 Batch: 100 /134 lost = 6.159256 ppl = 473.076
    Valid 4864 samples after epoch: 0077 lost = 6.656011 ppl = 777.443
    Epoch: 0078 Batch: 50 /134 lost = 6.197670 ppl = 491.602
    Epoch: 0078 Batch: 100 /134 lost = 6.157444 ppl = 472.22
    Valid 4864 samples after epoch: 0078 lost = 6.658026 ppl = 779.011
    Epoch: 0079 Batch: 50 /134 lost = 6.196353 ppl = 490.955
    Epoch: 0079 Batch: 100 /134 lost = 6.155732 ppl = 471.412
    Valid 4864 samples after epoch: 0079 lost = 6.660197 ppl = 780.705
    Epoch: 0080 Batch: 50 /134 lost = 6.195074 ppl = 490.328
    Epoch: 0080 Batch: 100 /134 lost = 6.154004 ppl = 470.598
    Valid 4864 samples after epoch: 0080 lost = 6.662220 ppl = 782.286
    Epoch: 0081 Batch: 50 /134 lost = 6.193828 ppl = 489.717
    Epoch: 0081 Batch: 100 /134 lost = 6.152085 ppl = 469.696
    Valid 4864 samples after epoch: 0081 lost = 6.664262 ppl = 783.884
    Epoch: 0082 Batch: 50 /134 lost = 6.192601 ppl = 489.117
    Epoch: 0082 Batch: 100 /134 lost = 6.149897 ppl = 468.669
    Valid 4864 samples after epoch: 0082 lost = 6.666315 ppl = 785.496
    Epoch: 0083 Batch: 50 /134 lost = 6.191308 ppl = 488.484
    Epoch: 0083 Batch: 100 /134 lost = 6.148003 ppl = 467.782
    Valid 4864 samples after epoch: 0083 lost = 6.668543 ppl = 787.248
    Epoch: 0084 Batch: 50 /134 lost = 6.189948 ppl = 487.821
    Epoch: 0084 Batch: 100 /134 lost = 6.146228 ppl = 466.953
    Valid 4864 samples after epoch: 0084 lost = 6.670806 ppl = 789.032
    Epoch: 0085 Batch: 50 /134 lost = 6.188581 ppl = 487.154
    Epoch: 0085 Batch: 100 /134 lost = 6.144484 ppl = 466.139
    Valid 4864 samples after epoch: 0085 lost = 6.673070 ppl = 790.82
    Epoch: 0086 Batch: 50 /134 lost = 6.186550 ppl = 486.166
    Epoch: 0086 Batch: 100 /134 lost = 6.141627 ppl = 464.809
    Valid 4864 samples after epoch: 0086 lost = 6.674832 ppl = 792.214
    Epoch: 0087 Batch: 50 /134 lost = 6.185147 ppl = 485.484
    Epoch: 0087 Batch: 100 /134 lost = 6.139969 ppl = 464.039
    Valid 4864 samples after epoch: 0087 lost = 6.676955 ppl = 793.898
    Epoch: 0088 Batch: 50 /134 lost = 6.183615 ppl = 484.741
    Epoch: 0088 Batch: 100 /134 lost = 6.138010 ppl = 463.131
    Valid 4864 samples after epoch: 0088 lost = 6.679155 ppl = 795.646
    Epoch: 0089 Batch: 50 /134 lost = 6.182101 ppl = 484.008
    Epoch: 0089 Batch: 100 /134 lost = 6.136256 ppl = 462.32
    Valid 4864 samples after epoch: 0089 lost = 6.681323 ppl = 797.374
    Epoch: 0090 Batch: 50 /134 lost = 6.180584 ppl = 483.274
    Epoch: 0090 Batch: 100 /134 lost = 6.134641 ppl = 461.573
    Valid 4864 samples after epoch: 0090 lost = 6.683342 ppl = 798.985
    Epoch: 0091 Batch: 50 /134 lost = 6.179121 ppl = 482.567
    Epoch: 0091 Batch: 100 /134 lost = 6.133139 ppl = 460.881
    Valid 4864 samples after epoch: 0091 lost = 6.685227 ppl = 800.492
    Epoch: 0092 Batch: 50 /134 lost = 6.177077 ppl = 481.582
    Epoch: 0092 Batch: 100 /134 lost = 6.131440 ppl = 460.098
    Valid 4864 samples after epoch: 0092 lost = 6.687078 ppl = 801.975
    Epoch: 0093 Batch: 50 /134 lost = 6.175473 ppl = 480.81
    Epoch: 0093 Batch: 100 /134 lost = 6.129857 ppl = 459.37
    Valid 4864 samples after epoch: 0093 lost = 6.689275 ppl = 803.739
    Epoch: 0094 Batch: 50 /134 lost = 6.174215 ppl = 480.206
    Epoch: 0094 Batch: 100 /134 lost = 6.128395 ppl = 458.699
    Valid 4864 samples after epoch: 0094 lost = 6.691433 ppl = 805.475
    Epoch: 0095 Batch: 50 /134 lost = 6.172757 ppl = 479.506
    Epoch: 0095 Batch: 100 /134 lost = 6.127058 ppl = 458.086
    Valid 4864 samples after epoch: 0095 lost = 6.693550 ppl = 807.183
    Epoch: 0096 Batch: 50 /134 lost = 6.171349 ppl = 478.832
    Epoch: 0096 Batch: 100 /134 lost = 6.125761 ppl = 457.493
    Valid 4864 samples after epoch: 0096 lost = 6.695779 ppl = 808.984
    Epoch: 0097 Batch: 50 /134 lost = 6.170044 ppl = 478.207
    Epoch: 0097 Batch: 100 /134 lost = 6.123951 ppl = 456.665
    Valid 4864 samples after epoch: 0097 lost = 6.696837 ppl = 809.841
    Epoch: 0098 Batch: 50 /134 lost = 6.168654 ppl = 477.543
    Epoch: 0098 Batch: 100 /134 lost = 6.122704 ppl = 456.096
    Valid 4864 samples after epoch: 0098 lost = 6.698930 ppl = 811.537
    Epoch: 0099 Batch: 50 /134 lost = 6.167839 ppl = 477.154
    Epoch: 0099 Batch: 100 /134 lost = 6.121514 ppl = 455.554
    Valid 4864 samples after epoch: 0099 lost = 6.701092 ppl = 813.293
    Epoch: 0100 Batch: 50 /134 lost = 6.166907 ppl = 476.709
    Epoch: 0100 Batch: 100 /134 lost = 6.120335 ppl = 455.017
    Valid 4864 samples after epoch: 0100 lost = 6.703119 ppl = 814.943
    Epoch: 0101 Batch: 50 /134 lost = 6.165794 ppl = 476.179
    Epoch: 0101 Batch: 100 /134 lost = 6.119123 ppl = 454.466
    Valid 4864 samples after epoch: 0101 lost = 6.705317 ppl = 816.737
    Epoch: 0102 Batch: 50 /134 lost = 6.164573 ppl = 475.598
    Epoch: 0102 Batch: 100 /134 lost = 6.117897 ppl = 453.909
    Valid 4864 samples after epoch: 0102 lost = 6.707452 ppl = 818.482
    Epoch: 0103 Batch: 50 /134 lost = 6.163272 ppl = 474.98
    Epoch: 0103 Batch: 100 /134 lost = 6.116711 ppl = 453.371
    Valid 4864 samples after epoch: 0103 lost = 6.709615 ppl = 820.255
    Epoch: 0104 Batch: 50 /134 lost = 6.161908 ppl = 474.332
    Epoch: 0104 Batch: 100 /134 lost = 6.115515 ppl = 452.829
    Valid 4864 samples after epoch: 0104 lost = 6.711547 ppl = 821.841
    Epoch: 0105 Batch: 50 /134 lost = 6.160798 ppl = 473.806
    Epoch: 0105 Batch: 100 /134 lost = 6.114199 ppl = 452.234
    Valid 4864 samples after epoch: 0105 lost = 6.713762 ppl = 823.664
    Epoch: 0106 Batch: 50 /134 lost = 6.159872 ppl = 473.368
    Epoch: 0106 Batch: 100 /134 lost = 6.112658 ppl = 451.537
    Valid 4864 samples after epoch: 0106 lost = 6.715671 ppl = 825.237
    Epoch: 0107 Batch: 50 /134 lost = 6.158836 ppl = 472.877
    Epoch: 0107 Batch: 100 /134 lost = 6.111190 ppl = 450.875
    Valid 4864 samples after epoch: 0107 lost = 6.717942 ppl = 827.114
    Epoch: 0108 Batch: 50 /134 lost = 6.157865 ppl = 472.418
    Epoch: 0108 Batch: 100 /134 lost = 6.109737 ppl = 450.22
    Valid 4864 samples after epoch: 0108 lost = 6.719879 ppl = 828.717
    Epoch: 0109 Batch: 50 /134 lost = 6.156963 ppl = 471.992
    Epoch: 0109 Batch: 100 /134 lost = 6.108204 ppl = 449.531
    Valid 4864 samples after epoch: 0109 lost = 6.722072 ppl = 830.537
    Epoch: 0110 Batch: 50 /134 lost = 6.155983 ppl = 471.53
    Epoch: 0110 Batch: 100 /134 lost = 6.106862 ppl = 448.928
    Valid 4864 samples after epoch: 0110 lost = 6.724193 ppl = 832.3
    Epoch: 0111 Batch: 50 /134 lost = 6.154934 ppl = 471.036
    Epoch: 0111 Batch: 100 /134 lost = 6.105689 ppl = 448.402
    Valid 4864 samples after epoch: 0111 lost = 6.726438 ppl = 834.171
    Epoch: 0112 Batch: 50 /134 lost = 6.153860 ppl = 470.53
    Epoch: 0112 Batch: 100 /134 lost = 6.104660 ppl = 447.94
    Valid 4864 samples after epoch: 0112 lost = 6.728500 ppl = 835.893
    Epoch: 0113 Batch: 50 /134 lost = 6.152950 ppl = 470.102
    Epoch: 0113 Batch: 100 /134 lost = 6.104013 ppl = 447.651
    Valid 4864 samples after epoch: 0113 lost = 6.730675 ppl = 837.713
    Epoch: 0114 Batch: 50 /134 lost = 6.151970 ppl = 469.642
    Epoch: 0114 Batch: 100 /134 lost = 6.103673 ppl = 447.498
    Valid 4864 samples after epoch: 0114 lost = 6.732807 ppl = 839.501
    Epoch: 0115 Batch: 50 /134 lost = 6.151080 ppl = 469.224
    Epoch: 0115 Batch: 100 /134 lost = 6.102942 ppl = 447.171
    Valid 4864 samples after epoch: 0115 lost = 6.734745 ppl = 841.129
    Epoch: 0116 Batch: 50 /134 lost = 6.150174 ppl = 468.799
    Epoch: 0116 Batch: 100 /134 lost = 6.102092 ppl = 446.791
    Valid 4864 samples after epoch: 0116 lost = 6.736802 ppl = 842.861
    Epoch: 0117 Batch: 50 /134 lost = 6.149359 ppl = 468.417
    Epoch: 0117 Batch: 100 /134 lost = 6.101163 ppl = 446.377
    Valid 4864 samples after epoch: 0117 lost = 6.738768 ppl = 844.52
    Epoch: 0118 Batch: 50 /134 lost = 6.148458 ppl = 467.995
    Epoch: 0118 Batch: 100 /134 lost = 6.100163 ppl = 445.93
    Valid 4864 samples after epoch: 0118 lost = 6.740652 ppl = 846.113
    Epoch: 0119 Batch: 50 /134 lost = 6.147577 ppl = 467.583
    Epoch: 0119 Batch: 100 /134 lost = 6.099094 ppl = 445.454
    Valid 4864 samples after epoch: 0119 lost = 6.742576 ppl = 847.741
    Epoch: 0120 Batch: 50 /134 lost = 6.146640 ppl = 467.145
    Epoch: 0120 Batch: 100 /134 lost = 6.098044 ppl = 444.987
    Valid 4864 samples after epoch: 0120 lost = 6.744502 ppl = 849.376
    Epoch: 0121 Batch: 50 /134 lost = 6.145795 ppl = 466.751
    Epoch: 0121 Batch: 100 /134 lost = 6.096944 ppl = 444.497
    Valid 4864 samples after epoch: 0121 lost = 6.746457 ppl = 851.038
    Epoch: 0122 Batch: 50 /134 lost = 6.144888 ppl = 466.327
    Epoch: 0122 Batch: 100 /134 lost = 6.095633 ppl = 443.915
    Valid 4864 samples after epoch: 0122 lost = 6.748232 ppl = 852.55
    Epoch: 0123 Batch: 50 /134 lost = 6.144047 ppl = 465.935
    Epoch: 0123 Batch: 100 /134 lost = 6.094085 ppl = 443.228
    Valid 4864 samples after epoch: 0123 lost = 6.750086 ppl = 854.132
    Epoch: 0124 Batch: 50 /134 lost = 6.143072 ppl = 465.481
    Epoch: 0124 Batch: 100 /134 lost = 6.092520 ppl = 442.535
    Valid 4864 samples after epoch: 0124 lost = 6.751968 ppl = 855.741
    Epoch: 0125 Batch: 50 /134 lost = 6.142087 ppl = 465.023
    Epoch: 0125 Batch: 100 /134 lost = 6.091220 ppl = 441.96
    Valid 4864 samples after epoch: 0125 lost = 6.753896 ppl = 857.392
    Epoch: 0126 Batch: 50 /134 lost = 6.141084 ppl = 464.557
    Epoch: 0126 Batch: 100 /134 lost = 6.090066 ppl = 441.451
    Valid 4864 samples after epoch: 0126 lost = 6.755779 ppl = 859.009
    Epoch: 0127 Batch: 50 /134 lost = 6.140055 ppl = 464.079
    Epoch: 0127 Batch: 100 /134 lost = 6.088911 ppl = 440.941
    Valid 4864 samples after epoch: 0127 lost = 6.757353 ppl = 860.362
    Epoch: 0128 Batch: 50 /134 lost = 6.139034 ppl = 463.605
    Epoch: 0128 Batch: 100 /134 lost = 6.087771 ppl = 440.439
    Valid 4864 samples after epoch: 0128 lost = 6.758874 ppl = 861.671
    Epoch: 0129 Batch: 50 /134 lost = 6.138130 ppl = 463.186
    Epoch: 0129 Batch: 100 /134 lost = 6.086574 ppl = 439.912
    Valid 4864 samples after epoch: 0129 lost = 6.760569 ppl = 863.134
    Epoch: 0130 Batch: 50 /134 lost = 6.137187 ppl = 462.75
    Epoch: 0130 Batch: 100 /134 lost = 6.085408 ppl = 439.399
    Valid 4864 samples after epoch: 0130 lost = 6.762198 ppl = 864.54
    Epoch: 0131 Batch: 50 /134 lost = 6.136302 ppl = 462.341
    Epoch: 0131 Batch: 100 /134 lost = 6.084304 ppl = 438.914
    Valid 4864 samples after epoch: 0131 lost = 6.763877 ppl = 865.993
    Epoch: 0132 Batch: 50 /134 lost = 6.135410 ppl = 461.929
    Epoch: 0132 Batch: 100 /134 lost = 6.083161 ppl = 438.413
    Valid 4864 samples after epoch: 0132 lost = 6.765559 ppl = 867.451
    Epoch: 0133 Batch: 50 /134 lost = 6.134586 ppl = 461.548
    Epoch: 0133 Batch: 100 /134 lost = 6.082163 ppl = 437.975
    Valid 4864 samples after epoch: 0133 lost = 6.767110 ppl = 868.798
    Epoch: 0134 Batch: 50 /134 lost = 6.133758 ppl = 461.166
    Epoch: 0134 Batch: 100 /134 lost = 6.081192 ppl = 437.55
    Valid 4864 samples after epoch: 0134 lost = 6.768852 ppl = 870.312
    Epoch: 0135 Batch: 50 /134 lost = 6.132932 ppl = 460.785
    Epoch: 0135 Batch: 100 /134 lost = 6.080206 ppl = 437.119
    Valid 4864 samples after epoch: 0135 lost = 6.770457 ppl = 871.71
    Epoch: 0136 Batch: 50 /134 lost = 6.132073 ppl = 460.39
    Epoch: 0136 Batch: 100 /134 lost = 6.079185 ppl = 436.673
    Valid 4864 samples after epoch: 0136 lost = 6.771960 ppl = 873.021
    Epoch: 0137 Batch: 50 /134 lost = 6.131234 ppl = 460.004
    Epoch: 0137 Batch: 100 /134 lost = 6.078120 ppl = 436.208
    Valid 4864 samples after epoch: 0137 lost = 6.773294 ppl = 874.187
    Epoch: 0138 Batch: 50 /134 lost = 6.130380 ppl = 459.611
    Epoch: 0138 Batch: 100 /134 lost = 6.077005 ppl = 435.722
    Valid 4864 samples after epoch: 0138 lost = 6.774832 ppl = 875.532
    Epoch: 0139 Batch: 50 /134 lost = 6.129553 ppl = 459.231
    Epoch: 0139 Batch: 100 /134 lost = 6.075888 ppl = 435.236
    Valid 4864 samples after epoch: 0139 lost = 6.776409 ppl = 876.914
    Epoch: 0140 Batch: 50 /134 lost = 6.128706 ppl = 458.842
    Epoch: 0140 Batch: 100 /134 lost = 6.074851 ppl = 434.785
    Valid 4864 samples after epoch: 0140 lost = 6.777811 ppl = 878.145
    Epoch: 0141 Batch: 50 /134 lost = 6.127880 ppl = 458.463
    Epoch: 0141 Batch: 100 /134 lost = 6.073908 ppl = 434.375
    Valid 4864 samples after epoch: 0141 lost = 6.779105 ppl = 879.281
    Epoch: 0142 Batch: 50 /134 lost = 6.127045 ppl = 458.08
    Epoch: 0142 Batch: 100 /134 lost = 6.073104 ppl = 434.026
    Valid 4864 samples after epoch: 0142 lost = 6.780582 ppl = 880.581
    Epoch: 0143 Batch: 50 /134 lost = 6.126220 ppl = 457.703
    Epoch: 0143 Batch: 100 /134 lost = 6.072370 ppl = 433.707
    Valid 4864 samples after epoch: 0143 lost = 6.781838 ppl = 881.688
    Epoch: 0144 Batch: 50 /134 lost = 6.125389 ppl = 457.322
    Epoch: 0144 Batch: 100 /134 lost = 6.071713 ppl = 433.423
    Valid 4864 samples after epoch: 0144 lost = 6.783159 ppl = 882.853
    Epoch: 0145 Batch: 50 /134 lost = 6.124580 ppl = 456.953
    Epoch: 0145 Batch: 100 /134 lost = 6.071105 ppl = 433.159
    Valid 4864 samples after epoch: 0145 lost = 6.784198 ppl = 883.771
    Epoch: 0146 Batch: 50 /134 lost = 6.123587 ppl = 456.499
    Epoch: 0146 Batch: 100 /134 lost = 6.070544 ppl = 432.916
    Valid 4864 samples after epoch: 0146 lost = 6.785429 ppl = 884.86
    Epoch: 0147 Batch: 50 /134 lost = 6.122442 ppl = 455.977
    Epoch: 0147 Batch: 100 /134 lost = 6.069912 ppl = 432.643
    Valid 4864 samples after epoch: 0147 lost = 6.786400 ppl = 885.719
    Epoch: 0148 Batch: 50 /134 lost = 6.121116 ppl = 455.373
    Epoch: 0148 Batch: 100 /134 lost = 6.069275 ppl = 432.367
    Valid 4864 samples after epoch: 0148 lost = 6.787613 ppl = 886.794
    Epoch: 0149 Batch: 50 /134 lost = 6.120037 ppl = 454.881
    Epoch: 0149 Batch: 100 /134 lost = 6.068174 ppl = 431.891
    Valid 4864 samples after epoch: 0149 lost = 6.788217 ppl = 887.33
    Epoch: 0150 Batch: 50 /134 lost = 6.117539 ppl = 453.747
    Epoch: 0150 Batch: 100 /134 lost = 6.066973 ppl = 431.373
    Valid 4864 samples after epoch: 0150 lost = 6.789212 ppl = 888.214
    
    Test the RNNLM……………………
    Test 5760 samples with models/3_layers_rnnlm_model_best.ckpt……………………
    lost = 6.537720 ppl = 690.71
    
