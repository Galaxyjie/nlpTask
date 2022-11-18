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
    Epoch: 0001 Batch: 50 /134 lost = 8.807278 ppl = 6682.7
    Epoch: 0001 Batch: 100 /134 lost = 8.683818 ppl = 5906.55
    Valid 4864 samples after epoch: 0001 lost = 8.596660 ppl = 5413.55
    Epoch: 0002 Batch: 50 /134 lost = 8.462983 ppl = 4736.17
    Epoch: 0002 Batch: 100 /134 lost = 8.355309 ppl = 4252.7
    Valid 4864 samples after epoch: 0002 lost = 8.286668 ppl = 3970.58
    Epoch: 0003 Batch: 50 /134 lost = 8.139415 ppl = 3426.91
    Epoch: 0003 Batch: 100 /134 lost = 8.038169 ppl = 3096.94
    Valid 4864 samples after epoch: 0003 lost = 7.988398 ppl = 2946.57
    Epoch: 0004 Batch: 50 /134 lost = 7.831702 ppl = 2519.21
    Epoch: 0004 Batch: 100 /134 lost = 7.743670 ppl = 2306.92
    Valid 4864 samples after epoch: 0004 lost = 7.716271 ppl = 2244.57
    Epoch: 0005 Batch: 50 /134 lost = 7.555758 ppl = 1911.72
    Epoch: 0005 Batch: 100 /134 lost = 7.481473 ppl = 1774.85
    Valid 4864 samples after epoch: 0005 lost = 7.478184 ppl = 1769.03
    Epoch: 0006 Batch: 50 /134 lost = 7.314807 ppl = 1502.38
    Epoch: 0006 Batch: 100 /134 lost = 7.251961 ppl = 1410.87
    Valid 4864 samples after epoch: 0006 lost = 7.273557 ppl = 1441.67
    Epoch: 0007 Batch: 50 /134 lost = 7.107678 ppl = 1221.31
    Epoch: 0007 Batch: 100 /134 lost = 7.055152 ppl = 1158.81
    Valid 4864 samples after epoch: 0007 lost = 7.102246 ppl = 1214.69
    Epoch: 0008 Batch: 50 /134 lost = 6.934387 ppl = 1026.99
    Epoch: 0008 Batch: 100 /134 lost = 6.891031 ppl = 983.415
    Valid 4864 samples after epoch: 0008 lost = 6.963282 ppl = 1057.1
    Epoch: 0009 Batch: 50 /134 lost = 6.793722 ppl = 892.228
    Epoch: 0009 Batch: 100 /134 lost = 6.758246 ppl = 861.13
    Valid 4864 samples after epoch: 0009 lost = 6.854609 ppl = 948.241
    Epoch: 0010 Batch: 50 /134 lost = 6.683599 ppl = 799.19
    Epoch: 0010 Batch: 100 /134 lost = 6.654685 ppl = 776.414
    Valid 4864 samples after epoch: 0010 lost = 6.773387 ppl = 874.268
    Epoch: 0011 Batch: 50 /134 lost = 6.600924 ppl = 735.775
    Epoch: 0011 Batch: 100 /134 lost = 6.577197 ppl = 718.523
    Valid 4864 samples after epoch: 0011 lost = 6.715829 ppl = 825.368
    Epoch: 0012 Batch: 50 /134 lost = 6.541504 ppl = 693.329
    Epoch: 0012 Batch: 100 /134 lost = 6.521617 ppl = 679.677
    Valid 4864 samples after epoch: 0012 lost = 6.677299 ppl = 794.171
    Epoch: 0013 Batch: 50 /134 lost = 6.500372 ppl = 665.389
    Epoch: 0013 Batch: 100 /134 lost = 6.483135 ppl = 654.018
    Valid 4864 samples after epoch: 0013 lost = 6.652841 ppl = 774.983
    Epoch: 0014 Batch: 50 /134 lost = 6.472573 ppl = 647.147
    Epoch: 0014 Batch: 100 /134 lost = 6.456931 ppl = 637.103
    Valid 4864 samples after epoch: 0014 lost = 6.637857 ppl = 763.457
    Epoch: 0015 Batch: 50 /134 lost = 6.453727 ppl = 635.065
    Epoch: 0015 Batch: 100 /134 lost = 6.438558 ppl = 625.504
    Valid 4864 samples after epoch: 0015 lost = 6.628446 ppl = 756.306
    Epoch: 0016 Batch: 50 /134 lost = 6.439854 ppl = 626.315
    Epoch: 0016 Batch: 100 /134 lost = 6.424559 ppl = 616.809
    Valid 4864 samples after epoch: 0016 lost = 6.622099 ppl = 751.521
    Epoch: 0017 Batch: 50 /134 lost = 6.429525 ppl = 619.88
    Epoch: 0017 Batch: 100 /134 lost = 6.413492 ppl = 610.02
    Valid 4864 samples after epoch: 0017 lost = 6.617244 ppl = 747.881
    Epoch: 0018 Batch: 50 /134 lost = 6.421385 ppl = 614.854
    Epoch: 0018 Batch: 100 /134 lost = 6.404711 ppl = 604.687
    Valid 4864 samples after epoch: 0018 lost = 6.613537 ppl = 745.114
    Epoch: 0019 Batch: 50 /134 lost = 6.414592 ppl = 610.692
    Epoch: 0019 Batch: 100 /134 lost = 6.397537 ppl = 600.365
    Valid 4864 samples after epoch: 0019 lost = 6.611062 ppl = 743.272
    Epoch: 0020 Batch: 50 /134 lost = 6.408766 ppl = 607.144
    Epoch: 0020 Batch: 100 /134 lost = 6.391253 ppl = 596.604
    Valid 4864 samples after epoch: 0020 lost = 6.609340 ppl = 741.993
    Epoch: 0021 Batch: 50 /134 lost = 6.403521 ppl = 603.968
    Epoch: 0021 Batch: 100 /134 lost = 6.385586 ppl = 593.232
    Valid 4864 samples after epoch: 0021 lost = 6.608084 ppl = 741.062
    Epoch: 0022 Batch: 50 /134 lost = 6.398663 ppl = 601.041
    Epoch: 0022 Batch: 100 /134 lost = 6.380411 ppl = 590.17
    Valid 4864 samples after epoch: 0022 lost = 6.607168 ppl = 740.383
    Epoch: 0023 Batch: 50 /134 lost = 6.394135 ppl = 598.326
    Epoch: 0023 Batch: 100 /134 lost = 6.375660 ppl = 587.373
    Valid 4864 samples after epoch: 0023 lost = 6.606492 ppl = 739.883
    Epoch: 0024 Batch: 50 /134 lost = 6.389815 ppl = 595.746
    Epoch: 0024 Batch: 100 /134 lost = 6.371219 ppl = 584.77
    Valid 4864 samples after epoch: 0024 lost = 6.605948 ppl = 739.48
    Epoch: 0025 Batch: 50 /134 lost = 6.385619 ppl = 593.252
    Epoch: 0025 Batch: 100 /134 lost = 6.366987 ppl = 582.301
    Valid 4864 samples after epoch: 0025 lost = 6.605507 ppl = 739.154
    Epoch: 0026 Batch: 50 /134 lost = 6.381588 ppl = 590.865
    Epoch: 0026 Batch: 100 /134 lost = 6.362802 ppl = 579.869
    Valid 4864 samples after epoch: 0026 lost = 6.605077 ppl = 738.837
    Epoch: 0027 Batch: 50 /134 lost = 6.377623 ppl = 588.527
    Epoch: 0027 Batch: 100 /134 lost = 6.358510 ppl = 577.385
    Valid 4864 samples after epoch: 0027 lost = 6.604561 ppl = 738.456
    Epoch: 0028 Batch: 50 /134 lost = 6.373627 ppl = 586.18
    Epoch: 0028 Batch: 100 /134 lost = 6.354109 ppl = 574.85
    Valid 4864 samples after epoch: 0028 lost = 6.604016 ppl = 738.053
    Epoch: 0029 Batch: 50 /134 lost = 6.369506 ppl = 583.77
    Epoch: 0029 Batch: 100 /134 lost = 6.349642 ppl = 572.288
    Valid 4864 samples after epoch: 0029 lost = 6.603503 ppl = 737.675
    Epoch: 0030 Batch: 50 /134 lost = 6.365220 ppl = 581.272
    Epoch: 0030 Batch: 100 /134 lost = 6.345057 ppl = 569.67
    Valid 4864 samples after epoch: 0030 lost = 6.603028 ppl = 737.325
    Epoch: 0031 Batch: 50 /134 lost = 6.360832 ppl = 578.728
    Epoch: 0031 Batch: 100 /134 lost = 6.340436 ppl = 567.043
    Valid 4864 samples after epoch: 0031 lost = 6.602593 ppl = 737.004
    Epoch: 0032 Batch: 50 /134 lost = 6.356513 ppl = 576.233
    Epoch: 0032 Batch: 100 /134 lost = 6.335926 ppl = 564.492
    Valid 4864 samples after epoch: 0032 lost = 6.602171 ppl = 736.693
    Epoch: 0033 Batch: 50 /134 lost = 6.352213 ppl = 573.761
    Epoch: 0033 Batch: 100 /134 lost = 6.331469 ppl = 561.981
    Valid 4864 samples after epoch: 0033 lost = 6.601727 ppl = 736.366
    Epoch: 0034 Batch: 50 /134 lost = 6.347884 ppl = 571.283
    Epoch: 0034 Batch: 100 /134 lost = 6.327021 ppl = 559.487
    Valid 4864 samples after epoch: 0034 lost = 6.601252 ppl = 736.016
    Epoch: 0035 Batch: 50 /134 lost = 6.343563 ppl = 568.819
    Epoch: 0035 Batch: 100 /134 lost = 6.322552 ppl = 556.993
    Valid 4864 samples after epoch: 0035 lost = 6.600749 ppl = 735.646
    Epoch: 0036 Batch: 50 /134 lost = 6.339280 ppl = 566.388
    Epoch: 0036 Batch: 100 /134 lost = 6.318052 ppl = 554.492
    Valid 4864 samples after epoch: 0036 lost = 6.600219 ppl = 735.256
    Epoch: 0037 Batch: 50 /134 lost = 6.335022 ppl = 563.982
    Epoch: 0037 Batch: 100 /134 lost = 6.313534 ppl = 551.992
    Valid 4864 samples after epoch: 0037 lost = 6.599702 ppl = 734.876
    Epoch: 0038 Batch: 50 /134 lost = 6.330768 ppl = 561.588
    Epoch: 0038 Batch: 100 /134 lost = 6.308993 ppl = 549.492
    Valid 4864 samples after epoch: 0038 lost = 6.599204 ppl = 734.51
    Epoch: 0039 Batch: 50 /134 lost = 6.326511 ppl = 559.202
    Epoch: 0039 Batch: 100 /134 lost = 6.304411 ppl = 546.979
    Valid 4864 samples after epoch: 0039 lost = 6.598713 ppl = 734.15
    Epoch: 0040 Batch: 50 /134 lost = 6.322257 ppl = 556.828
    Epoch: 0040 Batch: 100 /134 lost = 6.299774 ppl = 544.449
    Valid 4864 samples after epoch: 0040 lost = 6.598217 ppl = 733.786
    Epoch: 0041 Batch: 50 /134 lost = 6.317997 ppl = 554.461
    Epoch: 0041 Batch: 100 /134 lost = 6.295084 ppl = 541.901
    Valid 4864 samples after epoch: 0041 lost = 6.597711 ppl = 733.415
    Epoch: 0042 Batch: 50 /134 lost = 6.313723 ppl = 552.096
    Epoch: 0042 Batch: 100 /134 lost = 6.290337 ppl = 539.335
    Valid 4864 samples after epoch: 0042 lost = 6.597193 ppl = 733.035
    Epoch: 0043 Batch: 50 /134 lost = 6.309430 ppl = 549.732
    Epoch: 0043 Batch: 100 /134 lost = 6.285541 ppl = 536.755
    Valid 4864 samples after epoch: 0043 lost = 6.596664 ppl = 732.647
    Epoch: 0044 Batch: 50 /134 lost = 6.305125 ppl = 547.37
    Epoch: 0044 Batch: 100 /134 lost = 6.280696 ppl = 534.16
    Valid 4864 samples after epoch: 0044 lost = 6.596130 ppl = 732.256
    Epoch: 0045 Batch: 50 /134 lost = 6.300819 ppl = 545.018
    Epoch: 0045 Batch: 100 /134 lost = 6.275803 ppl = 531.553
    Valid 4864 samples after epoch: 0045 lost = 6.595595 ppl = 731.864
    Epoch: 0046 Batch: 50 /134 lost = 6.296518 ppl = 542.679
    Epoch: 0046 Batch: 100 /134 lost = 6.270862 ppl = 528.933
    Valid 4864 samples after epoch: 0046 lost = 6.595065 ppl = 731.476
    Epoch: 0047 Batch: 50 /134 lost = 6.292227 ppl = 540.355
    Epoch: 0047 Batch: 100 /134 lost = 6.265873 ppl = 526.301
    Valid 4864 samples after epoch: 0047 lost = 6.594538 ppl = 731.091
    Epoch: 0048 Batch: 50 /134 lost = 6.287951 ppl = 538.049
    Epoch: 0048 Batch: 100 /134 lost = 6.260849 ppl = 523.663
    Valid 4864 samples after epoch: 0048 lost = 6.594019 ppl = 730.711
    Epoch: 0049 Batch: 50 /134 lost = 6.283687 ppl = 535.76
    Epoch: 0049 Batch: 100 /134 lost = 6.255811 ppl = 521.032
    Valid 4864 samples after epoch: 0049 lost = 6.593514 ppl = 730.343
    Epoch: 0050 Batch: 50 /134 lost = 6.279440 ppl = 533.49
    Epoch: 0050 Batch: 100 /134 lost = 6.250792 ppl = 518.423
    Valid 4864 samples after epoch: 0050 lost = 6.593027 ppl = 729.987
    Epoch: 0051 Batch: 50 /134 lost = 6.275209 ppl = 531.237
    Epoch: 0051 Batch: 100 /134 lost = 6.245789 ppl = 515.836
    Valid 4864 samples after epoch: 0051 lost = 6.592559 ppl = 729.646
    Epoch: 0052 Batch: 50 /134 lost = 6.270996 ppl = 529.004
    Epoch: 0052 Batch: 100 /134 lost = 6.240799 ppl = 513.268
    Valid 4864 samples after epoch: 0052 lost = 6.592112 ppl = 729.319
    Epoch: 0053 Batch: 50 /134 lost = 6.266802 ppl = 526.79
    Epoch: 0053 Batch: 100 /134 lost = 6.235819 ppl = 510.719
    Valid 4864 samples after epoch: 0053 lost = 6.591684 ppl = 729.007
    Epoch: 0054 Batch: 50 /134 lost = 6.262623 ppl = 524.593
    Epoch: 0054 Batch: 100 /134 lost = 6.230844 ppl = 508.184
    Valid 4864 samples after epoch: 0054 lost = 6.591278 ppl = 728.711
    Epoch: 0055 Batch: 50 /134 lost = 6.258450 ppl = 522.409
    Epoch: 0055 Batch: 100 /134 lost = 6.225873 ppl = 505.665
    Valid 4864 samples after epoch: 0055 lost = 6.590895 ppl = 728.433
    Epoch: 0056 Batch: 50 /134 lost = 6.254277 ppl = 520.233
    Epoch: 0056 Batch: 100 /134 lost = 6.220904 ppl = 503.158
    Valid 4864 samples after epoch: 0056 lost = 6.590540 ppl = 728.174
    Epoch: 0057 Batch: 50 /134 lost = 6.250112 ppl = 518.071
    Epoch: 0057 Batch: 100 /134 lost = 6.215936 ppl = 500.664
    Valid 4864 samples after epoch: 0057 lost = 6.590211 ppl = 727.934
    Epoch: 0058 Batch: 50 /134 lost = 6.245963 ppl = 515.926
    Epoch: 0058 Batch: 100 /134 lost = 6.210966 ppl = 498.182
    Valid 4864 samples after epoch: 0058 lost = 6.589905 ppl = 727.712
    Epoch: 0059 Batch: 50 /134 lost = 6.241826 ppl = 513.796
    Epoch: 0059 Batch: 100 /134 lost = 6.205992 ppl = 495.71
    Valid 4864 samples after epoch: 0059 lost = 6.589625 ppl = 727.508
    Epoch: 0060 Batch: 50 /134 lost = 6.237653 ppl = 511.656
    Epoch: 0060 Batch: 100 /134 lost = 6.201019 ppl = 493.251
    Valid 4864 samples after epoch: 0060 lost = 6.589386 ppl = 727.334
    Epoch: 0061 Batch: 50 /134 lost = 6.233510 ppl = 509.541
    Epoch: 0061 Batch: 100 /134 lost = 6.196069 ppl = 490.816
    Valid 4864 samples after epoch: 0061 lost = 6.589188 ppl = 727.19
    Epoch: 0062 Batch: 50 /134 lost = 6.229454 ppl = 507.478
    Epoch: 0062 Batch: 100 /134 lost = 6.191148 ppl = 488.407
    Valid 4864 samples after epoch: 0062 lost = 6.589028 ppl = 727.074
    Epoch: 0063 Batch: 50 /134 lost = 6.225468 ppl = 505.459
    Epoch: 0063 Batch: 100 /134 lost = 6.186260 ppl = 486.025
    Valid 4864 samples after epoch: 0063 lost = 6.588905 ppl = 726.984
    Epoch: 0064 Batch: 50 /134 lost = 6.221545 ppl = 503.481
    Epoch: 0064 Batch: 100 /134 lost = 6.181407 ppl = 483.672
    Valid 4864 samples after epoch: 0064 lost = 6.588819 ppl = 726.922
    Epoch: 0065 Batch: 50 /134 lost = 6.217687 ppl = 501.542
    Epoch: 0065 Batch: 100 /134 lost = 6.176593 ppl = 481.349
    Valid 4864 samples after epoch: 0065 lost = 6.588767 ppl = 726.884
    Epoch: 0066 Batch: 50 /134 lost = 6.213893 ppl = 499.643
    Epoch: 0066 Batch: 100 /134 lost = 6.171817 ppl = 479.056
    Valid 4864 samples after epoch: 0066 lost = 6.588749 ppl = 726.871
    Epoch: 0067 Batch: 50 /134 lost = 6.210164 ppl = 497.783
    Epoch: 0067 Batch: 100 /134 lost = 6.167086 ppl = 476.795
    Valid 4864 samples after epoch: 0067 lost = 6.588764 ppl = 726.882
    Epoch: 0068 Batch: 50 /134 lost = 6.206500 ppl = 495.962
    Epoch: 0068 Batch: 100 /134 lost = 6.162396 ppl = 474.564
    Valid 4864 samples after epoch: 0068 lost = 6.588811 ppl = 726.916
    Epoch: 0069 Batch: 50 /134 lost = 6.202902 ppl = 494.181
    Epoch: 0069 Batch: 100 /134 lost = 6.157754 ppl = 472.366
    Valid 4864 samples after epoch: 0069 lost = 6.588893 ppl = 726.976
    Epoch: 0070 Batch: 50 /134 lost = 6.199368 ppl = 492.438
    Epoch: 0070 Batch: 100 /134 lost = 6.153158 ppl = 470.2
    Valid 4864 samples after epoch: 0070 lost = 6.589013 ppl = 727.063
    Epoch: 0071 Batch: 50 /134 lost = 6.195887 ppl = 490.726
    Epoch: 0071 Batch: 100 /134 lost = 6.148608 ppl = 468.065
    Valid 4864 samples after epoch: 0071 lost = 6.589173 ppl = 727.179
    Epoch: 0072 Batch: 50 /134 lost = 6.192454 ppl = 489.045
    Epoch: 0072 Batch: 100 /134 lost = 6.144102 ppl = 465.961
    Valid 4864 samples after epoch: 0072 lost = 6.589374 ppl = 727.325
    Epoch: 0073 Batch: 50 /134 lost = 6.189062 ppl = 487.389
    Epoch: 0073 Batch: 100 /134 lost = 6.139641 ppl = 463.887
    Valid 4864 samples after epoch: 0073 lost = 6.589616 ppl = 727.502
    Epoch: 0074 Batch: 50 /134 lost = 6.185712 ppl = 485.759
    Epoch: 0074 Batch: 100 /134 lost = 6.135226 ppl = 461.843
    Valid 4864 samples after epoch: 0074 lost = 6.589898 ppl = 727.707
    Epoch: 0075 Batch: 50 /134 lost = 6.182407 ppl = 484.156
    Epoch: 0075 Batch: 100 /134 lost = 6.130857 ppl = 459.83
    Valid 4864 samples after epoch: 0075 lost = 6.590218 ppl = 727.939
    Epoch: 0076 Batch: 50 /134 lost = 6.179144 ppl = 482.579
    Epoch: 0076 Batch: 100 /134 lost = 6.126539 ppl = 457.849
    Valid 4864 samples after epoch: 0076 lost = 6.590572 ppl = 728.198
    Epoch: 0077 Batch: 50 /134 lost = 6.175930 ppl = 481.03
    Epoch: 0077 Batch: 100 /134 lost = 6.122272 ppl = 455.899
    Valid 4864 samples after epoch: 0077 lost = 6.590961 ppl = 728.48
    Epoch: 0078 Batch: 50 /134 lost = 6.172761 ppl = 479.508
    Epoch: 0078 Batch: 100 /134 lost = 6.118062 ppl = 453.984
    Valid 4864 samples after epoch: 0078 lost = 6.591381 ppl = 728.787
    Epoch: 0079 Batch: 50 /134 lost = 6.169640 ppl = 478.014
    Epoch: 0079 Batch: 100 /134 lost = 6.113906 ppl = 452.101
    Valid 4864 samples after epoch: 0079 lost = 6.591833 ppl = 729.116
    Epoch: 0080 Batch: 50 /134 lost = 6.166565 ppl = 476.546
    Epoch: 0080 Batch: 100 /134 lost = 6.109810 ppl = 450.253
    Valid 4864 samples after epoch: 0080 lost = 6.592315 ppl = 729.468
    Epoch: 0081 Batch: 50 /134 lost = 6.163531 ppl = 475.103
    Epoch: 0081 Batch: 100 /134 lost = 6.105772 ppl = 448.439
    Valid 4864 samples after epoch: 0081 lost = 6.592827 ppl = 729.841
    Epoch: 0082 Batch: 50 /134 lost = 6.160537 ppl = 473.682
    Epoch: 0082 Batch: 100 /134 lost = 6.101791 ppl = 446.657
    Valid 4864 samples after epoch: 0082 lost = 6.593369 ppl = 730.237
    Epoch: 0083 Batch: 50 /134 lost = 6.157580 ppl = 472.284
    Epoch: 0083 Batch: 100 /134 lost = 6.097864 ppl = 444.907
    Valid 4864 samples after epoch: 0083 lost = 6.593940 ppl = 730.654
    Epoch: 0084 Batch: 50 /134 lost = 6.154654 ppl = 470.904
    Epoch: 0084 Batch: 100 /134 lost = 6.093992 ppl = 443.187
    Valid 4864 samples after epoch: 0084 lost = 6.594540 ppl = 731.093
    Epoch: 0085 Batch: 50 /134 lost = 6.151764 ppl = 469.545
    Epoch: 0085 Batch: 100 /134 lost = 6.090172 ppl = 441.497
    Valid 4864 samples after epoch: 0085 lost = 6.595170 ppl = 731.553
    Epoch: 0086 Batch: 50 /134 lost = 6.148906 ppl = 468.205
    Epoch: 0086 Batch: 100 /134 lost = 6.086400 ppl = 439.835
    Valid 4864 samples after epoch: 0086 lost = 6.595827 ppl = 732.034
    Epoch: 0087 Batch: 50 /134 lost = 6.146078 ppl = 466.883
    Epoch: 0087 Batch: 100 /134 lost = 6.082679 ppl = 438.201
    Valid 4864 samples after epoch: 0087 lost = 6.596513 ppl = 732.537
    Epoch: 0088 Batch: 50 /134 lost = 6.143284 ppl = 465.58
    Epoch: 0088 Batch: 100 /134 lost = 6.079001 ppl = 436.593
    Valid 4864 samples after epoch: 0088 lost = 6.597227 ppl = 733.06
    Epoch: 0089 Batch: 50 /134 lost = 6.140523 ppl = 464.296
    Epoch: 0089 Batch: 100 /134 lost = 6.075366 ppl = 435.009
    Valid 4864 samples after epoch: 0089 lost = 6.597968 ppl = 733.603
    Epoch: 0090 Batch: 50 /134 lost = 6.137794 ppl = 463.031
    Epoch: 0090 Batch: 100 /134 lost = 6.071774 ppl = 433.449
    Valid 4864 samples after epoch: 0090 lost = 6.598736 ppl = 734.166
    Epoch: 0091 Batch: 50 /134 lost = 6.135098 ppl = 461.784
    Epoch: 0091 Batch: 100 /134 lost = 6.068222 ppl = 431.912
    Valid 4864 samples after epoch: 0091 lost = 6.599530 ppl = 734.749
    Epoch: 0092 Batch: 50 /134 lost = 6.132439 ppl = 460.558
    Epoch: 0092 Batch: 100 /134 lost = 6.064709 ppl = 430.397
    Valid 4864 samples after epoch: 0092 lost = 6.600349 ppl = 735.352
    Epoch: 0093 Batch: 50 /134 lost = 6.129811 ppl = 459.349
    Epoch: 0093 Batch: 100 /134 lost = 6.061235 ppl = 428.905
    Valid 4864 samples after epoch: 0093 lost = 6.601194 ppl = 735.973
    Epoch: 0094 Batch: 50 /134 lost = 6.127217 ppl = 458.159
    Epoch: 0094 Batch: 100 /134 lost = 6.057800 ppl = 427.434
    Valid 4864 samples after epoch: 0094 lost = 6.602063 ppl = 736.613
    Epoch: 0095 Batch: 50 /134 lost = 6.124658 ppl = 456.988
    Epoch: 0095 Batch: 100 /134 lost = 6.054404 ppl = 425.985
    Valid 4864 samples after epoch: 0095 lost = 6.602956 ppl = 737.271
    Epoch: 0096 Batch: 50 /134 lost = 6.122132 ppl = 455.836
    Epoch: 0096 Batch: 100 /134 lost = 6.051044 ppl = 424.556
    Valid 4864 samples after epoch: 0096 lost = 6.603871 ppl = 737.946
    Epoch: 0097 Batch: 50 /134 lost = 6.119639 ppl = 454.701
    Epoch: 0097 Batch: 100 /134 lost = 6.047724 ppl = 423.149
    Valid 4864 samples after epoch: 0097 lost = 6.604809 ppl = 738.639
    Epoch: 0098 Batch: 50 /134 lost = 6.117179 ppl = 453.584
    Epoch: 0098 Batch: 100 /134 lost = 6.044442 ppl = 421.762
    Valid 4864 samples after epoch: 0098 lost = 6.605768 ppl = 739.347
    Epoch: 0099 Batch: 50 /134 lost = 6.114754 ppl = 452.485
    Epoch: 0099 Batch: 100 /134 lost = 6.041196 ppl = 420.395
    Valid 4864 samples after epoch: 0099 lost = 6.606746 ppl = 740.071
    Epoch: 0100 Batch: 50 /134 lost = 6.112357 ppl = 451.401
    Epoch: 0100 Batch: 100 /134 lost = 6.037988 ppl = 419.049
    Valid 4864 samples after epoch: 0100 lost = 6.607744 ppl = 740.81
    
    Test the LSTMLM……………………
    Test 5760 samples with models/2_layers_lstmlm_model_(hidden=5)_epoch100.ckpt……………………
    lost = 6.533055 ppl = 687.496
    
