```python
!python 1_layer_rnnlm_with_penn_assignment.py
```

    The size of the dictionary is: 7613
    The number of the train batch is: 134
    
    Train the RNNLM……………………
    TextRNN(
      (C): Embedding(7613, 128)
      (W_ax): Linear(in_features=128, out_features=5, bias=False)
      (W_aa): Linear(in_features=5, out_features=5, bias=False)
      (tanh): Tanh()
      (W): Linear(in_features=5, out_features=7613, bias=False)
    )
    Epoch: 0001 Batch: 50 /134 lost = 8.845674 ppl = 6944.28
    Epoch: 0001 Batch: 100 /134 lost = 8.670191 ppl = 5826.61
    Valid 4864 samples after epoch: 0001 lost = 8.488662 ppl = 4859.36
    ------Saving best model------
    Epoch: 0002 Batch: 50 /134 lost = 8.208819 ppl = 3673.2
    Epoch: 0002 Batch: 100 /134 lost = 7.963600 ppl = 2874.4
    Valid 4864 samples after epoch: 0002 lost = 7.810615 ppl = 2466.65
    ------Saving best model------
    Epoch: 0003 Batch: 50 /134 lost = 7.552178 ppl = 1904.89
    Epoch: 0003 Batch: 100 /134 lost = 7.396204 ppl = 1629.79
    Valid 4864 samples after epoch: 0003 lost = 7.331916 ppl = 1528.31
    ------Saving best model------
    Epoch: 0004 Batch: 50 /134 lost = 7.107940 ppl = 1221.63
    Epoch: 0004 Batch: 100 /134 lost = 7.008998 ppl = 1106.55
    Valid 4864 samples after epoch: 0004 lost = 7.015753 ppl = 1114.05
    ------Saving best model------
    Epoch: 0005 Batch: 50 /134 lost = 6.814297 ppl = 910.776
    Epoch: 0005 Batch: 100 /134 lost = 6.752227 ppl = 855.963
    Valid 4864 samples after epoch: 0005 lost = 6.818856 ppl = 914.938
    ------Saving best model------
    Epoch: 0006 Batch: 50 /134 lost = 6.633703 ppl = 760.293
    Epoch: 0006 Batch: 100 /134 lost = 6.594429 ppl = 731.012
    Valid 4864 samples after epoch: 0006 lost = 6.708384 ppl = 819.246
    ------Saving best model------
    Epoch: 0007 Batch: 50 /134 lost = 6.532714 ppl = 687.261
    Epoch: 0007 Batch: 100 /134 lost = 6.507375 ppl = 670.065
    Valid 4864 samples after epoch: 0007 lost = 6.654551 ppl = 776.309
    ------Saving best model------
    Epoch: 0008 Batch: 50 /134 lost = 6.480021 ppl = 651.984
    Epoch: 0008 Batch: 100 /134 lost = 6.457454 ppl = 637.436
    Valid 4864 samples after epoch: 0008 lost = 6.625220 ppl = 753.87
    ------Saving best model------
    Epoch: 0009 Batch: 50 /134 lost = 6.454242 ppl = 635.392
    Epoch: 0009 Batch: 100 /134 lost = 6.434854 ppl = 623.191
    Valid 4864 samples after epoch: 0009 lost = 6.615411 ppl = 746.511
    ------Saving best model------
    Epoch: 0010 Batch: 50 /134 lost = 6.438085 ppl = 625.208
    Epoch: 0010 Batch: 100 /134 lost = 6.419411 ppl = 613.642
    Valid 4864 samples after epoch: 0010 lost = 6.606038 ppl = 739.547
    ------Saving best model------
    Epoch: 0011 Batch: 50 /134 lost = 6.418584 ppl = 613.134
    Epoch: 0011 Batch: 100 /134 lost = 6.396980 ppl = 600.03
    Valid 4864 samples after epoch: 0011 lost = 6.598135 ppl = 733.726
    ------Saving best model------
    Epoch: 0012 Batch: 50 /134 lost = 6.403491 ppl = 603.95
    Epoch: 0012 Batch: 100 /134 lost = 6.377130 ppl = 588.237
    Valid 4864 samples after epoch: 0012 lost = 6.593047 ppl = 730.002
    ------Saving best model------
    Epoch: 0013 Batch: 50 /134 lost = 6.396413 ppl = 599.69
    Epoch: 0013 Batch: 100 /134 lost = 6.358578 ppl = 577.425
    Valid 4864 samples after epoch: 0013 lost = 6.588181 ppl = 726.458
    ------Saving best model------
    Epoch: 0014 Batch: 50 /134 lost = 6.382868 ppl = 591.622
    Epoch: 0014 Batch: 100 /134 lost = 6.342551 ppl = 568.244
    Valid 4864 samples after epoch: 0014 lost = 6.579015 ppl = 719.83
    ------Saving best model------
    Epoch: 0015 Batch: 50 /134 lost = 6.365605 ppl = 581.497
    Epoch: 0015 Batch: 100 /134 lost = 6.322038 ppl = 556.706
    Valid 4864 samples after epoch: 0015 lost = 6.568383 ppl = 712.217
    ------Saving best model------
    Epoch: 0016 Batch: 50 /134 lost = 6.344064 ppl = 569.104
    Epoch: 0016 Batch: 100 /134 lost = 6.303377 ppl = 546.414
    Valid 4864 samples after epoch: 0016 lost = 6.557406 ppl = 704.442
    ------Saving best model------
    Epoch: 0017 Batch: 50 /134 lost = 6.319401 ppl = 555.24
    Epoch: 0017 Batch: 100 /134 lost = 6.285328 ppl = 536.64
    Valid 4864 samples after epoch: 0017 lost = 6.550064 ppl = 699.289
    ------Saving best model------
    Epoch: 0018 Batch: 50 /134 lost = 6.298203 ppl = 543.594
    Epoch: 0018 Batch: 100 /134 lost = 6.265881 ppl = 526.305
    Valid 4864 samples after epoch: 0018 lost = 6.541612 ppl = 693.403
    ------Saving best model------
    Epoch: 0019 Batch: 50 /134 lost = 6.277267 ppl = 532.332
    Epoch: 0019 Batch: 100 /134 lost = 6.241341 ppl = 513.547
    Valid 4864 samples after epoch: 0019 lost = 6.528467 ppl = 684.348
    ------Saving best model------
    Epoch: 0020 Batch: 50 /134 lost = 6.258635 ppl = 522.505
    Epoch: 0020 Batch: 100 /134 lost = 6.215840 ppl = 500.616
    Valid 4864 samples after epoch: 0020 lost = 6.514005 ppl = 674.523
    ------Saving best model------
    Epoch: 0021 Batch: 50 /134 lost = 6.239009 ppl = 512.351
    Epoch: 0021 Batch: 100 /134 lost = 6.188183 ppl = 486.96
    Valid 4864 samples after epoch: 0021 lost = 6.502470 ppl = 666.787
    ------Saving best model------
    Epoch: 0022 Batch: 50 /134 lost = 6.222491 ppl = 503.957
    Epoch: 0022 Batch: 100 /134 lost = 6.152990 ppl = 470.121
    Valid 4864 samples after epoch: 0022 lost = 6.487920 ppl = 657.155
    ------Saving best model------
    Epoch: 0023 Batch: 50 /134 lost = 6.204490 ppl = 494.966
    Epoch: 0023 Batch: 100 /134 lost = 6.122581 ppl = 456.04
    Valid 4864 samples after epoch: 0023 lost = 6.475898 ppl = 649.302
    ------Saving best model------
    Epoch: 0024 Batch: 50 /134 lost = 6.181087 ppl = 483.517
    Epoch: 0024 Batch: 100 /134 lost = 6.095484 ppl = 443.849
    Valid 4864 samples after epoch: 0024 lost = 6.465225 ppl = 642.409
    ------Saving best model------
    Epoch: 0025 Batch: 50 /134 lost = 6.162911 ppl = 474.808
    Epoch: 0025 Batch: 100 /134 lost = 6.068707 ppl = 432.122
    Valid 4864 samples after epoch: 0025 lost = 6.455103 ppl = 635.939
    ------Saving best model------
    Epoch: 0026 Batch: 50 /134 lost = 6.146154 ppl = 466.918
    Epoch: 0026 Batch: 100 /134 lost = 6.044243 ppl = 421.679
    Valid 4864 samples after epoch: 0026 lost = 6.447076 ppl = 630.855
    ------Saving best model------
    Epoch: 0027 Batch: 50 /134 lost = 6.130814 ppl = 459.81
    Epoch: 0027 Batch: 100 /134 lost = 6.021626 ppl = 412.248
    Valid 4864 samples after epoch: 0027 lost = 6.440902 ppl = 626.972
    ------Saving best model------
    Epoch: 0028 Batch: 50 /134 lost = 6.114820 ppl = 452.515
    Epoch: 0028 Batch: 100 /134 lost = 5.999614 ppl = 403.273
    Valid 4864 samples after epoch: 0028 lost = 6.435570 ppl = 623.638
    ------Saving best model------
    Epoch: 0029 Batch: 50 /134 lost = 6.098366 ppl = 445.13
    Epoch: 0029 Batch: 100 /134 lost = 5.978670 ppl = 394.915
    Valid 4864 samples after epoch: 0029 lost = 6.431458 ppl = 621.079
    ------Saving best model------
    Epoch: 0030 Batch: 50 /134 lost = 6.080930 ppl = 437.436
    Epoch: 0030 Batch: 100 /134 lost = 5.960161 ppl = 387.673
    Valid 4864 samples after epoch: 0030 lost = 6.427445 ppl = 618.591
    ------Saving best model------
    Epoch: 0031 Batch: 50 /134 lost = 6.063331 ppl = 429.805
    Epoch: 0031 Batch: 100 /134 lost = 5.942762 ppl = 380.986
    Valid 4864 samples after epoch: 0031 lost = 6.422302 ppl = 615.418
    ------Saving best model------
    Epoch: 0032 Batch: 50 /134 lost = 6.043466 ppl = 421.351
    Epoch: 0032 Batch: 100 /134 lost = 5.925814 ppl = 374.583
    Valid 4864 samples after epoch: 0032 lost = 6.419193 ppl = 613.508
    ------Saving best model------
    Epoch: 0033 Batch: 50 /134 lost = 6.024804 ppl = 413.56
    Epoch: 0033 Batch: 100 /134 lost = 5.909009 ppl = 368.341
    Valid 4864 samples after epoch: 0033 lost = 6.416397 ppl = 611.795
    ------Saving best model------
    Epoch: 0034 Batch: 50 /134 lost = 6.007667 ppl = 406.534
    Epoch: 0034 Batch: 100 /134 lost = 5.892815 ppl = 362.424
    Valid 4864 samples after epoch: 0034 lost = 6.414022 ppl = 610.343
    ------Saving best model------
    Epoch: 0035 Batch: 50 /134 lost = 5.991254 ppl = 399.916
    Epoch: 0035 Batch: 100 /134 lost = 5.875312 ppl = 356.136
    Valid 4864 samples after epoch: 0035 lost = 6.412078 ppl = 609.158
    ------Saving best model------
    Epoch: 0036 Batch: 50 /134 lost = 5.974902 ppl = 393.429
    Epoch: 0036 Batch: 100 /134 lost = 5.858352 ppl = 350.147
    Valid 4864 samples after epoch: 0036 lost = 6.410501 ppl = 608.198
    ------Saving best model------
    Epoch: 0037 Batch: 50 /134 lost = 5.958606 ppl = 387.07
    Epoch: 0037 Batch: 100 /134 lost = 5.841872 ppl = 344.423
    Valid 4864 samples after epoch: 0037 lost = 6.409467 ppl = 607.57
    ------Saving best model------
    Epoch: 0038 Batch: 50 /134 lost = 5.942141 ppl = 380.749
    Epoch: 0038 Batch: 100 /134 lost = 5.826484 ppl = 339.164
    Valid 4864 samples after epoch: 0038 lost = 6.408166 ppl = 606.78
    ------Saving best model------
    Epoch: 0039 Batch: 50 /134 lost = 5.926814 ppl = 374.958
    Epoch: 0039 Batch: 100 /134 lost = 5.813734 ppl = 334.867
    Valid 4864 samples after epoch: 0039 lost = 6.404657 ppl = 604.654
    ------Saving best model------
    Epoch: 0040 Batch: 50 /134 lost = 5.912179 ppl = 369.51
    Epoch: 0040 Batch: 100 /134 lost = 5.801493 ppl = 330.793
    Valid 4864 samples after epoch: 0040 lost = 6.403257 ppl = 603.809
    ------Saving best model------
    Epoch: 0041 Batch: 50 /134 lost = 5.897398 ppl = 364.089
    Epoch: 0041 Batch: 100 /134 lost = 5.789351 ppl = 326.801
    Valid 4864 samples after epoch: 0041 lost = 6.402027 ppl = 603.066
    ------Saving best model------
    Epoch: 0042 Batch: 50 /134 lost = 5.883555 ppl = 359.083
    Epoch: 0042 Batch: 100 /134 lost = 5.778500 ppl = 323.274
    Valid 4864 samples after epoch: 0042 lost = 6.400770 ppl = 602.309
    ------Saving best model------
    Epoch: 0043 Batch: 50 /134 lost = 5.869788 ppl = 354.174
    Epoch: 0043 Batch: 100 /134 lost = 5.767859 ppl = 319.852
    Valid 4864 samples after epoch: 0043 lost = 6.399340 ppl = 601.448
    ------Saving best model------
    Epoch: 0044 Batch: 50 /134 lost = 5.857384 ppl = 349.808
    Epoch: 0044 Batch: 100 /134 lost = 5.759120 ppl = 317.069
    Valid 4864 samples after epoch: 0044 lost = 6.398729 ppl = 601.081
    ------Saving best model------
    Epoch: 0045 Batch: 50 /134 lost = 5.845693 ppl = 345.742
    Epoch: 0045 Batch: 100 /134 lost = 5.750931 ppl = 314.483
    Valid 4864 samples after epoch: 0045 lost = 6.397979 ppl = 600.63
    ------Saving best model------
    Epoch: 0046 Batch: 50 /134 lost = 5.833860 ppl = 341.675
    Epoch: 0046 Batch: 100 /134 lost = 5.742483 ppl = 311.838
    Valid 4864 samples after epoch: 0046 lost = 6.397509 ppl = 600.348
    ------Saving best model------
    Epoch: 0047 Batch: 50 /134 lost = 5.820170 ppl = 337.029
    Epoch: 0047 Batch: 100 /134 lost = 5.733631 ppl = 309.089
    Valid 4864 samples after epoch: 0047 lost = 6.396418 ppl = 599.693
    ------Saving best model------
    Epoch: 0048 Batch: 50 /134 lost = 5.809975 ppl = 333.611
    Epoch: 0048 Batch: 100 /134 lost = 5.723756 ppl = 306.052
    Valid 4864 samples after epoch: 0048 lost = 6.395011 ppl = 598.85
    ------Saving best model------
    Epoch: 0049 Batch: 50 /134 lost = 5.800992 ppl = 330.627
    Epoch: 0049 Batch: 100 /134 lost = 5.714070 ppl = 303.102
    Valid 4864 samples after epoch: 0049 lost = 6.395068 ppl = 598.884
    Epoch: 0050 Batch: 50 /134 lost = 5.791362 ppl = 327.459
    Epoch: 0050 Batch: 100 /134 lost = 5.705678 ppl = 300.569
    Valid 4864 samples after epoch: 0050 lost = 6.395203 ppl = 598.965
    Epoch: 0051 Batch: 50 /134 lost = 5.782359 ppl = 324.524
    Epoch: 0051 Batch: 100 /134 lost = 5.697922 ppl = 298.247
    Valid 4864 samples after epoch: 0051 lost = 6.395622 ppl = 599.216
    Epoch: 0052 Batch: 50 /134 lost = 5.774051 ppl = 321.839
    Epoch: 0052 Batch: 100 /134 lost = 5.690186 ppl = 295.949
    Valid 4864 samples after epoch: 0052 lost = 6.396097 ppl = 599.5
    Epoch: 0053 Batch: 50 /134 lost = 5.766627 ppl = 319.458
    Epoch: 0053 Batch: 100 /134 lost = 5.683051 ppl = 293.845
    Valid 4864 samples after epoch: 0053 lost = 6.395641 ppl = 599.228
    Epoch: 0054 Batch: 50 /134 lost = 5.759814 ppl = 317.289
    Epoch: 0054 Batch: 100 /134 lost = 5.676446 ppl = 291.91
    Valid 4864 samples after epoch: 0054 lost = 6.396087 ppl = 599.495
    Epoch: 0055 Batch: 50 /134 lost = 5.750843 ppl = 314.455
    Epoch: 0055 Batch: 100 /134 lost = 5.669764 ppl = 289.966
    Valid 4864 samples after epoch: 0055 lost = 6.396173 ppl = 599.546
    Epoch: 0056 Batch: 50 /134 lost = 5.741504 ppl = 311.533
    Epoch: 0056 Batch: 100 /134 lost = 5.662917 ppl = 287.987
    Valid 4864 samples after epoch: 0056 lost = 6.396342 ppl = 599.648
    Epoch: 0057 Batch: 50 /134 lost = 5.732690 ppl = 308.799
    Epoch: 0057 Batch: 100 /134 lost = 5.656163 ppl = 286.049
    Valid 4864 samples after epoch: 0057 lost = 6.397081 ppl = 600.091
    Epoch: 0058 Batch: 50 /134 lost = 5.724783 ppl = 306.367
    Epoch: 0058 Batch: 100 /134 lost = 5.649240 ppl = 284.075
    Valid 4864 samples after epoch: 0058 lost = 6.397630 ppl = 600.42
    Epoch: 0059 Batch: 50 /134 lost = 5.717590 ppl = 304.171
    Epoch: 0059 Batch: 100 /134 lost = 5.642522 ppl = 282.173
    Valid 4864 samples after epoch: 0059 lost = 6.398246 ppl = 600.79
    Epoch: 0060 Batch: 50 /134 lost = 5.710491 ppl = 302.019
    Epoch: 0060 Batch: 100 /134 lost = 5.635605 ppl = 280.228
    Valid 4864 samples after epoch: 0060 lost = 6.398848 ppl = 601.152
    Epoch: 0061 Batch: 50 /134 lost = 5.703743 ppl = 299.988
    Epoch: 0061 Batch: 100 /134 lost = 5.628906 ppl = 278.357
    Valid 4864 samples after epoch: 0061 lost = 6.399769 ppl = 601.706
    Epoch: 0062 Batch: 50 /134 lost = 5.697094 ppl = 298.0
    Epoch: 0062 Batch: 100 /134 lost = 5.621984 ppl = 276.437
    Valid 4864 samples after epoch: 0062 lost = 6.400702 ppl = 602.267
    Epoch: 0063 Batch: 50 /134 lost = 5.689917 ppl = 295.869
    Epoch: 0063 Batch: 100 /134 lost = 5.614941 ppl = 274.497
    Valid 4864 samples after epoch: 0063 lost = 6.401809 ppl = 602.935
    Epoch: 0064 Batch: 50 /134 lost = 5.682577 ppl = 293.705
    Epoch: 0064 Batch: 100 /134 lost = 5.608468 ppl = 272.726
    Valid 4864 samples after epoch: 0064 lost = 6.402731 ppl = 603.491
    Epoch: 0065 Batch: 50 /134 lost = 5.675828 ppl = 291.73
    Epoch: 0065 Batch: 100 /134 lost = 5.602179 ppl = 271.016
    Valid 4864 samples after epoch: 0065 lost = 6.403537 ppl = 603.977
    Epoch: 0066 Batch: 50 /134 lost = 5.668937 ppl = 289.726
    Epoch: 0066 Batch: 100 /134 lost = 5.596030 ppl = 269.355
    Valid 4864 samples after epoch: 0066 lost = 6.404022 ppl = 604.271
    Epoch: 0067 Batch: 50 /134 lost = 5.662503 ppl = 287.868
    Epoch: 0067 Batch: 100 /134 lost = 5.591167 ppl = 268.048
    Valid 4864 samples after epoch: 0067 lost = 6.405242 ppl = 605.008
    Epoch: 0068 Batch: 50 /134 lost = 5.656484 ppl = 286.141
    Epoch: 0068 Batch: 100 /134 lost = 5.586158 ppl = 266.709
    Valid 4864 samples after epoch: 0068 lost = 6.406546 ppl = 605.798
    Epoch: 0069 Batch: 50 /134 lost = 5.651057 ppl = 284.592
    Epoch: 0069 Batch: 100 /134 lost = 5.580914 ppl = 265.314
    Valid 4864 samples after epoch: 0069 lost = 6.407838 ppl = 606.581
    Epoch: 0070 Batch: 50 /134 lost = 5.646064 ppl = 283.175
    Epoch: 0070 Batch: 100 /134 lost = 5.575679 ppl = 263.929
    Valid 4864 samples after epoch: 0070 lost = 6.408921 ppl = 607.238
    Epoch: 0071 Batch: 50 /134 lost = 5.641137 ppl = 281.783
    Epoch: 0071 Batch: 100 /134 lost = 5.570639 ppl = 262.602
    Valid 4864 samples after epoch: 0071 lost = 6.410070 ppl = 607.936
    Epoch: 0072 Batch: 50 /134 lost = 5.636728 ppl = 280.543
    Epoch: 0072 Batch: 100 /134 lost = 5.565720 ppl = 261.313
    Valid 4864 samples after epoch: 0072 lost = 6.410977 ppl = 608.488
    Epoch: 0073 Batch: 50 /134 lost = 5.632540 ppl = 279.371
    Epoch: 0073 Batch: 100 /134 lost = 5.560758 ppl = 260.02
    Valid 4864 samples after epoch: 0073 lost = 6.412173 ppl = 609.216
    Epoch: 0074 Batch: 50 /134 lost = 5.628428 ppl = 278.225
    Epoch: 0074 Batch: 100 /134 lost = 5.555621 ppl = 258.688
    Valid 4864 samples after epoch: 0074 lost = 6.413301 ppl = 609.904
    Epoch: 0075 Batch: 50 /134 lost = 5.624411 ppl = 277.109
    Epoch: 0075 Batch: 100 /134 lost = 5.550317 ppl = 257.319
    Valid 4864 samples after epoch: 0075 lost = 6.414484 ppl = 610.626
    Epoch: 0076 Batch: 50 /134 lost = 5.620320 ppl = 275.978
    Epoch: 0076 Batch: 100 /134 lost = 5.544399 ppl = 255.801
    Valid 4864 samples after epoch: 0076 lost = 6.415712 ppl = 611.376
    Epoch: 0077 Batch: 50 /134 lost = 5.616116 ppl = 274.82
    Epoch: 0077 Batch: 100 /134 lost = 5.538802 ppl = 254.373
    Valid 4864 samples after epoch: 0077 lost = 6.416543 ppl = 611.884
    Epoch: 0078 Batch: 50 /134 lost = 5.611959 ppl = 273.68
    Epoch: 0078 Batch: 100 /134 lost = 5.533969 ppl = 253.147
    Valid 4864 samples after epoch: 0078 lost = 6.417784 ppl = 612.644
    Epoch: 0079 Batch: 50 /134 lost = 5.607893 ppl = 272.569
    Epoch: 0079 Batch: 100 /134 lost = 5.529143 ppl = 251.928
    Valid 4864 samples after epoch: 0079 lost = 6.418720 ppl = 613.218
    Epoch: 0080 Batch: 50 /134 lost = 5.603842 ppl = 271.467
    Epoch: 0080 Batch: 100 /134 lost = 5.524579 ppl = 250.781
    Valid 4864 samples after epoch: 0080 lost = 6.420012 ppl = 614.011
    Epoch: 0081 Batch: 50 /134 lost = 5.599512 ppl = 270.294
    Epoch: 0081 Batch: 100 /134 lost = 5.520219 ppl = 249.69
    Valid 4864 samples after epoch: 0081 lost = 6.421349 ppl = 614.832
    Epoch: 0082 Batch: 50 /134 lost = 5.595171 ppl = 269.124
    Epoch: 0082 Batch: 100 /134 lost = 5.515841 ppl = 248.599
    Valid 4864 samples after epoch: 0082 lost = 6.422451 ppl = 615.51
    Epoch: 0083 Batch: 50 /134 lost = 5.590669 ppl = 267.915
    Epoch: 0083 Batch: 100 /134 lost = 5.511012 ppl = 247.401
    Valid 4864 samples after epoch: 0083 lost = 6.423694 ppl = 616.276
    Epoch: 0084 Batch: 50 /134 lost = 5.586387 ppl = 266.77
    Epoch: 0084 Batch: 100 /134 lost = 5.506205 ppl = 246.215
    Valid 4864 samples after epoch: 0084 lost = 6.424782 ppl = 616.946
    Epoch: 0085 Batch: 50 /134 lost = 5.582231 ppl = 265.664
    Epoch: 0085 Batch: 100 /134 lost = 5.501496 ppl = 245.058
    Valid 4864 samples after epoch: 0085 lost = 6.425771 ppl = 617.557
    Epoch: 0086 Batch: 50 /134 lost = 5.578495 ppl = 264.673
    Epoch: 0086 Batch: 100 /134 lost = 5.496730 ppl = 243.893
    Valid 4864 samples after epoch: 0086 lost = 6.427009 ppl = 618.322
    Epoch: 0087 Batch: 50 /134 lost = 5.574741 ppl = 263.681
    Epoch: 0087 Batch: 100 /134 lost = 5.491910 ppl = 242.72
    Valid 4864 samples after epoch: 0087 lost = 6.427916 ppl = 618.883
    Epoch: 0088 Batch: 50 /134 lost = 5.571144 ppl = 262.734
    Epoch: 0088 Batch: 100 /134 lost = 5.486984 ppl = 241.528
    Valid 4864 samples after epoch: 0088 lost = 6.429408 ppl = 619.807
    Epoch: 0089 Batch: 50 /134 lost = 5.567331 ppl = 261.735
    Epoch: 0089 Batch: 100 /134 lost = 5.482414 ppl = 240.426
    Valid 4864 samples after epoch: 0089 lost = 6.430387 ppl = 620.414
    Epoch: 0090 Batch: 50 /134 lost = 5.563562 ppl = 260.75
    Epoch: 0090 Batch: 100 /134 lost = 5.477972 ppl = 239.361
    Valid 4864 samples after epoch: 0090 lost = 6.431937 ppl = 621.377
    Epoch: 0091 Batch: 50 /134 lost = 5.559684 ppl = 259.741
    Epoch: 0091 Batch: 100 /134 lost = 5.473926 ppl = 238.394
    Valid 4864 samples after epoch: 0091 lost = 6.432696 ppl = 621.848
    Epoch: 0092 Batch: 50 /134 lost = 5.555871 ppl = 258.752
    Epoch: 0092 Batch: 100 /134 lost = 5.470073 ppl = 237.477
    Valid 4864 samples after epoch: 0092 lost = 6.433787 ppl = 622.527
    Epoch: 0093 Batch: 50 /134 lost = 5.551027 ppl = 257.502
    Epoch: 0093 Batch: 100 /134 lost = 5.466315 ppl = 236.587
    Valid 4864 samples after epoch: 0093 lost = 6.433533 ppl = 622.369
    Epoch: 0094 Batch: 50 /134 lost = 5.545059 ppl = 255.97
    Epoch: 0094 Batch: 100 /134 lost = 5.461823 ppl = 235.526
    Valid 4864 samples after epoch: 0094 lost = 6.434264 ppl = 622.824
    Epoch: 0095 Batch: 50 /134 lost = 5.540541 ppl = 254.816
    Epoch: 0095 Batch: 100 /134 lost = 5.453381 ppl = 233.546
    Valid 4864 samples after epoch: 0095 lost = 6.433801 ppl = 622.536
    Epoch: 0096 Batch: 50 /134 lost = 5.537768 ppl = 254.11
    Epoch: 0096 Batch: 100 /134 lost = 5.447390 ppl = 232.151
    Valid 4864 samples after epoch: 0096 lost = 6.435378 ppl = 623.518
    Epoch: 0097 Batch: 50 /134 lost = 5.534982 ppl = 253.403
    Epoch: 0097 Batch: 100 /134 lost = 5.442543 ppl = 231.029
    Valid 4864 samples after epoch: 0097 lost = 6.436456 ppl = 624.191
    Epoch: 0098 Batch: 50 /134 lost = 5.532141 ppl = 252.684
    Epoch: 0098 Batch: 100 /134 lost = 5.437993 ppl = 229.98
    Valid 4864 samples after epoch: 0098 lost = 6.438489 ppl = 625.461
    Epoch: 0099 Batch: 50 /134 lost = 5.529590 ppl = 252.04
    Epoch: 0099 Batch: 100 /134 lost = 5.433609 ppl = 228.974
    Valid 4864 samples after epoch: 0099 lost = 6.439480 ppl = 626.081
    Epoch: 0100 Batch: 50 /134 lost = 5.527142 ppl = 251.424
    Epoch: 0100 Batch: 100 /134 lost = 5.429332 ppl = 227.997
    Valid 4864 samples after epoch: 0100 lost = 6.441166 ppl = 627.138
    Epoch: 0101 Batch: 50 /134 lost = 5.524468 ppl = 250.753
    Epoch: 0101 Batch: 100 /134 lost = 5.425243 ppl = 227.067
    Valid 4864 samples after epoch: 0101 lost = 6.441925 ppl = 627.614
    Epoch: 0102 Batch: 50 /134 lost = 5.521941 ppl = 250.12
    Epoch: 0102 Batch: 100 /134 lost = 5.420777 ppl = 226.055
    Valid 4864 samples after epoch: 0102 lost = 6.443571 ppl = 628.647
    Epoch: 0103 Batch: 50 /134 lost = 5.519704 ppl = 249.561
    Epoch: 0103 Batch: 100 /134 lost = 5.415729 ppl = 224.916
    Valid 4864 samples after epoch: 0103 lost = 6.444405 ppl = 629.172
    Epoch: 0104 Batch: 50 /134 lost = 5.518261 ppl = 249.201
    Epoch: 0104 Batch: 100 /134 lost = 5.411609 ppl = 223.992
    Valid 4864 samples after epoch: 0104 lost = 6.447057 ppl = 630.843
    Epoch: 0105 Batch: 50 /134 lost = 5.516458 ppl = 248.752
    Epoch: 0105 Batch: 100 /134 lost = 5.407423 ppl = 223.056
    Valid 4864 samples after epoch: 0105 lost = 6.448466 ppl = 631.733
    Epoch: 0106 Batch: 50 /134 lost = 5.514203 ppl = 248.192
    Epoch: 0106 Batch: 100 /134 lost = 5.403442 ppl = 222.17
    Valid 4864 samples after epoch: 0106 lost = 6.451158 ppl = 633.435
    Epoch: 0107 Batch: 50 /134 lost = 5.511954 ppl = 247.635
    Epoch: 0107 Batch: 100 /134 lost = 5.399495 ppl = 221.295
    Valid 4864 samples after epoch: 0107 lost = 6.452398 ppl = 634.221
    Epoch: 0108 Batch: 50 /134 lost = 5.509416 ppl = 247.007
    Epoch: 0108 Batch: 100 /134 lost = 5.395897 ppl = 220.5
    Valid 4864 samples after epoch: 0108 lost = 6.455079 ppl = 635.924
    Epoch: 0109 Batch: 50 /134 lost = 5.507032 ppl = 246.419
    Epoch: 0109 Batch: 100 /134 lost = 5.392269 ppl = 219.701
    Valid 4864 samples after epoch: 0109 lost = 6.456049 ppl = 636.541
    Epoch: 0110 Batch: 50 /134 lost = 5.504388 ppl = 245.768
    Epoch: 0110 Batch: 100 /134 lost = 5.389028 ppl = 218.99
    Valid 4864 samples after epoch: 0110 lost = 6.458447 ppl = 638.069
    Epoch: 0111 Batch: 50 /134 lost = 5.501855 ppl = 245.146
    Epoch: 0111 Batch: 100 /134 lost = 5.385646 ppl = 218.251
    Valid 4864 samples after epoch: 0111 lost = 6.459022 ppl = 638.436
    Epoch: 0112 Batch: 50 /134 lost = 5.499083 ppl = 244.468
    Epoch: 0112 Batch: 100 /134 lost = 5.382453 ppl = 217.555
    Valid 4864 samples after epoch: 0112 lost = 6.461655 ppl = 640.119
    Epoch: 0113 Batch: 50 /134 lost = 5.496631 ppl = 243.869
    Epoch: 0113 Batch: 100 /134 lost = 5.378841 ppl = 216.771
    Valid 4864 samples after epoch: 0113 lost = 6.462227 ppl = 640.486
    Epoch: 0114 Batch: 50 /134 lost = 5.493886 ppl = 243.201
    Epoch: 0114 Batch: 100 /134 lost = 5.375060 ppl = 215.953
    Valid 4864 samples after epoch: 0114 lost = 6.464563 ppl = 641.984
    Epoch: 0115 Batch: 50 /134 lost = 5.491361 ppl = 242.587
    Epoch: 0115 Batch: 100 /134 lost = 5.370355 ppl = 214.939
    Valid 4864 samples after epoch: 0115 lost = 6.463630 ppl = 641.385
    Epoch: 0116 Batch: 50 /134 lost = 5.483964 ppl = 240.799
    Epoch: 0116 Batch: 100 /134 lost = 5.361572 ppl = 213.06
    Valid 4864 samples after epoch: 0116 lost = 6.458809 ppl = 638.3
    Epoch: 0117 Batch: 50 /134 lost = 5.478124 ppl = 239.397
    Epoch: 0117 Batch: 100 /134 lost = 5.357046 ppl = 212.097
    Valid 4864 samples after epoch: 0117 lost = 6.459290 ppl = 638.607
    Epoch: 0118 Batch: 50 /134 lost = 5.474085 ppl = 238.432
    Epoch: 0118 Batch: 100 /134 lost = 5.353014 ppl = 211.244
    Valid 4864 samples after epoch: 0118 lost = 6.461679 ppl = 640.135
    Epoch: 0119 Batch: 50 /134 lost = 5.470705 ppl = 237.628
    Epoch: 0119 Batch: 100 /134 lost = 5.348917 ppl = 210.38
    Valid 4864 samples after epoch: 0119 lost = 6.462669 ppl = 640.769
    Epoch: 0120 Batch: 50 /134 lost = 5.467533 ppl = 236.875
    Epoch: 0120 Batch: 100 /134 lost = 5.345148 ppl = 209.589
    Valid 4864 samples after epoch: 0120 lost = 6.465131 ppl = 642.349
    Epoch: 0121 Batch: 50 /134 lost = 5.464886 ppl = 236.249
    Epoch: 0121 Batch: 100 /134 lost = 5.341273 ppl = 208.778
    Valid 4864 samples after epoch: 0121 lost = 6.465045 ppl = 642.293
    Epoch: 0122 Batch: 50 /134 lost = 5.462112 ppl = 235.595
    Epoch: 0122 Batch: 100 /134 lost = 5.337481 ppl = 207.988
    Valid 4864 samples after epoch: 0122 lost = 6.467673 ppl = 643.983
    Epoch: 0123 Batch: 50 /134 lost = 5.459730 ppl = 235.034
    Epoch: 0123 Batch: 100 /134 lost = 5.333580 ppl = 207.178
    Valid 4864 samples after epoch: 0123 lost = 6.468544 ppl = 644.545
    Epoch: 0124 Batch: 50 /134 lost = 5.456984 ppl = 234.389
    Epoch: 0124 Batch: 100 /134 lost = 5.330104 ppl = 206.459
    Valid 4864 samples after epoch: 0124 lost = 6.471553 ppl = 646.487
    Epoch: 0125 Batch: 50 /134 lost = 5.454583 ppl = 233.827
    Epoch: 0125 Batch: 100 /134 lost = 5.326531 ppl = 205.723
    Valid 4864 samples after epoch: 0125 lost = 6.472509 ppl = 647.105
    Epoch: 0126 Batch: 50 /134 lost = 5.451932 ppl = 233.208
    Epoch: 0126 Batch: 100 /134 lost = 5.323328 ppl = 205.065
    Valid 4864 samples after epoch: 0126 lost = 6.475365 ppl = 648.956
    Epoch: 0127 Batch: 50 /134 lost = 5.449638 ppl = 232.674
    Epoch: 0127 Batch: 100 /134 lost = 5.320060 ppl = 204.396
    Valid 4864 samples after epoch: 0127 lost = 6.476226 ppl = 649.515
    Epoch: 0128 Batch: 50 /134 lost = 5.447002 ppl = 232.061
    Epoch: 0128 Batch: 100 /134 lost = 5.316999 ppl = 203.771
    Valid 4864 samples after epoch: 0128 lost = 6.478981 ppl = 651.307
    Epoch: 0129 Batch: 50 /134 lost = 5.444812 ppl = 231.554
    Epoch: 0129 Batch: 100 /134 lost = 5.313667 ppl = 203.094
    Valid 4864 samples after epoch: 0129 lost = 6.480311 ppl = 652.174
    Epoch: 0130 Batch: 50 /134 lost = 5.441743 ppl = 230.844
    Epoch: 0130 Batch: 100 /134 lost = 5.310546 ppl = 202.461
    Valid 4864 samples after epoch: 0130 lost = 6.483206 ppl = 654.065
    Epoch: 0131 Batch: 50 /134 lost = 5.439428 ppl = 230.31
    Epoch: 0131 Batch: 100 /134 lost = 5.307141 ppl = 201.773
    Valid 4864 samples after epoch: 0131 lost = 6.484556 ppl = 654.948
    Epoch: 0132 Batch: 50 /134 lost = 5.436407 ppl = 229.616
    Epoch: 0132 Batch: 100 /134 lost = 5.303782 ppl = 201.096
    Valid 4864 samples after epoch: 0132 lost = 6.487738 ppl = 657.036
    Epoch: 0133 Batch: 50 /134 lost = 5.434319 ppl = 229.137
    Epoch: 0133 Batch: 100 /134 lost = 5.300136 ppl = 200.364
    Valid 4864 samples after epoch: 0133 lost = 6.489207 ppl = 658.001
    Epoch: 0134 Batch: 50 /134 lost = 5.431273 ppl = 228.44
    Epoch: 0134 Batch: 100 /134 lost = 5.296548 ppl = 199.647
    Valid 4864 samples after epoch: 0134 lost = 6.492567 ppl = 660.216
    Epoch: 0135 Batch: 50 /134 lost = 5.428752 ppl = 227.865
    Epoch: 0135 Batch: 100 /134 lost = 5.292780 ppl = 198.896
    Valid 4864 samples after epoch: 0135 lost = 6.493879 ppl = 661.082
    Epoch: 0136 Batch: 50 /134 lost = 5.425324 ppl = 227.085
    Epoch: 0136 Batch: 100 /134 lost = 5.288982 ppl = 198.142
    Valid 4864 samples after epoch: 0136 lost = 6.496735 ppl = 662.973
    Epoch: 0137 Batch: 50 /134 lost = 5.422709 ppl = 226.492
    Epoch: 0137 Batch: 100 /134 lost = 5.284977 ppl = 197.35
    Valid 4864 samples after epoch: 0137 lost = 6.497794 ppl = 663.676
    Epoch: 0138 Batch: 50 /134 lost = 5.420098 ppl = 225.901
    Epoch: 0138 Batch: 100 /134 lost = 5.280933 ppl = 196.553
    Valid 4864 samples after epoch: 0138 lost = 6.500616 ppl = 665.551
    Epoch: 0139 Batch: 50 /134 lost = 5.418195 ppl = 225.472
    Epoch: 0139 Batch: 100 /134 lost = 5.276950 ppl = 195.772
    Valid 4864 samples after epoch: 0139 lost = 6.501804 ppl = 666.343
    Epoch: 0140 Batch: 50 /134 lost = 5.415740 ppl = 224.919
    Epoch: 0140 Batch: 100 /134 lost = 5.273682 ppl = 195.133
    Valid 4864 samples after epoch: 0140 lost = 6.504744 ppl = 668.305
    Epoch: 0141 Batch: 50 /134 lost = 5.413947 ppl = 224.516
    Epoch: 0141 Batch: 100 /134 lost = 5.270661 ppl = 194.544
    Valid 4864 samples after epoch: 0141 lost = 6.505995 ppl = 669.141
    Epoch: 0142 Batch: 50 /134 lost = 5.411697 ppl = 224.011
    Epoch: 0142 Batch: 100 /134 lost = 5.267657 ppl = 193.961
    Valid 4864 samples after epoch: 0142 lost = 6.508967 ppl = 671.133
    Epoch: 0143 Batch: 50 /134 lost = 5.409997 ppl = 223.631
    Epoch: 0143 Batch: 100 /134 lost = 5.264323 ppl = 193.315
    Valid 4864 samples after epoch: 0143 lost = 6.510133 ppl = 671.916
    Epoch: 0144 Batch: 50 /134 lost = 5.407760 ppl = 223.131
    Epoch: 0144 Batch: 100 /134 lost = 5.261460 ppl = 192.763
    Valid 4864 samples after epoch: 0144 lost = 6.513227 ppl = 673.998
    Epoch: 0145 Batch: 50 /134 lost = 5.406278 ppl = 222.801
    Epoch: 0145 Batch: 100 /134 lost = 5.258708 ppl = 192.233
    Valid 4864 samples after epoch: 0145 lost = 6.514624 ppl = 674.94
    Epoch: 0146 Batch: 50 /134 lost = 5.404056 ppl = 222.306
    Epoch: 0146 Batch: 100 /134 lost = 5.256292 ppl = 191.769
    Valid 4864 samples after epoch: 0146 lost = 6.517731 ppl = 677.041
    Epoch: 0147 Batch: 50 /134 lost = 5.402492 ppl = 221.959
    Epoch: 0147 Batch: 100 /134 lost = 5.253855 ppl = 191.302
    Valid 4864 samples after epoch: 0147 lost = 6.519352 ppl = 678.139
    Epoch: 0148 Batch: 50 /134 lost = 5.400134 ppl = 221.436
    Epoch: 0148 Batch: 100 /134 lost = 5.251605 ppl = 190.872
    Valid 4864 samples after epoch: 0148 lost = 6.522564 ppl = 680.321
    Epoch: 0149 Batch: 50 /134 lost = 5.398109 ppl = 220.988
    Epoch: 0149 Batch: 100 /134 lost = 5.249102 ppl = 190.395
    Valid 4864 samples after epoch: 0149 lost = 6.523937 ppl = 681.255
    Epoch: 0150 Batch: 50 /134 lost = 5.395401 ppl = 220.39
    Epoch: 0150 Batch: 100 /134 lost = 5.246776 ppl = 189.953
    Valid 4864 samples after epoch: 0150 lost = 6.526998 ppl = 683.344
    
    Test the RNNLM……………………
    Test 5760 samples with models/1_layer_rnnlm_model_best.ckpt……………………
    lost = 6.297778 ppl = 543.363
    
