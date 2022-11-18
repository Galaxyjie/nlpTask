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
    Epoch: 0001 Batch: 50 /134 lost = 8.846700 ppl = 6951.41
    Epoch: 0001 Batch: 100 /134 lost = 8.728514 ppl = 6176.54
    Valid 4864 samples after epoch: 0001 lost = 8.571275 ppl = 5277.86
    ------Saving best model------
    Epoch: 0002 Batch: 50 /134 lost = 8.123495 ppl = 3372.79
    Epoch: 0002 Batch: 100 /134 lost = 7.768308 ppl = 2364.47
    Valid 4864 samples after epoch: 0002 lost = 7.606070 ppl = 2010.36
    ------Saving best model------
    Epoch: 0003 Batch: 50 /134 lost = 7.292941 ppl = 1469.89
    Epoch: 0003 Batch: 100 /134 lost = 7.159063 ppl = 1285.71
    Valid 4864 samples after epoch: 0003 lost = 7.137758 ppl = 1258.6
    ------Saving best model------
    Epoch: 0004 Batch: 50 /134 lost = 6.896614 ppl = 988.92
    Epoch: 0004 Batch: 100 /134 lost = 6.827032 ppl = 922.449
    Valid 4864 samples after epoch: 0004 lost = 6.883448 ppl = 975.986
    ------Saving best model------
    Epoch: 0005 Batch: 50 /134 lost = 6.676212 ppl = 793.308
    Epoch: 0005 Batch: 100 /134 lost = 6.635046 ppl = 761.314
    Valid 4864 samples after epoch: 0005 lost = 6.746806 ppl = 851.335
    ------Saving best model------
    Epoch: 0006 Batch: 50 /134 lost = 6.557475 ppl = 704.49
    Epoch: 0006 Batch: 100 /134 lost = 6.530149 ppl = 685.5
    Valid 4864 samples after epoch: 0006 lost = 6.680077 ppl = 796.38
    ------Saving best model------
    Epoch: 0007 Batch: 50 /134 lost = 6.497016 ppl = 663.16
    Epoch: 0007 Batch: 100 /134 lost = 6.476974 ppl = 650.001
    Valid 4864 samples after epoch: 0007 lost = 6.650935 ppl = 773.508
    ------Saving best model------
    Epoch: 0008 Batch: 50 /134 lost = 6.467144 ppl = 643.643
    Epoch: 0008 Batch: 100 /134 lost = 6.451283 ppl = 633.515
    Valid 4864 samples after epoch: 0008 lost = 6.640071 ppl = 765.149
    ------Saving best model------
    Epoch: 0009 Batch: 50 /134 lost = 6.452792 ppl = 634.471
    Epoch: 0009 Batch: 100 /134 lost = 6.439330 ppl = 625.987
    Valid 4864 samples after epoch: 0009 lost = 6.637817 ppl = 763.426
    ------Saving best model------
    Epoch: 0010 Batch: 50 /134 lost = 6.446153 ppl = 630.273
    Epoch: 0010 Batch: 100 /134 lost = 6.433694 ppl = 622.469
    Valid 4864 samples after epoch: 0010 lost = 6.639099 ppl = 764.406
    Epoch: 0011 Batch: 50 /134 lost = 6.442759 ppl = 628.137
    Epoch: 0011 Batch: 100 /134 lost = 6.430713 ppl = 620.616
    Valid 4864 samples after epoch: 0011 lost = 6.641767 ppl = 766.448
    Epoch: 0012 Batch: 50 /134 lost = 6.440884 ppl = 626.961
    Epoch: 0012 Batch: 100 /134 lost = 6.428896 ppl = 619.49
    Valid 4864 samples after epoch: 0012 lost = 6.644970 ppl = 768.907
    Epoch: 0013 Batch: 50 /134 lost = 6.439648 ppl = 626.186
    Epoch: 0013 Batch: 100 /134 lost = 6.427510 ppl = 618.632
    Valid 4864 samples after epoch: 0013 lost = 6.648242 ppl = 771.427
    Epoch: 0014 Batch: 50 /134 lost = 6.438605 ppl = 625.534
    Epoch: 0014 Batch: 100 /134 lost = 6.426129 ppl = 617.778
    Valid 4864 samples after epoch: 0014 lost = 6.651398 ppl = 773.866
    Epoch: 0015 Batch: 50 /134 lost = 6.437738 ppl = 624.992
    Epoch: 0015 Batch: 100 /134 lost = 6.424442 ppl = 616.737
    Valid 4864 samples after epoch: 0015 lost = 6.654334 ppl = 776.14
    Epoch: 0016 Batch: 50 /134 lost = 6.435920 ppl = 623.856
    Epoch: 0016 Batch: 100 /134 lost = 6.417995 ppl = 612.774
    Valid 4864 samples after epoch: 0016 lost = 6.647917 ppl = 771.177
    Epoch: 0017 Batch: 50 /134 lost = 6.430716 ppl = 620.618
    Epoch: 0017 Batch: 100 /134 lost = 6.404353 ppl = 604.47
    Valid 4864 samples after epoch: 0017 lost = 6.641320 ppl = 766.106
    Epoch: 0018 Batch: 50 /134 lost = 6.420819 ppl = 614.506
    Epoch: 0018 Batch: 100 /134 lost = 6.391707 ppl = 596.875
    Valid 4864 samples after epoch: 0018 lost = 6.638539 ppl = 763.978
    Epoch: 0019 Batch: 50 /134 lost = 6.405639 ppl = 605.249
    Epoch: 0019 Batch: 100 /134 lost = 6.379546 ppl = 589.66
    Valid 4864 samples after epoch: 0019 lost = 6.635465 ppl = 761.633
    ------Saving best model------
    Epoch: 0020 Batch: 50 /134 lost = 6.388727 ppl = 595.098
    Epoch: 0020 Batch: 100 /134 lost = 6.367445 ppl = 582.568
    Valid 4864 samples after epoch: 0020 lost = 6.633116 ppl = 759.847
    ------Saving best model------
    Epoch: 0021 Batch: 50 /134 lost = 6.378191 ppl = 588.862
    Epoch: 0021 Batch: 100 /134 lost = 6.352103 ppl = 573.698
    Valid 4864 samples after epoch: 0021 lost = 6.632192 ppl = 759.144
    ------Saving best model------
    Epoch: 0022 Batch: 50 /134 lost = 6.363429 ppl = 580.232
    Epoch: 0022 Batch: 100 /134 lost = 6.334452 ppl = 563.66
    Valid 4864 samples after epoch: 0022 lost = 6.632213 ppl = 759.16
    Epoch: 0023 Batch: 50 /134 lost = 6.350062 ppl = 572.528
    Epoch: 0023 Batch: 100 /134 lost = 6.321131 ppl = 556.202
    Valid 4864 samples after epoch: 0023 lost = 6.632760 ppl = 759.576
    Epoch: 0024 Batch: 50 /134 lost = 6.337953 ppl = 565.637
    Epoch: 0024 Batch: 100 /134 lost = 6.305933 ppl = 547.812
    Valid 4864 samples after epoch: 0024 lost = 6.634536 ppl = 760.926
    Epoch: 0025 Batch: 50 /134 lost = 6.323568 ppl = 557.559
    Epoch: 0025 Batch: 100 /134 lost = 6.289780 ppl = 539.035
    Valid 4864 samples after epoch: 0025 lost = 6.634439 ppl = 760.852
    Epoch: 0026 Batch: 50 /134 lost = 6.310277 ppl = 550.197
    Epoch: 0026 Batch: 100 /134 lost = 6.274459 ppl = 530.839
    Valid 4864 samples after epoch: 0026 lost = 6.634143 ppl = 760.627
    Epoch: 0027 Batch: 50 /134 lost = 6.298803 ppl = 543.921
    Epoch: 0027 Batch: 100 /134 lost = 6.257607 ppl = 521.968
    Valid 4864 samples after epoch: 0027 lost = 6.634400 ppl = 760.822
    Epoch: 0028 Batch: 50 /134 lost = 6.287724 ppl = 537.927
    Epoch: 0028 Batch: 100 /134 lost = 6.244198 ppl = 515.016
    Valid 4864 samples after epoch: 0028 lost = 6.635894 ppl = 761.96
    Epoch: 0029 Batch: 50 /134 lost = 6.274694 ppl = 530.964
    Epoch: 0029 Batch: 100 /134 lost = 6.231139 ppl = 508.334
    Valid 4864 samples after epoch: 0029 lost = 6.637159 ppl = 762.925
    Epoch: 0030 Batch: 50 /134 lost = 6.258517 ppl = 522.443
    Epoch: 0030 Batch: 100 /134 lost = 6.218448 ppl = 501.923
    Valid 4864 samples after epoch: 0030 lost = 6.639834 ppl = 764.968
    Epoch: 0031 Batch: 50 /134 lost = 6.247087 ppl = 516.506
    Epoch: 0031 Batch: 100 /134 lost = 6.205853 ppl = 495.642
    Valid 4864 samples after epoch: 0031 lost = 6.641637 ppl = 766.348
    Epoch: 0032 Batch: 50 /134 lost = 6.234284 ppl = 509.935
    Epoch: 0032 Batch: 100 /134 lost = 6.194336 ppl = 489.966
    Valid 4864 samples after epoch: 0032 lost = 6.643552 ppl = 767.818
    Epoch: 0033 Batch: 50 /134 lost = 6.221239 ppl = 503.327
    Epoch: 0033 Batch: 100 /134 lost = 6.182248 ppl = 484.079
    Valid 4864 samples after epoch: 0033 lost = 6.647496 ppl = 770.852
    Epoch: 0034 Batch: 50 /134 lost = 6.209850 ppl = 497.627
    Epoch: 0034 Batch: 100 /134 lost = 6.173349 ppl = 479.79
    Valid 4864 samples after epoch: 0034 lost = 6.650014 ppl = 772.795
    Epoch: 0035 Batch: 50 /134 lost = 6.198951 ppl = 492.233
    Epoch: 0035 Batch: 100 /134 lost = 6.162889 ppl = 474.798
    Valid 4864 samples after epoch: 0035 lost = 6.656573 ppl = 777.88
    Epoch: 0036 Batch: 50 /134 lost = 6.182210 ppl = 484.061
    Epoch: 0036 Batch: 100 /134 lost = 6.149732 ppl = 468.592
    Valid 4864 samples after epoch: 0036 lost = 6.661149 ppl = 781.448
    Epoch: 0037 Batch: 50 /134 lost = 6.172853 ppl = 479.552
    Epoch: 0037 Batch: 100 /134 lost = 6.137723 ppl = 462.998
    Valid 4864 samples after epoch: 0037 lost = 6.663982 ppl = 783.665
    Epoch: 0038 Batch: 50 /134 lost = 6.161327 ppl = 474.057
    Epoch: 0038 Batch: 100 /134 lost = 6.125060 ppl = 457.172
    Valid 4864 samples after epoch: 0038 lost = 6.670696 ppl = 788.945
    Epoch: 0039 Batch: 50 /134 lost = 6.151761 ppl = 469.544
    Epoch: 0039 Batch: 100 /134 lost = 6.115134 ppl = 452.657
    Valid 4864 samples after epoch: 0039 lost = 6.674445 ppl = 791.908
    Epoch: 0040 Batch: 50 /134 lost = 6.141788 ppl = 464.884
    Epoch: 0040 Batch: 100 /134 lost = 6.104420 ppl = 447.833
    Valid 4864 samples after epoch: 0040 lost = 6.678298 ppl = 794.965
    Epoch: 0041 Batch: 50 /134 lost = 6.130616 ppl = 459.719
    Epoch: 0041 Batch: 100 /134 lost = 6.094065 ppl = 443.22
    Valid 4864 samples after epoch: 0041 lost = 6.682444 ppl = 798.268
    Epoch: 0042 Batch: 50 /134 lost = 6.121699 ppl = 455.638
    Epoch: 0042 Batch: 100 /134 lost = 6.083803 ppl = 438.694
    Valid 4864 samples after epoch: 0042 lost = 6.689270 ppl = 803.735
    Epoch: 0043 Batch: 50 /134 lost = 6.111657 ppl = 451.086
    Epoch: 0043 Batch: 100 /134 lost = 6.072943 ppl = 433.956
    Valid 4864 samples after epoch: 0043 lost = 6.693673 ppl = 807.282
    Epoch: 0044 Batch: 50 /134 lost = 6.103460 ppl = 447.403
    Epoch: 0044 Batch: 100 /134 lost = 6.062086 ppl = 429.27
    Valid 4864 samples after epoch: 0044 lost = 6.701932 ppl = 813.977
    Epoch: 0045 Batch: 50 /134 lost = 6.095105 ppl = 443.68
    Epoch: 0045 Batch: 100 /134 lost = 6.052364 ppl = 425.117
    Valid 4864 samples after epoch: 0045 lost = 6.705096 ppl = 816.557
    Epoch: 0046 Batch: 50 /134 lost = 6.087389 ppl = 440.271
    Epoch: 0046 Batch: 100 /134 lost = 6.047180 ppl = 422.919
    Valid 4864 samples after epoch: 0046 lost = 6.712197 ppl = 822.376
    Epoch: 0047 Batch: 50 /134 lost = 6.079844 ppl = 436.961
    Epoch: 0047 Batch: 100 /134 lost = 6.037661 ppl = 418.912
    Valid 4864 samples after epoch: 0047 lost = 6.718299 ppl = 827.409
    Epoch: 0048 Batch: 50 /134 lost = 6.070094 ppl = 432.721
    Epoch: 0048 Batch: 100 /134 lost = 6.029690 ppl = 415.586
    Valid 4864 samples after epoch: 0048 lost = 6.723982 ppl = 832.124
    Epoch: 0049 Batch: 50 /134 lost = 6.063748 ppl = 429.984
    Epoch: 0049 Batch: 100 /134 lost = 6.021736 ppl = 412.294
    Valid 4864 samples after epoch: 0049 lost = 6.733001 ppl = 839.663
    Epoch: 0050 Batch: 50 /134 lost = 6.055998 ppl = 426.665
    Epoch: 0050 Batch: 100 /134 lost = 6.016743 ppl = 410.24
    Valid 4864 samples after epoch: 0050 lost = 6.736467 ppl = 842.578
    Epoch: 0051 Batch: 50 /134 lost = 6.050992 ppl = 424.534
    Epoch: 0051 Batch: 100 /134 lost = 6.008807 ppl = 406.998
    Valid 4864 samples after epoch: 0051 lost = 6.746978 ppl = 851.481
    Epoch: 0052 Batch: 50 /134 lost = 6.045368 ppl = 422.153
    Epoch: 0052 Batch: 100 /134 lost = 6.000560 ppl = 403.655
    Valid 4864 samples after epoch: 0052 lost = 6.748886 ppl = 853.108
    Epoch: 0053 Batch: 50 /134 lost = 6.036588 ppl = 418.463
    Epoch: 0053 Batch: 100 /134 lost = 5.994015 ppl = 401.021
    Valid 4864 samples after epoch: 0053 lost = 6.757694 ppl = 860.655
    Epoch: 0054 Batch: 50 /134 lost = 6.028821 ppl = 415.225
    Epoch: 0054 Batch: 100 /134 lost = 5.987700 ppl = 398.497
    Valid 4864 samples after epoch: 0054 lost = 6.760675 ppl = 863.225
    Epoch: 0055 Batch: 50 /134 lost = 6.020538 ppl = 411.8
    Epoch: 0055 Batch: 100 /134 lost = 5.980500 ppl = 395.638
    Valid 4864 samples after epoch: 0055 lost = 6.769181 ppl = 870.599
    Epoch: 0056 Batch: 50 /134 lost = 6.012294 ppl = 408.419
    Epoch: 0056 Batch: 100 /134 lost = 5.975821 ppl = 393.791
    Valid 4864 samples after epoch: 0056 lost = 6.770467 ppl = 871.719
    Epoch: 0057 Batch: 50 /134 lost = 6.008038 ppl = 406.685
    Epoch: 0057 Batch: 100 /134 lost = 5.967462 ppl = 390.513
    Valid 4864 samples after epoch: 0057 lost = 6.778170 ppl = 878.46
    Epoch: 0058 Batch: 50 /134 lost = 6.002807 ppl = 404.563
    Epoch: 0058 Batch: 100 /134 lost = 5.962990 ppl = 388.771
    Valid 4864 samples after epoch: 0058 lost = 6.784364 ppl = 883.918
    Epoch: 0059 Batch: 50 /134 lost = 5.998594 ppl = 402.862
    Epoch: 0059 Batch: 100 /134 lost = 5.953142 ppl = 384.961
    Valid 4864 samples after epoch: 0059 lost = 6.789921 ppl = 888.844
    Epoch: 0060 Batch: 50 /134 lost = 5.991128 ppl = 399.866
    Epoch: 0060 Batch: 100 /134 lost = 5.949404 ppl = 383.525
    Valid 4864 samples after epoch: 0060 lost = 6.795963 ppl = 894.23
    Epoch: 0061 Batch: 50 /134 lost = 5.980258 ppl = 395.542
    Epoch: 0061 Batch: 100 /134 lost = 5.941097 ppl = 380.352
    Valid 4864 samples after epoch: 0061 lost = 6.800039 ppl = 897.883
    Epoch: 0062 Batch: 50 /134 lost = 5.978254 ppl = 394.751
    Epoch: 0062 Batch: 100 /134 lost = 5.938278 ppl = 379.281
    Valid 4864 samples after epoch: 0062 lost = 6.804246 ppl = 901.668
    Epoch: 0063 Batch: 50 /134 lost = 5.973398 ppl = 392.838
    Epoch: 0063 Batch: 100 /134 lost = 5.922536 ppl = 373.357
    Valid 4864 samples after epoch: 0063 lost = 6.808254 ppl = 905.289
    Epoch: 0064 Batch: 50 /134 lost = 5.967962 ppl = 390.709
    Epoch: 0064 Batch: 100 /134 lost = 5.921845 ppl = 373.1
    Valid 4864 samples after epoch: 0064 lost = 6.815591 ppl = 911.956
    Epoch: 0065 Batch: 50 /134 lost = 5.965543 ppl = 389.765
    Epoch: 0065 Batch: 100 /134 lost = 5.914569 ppl = 370.395
    Valid 4864 samples after epoch: 0065 lost = 6.820894 ppl = 916.804
    Epoch: 0066 Batch: 50 /134 lost = 5.957601 ppl = 386.681
    Epoch: 0066 Batch: 100 /134 lost = 5.907973 ppl = 367.96
    Valid 4864 samples after epoch: 0066 lost = 6.824235 ppl = 919.873
    Epoch: 0067 Batch: 50 /134 lost = 5.948102 ppl = 383.026
    Epoch: 0067 Batch: 100 /134 lost = 5.900126 ppl = 365.083
    Valid 4864 samples after epoch: 0067 lost = 6.829642 ppl = 924.86
    Epoch: 0068 Batch: 50 /134 lost = 5.944581 ppl = 381.679
    Epoch: 0068 Batch: 100 /134 lost = 5.899335 ppl = 364.795
    Valid 4864 samples after epoch: 0068 lost = 6.832528 ppl = 927.532
    Epoch: 0069 Batch: 50 /134 lost = 5.939349 ppl = 379.688
    Epoch: 0069 Batch: 100 /134 lost = 5.890335 ppl = 361.526
    Valid 4864 samples after epoch: 0069 lost = 6.838106 ppl = 932.72
    Epoch: 0070 Batch: 50 /134 lost = 5.935452 ppl = 378.211
    Epoch: 0070 Batch: 100 /134 lost = 5.888250 ppl = 360.774
    Valid 4864 samples after epoch: 0070 lost = 6.843349 ppl = 937.624
    Epoch: 0071 Batch: 50 /134 lost = 5.922200 ppl = 373.232
    Epoch: 0071 Batch: 100 /134 lost = 5.878932 ppl = 357.427
    Valid 4864 samples after epoch: 0071 lost = 6.848642 ppl = 942.6
    Epoch: 0072 Batch: 50 /134 lost = 5.918067 ppl = 371.693
    Epoch: 0072 Batch: 100 /134 lost = 5.873517 ppl = 355.497
    Valid 4864 samples after epoch: 0072 lost = 6.854134 ppl = 947.791
    Epoch: 0073 Batch: 50 /134 lost = 5.910017 ppl = 368.713
    Epoch: 0073 Batch: 100 /134 lost = 5.869276 ppl = 353.992
    Valid 4864 samples after epoch: 0073 lost = 6.857254 ppl = 950.753
    Epoch: 0074 Batch: 50 /134 lost = 5.906050 ppl = 367.253
    Epoch: 0074 Batch: 100 /134 lost = 5.862730 ppl = 351.683
    Valid 4864 samples after epoch: 0074 lost = 6.860202 ppl = 953.559
    Epoch: 0075 Batch: 50 /134 lost = 5.900100 ppl = 365.074
    Epoch: 0075 Batch: 100 /134 lost = 5.859453 ppl = 350.532
    Valid 4864 samples after epoch: 0075 lost = 6.869859 ppl = 962.813
    Epoch: 0076 Batch: 50 /134 lost = 5.895595 ppl = 363.433
    Epoch: 0076 Batch: 100 /134 lost = 5.853942 ppl = 348.606
    Valid 4864 samples after epoch: 0076 lost = 6.873887 ppl = 966.699
    Epoch: 0077 Batch: 50 /134 lost = 5.890073 ppl = 361.432
    Epoch: 0077 Batch: 100 /134 lost = 5.855825 ppl = 349.263
    Valid 4864 samples after epoch: 0077 lost = 6.876353 ppl = 969.086
    Epoch: 0078 Batch: 50 /134 lost = 5.882686 ppl = 358.771
    Epoch: 0078 Batch: 100 /134 lost = 5.846811 ppl = 346.129
    Valid 4864 samples after epoch: 0078 lost = 6.880183 ppl = 972.805
    Epoch: 0079 Batch: 50 /134 lost = 5.876832 ppl = 356.677
    Epoch: 0079 Batch: 100 /134 lost = 5.840065 ppl = 343.802
    Valid 4864 samples after epoch: 0079 lost = 6.883885 ppl = 976.412
    Epoch: 0080 Batch: 50 /134 lost = 5.874809 ppl = 355.957
    Epoch: 0080 Batch: 100 /134 lost = 5.829659 ppl = 340.243
    Valid 4864 samples after epoch: 0080 lost = 6.891226 ppl = 983.607
    Epoch: 0081 Batch: 50 /134 lost = 5.873862 ppl = 355.62
    Epoch: 0081 Batch: 100 /134 lost = 5.825591 ppl = 338.861
    Valid 4864 samples after epoch: 0081 lost = 6.894584 ppl = 986.915
    Epoch: 0082 Batch: 50 /134 lost = 5.866048 ppl = 352.852
    Epoch: 0082 Batch: 100 /134 lost = 5.827580 ppl = 339.536
    Valid 4864 samples after epoch: 0082 lost = 6.900525 ppl = 992.796
    Epoch: 0083 Batch: 50 /134 lost = 5.860430 ppl = 350.875
    Epoch: 0083 Batch: 100 /134 lost = 5.818378 ppl = 336.426
    Valid 4864 samples after epoch: 0083 lost = 6.904006 ppl = 996.258
    Epoch: 0084 Batch: 50 /134 lost = 5.855140 ppl = 349.024
    Epoch: 0084 Batch: 100 /134 lost = 5.811797 ppl = 334.219
    Valid 4864 samples after epoch: 0084 lost = 6.909894 ppl = 1002.14
    Epoch: 0085 Batch: 50 /134 lost = 5.844063 ppl = 345.179
    Epoch: 0085 Batch: 100 /134 lost = 5.809646 ppl = 333.501
    Valid 4864 samples after epoch: 0085 lost = 6.919653 ppl = 1011.97
    Epoch: 0086 Batch: 50 /134 lost = 5.842882 ppl = 344.772
    Epoch: 0086 Batch: 100 /134 lost = 5.807312 ppl = 332.723
    Valid 4864 samples after epoch: 0086 lost = 6.923649 ppl = 1016.02
    Epoch: 0087 Batch: 50 /134 lost = 5.841198 ppl = 344.191
    Epoch: 0087 Batch: 100 /134 lost = 5.796634 ppl = 329.19
    Valid 4864 samples after epoch: 0087 lost = 6.929449 ppl = 1021.93
    Epoch: 0088 Batch: 50 /134 lost = 5.833551 ppl = 341.57
    Epoch: 0088 Batch: 100 /134 lost = 5.791973 ppl = 327.659
    Valid 4864 samples after epoch: 0088 lost = 6.935359 ppl = 1027.99
    Epoch: 0089 Batch: 50 /134 lost = 5.825973 ppl = 338.991
    Epoch: 0089 Batch: 100 /134 lost = 5.786975 ppl = 326.025
    Valid 4864 samples after epoch: 0089 lost = 6.942251 ppl = 1035.1
    Epoch: 0090 Batch: 50 /134 lost = 5.827412 ppl = 339.479
    Epoch: 0090 Batch: 100 /134 lost = 5.790211 ppl = 327.082
    Valid 4864 samples after epoch: 0090 lost = 6.943796 ppl = 1036.7
    Epoch: 0091 Batch: 50 /134 lost = 5.817186 ppl = 336.025
    Epoch: 0091 Batch: 100 /134 lost = 5.781486 ppl = 324.241
    Valid 4864 samples after epoch: 0091 lost = 6.950301 ppl = 1043.46
    Epoch: 0092 Batch: 50 /134 lost = 5.817903 ppl = 336.266
    Epoch: 0092 Batch: 100 /134 lost = 5.771891 ppl = 321.144
    Valid 4864 samples after epoch: 0092 lost = 6.958308 ppl = 1051.85
    Epoch: 0093 Batch: 50 /134 lost = 5.814393 ppl = 335.088
    Epoch: 0093 Batch: 100 /134 lost = 5.770923 ppl = 320.834
    Valid 4864 samples after epoch: 0093 lost = 6.960107 ppl = 1053.75
    Epoch: 0094 Batch: 50 /134 lost = 5.809452 ppl = 333.436
    Epoch: 0094 Batch: 100 /134 lost = 5.767049 ppl = 319.593
    Valid 4864 samples after epoch: 0094 lost = 6.970469 ppl = 1064.72
    Epoch: 0095 Batch: 50 /134 lost = 5.800840 ppl = 330.577
    Epoch: 0095 Batch: 100 /134 lost = 5.757854 ppl = 316.668
    Valid 4864 samples after epoch: 0095 lost = 6.971169 ppl = 1065.47
    Epoch: 0096 Batch: 50 /134 lost = 5.800466 ppl = 330.454
    Epoch: 0096 Batch: 100 /134 lost = 5.753788 ppl = 315.383
    Valid 4864 samples after epoch: 0096 lost = 6.981478 ppl = 1076.51
    Epoch: 0097 Batch: 50 /134 lost = 5.799938 ppl = 330.279
    Epoch: 0097 Batch: 100 /134 lost = 5.753882 ppl = 315.413
    Valid 4864 samples after epoch: 0097 lost = 6.982801 ppl = 1077.93
    Epoch: 0098 Batch: 50 /134 lost = 5.794199 ppl = 328.389
    Epoch: 0098 Batch: 100 /134 lost = 5.747601 ppl = 313.438
    Valid 4864 samples after epoch: 0098 lost = 6.987233 ppl = 1082.72
    Epoch: 0099 Batch: 50 /134 lost = 5.791185 ppl = 327.401
    Epoch: 0099 Batch: 100 /134 lost = 5.741210 ppl = 311.441
    Valid 4864 samples after epoch: 0099 lost = 6.992417 ppl = 1088.35
    Epoch: 0100 Batch: 50 /134 lost = 5.785131 ppl = 325.425
    Epoch: 0100 Batch: 100 /134 lost = 5.739848 ppl = 311.017
    Valid 4864 samples after epoch: 0100 lost = 7.003383 ppl = 1100.35
    Epoch: 0101 Batch: 50 /134 lost = 5.786685 ppl = 325.931
    Epoch: 0101 Batch: 100 /134 lost = 5.737765 ppl = 310.37
    Valid 4864 samples after epoch: 0101 lost = 7.009472 ppl = 1107.07
    Epoch: 0102 Batch: 50 /134 lost = 5.778892 ppl = 323.401
    Epoch: 0102 Batch: 100 /134 lost = 5.733167 ppl = 308.946
    Valid 4864 samples after epoch: 0102 lost = 7.011467 ppl = 1109.28
    Epoch: 0103 Batch: 50 /134 lost = 5.776124 ppl = 322.507
    Epoch: 0103 Batch: 100 /134 lost = 5.724628 ppl = 306.319
    Valid 4864 samples after epoch: 0103 lost = 7.017255 ppl = 1115.72
    Epoch: 0104 Batch: 50 /134 lost = 5.772782 ppl = 321.431
    Epoch: 0104 Batch: 100 /134 lost = 5.722098 ppl = 305.545
    Valid 4864 samples after epoch: 0104 lost = 7.021956 ppl = 1120.98
    Epoch: 0105 Batch: 50 /134 lost = 5.768145 ppl = 319.944
    Epoch: 0105 Batch: 100 /134 lost = 5.717365 ppl = 304.102
    Valid 4864 samples after epoch: 0105 lost = 7.030971 ppl = 1131.13
    Epoch: 0106 Batch: 50 /134 lost = 5.767833 ppl = 319.844
    Epoch: 0106 Batch: 100 /134 lost = 5.709536 ppl = 301.731
    Valid 4864 samples after epoch: 0106 lost = 7.036843 ppl = 1137.79
    Epoch: 0107 Batch: 50 /134 lost = 5.762663 ppl = 318.195
    Epoch: 0107 Batch: 100 /134 lost = 5.710478 ppl = 302.015
    Valid 4864 samples after epoch: 0107 lost = 7.036608 ppl = 1137.52
    Epoch: 0108 Batch: 50 /134 lost = 5.760850 ppl = 317.618
    Epoch: 0108 Batch: 100 /134 lost = 5.706423 ppl = 300.793
    Valid 4864 samples after epoch: 0108 lost = 7.040821 ppl = 1142.32
    Epoch: 0109 Batch: 50 /134 lost = 5.757368 ppl = 316.514
    Epoch: 0109 Batch: 100 /134 lost = 5.704983 ppl = 300.36
    Valid 4864 samples after epoch: 0109 lost = 7.048205 ppl = 1150.79
    Epoch: 0110 Batch: 50 /134 lost = 5.757150 ppl = 316.445
    Epoch: 0110 Batch: 100 /134 lost = 5.702452 ppl = 299.601
    Valid 4864 samples after epoch: 0110 lost = 7.054577 ppl = 1158.15
    Epoch: 0111 Batch: 50 /134 lost = 5.752030 ppl = 314.829
    Epoch: 0111 Batch: 100 /134 lost = 5.695375 ppl = 297.488
    Valid 4864 samples after epoch: 0111 lost = 7.059098 ppl = 1163.4
    Epoch: 0112 Batch: 50 /134 lost = 5.751501 ppl = 314.662
    Epoch: 0112 Batch: 100 /134 lost = 5.698121 ppl = 298.306
    Valid 4864 samples after epoch: 0112 lost = 7.059406 ppl = 1163.75
    Epoch: 0113 Batch: 50 /134 lost = 5.744591 ppl = 312.496
    Epoch: 0113 Batch: 100 /134 lost = 5.689947 ppl = 295.878
    Valid 4864 samples after epoch: 0113 lost = 7.064178 ppl = 1169.32
    Epoch: 0114 Batch: 50 /134 lost = 5.747604 ppl = 313.439
    Epoch: 0114 Batch: 100 /134 lost = 5.687644 ppl = 295.197
    Valid 4864 samples after epoch: 0114 lost = 7.068507 ppl = 1174.39
    Epoch: 0115 Batch: 50 /134 lost = 5.741977 ppl = 311.68
    Epoch: 0115 Batch: 100 /134 lost = 5.686929 ppl = 294.986
    Valid 4864 samples after epoch: 0115 lost = 7.075041 ppl = 1182.09
    Epoch: 0116 Batch: 50 /134 lost = 5.746196 ppl = 312.998
    Epoch: 0116 Batch: 100 /134 lost = 5.680011 ppl = 292.953
    Valid 4864 samples after epoch: 0116 lost = 7.082690 ppl = 1191.17
    Epoch: 0117 Batch: 50 /134 lost = 5.737453 ppl = 310.273
    Epoch: 0117 Batch: 100 /134 lost = 5.678225 ppl = 292.43
    Valid 4864 samples after epoch: 0117 lost = 7.090964 ppl = 1201.06
    Epoch: 0118 Batch: 50 /134 lost = 5.734518 ppl = 309.364
    Epoch: 0118 Batch: 100 /134 lost = 5.674700 ppl = 291.401
    Valid 4864 samples after epoch: 0118 lost = 7.092929 ppl = 1203.43
    Epoch: 0119 Batch: 50 /134 lost = 5.729563 ppl = 307.835
    Epoch: 0119 Batch: 100 /134 lost = 5.671360 ppl = 290.429
    Valid 4864 samples after epoch: 0119 lost = 7.101116 ppl = 1213.32
    Epoch: 0120 Batch: 50 /134 lost = 5.721208 ppl = 305.273
    Epoch: 0120 Batch: 100 /134 lost = 5.672492 ppl = 290.758
    Valid 4864 samples after epoch: 0120 lost = 7.108118 ppl = 1221.85
    Epoch: 0121 Batch: 50 /134 lost = 5.717763 ppl = 304.224
    Epoch: 0121 Batch: 100 /134 lost = 5.673079 ppl = 290.929
    Valid 4864 samples after epoch: 0121 lost = 7.111236 ppl = 1225.66
    Epoch: 0122 Batch: 50 /134 lost = 5.716691 ppl = 303.898
    Epoch: 0122 Batch: 100 /134 lost = 5.664239 ppl = 288.369
    Valid 4864 samples after epoch: 0122 lost = 7.109023 ppl = 1222.95
    Epoch: 0123 Batch: 50 /134 lost = 5.712935 ppl = 302.758
    Epoch: 0123 Batch: 100 /134 lost = 5.660651 ppl = 287.336
    Valid 4864 samples after epoch: 0123 lost = 7.124112 ppl = 1241.55
    Epoch: 0124 Batch: 50 /134 lost = 5.716029 ppl = 303.697
    Epoch: 0124 Batch: 100 /134 lost = 5.657855 ppl = 286.533
    Valid 4864 samples after epoch: 0124 lost = 7.130538 ppl = 1249.55
    Epoch: 0125 Batch: 50 /134 lost = 5.712497 ppl = 302.626
    Epoch: 0125 Batch: 100 /134 lost = 5.655316 ppl = 285.807
    Valid 4864 samples after epoch: 0125 lost = 7.132316 ppl = 1251.77
    Epoch: 0126 Batch: 50 /134 lost = 5.709711 ppl = 301.784
    Epoch: 0126 Batch: 100 /134 lost = 5.655147 ppl = 285.759
    Valid 4864 samples after epoch: 0126 lost = 7.140103 ppl = 1261.56
    Epoch: 0127 Batch: 50 /134 lost = 5.704748 ppl = 300.29
    Epoch: 0127 Batch: 100 /134 lost = 5.651347 ppl = 284.675
    Valid 4864 samples after epoch: 0127 lost = 7.140717 ppl = 1262.33
    Epoch: 0128 Batch: 50 /134 lost = 5.705202 ppl = 300.426
    Epoch: 0128 Batch: 100 /134 lost = 5.660682 ppl = 287.345
    Valid 4864 samples after epoch: 0128 lost = 7.143952 ppl = 1266.42
    Epoch: 0129 Batch: 50 /134 lost = 5.696649 ppl = 297.867
    Epoch: 0129 Batch: 100 /134 lost = 5.647663 ppl = 283.628
    Valid 4864 samples after epoch: 0129 lost = 7.152030 ppl = 1276.7
    Epoch: 0130 Batch: 50 /134 lost = 5.695763 ppl = 297.604
    Epoch: 0130 Batch: 100 /134 lost = 5.646184 ppl = 283.209
    Valid 4864 samples after epoch: 0130 lost = 7.162165 ppl = 1289.7
    Epoch: 0131 Batch: 50 /134 lost = 5.699146 ppl = 298.612
    Epoch: 0131 Batch: 100 /134 lost = 5.640760 ppl = 281.677
    Valid 4864 samples after epoch: 0131 lost = 7.165497 ppl = 1294.0
    Epoch: 0132 Batch: 50 /134 lost = 5.690875 ppl = 296.153
    Epoch: 0132 Batch: 100 /134 lost = 5.639246 ppl = 281.25
    Valid 4864 samples after epoch: 0132 lost = 7.175355 ppl = 1306.82
    Epoch: 0133 Batch: 50 /134 lost = 5.688667 ppl = 295.499
    Epoch: 0133 Batch: 100 /134 lost = 5.647006 ppl = 283.442
    Valid 4864 samples after epoch: 0133 lost = 7.175568 ppl = 1307.1
    Epoch: 0134 Batch: 50 /134 lost = 5.690348 ppl = 295.997
    Epoch: 0134 Batch: 100 /134 lost = 5.641113 ppl = 281.776
    Valid 4864 samples after epoch: 0134 lost = 7.179159 ppl = 1311.8
    Epoch: 0135 Batch: 50 /134 lost = 5.694489 ppl = 297.225
    Epoch: 0135 Batch: 100 /134 lost = 5.634395 ppl = 279.889
    Valid 4864 samples after epoch: 0135 lost = 7.184093 ppl = 1318.29
    Epoch: 0136 Batch: 50 /134 lost = 5.683077 ppl = 293.852
    Epoch: 0136 Batch: 100 /134 lost = 5.630317 ppl = 278.75
    Valid 4864 samples after epoch: 0136 lost = 7.186093 ppl = 1320.93
    Epoch: 0137 Batch: 50 /134 lost = 5.682961 ppl = 293.818
    Epoch: 0137 Batch: 100 /134 lost = 5.628717 ppl = 278.305
    Valid 4864 samples after epoch: 0137 lost = 7.194290 ppl = 1331.8
    Epoch: 0138 Batch: 50 /134 lost = 5.675701 ppl = 291.693
    Epoch: 0138 Batch: 100 /134 lost = 5.625797 ppl = 277.493
    Valid 4864 samples after epoch: 0138 lost = 7.199093 ppl = 1338.22
    Epoch: 0139 Batch: 50 /134 lost = 5.669159 ppl = 289.791
    Epoch: 0139 Batch: 100 /134 lost = 5.630525 ppl = 278.808
    Valid 4864 samples after epoch: 0139 lost = 7.205823 ppl = 1347.25
    Epoch: 0140 Batch: 50 /134 lost = 5.672861 ppl = 290.866
    Epoch: 0140 Batch: 100 /134 lost = 5.623347 ppl = 276.814
    Valid 4864 samples after epoch: 0140 lost = 7.209855 ppl = 1352.7
    Epoch: 0141 Batch: 50 /134 lost = 5.674913 ppl = 291.463
    Epoch: 0141 Batch: 100 /134 lost = 5.621044 ppl = 276.178
    Valid 4864 samples after epoch: 0141 lost = 7.213264 ppl = 1357.31
    Epoch: 0142 Batch: 50 /134 lost = 5.675284 ppl = 291.571
    Epoch: 0142 Batch: 100 /134 lost = 5.609426 ppl = 272.988
    Valid 4864 samples after epoch: 0142 lost = 7.225112 ppl = 1373.49
    Epoch: 0143 Batch: 50 /134 lost = 5.665596 ppl = 288.76
    Epoch: 0143 Batch: 100 /134 lost = 5.606678 ppl = 272.238
    Valid 4864 samples after epoch: 0143 lost = 7.224705 ppl = 1372.93
    Epoch: 0144 Batch: 50 /134 lost = 5.660563 ppl = 287.31
    Epoch: 0144 Batch: 100 /134 lost = 5.609206 ppl = 272.928
    Valid 4864 samples after epoch: 0144 lost = 7.228818 ppl = 1378.59
    Epoch: 0145 Batch: 50 /134 lost = 5.663972 ppl = 288.291
    Epoch: 0145 Batch: 100 /134 lost = 5.604317 ppl = 271.596
    Valid 4864 samples after epoch: 0145 lost = 7.227435 ppl = 1376.69
    Epoch: 0146 Batch: 50 /134 lost = 5.658449 ppl = 286.704
    Epoch: 0146 Batch: 100 /134 lost = 5.613780 ppl = 274.179
    Valid 4864 samples after epoch: 0146 lost = 7.241026 ppl = 1395.52
    Epoch: 0147 Batch: 50 /134 lost = 5.656664 ppl = 286.192
    Epoch: 0147 Batch: 100 /134 lost = 5.599820 ppl = 270.378
    Valid 4864 samples after epoch: 0147 lost = 7.237278 ppl = 1390.3
    Epoch: 0148 Batch: 50 /134 lost = 5.652810 ppl = 285.091
    Epoch: 0148 Batch: 100 /134 lost = 5.600311 ppl = 270.51
    Valid 4864 samples after epoch: 0148 lost = 7.246642 ppl = 1403.38
    Epoch: 0149 Batch: 50 /134 lost = 5.652218 ppl = 284.923
    Epoch: 0149 Batch: 100 /134 lost = 5.597011 ppl = 269.619
    Valid 4864 samples after epoch: 0149 lost = 7.252052 ppl = 1411.0
    Epoch: 0150 Batch: 50 /134 lost = 5.652214 ppl = 284.921
    Epoch: 0150 Batch: 100 /134 lost = 5.599418 ppl = 270.269
    Valid 4864 samples after epoch: 0150 lost = 7.261268 ppl = 1424.06
    
    Test the LSTMLM……………………
    Test 5760 samples with models/(pytorch_api)2_layers_lstmlm_model_best.ckpt……………………
    lost = 6.584678 ppl = 723.918
    
