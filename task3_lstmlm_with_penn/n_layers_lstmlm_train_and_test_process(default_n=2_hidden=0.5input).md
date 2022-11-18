hidden_size=input_size/2 本例中, 第0层hidden_size=emb_size/2=64, 第1层hidden_size=64/2=32


```python
!python n_layers_lstmlm_with_penn_assignment(default_n=2_hidden=0.5input).py
```

    The size of the dictionary is: 7613
    The number of the train batch is: 134
    
    Train the LSTMLM……………………
    TextLSTM(
      (embedding): Embedding(7613, 128)
      (W_hq): Linear(in_features=32, out_features=7613, bias=False)
      (sigmoid): Sigmoid()
      (tanh): Tanh()
    )
    Epoch: 0001 Batch: 50 /134 lost = 8.200584 ppl = 3643.08
    Epoch: 0001 Batch: 100 /134 lost = 7.608777 ppl = 2015.81
    Valid 4864 samples after epoch: 0001 lost = 7.305039 ppl = 1487.78
    ------Saving best model------
    Epoch: 0002 Batch: 50 /134 lost = 6.894519 ppl = 986.851
    Epoch: 0002 Batch: 100 /134 lost = 6.683943 ppl = 799.465
    Valid 4864 samples after epoch: 0002 lost = 6.708317 ppl = 819.191
    ------Saving best model------
    Epoch: 0003 Batch: 50 /134 lost = 6.497306 ppl = 663.352
    Epoch: 0003 Batch: 100 /134 lost = 6.463915 ppl = 641.568
    Valid 4864 samples after epoch: 0003 lost = 6.626275 ppl = 754.665
    ------Saving best model------
    Epoch: 0004 Batch: 50 /134 lost = 6.446404 ppl = 630.431
    Epoch: 0004 Batch: 100 /134 lost = 6.435983 ppl = 623.895
    Valid 4864 samples after epoch: 0004 lost = 6.625165 ppl = 753.829
    ------Saving best model------
    Epoch: 0005 Batch: 50 /134 lost = 6.435796 ppl = 623.779
    Epoch: 0005 Batch: 100 /134 lost = 6.423555 ppl = 616.19
    Valid 4864 samples after epoch: 0005 lost = 6.628232 ppl = 756.144
    Epoch: 0006 Batch: 50 /134 lost = 6.428432 ppl = 619.202
    Epoch: 0006 Batch: 100 /134 lost = 6.413056 ppl = 609.754
    Valid 4864 samples after epoch: 0006 lost = 6.630877 ppl = 758.147
    Epoch: 0007 Batch: 50 /134 lost = 6.421126 ppl = 614.695
    Epoch: 0007 Batch: 100 /134 lost = 6.402418 ppl = 603.302
    Valid 4864 samples after epoch: 0007 lost = 6.632020 ppl = 759.013
    Epoch: 0008 Batch: 50 /134 lost = 6.412930 ppl = 609.677
    Epoch: 0008 Batch: 100 /134 lost = 6.390669 ppl = 596.256
    Valid 4864 samples after epoch: 0008 lost = 6.631230 ppl = 758.414
    Epoch: 0009 Batch: 50 /134 lost = 6.403366 ppl = 603.874
    Epoch: 0009 Batch: 100 /134 lost = 6.377252 ppl = 588.309
    Valid 4864 samples after epoch: 0009 lost = 6.628329 ppl = 756.217
    Epoch: 0010 Batch: 50 /134 lost = 6.392194 ppl = 597.165
    Epoch: 0010 Batch: 100 /134 lost = 6.361926 ppl = 579.361
    Valid 4864 samples after epoch: 0010 lost = 6.623327 ppl = 752.444
    ------Saving best model------
    Epoch: 0011 Batch: 50 /134 lost = 6.379419 ppl = 589.585
    Epoch: 0011 Batch: 100 /134 lost = 6.344828 ppl = 569.539
    Valid 4864 samples after epoch: 0011 lost = 6.616529 ppl = 747.346
    ------Saving best model------
    Epoch: 0012 Batch: 50 /134 lost = 6.365434 ppl = 581.397
    Epoch: 0012 Batch: 100 /134 lost = 6.326545 ppl = 559.221
    Valid 4864 samples after epoch: 0012 lost = 6.608515 ppl = 741.381
    ------Saving best model------
    Epoch: 0013 Batch: 50 /134 lost = 6.350811 ppl = 572.957
    Epoch: 0013 Batch: 100 /134 lost = 6.307724 ppl = 548.794
    Valid 4864 samples after epoch: 0013 lost = 6.599808 ppl = 734.954
    ------Saving best model------
    Epoch: 0014 Batch: 50 /134 lost = 6.335924 ppl = 564.491
    Epoch: 0014 Batch: 100 /134 lost = 6.288806 ppl = 538.51
    Valid 4864 samples after epoch: 0014 lost = 6.590785 ppl = 728.353
    ------Saving best model------
    Epoch: 0015 Batch: 50 /134 lost = 6.320985 ppl = 556.121
    Epoch: 0015 Batch: 100 /134 lost = 6.270070 ppl = 528.514
    Valid 4864 samples after epoch: 0015 lost = 6.581667 ppl = 721.741
    ------Saving best model------
    Epoch: 0016 Batch: 50 /134 lost = 6.306063 ppl = 547.884
    Epoch: 0016 Batch: 100 /134 lost = 6.251600 ppl = 518.842
    Valid 4864 samples after epoch: 0016 lost = 6.572527 ppl = 715.175
    ------Saving best model------
    Epoch: 0017 Batch: 50 /134 lost = 6.291137 ppl = 539.767
    Epoch: 0017 Batch: 100 /134 lost = 6.233377 ppl = 509.473
    Valid 4864 samples after epoch: 0017 lost = 6.563376 ppl = 708.66
    ------Saving best model------
    Epoch: 0018 Batch: 50 /134 lost = 6.276174 ppl = 531.75
    Epoch: 0018 Batch: 100 /134 lost = 6.215349 ppl = 500.37
    Valid 4864 samples after epoch: 0018 lost = 6.554210 ppl = 702.194
    ------Saving best model------
    Epoch: 0019 Batch: 50 /134 lost = 6.261151 ppl = 523.822
    Epoch: 0019 Batch: 100 /134 lost = 6.197468 ppl = 491.503
    Valid 4864 samples after epoch: 0019 lost = 6.545031 ppl = 695.778
    ------Saving best model------
    Epoch: 0020 Batch: 50 /134 lost = 6.246069 ppl = 515.98
    Epoch: 0020 Batch: 100 /134 lost = 6.179708 ppl = 482.851
    Valid 4864 samples after epoch: 0020 lost = 6.535844 ppl = 689.415
    ------Saving best model------
    Epoch: 0021 Batch: 50 /134 lost = 6.230919 ppl = 508.223
    Epoch: 0021 Batch: 100 /134 lost = 6.162045 ppl = 474.397
    Valid 4864 samples after epoch: 0021 lost = 6.526650 ppl = 683.106
    ------Saving best model------
    Epoch: 0022 Batch: 50 /134 lost = 6.215668 ppl = 500.53
    Epoch: 0022 Batch: 100 /134 lost = 6.144455 ppl = 466.126
    Valid 4864 samples after epoch: 0022 lost = 6.517442 ppl = 676.845
    ------Saving best model------
    Epoch: 0023 Batch: 50 /134 lost = 6.200284 ppl = 492.889
    Epoch: 0023 Batch: 100 /134 lost = 6.126924 ppl = 458.025
    Valid 4864 samples after epoch: 0023 lost = 6.508223 ppl = 670.633
    ------Saving best model------
    Epoch: 0024 Batch: 50 /134 lost = 6.184776 ppl = 485.304
    Epoch: 0024 Batch: 100 /134 lost = 6.109468 ppl = 450.099
    Valid 4864 samples after epoch: 0024 lost = 6.499026 ppl = 664.494
    ------Saving best model------
    Epoch: 0025 Batch: 50 /134 lost = 6.169216 ppl = 477.811
    Epoch: 0025 Batch: 100 /134 lost = 6.092126 ppl = 442.361
    Valid 4864 samples after epoch: 0025 lost = 6.489912 ppl = 658.465
    ------Saving best model------
    Epoch: 0026 Batch: 50 /134 lost = 6.153687 ppl = 470.449
    Epoch: 0026 Batch: 100 /134 lost = 6.074925 ppl = 434.817
    Valid 4864 samples after epoch: 0026 lost = 6.480930 ppl = 652.577
    ------Saving best model------
    Epoch: 0027 Batch: 50 /134 lost = 6.138241 ppl = 463.238
    Epoch: 0027 Batch: 100 /134 lost = 6.057878 ppl = 427.468
    Valid 4864 samples after epoch: 0027 lost = 6.472106 ppl = 646.845
    ------Saving best model------
    Epoch: 0028 Batch: 50 /134 lost = 6.122921 ppl = 456.195
    Epoch: 0028 Batch: 100 /134 lost = 6.040997 ppl = 420.312
    Valid 4864 samples after epoch: 0028 lost = 6.463450 ppl = 641.27
    ------Saving best model------
    Epoch: 0029 Batch: 50 /134 lost = 6.107761 ppl = 449.331
    Epoch: 0029 Batch: 100 /134 lost = 6.024302 ppl = 413.353
    Valid 4864 samples after epoch: 0029 lost = 6.454970 ppl = 635.855
    ------Saving best model------
    Epoch: 0030 Batch: 50 /134 lost = 6.092784 ppl = 442.652
    Epoch: 0030 Batch: 100 /134 lost = 6.007811 ppl = 406.592
    Valid 4864 samples after epoch: 0030 lost = 6.446679 ppl = 630.605
    ------Saving best model------
    Epoch: 0031 Batch: 50 /134 lost = 6.078003 ppl = 436.157
    Epoch: 0031 Batch: 100 /134 lost = 5.991538 ppl = 400.029
    Valid 4864 samples after epoch: 0031 lost = 6.438600 ppl = 625.53
    ------Saving best model------
    Epoch: 0032 Batch: 50 /134 lost = 6.063442 ppl = 429.853
    Epoch: 0032 Batch: 100 /134 lost = 5.975496 ppl = 393.663
    Valid 4864 samples after epoch: 0032 lost = 6.430757 ppl = 620.644
    ------Saving best model------
    Epoch: 0033 Batch: 50 /134 lost = 6.049117 ppl = 423.739
    Epoch: 0033 Batch: 100 /134 lost = 5.959683 ppl = 387.487
    Valid 4864 samples after epoch: 0033 lost = 6.423158 ppl = 615.945
    ------Saving best model------
    Epoch: 0034 Batch: 50 /134 lost = 6.035030 ppl = 417.811
    Epoch: 0034 Batch: 100 /134 lost = 5.944081 ppl = 381.489
    Valid 4864 samples after epoch: 0034 lost = 6.415807 ppl = 611.434
    ------Saving best model------
    Epoch: 0035 Batch: 50 /134 lost = 6.021204 ppl = 412.074
    Epoch: 0035 Batch: 100 /134 lost = 5.928692 ppl = 375.663
    Valid 4864 samples after epoch: 0035 lost = 6.408715 ppl = 607.113
    ------Saving best model------
    Epoch: 0036 Batch: 50 /134 lost = 6.007658 ppl = 406.53
    Epoch: 0036 Batch: 100 /134 lost = 5.913526 ppl = 370.008
    Valid 4864 samples after epoch: 0036 lost = 6.401883 ppl = 602.98
    ------Saving best model------
    Epoch: 0037 Batch: 50 /134 lost = 5.994394 ppl = 401.173
    Epoch: 0037 Batch: 100 /134 lost = 5.898573 ppl = 364.517
    Valid 4864 samples after epoch: 0037 lost = 6.395305 ppl = 599.026
    ------Saving best model------
    Epoch: 0038 Batch: 50 /134 lost = 5.981385 ppl = 395.989
    Epoch: 0038 Batch: 100 /134 lost = 5.883820 ppl = 359.179
    Valid 4864 samples after epoch: 0038 lost = 6.388969 ppl = 595.242
    ------Saving best model------
    Epoch: 0039 Batch: 50 /134 lost = 5.968607 ppl = 390.961
    Epoch: 0039 Batch: 100 /134 lost = 5.869246 ppl = 353.982
    Valid 4864 samples after epoch: 0039 lost = 6.382866 ppl = 591.621
    ------Saving best model------
    Epoch: 0040 Batch: 50 /134 lost = 5.956048 ppl = 386.082
    Epoch: 0040 Batch: 100 /134 lost = 5.854865 ppl = 348.928
    Valid 4864 samples after epoch: 0040 lost = 6.376991 ppl = 588.155
    ------Saving best model------
    Epoch: 0041 Batch: 50 /134 lost = 5.943727 ppl = 381.354
    Epoch: 0041 Batch: 100 /134 lost = 5.840734 ppl = 344.032
    Valid 4864 samples after epoch: 0041 lost = 6.371341 ppl = 584.842
    ------Saving best model------
    Epoch: 0042 Batch: 50 /134 lost = 5.931645 ppl = 376.774
    Epoch: 0042 Batch: 100 /134 lost = 5.826869 ppl = 339.295
    Valid 4864 samples after epoch: 0042 lost = 6.365919 ppl = 581.679
    ------Saving best model------
    Epoch: 0043 Batch: 50 /134 lost = 5.919786 ppl = 372.332
    Epoch: 0043 Batch: 100 /134 lost = 5.813244 ppl = 334.703
    Valid 4864 samples after epoch: 0043 lost = 6.360726 ppl = 578.666
    ------Saving best model------
    Epoch: 0044 Batch: 50 /134 lost = 5.908131 ppl = 368.018
    Epoch: 0044 Batch: 100 /134 lost = 5.799836 ppl = 330.245
    Valid 4864 samples after epoch: 0044 lost = 6.355754 ppl = 575.796
    ------Saving best model------
    Epoch: 0045 Batch: 50 /134 lost = 5.896660 ppl = 363.82
    Epoch: 0045 Batch: 100 /134 lost = 5.786631 ppl = 325.913
    Valid 4864 samples after epoch: 0045 lost = 6.350996 ppl = 573.063
    ------Saving best model------
    Epoch: 0046 Batch: 50 /134 lost = 5.885360 ppl = 359.732
    Epoch: 0046 Batch: 100 /134 lost = 5.773617 ppl = 321.699
    Valid 4864 samples after epoch: 0046 lost = 6.346443 ppl = 570.46
    ------Saving best model------
    Epoch: 0047 Batch: 50 /134 lost = 5.874223 ppl = 355.748
    Epoch: 0047 Batch: 100 /134 lost = 5.760800 ppl = 317.602
    Valid 4864 samples after epoch: 0047 lost = 6.342094 ppl = 567.984
    ------Saving best model------
    Epoch: 0048 Batch: 50 /134 lost = 5.863254 ppl = 351.867
    Epoch: 0048 Batch: 100 /134 lost = 5.748185 ppl = 313.621
    Valid 4864 samples after epoch: 0048 lost = 6.337948 ppl = 565.634
    ------Saving best model------
    Epoch: 0049 Batch: 50 /134 lost = 5.852452 ppl = 348.087
    Epoch: 0049 Batch: 100 /134 lost = 5.735770 ppl = 309.751
    Valid 4864 samples after epoch: 0049 lost = 6.333999 ppl = 563.405
    ------Saving best model------
    Epoch: 0050 Batch: 50 /134 lost = 5.841812 ppl = 344.403
    Epoch: 0050 Batch: 100 /134 lost = 5.723545 ppl = 305.988
    Valid 4864 samples after epoch: 0050 lost = 6.330240 ppl = 561.291
    ------Saving best model------
    Epoch: 0051 Batch: 50 /134 lost = 5.831321 ppl = 340.809
    Epoch: 0051 Batch: 100 /134 lost = 5.711502 ppl = 302.325
    Valid 4864 samples after epoch: 0051 lost = 6.326665 ppl = 559.288
    ------Saving best model------
    Epoch: 0052 Batch: 50 /134 lost = 5.820979 ppl = 337.302
    Epoch: 0052 Batch: 100 /134 lost = 5.699638 ppl = 298.759
    Valid 4864 samples after epoch: 0052 lost = 6.323266 ppl = 557.39
    ------Saving best model------
    Epoch: 0053 Batch: 50 /134 lost = 5.810780 ppl = 333.879
    Epoch: 0053 Batch: 100 /134 lost = 5.687950 ppl = 295.288
    Valid 4864 samples after epoch: 0053 lost = 6.320037 ppl = 555.594
    ------Saving best model------
    Epoch: 0054 Batch: 50 /134 lost = 5.800719 ppl = 330.537
    Epoch: 0054 Batch: 100 /134 lost = 5.676434 ppl = 291.907
    Valid 4864 samples after epoch: 0054 lost = 6.316973 ppl = 553.894
    ------Saving best model------
    Epoch: 0055 Batch: 50 /134 lost = 5.790795 ppl = 327.273
    Epoch: 0055 Batch: 100 /134 lost = 5.665085 ppl = 288.612
    Valid 4864 samples after epoch: 0055 lost = 6.314065 ppl = 552.285
    ------Saving best model------
    Epoch: 0056 Batch: 50 /134 lost = 5.781003 ppl = 324.084
    Epoch: 0056 Batch: 100 /134 lost = 5.653903 ppl = 285.403
    Valid 4864 samples after epoch: 0056 lost = 6.311309 ppl = 550.765
    ------Saving best model------
    Epoch: 0057 Batch: 50 /134 lost = 5.771341 ppl = 320.968
    Epoch: 0057 Batch: 100 /134 lost = 5.642879 ppl = 282.274
    Valid 4864 samples after epoch: 0057 lost = 6.308698 ppl = 549.329
    ------Saving best model------
    Epoch: 0058 Batch: 50 /134 lost = 5.761806 ppl = 317.922
    Epoch: 0058 Batch: 100 /134 lost = 5.632010 ppl = 279.223
    Valid 4864 samples after epoch: 0058 lost = 6.306226 ppl = 547.973
    ------Saving best model------
    Epoch: 0059 Batch: 50 /134 lost = 5.752394 ppl = 314.944
    Epoch: 0059 Batch: 100 /134 lost = 5.621291 ppl = 276.246
    Valid 4864 samples after epoch: 0059 lost = 6.303887 ppl = 546.693
    ------Saving best model------
    Epoch: 0060 Batch: 50 /134 lost = 5.743103 ppl = 312.031
    Epoch: 0060 Batch: 100 /134 lost = 5.610713 ppl = 273.339
    Valid 4864 samples after epoch: 0060 lost = 6.301676 ppl = 545.486
    ------Saving best model------
    Epoch: 0061 Batch: 50 /134 lost = 5.733934 ppl = 309.183
    Epoch: 0061 Batch: 100 /134 lost = 5.600269 ppl = 270.499
    Valid 4864 samples after epoch: 0061 lost = 6.299590 ppl = 544.349
    ------Saving best model------
    Epoch: 0062 Batch: 50 /134 lost = 5.724882 ppl = 306.397
    Epoch: 0062 Batch: 100 /134 lost = 5.589951 ppl = 267.723
    Valid 4864 samples after epoch: 0062 lost = 6.297626 ppl = 543.281
    ------Saving best model------
    Epoch: 0063 Batch: 50 /134 lost = 5.715946 ppl = 303.671
    Epoch: 0063 Batch: 100 /134 lost = 5.579757 ppl = 265.007
    Valid 4864 samples after epoch: 0063 lost = 6.295781 ppl = 542.279
    ------Saving best model------
    Epoch: 0064 Batch: 50 /134 lost = 5.707122 ppl = 301.003
    Epoch: 0064 Batch: 100 /134 lost = 5.569683 ppl = 262.351
    Valid 4864 samples after epoch: 0064 lost = 6.294057 ppl = 541.345
    ------Saving best model------
    Epoch: 0065 Batch: 50 /134 lost = 5.698407 ppl = 298.392
    Epoch: 0065 Batch: 100 /134 lost = 5.559734 ppl = 259.754
    Valid 4864 samples after epoch: 0065 lost = 6.292451 ppl = 540.476
    ------Saving best model------
    Epoch: 0066 Batch: 50 /134 lost = 5.689800 ppl = 295.834
    Epoch: 0066 Batch: 100 /134 lost = 5.549917 ppl = 257.216
    Valid 4864 samples after epoch: 0066 lost = 6.290959 ppl = 539.67
    ------Saving best model------
    Epoch: 0067 Batch: 50 /134 lost = 5.681297 ppl = 293.33
    Epoch: 0067 Batch: 100 /134 lost = 5.540243 ppl = 254.74
    Valid 4864 samples after epoch: 0067 lost = 6.289572 ppl = 538.923
    ------Saving best model------
    Epoch: 0068 Batch: 50 /134 lost = 5.672898 ppl = 290.876
    Epoch: 0068 Batch: 100 /134 lost = 5.530724 ppl = 252.326
    Valid 4864 samples after epoch: 0068 lost = 6.288284 ppl = 538.229
    ------Saving best model------
    Epoch: 0069 Batch: 50 /134 lost = 5.664601 ppl = 288.473
    Epoch: 0069 Batch: 100 /134 lost = 5.521361 ppl = 249.975
    Valid 4864 samples after epoch: 0069 lost = 6.287088 ppl = 537.586
    ------Saving best model------
    Epoch: 0070 Batch: 50 /134 lost = 5.656398 ppl = 286.116
    Epoch: 0070 Batch: 100 /134 lost = 5.512145 ppl = 247.682
    Valid 4864 samples after epoch: 0070 lost = 6.285984 ppl = 536.993
    ------Saving best model------
    Epoch: 0071 Batch: 50 /134 lost = 5.648289 ppl = 283.806
    Epoch: 0071 Batch: 100 /134 lost = 5.503068 ppl = 245.444
    Valid 4864 samples after epoch: 0071 lost = 6.284971 ppl = 536.449
    ------Saving best model------
    Epoch: 0072 Batch: 50 /134 lost = 5.640272 ppl = 281.539
    Epoch: 0072 Batch: 100 /134 lost = 5.494126 ppl = 243.259
    Valid 4864 samples after epoch: 0072 lost = 6.284046 ppl = 535.953
    ------Saving best model------
    Epoch: 0073 Batch: 50 /134 lost = 5.632344 ppl = 279.316
    Epoch: 0073 Batch: 100 /134 lost = 5.485308 ppl = 241.123
    Valid 4864 samples after epoch: 0073 lost = 6.283208 ppl = 535.504
    ------Saving best model------
    Epoch: 0074 Batch: 50 /134 lost = 5.624503 ppl = 277.135
    Epoch: 0074 Batch: 100 /134 lost = 5.476607 ppl = 239.034
    Valid 4864 samples after epoch: 0074 lost = 6.282454 ppl = 535.1
    ------Saving best model------
    Epoch: 0075 Batch: 50 /134 lost = 5.616746 ppl = 274.993
    Epoch: 0075 Batch: 100 /134 lost = 5.468023 ppl = 236.991
    Valid 4864 samples after epoch: 0075 lost = 6.281781 ppl = 534.74
    ------Saving best model------
    Epoch: 0076 Batch: 50 /134 lost = 5.609072 ppl = 272.891
    Epoch: 0076 Batch: 100 /134 lost = 5.459547 ppl = 234.991
    Valid 4864 samples after epoch: 0076 lost = 6.281185 ppl = 534.421
    ------Saving best model------
    Epoch: 0077 Batch: 50 /134 lost = 5.601478 ppl = 270.826
    Epoch: 0077 Batch: 100 /134 lost = 5.451180 ppl = 233.033
    Valid 4864 samples after epoch: 0077 lost = 6.280663 ppl = 534.143
    ------Saving best model------
    Epoch: 0078 Batch: 50 /134 lost = 5.593959 ppl = 268.798
    Epoch: 0078 Batch: 100 /134 lost = 5.442916 ppl = 231.115
    Valid 4864 samples after epoch: 0078 lost = 6.280212 ppl = 533.902
    ------Saving best model------
    Epoch: 0079 Batch: 50 /134 lost = 5.586518 ppl = 266.805
    Epoch: 0079 Batch: 100 /134 lost = 5.434753 ppl = 229.236
    Valid 4864 samples after epoch: 0079 lost = 6.279829 ppl = 533.697
    ------Saving best model------
    Epoch: 0080 Batch: 50 /134 lost = 5.579149 ppl = 264.846
    Epoch: 0080 Batch: 100 /134 lost = 5.426692 ppl = 227.396
    Valid 4864 samples after epoch: 0080 lost = 6.279512 ppl = 533.528
    ------Saving best model------
    Epoch: 0081 Batch: 50 /134 lost = 5.571853 ppl = 262.921
    Epoch: 0081 Batch: 100 /134 lost = 5.418725 ppl = 225.591
    Valid 4864 samples after epoch: 0081 lost = 6.279258 ppl = 533.393
    ------Saving best model------
    Epoch: 0082 Batch: 50 /134 lost = 5.564627 ppl = 261.028
    Epoch: 0082 Batch: 100 /134 lost = 5.410854 ppl = 223.823
    Valid 4864 samples after epoch: 0082 lost = 6.279064 ppl = 533.289
    ------Saving best model------
    Epoch: 0083 Batch: 50 /134 lost = 5.557469 ppl = 259.166
    Epoch: 0083 Batch: 100 /134 lost = 5.403077 ppl = 222.089
    Valid 4864 samples after epoch: 0083 lost = 6.278928 ppl = 533.217
    ------Saving best model------
    Epoch: 0084 Batch: 50 /134 lost = 5.550379 ppl = 257.335
    Epoch: 0084 Batch: 100 /134 lost = 5.395391 ppl = 220.388
    Valid 4864 samples after epoch: 0084 lost = 6.278848 ppl = 533.174
    ------Saving best model------
    Epoch: 0085 Batch: 50 /134 lost = 5.543353 ppl = 255.533
    Epoch: 0085 Batch: 100 /134 lost = 5.387794 ppl = 218.72
    Valid 4864 samples after epoch: 0085 lost = 6.278822 ppl = 533.16
    ------Saving best model------
    Epoch: 0086 Batch: 50 /134 lost = 5.536393 ppl = 253.761
    Epoch: 0086 Batch: 100 /134 lost = 5.380282 ppl = 217.083
    Valid 4864 samples after epoch: 0086 lost = 6.278850 ppl = 533.175
    Epoch: 0087 Batch: 50 /134 lost = 5.529494 ppl = 252.016
    Epoch: 0087 Batch: 100 /134 lost = 5.372853 ppl = 215.477
    Valid 4864 samples after epoch: 0087 lost = 6.278928 ppl = 533.217
    Epoch: 0088 Batch: 50 /134 lost = 5.522658 ppl = 250.299
    Epoch: 0088 Batch: 100 /134 lost = 5.365506 ppl = 213.899
    Valid 4864 samples after epoch: 0088 lost = 6.279056 ppl = 533.285
    Epoch: 0089 Batch: 50 /134 lost = 5.515882 ppl = 248.609
    Epoch: 0089 Batch: 100 /134 lost = 5.358236 ppl = 212.35
    Valid 4864 samples after epoch: 0089 lost = 6.279228 ppl = 533.377
    Epoch: 0090 Batch: 50 /134 lost = 5.509165 ppl = 246.945
    Epoch: 0090 Batch: 100 /134 lost = 5.351042 ppl = 210.828
    Valid 4864 samples after epoch: 0090 lost = 6.279445 ppl = 533.492
    Epoch: 0091 Batch: 50 /134 lost = 5.502511 ppl = 245.307
    Epoch: 0091 Batch: 100 /134 lost = 5.343925 ppl = 209.333
    Valid 4864 samples after epoch: 0091 lost = 6.279703 ppl = 533.63
    Epoch: 0092 Batch: 50 /134 lost = 5.495918 ppl = 243.695
    Epoch: 0092 Batch: 100 /134 lost = 5.336878 ppl = 207.863
    Valid 4864 samples after epoch: 0092 lost = 6.280001 ppl = 533.789
    Epoch: 0093 Batch: 50 /134 lost = 5.489387 ppl = 242.109
    Epoch: 0093 Batch: 100 /134 lost = 5.329905 ppl = 206.418
    Valid 4864 samples after epoch: 0093 lost = 6.280339 ppl = 533.969
    Epoch: 0094 Batch: 50 /134 lost = 5.482918 ppl = 240.548
    Epoch: 0094 Batch: 100 /134 lost = 5.323001 ppl = 204.998
    Valid 4864 samples after epoch: 0094 lost = 6.280711 ppl = 534.168
    Epoch: 0095 Batch: 50 /134 lost = 5.476510 ppl = 239.011
    Epoch: 0095 Batch: 100 /134 lost = 5.316166 ppl = 203.602
    Valid 4864 samples after epoch: 0095 lost = 6.281116 ppl = 534.385
    Epoch: 0096 Batch: 50 /134 lost = 5.470159 ppl = 237.498
    Epoch: 0096 Batch: 100 /134 lost = 5.309398 ppl = 202.228
    Valid 4864 samples after epoch: 0096 lost = 6.281550 ppl = 534.617
    Epoch: 0097 Batch: 50 /134 lost = 5.463863 ppl = 236.007
    Epoch: 0097 Batch: 100 /134 lost = 5.302695 ppl = 200.877
    Valid 4864 samples after epoch: 0097 lost = 6.282011 ppl = 534.863
    Epoch: 0098 Batch: 50 /134 lost = 5.457621 ppl = 234.539
    Epoch: 0098 Batch: 100 /134 lost = 5.296058 ppl = 199.549
    Valid 4864 samples after epoch: 0098 lost = 6.282496 ppl = 535.122
    Epoch: 0099 Batch: 50 /134 lost = 5.451430 ppl = 233.091
    Epoch: 0099 Batch: 100 /134 lost = 5.289484 ppl = 198.241
    Valid 4864 samples after epoch: 0099 lost = 6.283002 ppl = 535.393
    Epoch: 0100 Batch: 50 /134 lost = 5.445289 ppl = 231.664
    Epoch: 0100 Batch: 100 /134 lost = 5.282974 ppl = 196.955
    Valid 4864 samples after epoch: 0100 lost = 6.283528 ppl = 535.675
    Epoch: 0101 Batch: 50 /134 lost = 5.439198 ppl = 230.258
    Epoch: 0101 Batch: 100 /134 lost = 5.276526 ppl = 195.689
    Valid 4864 samples after epoch: 0101 lost = 6.284072 ppl = 535.967
    Epoch: 0102 Batch: 50 /134 lost = 5.433155 ppl = 228.87
    Epoch: 0102 Batch: 100 /134 lost = 5.270139 ppl = 194.443
    Valid 4864 samples after epoch: 0102 lost = 6.284632 ppl = 536.267
    Epoch: 0103 Batch: 50 /134 lost = 5.427159 ppl = 227.502
    Epoch: 0103 Batch: 100 /134 lost = 5.263813 ppl = 193.217
    Valid 4864 samples after epoch: 0103 lost = 6.285206 ppl = 536.575
    Epoch: 0104 Batch: 50 /134 lost = 5.421209 ppl = 226.152
    Epoch: 0104 Batch: 100 /134 lost = 5.257545 ppl = 192.01
    Valid 4864 samples after epoch: 0104 lost = 6.285792 ppl = 536.889
    Epoch: 0105 Batch: 50 /134 lost = 5.415305 ppl = 224.821
    Epoch: 0105 Batch: 100 /134 lost = 5.251339 ppl = 190.822
    Valid 4864 samples after epoch: 0105 lost = 6.286389 ppl = 537.21
    Epoch: 0106 Batch: 50 /134 lost = 5.409443 ppl = 223.507
    Epoch: 0106 Batch: 100 /134 lost = 5.245190 ppl = 189.652
    Valid 4864 samples after epoch: 0106 lost = 6.286996 ppl = 537.536
    Epoch: 0107 Batch: 50 /134 lost = 5.403626 ppl = 222.211
    Epoch: 0107 Batch: 100 /134 lost = 5.239100 ppl = 188.5
    Valid 4864 samples after epoch: 0107 lost = 6.287610 ppl = 537.866
    Epoch: 0108 Batch: 50 /134 lost = 5.397849 ppl = 220.931
    Epoch: 0108 Batch: 100 /134 lost = 5.233067 ppl = 187.367
    Valid 4864 samples after epoch: 0108 lost = 6.288230 ppl = 538.2
    Epoch: 0109 Batch: 50 /134 lost = 5.392116 ppl = 219.668
    Epoch: 0109 Batch: 100 /134 lost = 5.227090 ppl = 186.25
    Valid 4864 samples after epoch: 0109 lost = 6.288855 ppl = 538.536
    Epoch: 0110 Batch: 50 /134 lost = 5.386423 ppl = 218.421
    Epoch: 0110 Batch: 100 /134 lost = 5.221172 ppl = 185.151
    Valid 4864 samples after epoch: 0110 lost = 6.289484 ppl = 538.875
    Epoch: 0111 Batch: 50 /134 lost = 5.380768 ppl = 217.189
    Epoch: 0111 Batch: 100 /134 lost = 5.215307 ppl = 184.068
    Valid 4864 samples after epoch: 0111 lost = 6.290116 ppl = 539.216
    Epoch: 0112 Batch: 50 /134 lost = 5.375155 ppl = 215.973
    Epoch: 0112 Batch: 100 /134 lost = 5.209499 ppl = 183.002
    Valid 4864 samples after epoch: 0112 lost = 6.290750 ppl = 539.558
    Epoch: 0113 Batch: 50 /134 lost = 5.369578 ppl = 214.772
    Epoch: 0113 Batch: 100 /134 lost = 5.203746 ppl = 181.953
    Valid 4864 samples after epoch: 0113 lost = 6.291384 ppl = 539.9
    Epoch: 0114 Batch: 50 /134 lost = 5.364041 ppl = 213.586
    Epoch: 0114 Batch: 100 /134 lost = 5.198045 ppl = 180.918
    Valid 4864 samples after epoch: 0114 lost = 6.292018 ppl = 540.242
    Epoch: 0115 Batch: 50 /134 lost = 5.358541 ppl = 212.415
    Epoch: 0115 Batch: 100 /134 lost = 5.192400 ppl = 179.9
    Valid 4864 samples after epoch: 0115 lost = 6.292651 ppl = 540.584
    Epoch: 0116 Batch: 50 /134 lost = 5.353077 ppl = 211.257
    Epoch: 0116 Batch: 100 /134 lost = 5.186804 ppl = 178.896
    Valid 4864 samples after epoch: 0116 lost = 6.293282 ppl = 540.926
    Epoch: 0117 Batch: 50 /134 lost = 5.347650 ppl = 210.114
    Epoch: 0117 Batch: 100 /134 lost = 5.181260 ppl = 177.907
    Valid 4864 samples after epoch: 0117 lost = 6.293910 ppl = 541.266
    Epoch: 0118 Batch: 50 /134 lost = 5.342259 ppl = 208.984
    Epoch: 0118 Batch: 100 /134 lost = 5.175767 ppl = 176.932
    Valid 4864 samples after epoch: 0118 lost = 6.294535 ppl = 541.604
    Epoch: 0119 Batch: 50 /134 lost = 5.336904 ppl = 207.868
    Epoch: 0119 Batch: 100 /134 lost = 5.170324 ppl = 175.972
    Valid 4864 samples after epoch: 0119 lost = 6.295155 ppl = 541.94
    Epoch: 0120 Batch: 50 /134 lost = 5.331582 ppl = 206.765
    Epoch: 0120 Batch: 100 /134 lost = 5.164929 ppl = 175.025
    Valid 4864 samples after epoch: 0120 lost = 6.295771 ppl = 542.274
    Epoch: 0121 Batch: 50 /134 lost = 5.326297 ppl = 205.675
    Epoch: 0121 Batch: 100 /134 lost = 5.159582 ppl = 174.092
    Valid 4864 samples after epoch: 0121 lost = 6.296380 ppl = 542.604
    Epoch: 0122 Batch: 50 /134 lost = 5.321046 ppl = 204.598
    Epoch: 0122 Batch: 100 /134 lost = 5.154284 ppl = 173.172
    Valid 4864 samples after epoch: 0122 lost = 6.296984 ppl = 542.932
    Epoch: 0123 Batch: 50 /134 lost = 5.315829 ppl = 203.533
    Epoch: 0123 Batch: 100 /134 lost = 5.149030 ppl = 172.264
    Valid 4864 samples after epoch: 0123 lost = 6.297582 ppl = 543.257
    Epoch: 0124 Batch: 50 /134 lost = 5.310647 ppl = 202.481
    Epoch: 0124 Batch: 100 /134 lost = 5.143824 ppl = 171.37
    Valid 4864 samples after epoch: 0124 lost = 6.298175 ppl = 543.579
    Epoch: 0125 Batch: 50 /134 lost = 5.305498 ppl = 201.441
    Epoch: 0125 Batch: 100 /134 lost = 5.138661 ppl = 170.487
    Valid 4864 samples after epoch: 0125 lost = 6.298762 ppl = 543.898
    Epoch: 0126 Batch: 50 /134 lost = 5.300385 ppl = 200.414
    Epoch: 0126 Batch: 100 /134 lost = 5.133543 ppl = 169.617
    Valid 4864 samples after epoch: 0126 lost = 6.299343 ppl = 544.214
    Epoch: 0127 Batch: 50 /134 lost = 5.295304 ppl = 199.398
    Epoch: 0127 Batch: 100 /134 lost = 5.128469 ppl = 168.758
    Valid 4864 samples after epoch: 0127 lost = 6.299919 ppl = 544.528
    Epoch: 0128 Batch: 50 /134 lost = 5.290257 ppl = 198.394
    Epoch: 0128 Batch: 100 /134 lost = 5.123436 ppl = 167.911
    Valid 4864 samples after epoch: 0128 lost = 6.300490 ppl = 544.839
    Epoch: 0129 Batch: 50 /134 lost = 5.285245 ppl = 197.403
    Epoch: 0129 Batch: 100 /134 lost = 5.118447 ppl = 167.076
    Valid 4864 samples after epoch: 0129 lost = 6.301054 ppl = 545.146
    Epoch: 0130 Batch: 50 /134 lost = 5.280264 ppl = 196.422
    Epoch: 0130 Batch: 100 /134 lost = 5.113501 ppl = 166.251
    Valid 4864 samples after epoch: 0130 lost = 6.301612 ppl = 545.451
    Epoch: 0131 Batch: 50 /134 lost = 5.275317 ppl = 195.452
    Epoch: 0131 Batch: 100 /134 lost = 5.108593 ppl = 165.437
    Valid 4864 samples after epoch: 0131 lost = 6.302164 ppl = 545.752
    Epoch: 0132 Batch: 50 /134 lost = 5.270401 ppl = 194.494
    Epoch: 0132 Batch: 100 /134 lost = 5.103729 ppl = 164.635
    Valid 4864 samples after epoch: 0132 lost = 6.302709 ppl = 546.049
    Epoch: 0133 Batch: 50 /134 lost = 5.265518 ppl = 193.546
    Epoch: 0133 Batch: 100 /134 lost = 5.098902 ppl = 163.842
    Valid 4864 samples after epoch: 0133 lost = 6.303247 ppl = 546.343
    Epoch: 0134 Batch: 50 /134 lost = 5.260667 ppl = 192.61
    Epoch: 0134 Batch: 100 /134 lost = 5.094114 ppl = 163.059
    Valid 4864 samples after epoch: 0134 lost = 6.303779 ppl = 546.634
    Epoch: 0135 Batch: 50 /134 lost = 5.255846 ppl = 191.684
    Epoch: 0135 Batch: 100 /134 lost = 5.089365 ppl = 162.287
    Valid 4864 samples after epoch: 0135 lost = 6.304303 ppl = 546.92
    Epoch: 0136 Batch: 50 /134 lost = 5.251057 ppl = 190.768
    Epoch: 0136 Batch: 100 /134 lost = 5.084652 ppl = 161.524
    Valid 4864 samples after epoch: 0136 lost = 6.304821 ppl = 547.204
    Epoch: 0137 Batch: 50 /134 lost = 5.246296 ppl = 189.862
    Epoch: 0137 Batch: 100 /134 lost = 5.079977 ppl = 160.77
    Valid 4864 samples after epoch: 0137 lost = 6.305332 ppl = 547.483
    Epoch: 0138 Batch: 50 /134 lost = 5.241567 ppl = 188.966
    Epoch: 0138 Batch: 100 /134 lost = 5.075338 ppl = 160.026
    Valid 4864 samples after epoch: 0138 lost = 6.305835 ppl = 547.759
    Epoch: 0139 Batch: 50 /134 lost = 5.236866 ppl = 188.08
    Epoch: 0139 Batch: 100 /134 lost = 5.070734 ppl = 159.291
    Valid 4864 samples after epoch: 0139 lost = 6.306332 ppl = 548.031
    Epoch: 0140 Batch: 50 /134 lost = 5.232194 ppl = 187.203
    Epoch: 0140 Batch: 100 /134 lost = 5.066163 ppl = 158.565
    Valid 4864 samples after epoch: 0140 lost = 6.306822 ppl = 548.3
    Epoch: 0141 Batch: 50 /134 lost = 5.227551 ppl = 186.336
    Epoch: 0141 Batch: 100 /134 lost = 5.061625 ppl = 157.847
    Valid 4864 samples after epoch: 0141 lost = 6.307305 ppl = 548.565
    Epoch: 0142 Batch: 50 /134 lost = 5.222935 ppl = 185.478
    Epoch: 0142 Batch: 100 /134 lost = 5.057121 ppl = 157.138
    Valid 4864 samples after epoch: 0142 lost = 6.307782 ppl = 548.827
    Epoch: 0143 Batch: 50 /134 lost = 5.218345 ppl = 184.628
    Epoch: 0143 Batch: 100 /134 lost = 5.052649 ppl = 156.436
    Valid 4864 samples after epoch: 0143 lost = 6.308253 ppl = 549.085
    Epoch: 0144 Batch: 50 /134 lost = 5.213783 ppl = 183.788
    Epoch: 0144 Batch: 100 /134 lost = 5.048207 ppl = 155.743
    Valid 4864 samples after epoch: 0144 lost = 6.308717 ppl = 549.34
    Epoch: 0145 Batch: 50 /134 lost = 5.209246 ppl = 182.956
    Epoch: 0145 Batch: 100 /134 lost = 5.043797 ppl = 155.058
    Valid 4864 samples after epoch: 0145 lost = 6.309176 ppl = 549.592
    Epoch: 0146 Batch: 50 /134 lost = 5.204735 ppl = 182.133
    Epoch: 0146 Batch: 100 /134 lost = 5.039416 ppl = 154.38
    Valid 4864 samples after epoch: 0146 lost = 6.309629 ppl = 549.841
    Epoch: 0147 Batch: 50 /134 lost = 5.200249 ppl = 181.317
    Epoch: 0147 Batch: 100 /134 lost = 5.035063 ppl = 153.709
    Valid 4864 samples after epoch: 0147 lost = 6.310076 ppl = 550.087
    Epoch: 0148 Batch: 50 /134 lost = 5.195786 ppl = 180.51
    Epoch: 0148 Batch: 100 /134 lost = 5.030740 ppl = 153.046
    Valid 4864 samples after epoch: 0148 lost = 6.310517 ppl = 550.33
    Epoch: 0149 Batch: 50 /134 lost = 5.191350 ppl = 179.711
    Epoch: 0149 Batch: 100 /134 lost = 5.026444 ppl = 152.39
    Valid 4864 samples after epoch: 0149 lost = 6.310954 ppl = 550.57
    Epoch: 0150 Batch: 50 /134 lost = 5.186937 ppl = 178.92
    Epoch: 0150 Batch: 100 /134 lost = 5.022177 ppl = 151.741
    Valid 4864 samples after epoch: 0150 lost = 6.311385 ppl = 550.807
    
    Test the LSTMLM……………………
    Test 5760 samples with models/2_layers_lstmlm_model_(hidden=0.5input)_best.ckpt……………………
    lost = 6.183000 ppl = 484.443
    
