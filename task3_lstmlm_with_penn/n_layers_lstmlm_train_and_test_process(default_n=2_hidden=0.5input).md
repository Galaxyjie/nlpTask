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
    Epoch: 0001 Batch: 50 /134 lost = 8.241237 ppl = 3794.23
    Epoch: 0001 Batch: 100 /134 lost = 7.696887 ppl = 2201.48
    Valid 4864 samples after epoch: 0001 lost = 7.415844 ppl = 1662.11
    Epoch: 0002 Batch: 50 /134 lost = 6.973639 ppl = 1068.1
    Epoch: 0002 Batch: 100 /134 lost = 6.751297 ppl = 855.167
    Valid 4864 samples after epoch: 0002 lost = 6.762103 ppl = 864.458
    Epoch: 0003 Batch: 50 /134 lost = 6.517264 ppl = 676.724
    Epoch: 0003 Batch: 100 /134 lost = 6.475709 ppl = 649.179
    Valid 4864 samples after epoch: 0003 lost = 6.637639 ppl = 763.291
    Epoch: 0004 Batch: 50 /134 lost = 6.444422 ppl = 629.183
    Epoch: 0004 Batch: 100 /134 lost = 6.435386 ppl = 623.523
    Valid 4864 samples after epoch: 0004 lost = 6.629305 ppl = 756.956
    Epoch: 0005 Batch: 50 /134 lost = 6.429625 ppl = 619.941
    Epoch: 0005 Batch: 100 /134 lost = 6.420051 ppl = 614.034
    Valid 4864 samples after epoch: 0005 lost = 6.628858 ppl = 756.617
    Epoch: 0006 Batch: 50 /134 lost = 6.419792 ppl = 613.876
    Epoch: 0006 Batch: 100 /134 lost = 6.407299 ppl = 606.254
    Valid 4864 samples after epoch: 0006 lost = 6.628469 ppl = 756.324
    Epoch: 0007 Batch: 50 /134 lost = 6.409880 ppl = 607.821
    Epoch: 0007 Batch: 100 /134 lost = 6.394029 ppl = 598.262
    Valid 4864 samples after epoch: 0007 lost = 6.626406 ppl = 754.765
    Epoch: 0008 Batch: 50 /134 lost = 6.398593 ppl = 600.999
    Epoch: 0008 Batch: 100 /134 lost = 6.378943 ppl = 589.305
    Valid 4864 samples after epoch: 0008 lost = 6.621994 ppl = 751.442
    Epoch: 0009 Batch: 50 /134 lost = 6.385380 ppl = 593.11
    Epoch: 0009 Batch: 100 /134 lost = 6.361441 ppl = 579.08
    Valid 4864 samples after epoch: 0009 lost = 6.615063 ppl = 746.252
    Epoch: 0010 Batch: 50 /134 lost = 6.370050 ppl = 584.087
    Epoch: 0010 Batch: 100 /134 lost = 6.341304 ppl = 567.536
    Valid 4864 samples after epoch: 0010 lost = 6.605698 ppl = 739.296
    Epoch: 0011 Batch: 50 /134 lost = 6.352631 ppl = 574.001
    Epoch: 0011 Batch: 100 /134 lost = 6.318581 ppl = 554.785
    Valid 4864 samples after epoch: 0011 lost = 6.594121 ppl = 730.786
    Epoch: 0012 Batch: 50 /134 lost = 6.333390 ppl = 563.062
    Epoch: 0012 Batch: 100 /134 lost = 6.293688 ppl = 541.145
    Valid 4864 samples after epoch: 0012 lost = 6.580808 ppl = 721.122
    Epoch: 0013 Batch: 50 /134 lost = 6.312919 ppl = 551.653
    Epoch: 0013 Batch: 100 /134 lost = 6.267619 ppl = 527.22
    Valid 4864 samples after epoch: 0013 lost = 6.566656 ppl = 710.988
    Epoch: 0014 Batch: 50 /134 lost = 6.292006 ppl = 540.236
    Epoch: 0014 Batch: 100 /134 lost = 6.241504 ppl = 513.631
    Valid 4864 samples after epoch: 0014 lost = 6.552479 ppl = 700.98
    Epoch: 0015 Batch: 50 /134 lost = 6.271137 ppl = 529.078
    Epoch: 0015 Batch: 100 /134 lost = 6.215786 ppl = 500.589
    Valid 4864 samples after epoch: 0015 lost = 6.538560 ppl = 691.291
    Epoch: 0016 Batch: 50 /134 lost = 6.250528 ppl = 518.286
    Epoch: 0016 Batch: 100 /134 lost = 6.190649 ppl = 488.163
    Valid 4864 samples after epoch: 0016 lost = 6.525058 ppl = 682.019
    Epoch: 0017 Batch: 50 /134 lost = 6.230322 ppl = 507.919
    Epoch: 0017 Batch: 100 /134 lost = 6.166191 ppl = 476.368
    Valid 4864 samples after epoch: 0017 lost = 6.512049 ppl = 673.204
    Epoch: 0018 Batch: 50 /134 lost = 6.210588 ppl = 497.994
    Epoch: 0018 Batch: 100 /134 lost = 6.142431 ppl = 465.183
    Valid 4864 samples after epoch: 0018 lost = 6.499544 ppl = 664.839
    Epoch: 0019 Batch: 50 /134 lost = 6.191368 ppl = 488.514
    Epoch: 0019 Batch: 100 /134 lost = 6.119351 ppl = 454.57
    Valid 4864 samples after epoch: 0019 lost = 6.487535 ppl = 656.902
    Epoch: 0020 Batch: 50 /134 lost = 6.172689 ppl = 479.474
    Epoch: 0020 Batch: 100 /134 lost = 6.096997 ppl = 444.521
    Valid 4864 samples after epoch: 0020 lost = 6.476104 ppl = 649.436
    Epoch: 0021 Batch: 50 /134 lost = 6.154562 ppl = 470.86
    Epoch: 0021 Batch: 100 /134 lost = 6.075472 ppl = 435.055
    Valid 4864 samples after epoch: 0021 lost = 6.465354 ppl = 642.492
    Epoch: 0022 Batch: 50 /134 lost = 6.136954 ppl = 462.642
    Epoch: 0022 Batch: 100 /134 lost = 6.054743 ppl = 426.129
    Valid 4864 samples after epoch: 0022 lost = 6.455221 ppl = 636.015
    Epoch: 0023 Batch: 50 /134 lost = 6.119813 ppl = 454.78
    Epoch: 0023 Batch: 100 /134 lost = 6.034731 ppl = 417.687
    Valid 4864 samples after epoch: 0023 lost = 6.445626 ppl = 629.941
    Epoch: 0024 Batch: 50 /134 lost = 6.103098 ppl = 447.241
    Epoch: 0024 Batch: 100 /134 lost = 6.015369 ppl = 409.677
    Valid 4864 samples after epoch: 0024 lost = 6.436504 ppl = 624.221
    Epoch: 0025 Batch: 50 /134 lost = 6.086771 ppl = 439.999
    Epoch: 0025 Batch: 100 /134 lost = 5.996596 ppl = 402.058
    Valid 4864 samples after epoch: 0025 lost = 6.427799 ppl = 618.811
    Epoch: 0026 Batch: 50 /134 lost = 6.070816 ppl = 433.034
    Epoch: 0026 Batch: 100 /134 lost = 5.978359 ppl = 394.792
    Valid 4864 samples after epoch: 0026 lost = 6.419467 ppl = 613.676
    Epoch: 0027 Batch: 50 /134 lost = 6.055213 ppl = 426.33
    Epoch: 0027 Batch: 100 /134 lost = 5.960609 ppl = 387.846
    Valid 4864 samples after epoch: 0027 lost = 6.411474 ppl = 608.791
    Epoch: 0028 Batch: 50 /134 lost = 6.039959 ppl = 419.876
    Epoch: 0028 Batch: 100 /134 lost = 5.943308 ppl = 381.194
    Valid 4864 samples after epoch: 0028 lost = 6.403802 ppl = 604.137
    Epoch: 0029 Batch: 50 /134 lost = 6.025054 ppl = 413.664
    Epoch: 0029 Batch: 100 /134 lost = 5.926431 ppl = 374.814
    Valid 4864 samples after epoch: 0029 lost = 6.396445 ppl = 599.709
    Epoch: 0030 Batch: 50 /134 lost = 6.010508 ppl = 407.69
    Epoch: 0030 Batch: 100 /134 lost = 5.909985 ppl = 368.701
    Valid 4864 samples after epoch: 0030 lost = 6.389418 ppl = 595.51
    Epoch: 0031 Batch: 50 /134 lost = 5.996318 ppl = 401.946
    Epoch: 0031 Batch: 100 /134 lost = 5.893981 ppl = 362.847
    Valid 4864 samples after epoch: 0031 lost = 6.382719 ppl = 591.534
    Epoch: 0032 Batch: 50 /134 lost = 5.982457 ppl = 396.413
    Epoch: 0032 Batch: 100 /134 lost = 5.878392 ppl = 357.234
    Valid 4864 samples after epoch: 0032 lost = 6.376324 ppl = 587.763
    Epoch: 0033 Batch: 50 /134 lost = 5.968883 ppl = 391.068
    Epoch: 0033 Batch: 100 /134 lost = 5.863173 ppl = 351.839
    Valid 4864 samples after epoch: 0033 lost = 6.370202 ppl = 584.176
    Epoch: 0034 Batch: 50 /134 lost = 5.955569 ppl = 385.896
    Epoch: 0034 Batch: 100 /134 lost = 5.848288 ppl = 346.64
    Valid 4864 samples after epoch: 0034 lost = 6.364334 ppl = 580.758
    Epoch: 0035 Batch: 50 /134 lost = 5.942502 ppl = 380.887
    Epoch: 0035 Batch: 100 /134 lost = 5.833708 ppl = 341.623
    Valid 4864 samples after epoch: 0035 lost = 6.358701 ppl = 577.495
    Epoch: 0036 Batch: 50 /134 lost = 5.929664 ppl = 376.028
    Epoch: 0036 Batch: 100 /134 lost = 5.819414 ppl = 336.775
    Valid 4864 samples after epoch: 0036 lost = 6.353289 ppl = 574.379
    Epoch: 0037 Batch: 50 /134 lost = 5.917051 ppl = 371.315
    Epoch: 0037 Batch: 100 /134 lost = 5.805384 ppl = 332.083
    Valid 4864 samples after epoch: 0037 lost = 6.348091 ppl = 571.401
    Epoch: 0038 Batch: 50 /134 lost = 5.904649 ppl = 366.738
    Epoch: 0038 Batch: 100 /134 lost = 5.791610 ppl = 327.54
    Valid 4864 samples after epoch: 0038 lost = 6.343100 ppl = 568.556
    Epoch: 0039 Batch: 50 /134 lost = 5.892448 ppl = 362.291
    Epoch: 0039 Batch: 100 /134 lost = 5.778078 ppl = 323.138
    Valid 4864 samples after epoch: 0039 lost = 6.338310 ppl = 565.839
    Epoch: 0040 Batch: 50 /134 lost = 5.880442 ppl = 357.967
    Epoch: 0040 Batch: 100 /134 lost = 5.764780 ppl = 318.869
    Valid 4864 samples after epoch: 0040 lost = 6.333718 ppl = 563.247
    Epoch: 0041 Batch: 50 /134 lost = 5.868627 ppl = 353.763
    Epoch: 0041 Batch: 100 /134 lost = 5.751704 ppl = 314.727
    Valid 4864 samples after epoch: 0041 lost = 6.329319 ppl = 560.774
    Epoch: 0042 Batch: 50 /134 lost = 5.856991 ppl = 349.67
    Epoch: 0042 Batch: 100 /134 lost = 5.738840 ppl = 310.704
    Valid 4864 samples after epoch: 0042 lost = 6.325109 ppl = 558.418
    Epoch: 0043 Batch: 50 /134 lost = 5.845535 ppl = 345.688
    Epoch: 0043 Batch: 100 /134 lost = 5.726181 ppl = 306.795
    Valid 4864 samples after epoch: 0043 lost = 6.321083 ppl = 556.175
    Epoch: 0044 Batch: 50 /134 lost = 5.834252 ppl = 341.809
    Epoch: 0044 Batch: 100 /134 lost = 5.713706 ppl = 302.992
    Valid 4864 samples after epoch: 0044 lost = 6.317237 ppl = 554.04
    Epoch: 0045 Batch: 50 /134 lost = 5.823136 ppl = 338.031
    Epoch: 0045 Batch: 100 /134 lost = 5.701414 ppl = 299.29
    Valid 4864 samples after epoch: 0045 lost = 6.313567 ppl = 552.01
    Epoch: 0046 Batch: 50 /134 lost = 5.812184 ppl = 334.349
    Epoch: 0046 Batch: 100 /134 lost = 5.689296 ppl = 295.685
    Valid 4864 samples after epoch: 0046 lost = 6.310069 ppl = 550.083
    Epoch: 0047 Batch: 50 /134 lost = 5.801393 ppl = 330.76
    Epoch: 0047 Batch: 100 /134 lost = 5.677353 ppl = 292.175
    Valid 4864 samples after epoch: 0047 lost = 6.306742 ppl = 548.256
    Epoch: 0048 Batch: 50 /134 lost = 5.790756 ppl = 327.26
    Epoch: 0048 Batch: 100 /134 lost = 5.665590 ppl = 288.758
    Valid 4864 samples after epoch: 0048 lost = 6.303580 ppl = 546.525
    Epoch: 0049 Batch: 50 /134 lost = 5.780274 ppl = 323.848
    Epoch: 0049 Batch: 100 /134 lost = 5.654015 ppl = 285.435
    Valid 4864 samples after epoch: 0049 lost = 6.300572 ppl = 544.884
    Epoch: 0050 Batch: 50 /134 lost = 5.769941 ppl = 320.519
    Epoch: 0050 Batch: 100 /134 lost = 5.642629 ppl = 282.204
    Valid 4864 samples after epoch: 0050 lost = 6.297711 ppl = 543.327
    Epoch: 0051 Batch: 50 /134 lost = 5.759752 ppl = 317.27
    Epoch: 0051 Batch: 100 /134 lost = 5.631433 ppl = 279.062
    Valid 4864 samples after epoch: 0051 lost = 6.294993 ppl = 541.852
    Epoch: 0052 Batch: 50 /134 lost = 5.749708 ppl = 314.099
    Epoch: 0052 Batch: 100 /134 lost = 5.620421 ppl = 276.006
    Valid 4864 samples after epoch: 0052 lost = 6.292420 ppl = 540.46
    Epoch: 0053 Batch: 50 /134 lost = 5.739810 ppl = 311.005
    Epoch: 0053 Batch: 100 /134 lost = 5.609592 ppl = 273.033
    Valid 4864 samples after epoch: 0053 lost = 6.289992 ppl = 539.149
    Epoch: 0054 Batch: 50 /134 lost = 5.730055 ppl = 307.986
    Epoch: 0054 Batch: 100 /134 lost = 5.598940 ppl = 270.14
    Valid 4864 samples after epoch: 0054 lost = 6.287705 ppl = 537.917
    Epoch: 0055 Batch: 50 /134 lost = 5.720437 ppl = 305.038
    Epoch: 0055 Batch: 100 /134 lost = 5.588458 ppl = 267.323
    Valid 4864 samples after epoch: 0055 lost = 6.285557 ppl = 536.763
    Epoch: 0056 Batch: 50 /134 lost = 5.710951 ppl = 302.158
    Epoch: 0056 Batch: 100 /134 lost = 5.578142 ppl = 264.579
    Valid 4864 samples after epoch: 0056 lost = 6.283541 ppl = 535.682
    Epoch: 0057 Batch: 50 /134 lost = 5.701593 ppl = 299.344
    Epoch: 0057 Batch: 100 /134 lost = 5.567984 ppl = 261.906
    Valid 4864 samples after epoch: 0057 lost = 6.281655 ppl = 534.673
    Epoch: 0058 Batch: 50 /134 lost = 5.692357 ppl = 296.592
    Epoch: 0058 Batch: 100 /134 lost = 5.557981 ppl = 259.299
    Valid 4864 samples after epoch: 0058 lost = 6.279893 ppl = 533.732
    Epoch: 0059 Batch: 50 /134 lost = 5.683241 ppl = 293.901
    Epoch: 0059 Batch: 100 /134 lost = 5.548131 ppl = 256.757
    Valid 4864 samples after epoch: 0059 lost = 6.278252 ppl = 532.856
    Epoch: 0060 Batch: 50 /134 lost = 5.674242 ppl = 291.268
    Epoch: 0060 Batch: 100 /134 lost = 5.538428 ppl = 254.278
    Valid 4864 samples after epoch: 0060 lost = 6.276727 ppl = 532.044
    Epoch: 0061 Batch: 50 /134 lost = 5.665356 ppl = 288.691
    Epoch: 0061 Batch: 100 /134 lost = 5.528869 ppl = 251.859
    Valid 4864 samples after epoch: 0061 lost = 6.275313 ppl = 531.293
    Epoch: 0062 Batch: 50 /134 lost = 5.656579 ppl = 286.168
    Epoch: 0062 Batch: 100 /134 lost = 5.519451 ppl = 249.498
    Valid 4864 samples after epoch: 0062 lost = 6.274007 ppl = 530.599
    Epoch: 0063 Batch: 50 /134 lost = 5.647911 ppl = 283.698
    Epoch: 0063 Batch: 100 /134 lost = 5.510169 ppl = 247.193
    Valid 4864 samples after epoch: 0063 lost = 6.272805 ppl = 529.962
    Epoch: 0064 Batch: 50 /134 lost = 5.639346 ppl = 281.279
    Epoch: 0064 Batch: 100 /134 lost = 5.501020 ppl = 244.942
    Valid 4864 samples after epoch: 0064 lost = 6.271702 ppl = 529.378
    Epoch: 0065 Batch: 50 /134 lost = 5.630882 ppl = 278.908
    Epoch: 0065 Batch: 100 /134 lost = 5.492000 ppl = 242.742
    Valid 4864 samples after epoch: 0065 lost = 6.270694 ppl = 528.844
    Epoch: 0066 Batch: 50 /134 lost = 5.622518 ppl = 276.585
    Epoch: 0066 Batch: 100 /134 lost = 5.483105 ppl = 240.593
    Valid 4864 samples after epoch: 0066 lost = 6.269778 ppl = 528.36
    Epoch: 0067 Batch: 50 /134 lost = 5.614248 ppl = 274.307
    Epoch: 0067 Batch: 100 /134 lost = 5.474330 ppl = 238.491
    Valid 4864 samples after epoch: 0067 lost = 6.268949 ppl = 527.922
    Epoch: 0068 Batch: 50 /134 lost = 5.606072 ppl = 272.074
    Epoch: 0068 Batch: 100 /134 lost = 5.465673 ppl = 236.435
    Valid 4864 samples after epoch: 0068 lost = 6.268204 ppl = 527.529
    Epoch: 0069 Batch: 50 /134 lost = 5.597985 ppl = 269.882
    Epoch: 0069 Batch: 100 /134 lost = 5.457128 ppl = 234.423
    Valid 4864 samples after epoch: 0069 lost = 6.267537 ppl = 527.177
    Epoch: 0070 Batch: 50 /134 lost = 5.589986 ppl = 267.732
    Epoch: 0070 Batch: 100 /134 lost = 5.448691 ppl = 232.454
    Valid 4864 samples after epoch: 0070 lost = 6.266945 ppl = 526.865
    Epoch: 0071 Batch: 50 /134 lost = 5.582070 ppl = 265.621
    Epoch: 0071 Batch: 100 /134 lost = 5.440361 ppl = 230.525
    Valid 4864 samples after epoch: 0071 lost = 6.266424 ppl = 526.591
    Epoch: 0072 Batch: 50 /134 lost = 5.574235 ppl = 263.548
    Epoch: 0072 Batch: 100 /134 lost = 5.432131 ppl = 228.636
    Valid 4864 samples after epoch: 0072 lost = 6.265972 ppl = 526.353
    Epoch: 0073 Batch: 50 /134 lost = 5.566481 ppl = 261.512
    Epoch: 0073 Batch: 100 /134 lost = 5.423998 ppl = 226.784
    Valid 4864 samples after epoch: 0073 lost = 6.265583 ppl = 526.148
    Epoch: 0074 Batch: 50 /134 lost = 5.558804 ppl = 259.512
    Epoch: 0074 Batch: 100 /134 lost = 5.415961 ppl = 224.969
    Valid 4864 samples after epoch: 0074 lost = 6.265255 ppl = 525.976
    Epoch: 0075 Batch: 50 /134 lost = 5.551200 ppl = 257.546
    Epoch: 0075 Batch: 100 /134 lost = 5.408013 ppl = 223.188
    Valid 4864 samples after epoch: 0075 lost = 6.264983 ppl = 525.833
    Epoch: 0076 Batch: 50 /134 lost = 5.543670 ppl = 255.614
    Epoch: 0076 Batch: 100 /134 lost = 5.400154 ppl = 221.441
    Valid 4864 samples after epoch: 0076 lost = 6.264765 ppl = 525.718
    Epoch: 0077 Batch: 50 /134 lost = 5.536210 ppl = 253.714
    Epoch: 0077 Batch: 100 /134 lost = 5.392378 ppl = 219.725
    Valid 4864 samples after epoch: 0077 lost = 6.264601 ppl = 525.632
    Epoch: 0078 Batch: 50 /134 lost = 5.528817 ppl = 251.846
    Epoch: 0078 Batch: 100 /134 lost = 5.384684 ppl = 218.041
    Valid 4864 samples after epoch: 0078 lost = 6.264492 ppl = 525.575
    Epoch: 0079 Batch: 50 /134 lost = 5.521490 ppl = 250.007
    Epoch: 0079 Batch: 100 /134 lost = 5.377064 ppl = 216.386
    Valid 4864 samples after epoch: 0079 lost = 6.264439 ppl = 525.547
    Epoch: 0080 Batch: 50 /134 lost = 5.514225 ppl = 248.198
    Epoch: 0080 Batch: 100 /134 lost = 5.369520 ppl = 214.76
    Valid 4864 samples after epoch: 0080 lost = 6.264442 ppl = 525.548
    Epoch: 0081 Batch: 50 /134 lost = 5.507021 ppl = 246.416
    Epoch: 0081 Batch: 100 /134 lost = 5.362045 ppl = 213.16
    Valid 4864 samples after epoch: 0081 lost = 6.264496 ppl = 525.577
    Epoch: 0082 Batch: 50 /134 lost = 5.499877 ppl = 244.662
    Epoch: 0082 Batch: 100 /134 lost = 5.354641 ppl = 211.588
    Valid 4864 samples after epoch: 0082 lost = 6.264600 ppl = 525.631
    Epoch: 0083 Batch: 50 /134 lost = 5.492792 ppl = 242.935
    Epoch: 0083 Batch: 100 /134 lost = 5.347305 ppl = 210.041
    Valid 4864 samples after epoch: 0083 lost = 6.264749 ppl = 525.71
    Epoch: 0084 Batch: 50 /134 lost = 5.485765 ppl = 241.233
    Epoch: 0084 Batch: 100 /134 lost = 5.340036 ppl = 208.52
    Valid 4864 samples after epoch: 0084 lost = 6.264943 ppl = 525.812
    Epoch: 0085 Batch: 50 /134 lost = 5.478791 ppl = 239.557
    Epoch: 0085 Batch: 100 /134 lost = 5.332832 ppl = 207.024
    Valid 4864 samples after epoch: 0085 lost = 6.265178 ppl = 525.935
    Epoch: 0086 Batch: 50 /134 lost = 5.471872 ppl = 237.905
    Epoch: 0086 Batch: 100 /134 lost = 5.325692 ppl = 205.551
    Valid 4864 samples after epoch: 0086 lost = 6.265453 ppl = 526.08
    Epoch: 0087 Batch: 50 /134 lost = 5.465005 ppl = 236.277
    Epoch: 0087 Batch: 100 /134 lost = 5.318614 ppl = 204.101
    Valid 4864 samples after epoch: 0087 lost = 6.265765 ppl = 526.244
    Epoch: 0088 Batch: 50 /134 lost = 5.458185 ppl = 234.671
    Epoch: 0088 Batch: 100 /134 lost = 5.311596 ppl = 202.674
    Valid 4864 samples after epoch: 0088 lost = 6.266113 ppl = 526.427
    Epoch: 0089 Batch: 50 /134 lost = 5.451412 ppl = 233.087
    Epoch: 0089 Batch: 100 /134 lost = 5.304634 ppl = 201.267
    Valid 4864 samples after epoch: 0089 lost = 6.266494 ppl = 526.628
    Epoch: 0090 Batch: 50 /134 lost = 5.444685 ppl = 231.524
    Epoch: 0090 Batch: 100 /134 lost = 5.297728 ppl = 199.882
    Valid 4864 samples after epoch: 0090 lost = 6.266909 ppl = 526.846
    Epoch: 0091 Batch: 50 /134 lost = 5.438001 ppl = 229.982
    Epoch: 0091 Batch: 100 /134 lost = 5.290879 ppl = 198.518
    Valid 4864 samples after epoch: 0091 lost = 6.267353 ppl = 527.08
    Epoch: 0092 Batch: 50 /134 lost = 5.431361 ppl = 228.46
    Epoch: 0092 Batch: 100 /134 lost = 5.284087 ppl = 197.174
    Valid 4864 samples after epoch: 0092 lost = 6.267825 ppl = 527.329
    Epoch: 0093 Batch: 50 /134 lost = 5.424762 ppl = 226.957
    Epoch: 0093 Batch: 100 /134 lost = 5.277352 ppl = 195.851
    Valid 4864 samples after epoch: 0093 lost = 6.268322 ppl = 527.592
    Epoch: 0094 Batch: 50 /134 lost = 5.418208 ppl = 225.475
    Epoch: 0094 Batch: 100 /134 lost = 5.270676 ppl = 194.547
    Valid 4864 samples after epoch: 0094 lost = 6.268843 ppl = 527.866
    Epoch: 0095 Batch: 50 /134 lost = 5.411697 ppl = 224.011
    Epoch: 0095 Batch: 100 /134 lost = 5.264056 ppl = 193.264
    Valid 4864 samples after epoch: 0095 lost = 6.269384 ppl = 528.152
    Epoch: 0096 Batch: 50 /134 lost = 5.405230 ppl = 222.567
    Epoch: 0096 Batch: 100 /134 lost = 5.257490 ppl = 191.999
    Valid 4864 samples after epoch: 0096 lost = 6.269945 ppl = 528.448
    Epoch: 0097 Batch: 50 /134 lost = 5.398806 ppl = 221.142
    Epoch: 0097 Batch: 100 /134 lost = 5.250980 ppl = 190.753
    Valid 4864 samples after epoch: 0097 lost = 6.270522 ppl = 528.753
    Epoch: 0098 Batch: 50 /134 lost = 5.392427 ppl = 219.736
    Epoch: 0098 Batch: 100 /134 lost = 5.244524 ppl = 189.525
    Valid 4864 samples after epoch: 0098 lost = 6.271114 ppl = 529.067
    Epoch: 0099 Batch: 50 /134 lost = 5.386089 ppl = 218.348
    Epoch: 0099 Batch: 100 /134 lost = 5.238122 ppl = 188.316
    Valid 4864 samples after epoch: 0099 lost = 6.271719 ppl = 529.387
    Epoch: 0100 Batch: 50 /134 lost = 5.379796 ppl = 216.978
    Epoch: 0100 Batch: 100 /134 lost = 5.231771 ppl = 187.124
    Valid 4864 samples after epoch: 0100 lost = 6.272336 ppl = 529.714
    
    Test the LSTMLM……………………
    Test 5760 samples with models/2_layers_lstmlm_model_(hidden=0.5input)_epoch100.ckpt……………………
    lost = 6.170979 ppl = 478.655
    
