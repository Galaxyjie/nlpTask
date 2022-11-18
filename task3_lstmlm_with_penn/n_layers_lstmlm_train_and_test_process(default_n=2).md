```python
!python n_layers_lstmlm_with_penn_assignment(default_n=2).py
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
    Epoch: 0001 Batch: 50 /134 lost = 8.247692 ppl = 3818.8
    Epoch: 0001 Batch: 100 /134 lost = 7.712950 ppl = 2237.13
    Valid 4864 samples after epoch: 0001 lost = 7.394124 ppl = 1626.4
    Epoch: 0002 Batch: 50 /134 lost = 6.982123 ppl = 1077.2
    Epoch: 0002 Batch: 100 /134 lost = 6.748810 ppl = 853.043
    Valid 4864 samples after epoch: 0002 lost = 6.732721 ppl = 839.429
    Epoch: 0003 Batch: 50 /134 lost = 6.513837 ppl = 674.409
    Epoch: 0003 Batch: 100 /134 lost = 6.471617 ppl = 646.528
    Valid 4864 samples after epoch: 0003 lost = 6.615870 ppl = 746.854
    Epoch: 0004 Batch: 50 /134 lost = 6.442818 ppl = 628.175
    Epoch: 0004 Batch: 100 /134 lost = 6.431133 ppl = 620.877
    Valid 4864 samples after epoch: 0004 lost = 6.608877 ppl = 741.65
    Epoch: 0005 Batch: 50 /134 lost = 6.427310 ppl = 618.508
    Epoch: 0005 Batch: 100 /134 lost = 6.413999 ppl = 610.33
    Valid 4864 samples after epoch: 0005 lost = 6.608086 ppl = 741.064
    Epoch: 0006 Batch: 50 /134 lost = 6.416022 ppl = 611.565
    Epoch: 0006 Batch: 100 /134 lost = 6.398947 ppl = 601.211
    Valid 4864 samples after epoch: 0006 lost = 6.606937 ppl = 740.212
    Epoch: 0007 Batch: 50 /134 lost = 6.404455 ppl = 604.532
    Epoch: 0007 Batch: 100 /134 lost = 6.383271 ppl = 591.86
    Valid 4864 samples after epoch: 0007 lost = 6.604153 ppl = 738.155
    Epoch: 0008 Batch: 50 /134 lost = 6.391828 ppl = 596.947
    Epoch: 0008 Batch: 100 /134 lost = 6.366553 ppl = 582.048
    Valid 4864 samples after epoch: 0008 lost = 6.599709 ppl = 734.882
    Epoch: 0009 Batch: 50 /134 lost = 6.378254 ppl = 588.899
    Epoch: 0009 Batch: 100 /134 lost = 6.348977 ppl = 571.907
    Valid 4864 samples after epoch: 0009 lost = 6.593913 ppl = 730.634
    Epoch: 0010 Batch: 50 /134 lost = 6.363951 ppl = 580.536
    Epoch: 0010 Batch: 100 /134 lost = 6.330809 ppl = 561.611
    Valid 4864 samples after epoch: 0010 lost = 6.587171 ppl = 725.725
    Epoch: 0011 Batch: 50 /134 lost = 6.349242 ppl = 572.059
    Epoch: 0011 Batch: 100 /134 lost = 6.312396 ppl = 551.364
    Valid 4864 samples after epoch: 0011 lost = 6.579902 ppl = 720.469
    Epoch: 0012 Batch: 50 /134 lost = 6.334362 ppl = 563.61
    Epoch: 0012 Batch: 100 /134 lost = 6.293781 ppl = 541.196
    Valid 4864 samples after epoch: 0012 lost = 6.572209 ppl = 714.947
    Epoch: 0013 Batch: 50 /134 lost = 6.319293 ppl = 555.181
    Epoch: 0013 Batch: 100 /134 lost = 6.274874 ppl = 531.059
    Valid 4864 samples after epoch: 0013 lost = 6.564085 ppl = 709.163
    Epoch: 0014 Batch: 50 /134 lost = 6.304018 ppl = 546.764
    Epoch: 0014 Batch: 100 /134 lost = 6.255690 ppl = 520.969
    Valid 4864 samples after epoch: 0014 lost = 6.555582 ppl = 703.158
    Epoch: 0015 Batch: 50 /134 lost = 6.288558 ppl = 538.376
    Epoch: 0015 Batch: 100 /134 lost = 6.236298 ppl = 510.963
    Valid 4864 samples after epoch: 0015 lost = 6.546762 ppl = 696.984
    Epoch: 0016 Batch: 50 /134 lost = 6.272936 ppl = 530.031
    Epoch: 0016 Batch: 100 /134 lost = 6.216713 ppl = 501.054
    Valid 4864 samples after epoch: 0016 lost = 6.537665 ppl = 690.672
    Epoch: 0017 Batch: 50 /134 lost = 6.257161 ppl = 521.736
    Epoch: 0017 Batch: 100 /134 lost = 6.196911 ppl = 491.229
    Valid 4864 samples after epoch: 0017 lost = 6.528305 ppl = 684.237
    Epoch: 0018 Batch: 50 /134 lost = 6.241205 ppl = 513.477
    Epoch: 0018 Batch: 100 /134 lost = 6.176821 ppl = 481.459
    Valid 4864 samples after epoch: 0018 lost = 6.518676 ppl = 677.681
    Epoch: 0019 Batch: 50 /134 lost = 6.225029 ppl = 505.238
    Epoch: 0019 Batch: 100 /134 lost = 6.156407 ppl = 471.73
    Valid 4864 samples after epoch: 0019 lost = 6.508817 ppl = 671.032
    Epoch: 0020 Batch: 50 /134 lost = 6.208679 ppl = 497.044
    Epoch: 0020 Batch: 100 /134 lost = 6.135810 ppl = 462.113
    Valid 4864 samples after epoch: 0020 lost = 6.498869 ppl = 664.39
    Epoch: 0021 Batch: 50 /134 lost = 6.192300 ppl = 488.97
    Epoch: 0021 Batch: 100 /134 lost = 6.115197 ppl = 452.685
    Valid 4864 samples after epoch: 0021 lost = 6.488961 ppl = 657.84
    Epoch: 0022 Batch: 50 /134 lost = 6.176004 ppl = 481.066
    Epoch: 0022 Batch: 100 /134 lost = 6.094646 ppl = 443.477
    Valid 4864 samples after epoch: 0022 lost = 6.479152 ppl = 651.419
    Epoch: 0023 Batch: 50 /134 lost = 6.159831 ppl = 473.348
    Epoch: 0023 Batch: 100 /134 lost = 6.074215 ppl = 434.508
    Valid 4864 samples after epoch: 0023 lost = 6.469441 ppl = 645.123
    Epoch: 0024 Batch: 50 /134 lost = 6.143739 ppl = 465.792
    Epoch: 0024 Batch: 100 /134 lost = 6.053940 ppl = 425.787
    Valid 4864 samples after epoch: 0024 lost = 6.459826 ppl = 638.95
    Epoch: 0025 Batch: 50 /134 lost = 6.127684 ppl = 458.373
    Epoch: 0025 Batch: 100 /134 lost = 6.033892 ppl = 417.336
    Valid 4864 samples after epoch: 0025 lost = 6.450355 ppl = 632.927
    Epoch: 0026 Batch: 50 /134 lost = 6.111698 ppl = 451.104
    Epoch: 0026 Batch: 100 /134 lost = 6.014187 ppl = 409.193
    Valid 4864 samples after epoch: 0026 lost = 6.441115 ppl = 627.106
    Epoch: 0027 Batch: 50 /134 lost = 6.095885 ppl = 444.027
    Epoch: 0027 Batch: 100 /134 lost = 5.994865 ppl = 401.363
    Valid 4864 samples after epoch: 0027 lost = 6.432135 ppl = 621.499
    Epoch: 0028 Batch: 50 /134 lost = 6.080294 ppl = 437.158
    Epoch: 0028 Batch: 100 /134 lost = 5.975904 ppl = 393.824
    Valid 4864 samples after epoch: 0028 lost = 6.423417 ppl = 616.105
    Epoch: 0029 Batch: 50 /134 lost = 6.064939 ppl = 430.496
    Epoch: 0029 Batch: 100 /134 lost = 5.957291 ppl = 386.562
    Valid 4864 samples after epoch: 0029 lost = 6.414979 ppl = 610.928
    Epoch: 0030 Batch: 50 /134 lost = 6.049835 ppl = 424.043
    Epoch: 0030 Batch: 100 /134 lost = 5.939025 ppl = 379.565
    Valid 4864 samples after epoch: 0030 lost = 6.406830 ppl = 605.97
    Epoch: 0031 Batch: 50 /134 lost = 6.034989 ppl = 417.794
    Epoch: 0031 Batch: 100 /134 lost = 5.921097 ppl = 372.821
    Valid 4864 samples after epoch: 0031 lost = 6.398958 ppl = 601.219
    Epoch: 0032 Batch: 50 /134 lost = 6.020404 ppl = 411.745
    Epoch: 0032 Batch: 100 /134 lost = 5.903509 ppl = 366.321
    Valid 4864 samples after epoch: 0032 lost = 6.391352 ppl = 596.663
    Epoch: 0033 Batch: 50 /134 lost = 6.006059 ppl = 405.88
    Epoch: 0033 Batch: 100 /134 lost = 5.886252 ppl = 360.053
    Valid 4864 samples after epoch: 0033 lost = 6.384000 ppl = 592.292
    Epoch: 0034 Batch: 50 /134 lost = 5.991944 ppl = 400.192
    Epoch: 0034 Batch: 100 /134 lost = 5.869319 ppl = 354.008
    Valid 4864 samples after epoch: 0034 lost = 6.376891 ppl = 588.097
    Epoch: 0035 Batch: 50 /134 lost = 5.978039 ppl = 394.666
    Epoch: 0035 Batch: 100 /134 lost = 5.852705 ppl = 348.175
    Valid 4864 samples after epoch: 0035 lost = 6.370016 ppl = 584.067
    Epoch: 0036 Batch: 50 /134 lost = 5.964335 ppl = 389.294
    Epoch: 0036 Batch: 100 /134 lost = 5.836401 ppl = 342.544
    Valid 4864 samples after epoch: 0036 lost = 6.363368 ppl = 580.197
    Epoch: 0037 Batch: 50 /134 lost = 5.950822 ppl = 384.069
    Epoch: 0037 Batch: 100 /134 lost = 5.820407 ppl = 337.109
    Valid 4864 samples after epoch: 0037 lost = 6.356943 ppl = 576.481
    Epoch: 0038 Batch: 50 /134 lost = 5.937504 ppl = 378.988
    Epoch: 0038 Batch: 100 /134 lost = 5.804718 ppl = 331.862
    Valid 4864 samples after epoch: 0038 lost = 6.350737 ppl = 572.915
    Epoch: 0039 Batch: 50 /134 lost = 5.924375 ppl = 374.045
    Epoch: 0039 Batch: 100 /134 lost = 5.789327 ppl = 326.793
    Valid 4864 samples after epoch: 0039 lost = 6.344748 ppl = 569.494
    Epoch: 0040 Batch: 50 /134 lost = 5.911435 ppl = 369.236
    Epoch: 0040 Batch: 100 /134 lost = 5.774228 ppl = 321.896
    Valid 4864 samples after epoch: 0040 lost = 6.338973 ppl = 566.214
    Epoch: 0041 Batch: 50 /134 lost = 5.898678 ppl = 364.555
    Epoch: 0041 Batch: 100 /134 lost = 5.759415 ppl = 317.163
    Valid 4864 samples after epoch: 0041 lost = 6.333410 ppl = 563.073
    Epoch: 0042 Batch: 50 /134 lost = 5.886092 ppl = 359.996
    Epoch: 0042 Batch: 100 /134 lost = 5.744886 ppl = 312.588
    Valid 4864 samples after epoch: 0042 lost = 6.328058 ppl = 560.068
    Epoch: 0043 Batch: 50 /134 lost = 5.873667 ppl = 355.55
    Epoch: 0043 Batch: 100 /134 lost = 5.730643 ppl = 308.167
    Valid 4864 samples after epoch: 0043 lost = 6.322915 ppl = 557.195
    Epoch: 0044 Batch: 50 /134 lost = 5.861394 ppl = 351.214
    Epoch: 0044 Batch: 100 /134 lost = 5.716681 ppl = 303.894
    Valid 4864 samples after epoch: 0044 lost = 6.317978 ppl = 554.451
    Epoch: 0045 Batch: 50 /134 lost = 5.849265 ppl = 346.979
    Epoch: 0045 Batch: 100 /134 lost = 5.703000 ppl = 299.765
    Valid 4864 samples after epoch: 0045 lost = 6.313245 ppl = 551.833
    Epoch: 0046 Batch: 50 /134 lost = 5.837275 ppl = 342.844
    Epoch: 0046 Batch: 100 /134 lost = 5.689594 ppl = 295.773
    Valid 4864 samples after epoch: 0046 lost = 6.308715 ppl = 549.338
    Epoch: 0047 Batch: 50 /134 lost = 5.825422 ppl = 338.804
    Epoch: 0047 Batch: 100 /134 lost = 5.676448 ppl = 291.911
    Valid 4864 samples after epoch: 0047 lost = 6.304385 ppl = 546.965
    Epoch: 0048 Batch: 50 /134 lost = 5.813705 ppl = 334.858
    Epoch: 0048 Batch: 100 /134 lost = 5.663552 ppl = 288.17
    Valid 4864 samples after epoch: 0048 lost = 6.300252 ppl = 544.709
    Epoch: 0049 Batch: 50 /134 lost = 5.802127 ppl = 331.003
    Epoch: 0049 Batch: 100 /134 lost = 5.650889 ppl = 284.544
    Valid 4864 samples after epoch: 0049 lost = 6.296314 ppl = 542.568
    Epoch: 0050 Batch: 50 /134 lost = 5.790685 ppl = 327.237
    Epoch: 0050 Batch: 100 /134 lost = 5.638449 ppl = 281.026
    Valid 4864 samples after epoch: 0050 lost = 6.292565 ppl = 540.538
    Epoch: 0051 Batch: 50 /134 lost = 5.779377 ppl = 323.558
    Epoch: 0051 Batch: 100 /134 lost = 5.626215 ppl = 277.609
    Valid 4864 samples after epoch: 0051 lost = 6.288998 ppl = 538.613
    Epoch: 0052 Batch: 50 /134 lost = 5.768202 ppl = 319.962
    Epoch: 0052 Batch: 100 /134 lost = 5.614176 ppl = 274.287
    Valid 4864 samples after epoch: 0052 lost = 6.285605 ppl = 536.789
    Epoch: 0053 Batch: 50 /134 lost = 5.757154 ppl = 316.447
    Epoch: 0053 Batch: 100 /134 lost = 5.602321 ppl = 271.055
    Valid 4864 samples after epoch: 0053 lost = 6.282379 ppl = 535.06
    Epoch: 0054 Batch: 50 /134 lost = 5.746230 ppl = 313.008
    Epoch: 0054 Batch: 100 /134 lost = 5.590641 ppl = 267.907
    Valid 4864 samples after epoch: 0054 lost = 6.279313 ppl = 533.422
    Epoch: 0055 Batch: 50 /134 lost = 5.735427 ppl = 309.645
    Epoch: 0055 Batch: 100 /134 lost = 5.579131 ppl = 264.841
    Valid 4864 samples after epoch: 0055 lost = 6.276404 ppl = 531.872
    Epoch: 0056 Batch: 50 /134 lost = 5.724741 ppl = 306.354
    Epoch: 0056 Batch: 100 /134 lost = 5.567782 ppl = 261.853
    Valid 4864 samples after epoch: 0056 lost = 6.273648 ppl = 530.409
    Epoch: 0057 Batch: 50 /134 lost = 5.714172 ppl = 303.133
    Epoch: 0057 Batch: 100 /134 lost = 5.556592 ppl = 258.939
    Valid 4864 samples after epoch: 0057 lost = 6.271045 ppl = 529.03
    Epoch: 0058 Batch: 50 /134 lost = 5.703720 ppl = 299.981
    Epoch: 0058 Batch: 100 /134 lost = 5.545559 ppl = 256.098
    Valid 4864 samples after epoch: 0058 lost = 6.268591 ppl = 527.733
    Epoch: 0059 Batch: 50 /134 lost = 5.693381 ppl = 296.896
    Epoch: 0059 Batch: 100 /134 lost = 5.534684 ppl = 253.328
    Valid 4864 samples after epoch: 0059 lost = 6.266282 ppl = 526.516
    Epoch: 0060 Batch: 50 /134 lost = 5.683156 ppl = 293.875
    Epoch: 0060 Batch: 100 /134 lost = 5.523964 ppl = 250.627
    Valid 4864 samples after epoch: 0060 lost = 6.264113 ppl = 525.376
    Epoch: 0061 Batch: 50 /134 lost = 5.673041 ppl = 290.918
    Epoch: 0061 Batch: 100 /134 lost = 5.513403 ppl = 247.994
    Valid 4864 samples after epoch: 0061 lost = 6.262083 ppl = 524.31
    Epoch: 0062 Batch: 50 /134 lost = 5.663040 ppl = 288.023
    Epoch: 0062 Batch: 100 /134 lost = 5.502997 ppl = 245.426
    Valid 4864 samples after epoch: 0062 lost = 6.260187 ppl = 523.317
    Epoch: 0063 Batch: 50 /134 lost = 5.653149 ppl = 285.188
    Epoch: 0063 Batch: 100 /134 lost = 5.492746 ppl = 242.923
    Valid 4864 samples after epoch: 0063 lost = 6.258423 ppl = 522.394
    Epoch: 0064 Batch: 50 /134 lost = 5.643371 ppl = 282.413
    Epoch: 0064 Batch: 100 /134 lost = 5.482646 ppl = 240.482
    Valid 4864 samples after epoch: 0064 lost = 6.256788 ppl = 521.541
    Epoch: 0065 Batch: 50 /134 lost = 5.633706 ppl = 279.697
    Epoch: 0065 Batch: 100 /134 lost = 5.472694 ppl = 238.101
    Valid 4864 samples after epoch: 0065 lost = 6.255278 ppl = 520.754
    Epoch: 0066 Batch: 50 /134 lost = 5.624153 ppl = 277.037
    Epoch: 0066 Batch: 100 /134 lost = 5.462889 ppl = 235.778
    Valid 4864 samples after epoch: 0066 lost = 6.253889 ppl = 520.031
    Epoch: 0067 Batch: 50 /134 lost = 5.614714 ppl = 274.435
    Epoch: 0067 Batch: 100 /134 lost = 5.453228 ppl = 233.511
    Valid 4864 samples after epoch: 0067 lost = 6.252615 ppl = 519.369
    Epoch: 0068 Batch: 50 /134 lost = 5.605386 ppl = 271.887
    Epoch: 0068 Batch: 100 /134 lost = 5.443712 ppl = 231.299
    Valid 4864 samples after epoch: 0068 lost = 6.251454 ppl = 518.766
    Epoch: 0069 Batch: 50 /134 lost = 5.596169 ppl = 269.392
    Epoch: 0069 Batch: 100 /134 lost = 5.434336 ppl = 229.141
    Valid 4864 samples after epoch: 0069 lost = 6.250399 ppl = 518.22
    Epoch: 0070 Batch: 50 /134 lost = 5.587059 ppl = 266.949
    Epoch: 0070 Batch: 100 /134 lost = 5.425097 ppl = 227.033
    Valid 4864 samples after epoch: 0070 lost = 6.249448 ppl = 517.727
    Epoch: 0071 Batch: 50 /134 lost = 5.578053 ppl = 264.556
    Epoch: 0071 Batch: 100 /134 lost = 5.415991 ppl = 224.975
    Valid 4864 samples after epoch: 0071 lost = 6.248595 ppl = 517.285
    Epoch: 0072 Batch: 50 /134 lost = 5.569148 ppl = 262.211
    Epoch: 0072 Batch: 100 /134 lost = 5.407010 ppl = 222.964
    Valid 4864 samples after epoch: 0072 lost = 6.247837 ppl = 516.893
    Epoch: 0073 Batch: 50 /134 lost = 5.560337 ppl = 259.91
    Epoch: 0073 Batch: 100 /134 lost = 5.398149 ppl = 220.997
    Valid 4864 samples after epoch: 0073 lost = 6.247167 ppl = 516.547
    Epoch: 0074 Batch: 50 /134 lost = 5.551618 ppl = 257.654
    Epoch: 0074 Batch: 100 /134 lost = 5.389402 ppl = 219.072
    Valid 4864 samples after epoch: 0074 lost = 6.246581 ppl = 516.245
    Epoch: 0075 Batch: 50 /134 lost = 5.542990 ppl = 255.441
    Epoch: 0075 Batch: 100 /134 lost = 5.380764 ppl = 217.188
    Valid 4864 samples after epoch: 0075 lost = 6.246076 ppl = 515.984
    Epoch: 0076 Batch: 50 /134 lost = 5.534453 ppl = 253.269
    Epoch: 0076 Batch: 100 /134 lost = 5.372236 ppl = 215.344
    Valid 4864 samples after epoch: 0076 lost = 6.245649 ppl = 515.764
    Epoch: 0077 Batch: 50 /134 lost = 5.526018 ppl = 251.142
    Epoch: 0077 Batch: 100 /134 lost = 5.363818 ppl = 213.539
    Valid 4864 samples after epoch: 0077 lost = 6.245300 ppl = 515.584
    Epoch: 0078 Batch: 50 /134 lost = 5.517678 ppl = 249.056
    Epoch: 0078 Batch: 100 /134 lost = 5.355507 ppl = 211.771
    Valid 4864 samples after epoch: 0078 lost = 6.245025 ppl = 515.442
    Epoch: 0079 Batch: 50 /134 lost = 5.509434 ppl = 247.011
    Epoch: 0079 Batch: 100 /134 lost = 5.347300 ppl = 210.04
    Valid 4864 samples after epoch: 0079 lost = 6.244824 ppl = 515.338
    Epoch: 0080 Batch: 50 /134 lost = 5.501279 ppl = 245.005
    Epoch: 0080 Batch: 100 /134 lost = 5.339190 ppl = 208.344
    Valid 4864 samples after epoch: 0080 lost = 6.244692 ppl = 515.271
    Epoch: 0081 Batch: 50 /134 lost = 5.493214 ppl = 243.037
    Epoch: 0081 Batch: 100 /134 lost = 5.331175 ppl = 206.681
    Valid 4864 samples after epoch: 0081 lost = 6.244630 ppl = 515.239
    Epoch: 0082 Batch: 50 /134 lost = 5.485234 ppl = 241.105
    Epoch: 0082 Batch: 100 /134 lost = 5.323249 ppl = 205.049
    Valid 4864 samples after epoch: 0082 lost = 6.244635 ppl = 515.241
    Epoch: 0083 Batch: 50 /134 lost = 5.477339 ppl = 239.209
    Epoch: 0083 Batch: 100 /134 lost = 5.315409 ppl = 203.448
    Valid 4864 samples after epoch: 0083 lost = 6.244704 ppl = 515.276
    Epoch: 0084 Batch: 50 /134 lost = 5.469530 ppl = 237.349
    Epoch: 0084 Batch: 100 /134 lost = 5.307653 ppl = 201.876
    Valid 4864 samples after epoch: 0084 lost = 6.244833 ppl = 515.343
    Epoch: 0085 Batch: 50 /134 lost = 5.461806 ppl = 235.522
    Epoch: 0085 Batch: 100 /134 lost = 5.299976 ppl = 200.332
    Valid 4864 samples after epoch: 0085 lost = 6.245020 ppl = 515.44
    Epoch: 0086 Batch: 50 /134 lost = 5.454162 ppl = 233.729
    Epoch: 0086 Batch: 100 /134 lost = 5.292376 ppl = 198.815
    Valid 4864 samples after epoch: 0086 lost = 6.245263 ppl = 515.565
    Epoch: 0087 Batch: 50 /134 lost = 5.446600 ppl = 231.968
    Epoch: 0087 Batch: 100 /134 lost = 5.284848 ppl = 197.324
    Valid 4864 samples after epoch: 0087 lost = 6.245560 ppl = 515.718
    Epoch: 0088 Batch: 50 /134 lost = 5.439117 ppl = 230.239
    Epoch: 0088 Batch: 100 /134 lost = 5.277392 ppl = 195.858
    Valid 4864 samples after epoch: 0088 lost = 6.245908 ppl = 515.898
    Epoch: 0089 Batch: 50 /134 lost = 5.431712 ppl = 228.54
    Epoch: 0089 Batch: 100 /134 lost = 5.270006 ppl = 194.417
    Valid 4864 samples after epoch: 0089 lost = 6.246306 ppl = 516.103
    Epoch: 0090 Batch: 50 /134 lost = 5.424383 ppl = 226.871
    Epoch: 0090 Batch: 100 /134 lost = 5.262684 ppl = 192.999
    Valid 4864 samples after epoch: 0090 lost = 6.246750 ppl = 516.332
    Epoch: 0091 Batch: 50 /134 lost = 5.417127 ppl = 225.231
    Epoch: 0091 Batch: 100 /134 lost = 5.255428 ppl = 191.603
    Valid 4864 samples after epoch: 0091 lost = 6.247239 ppl = 516.585
    Epoch: 0092 Batch: 50 /134 lost = 5.409942 ppl = 223.619
    Epoch: 0092 Batch: 100 /134 lost = 5.248233 ppl = 190.23
    Valid 4864 samples after epoch: 0092 lost = 6.247771 ppl = 516.859
    Epoch: 0093 Batch: 50 /134 lost = 5.402826 ppl = 222.033
    Epoch: 0093 Batch: 100 /134 lost = 5.241101 ppl = 188.878
    Valid 4864 samples after epoch: 0093 lost = 6.248342 ppl = 517.154
    Epoch: 0094 Batch: 50 /134 lost = 5.395779 ppl = 220.474
    Epoch: 0094 Batch: 100 /134 lost = 5.234027 ppl = 187.547
    Valid 4864 samples after epoch: 0094 lost = 6.248950 ppl = 517.469
    Epoch: 0095 Batch: 50 /134 lost = 5.388796 ppl = 218.94
    Epoch: 0095 Batch: 100 /134 lost = 5.227013 ppl = 186.236
    Valid 4864 samples after epoch: 0095 lost = 6.249595 ppl = 517.803
    Epoch: 0096 Batch: 50 /134 lost = 5.381877 ppl = 217.43
    Epoch: 0096 Batch: 100 /134 lost = 5.220057 ppl = 184.945
    Valid 4864 samples after epoch: 0096 lost = 6.250273 ppl = 518.154
    Epoch: 0097 Batch: 50 /134 lost = 5.375022 ppl = 215.945
    Epoch: 0097 Batch: 100 /134 lost = 5.213158 ppl = 183.673
    Valid 4864 samples after epoch: 0097 lost = 6.250984 ppl = 518.523
    Epoch: 0098 Batch: 50 /134 lost = 5.368227 ppl = 214.482
    Epoch: 0098 Batch: 100 /134 lost = 5.206314 ppl = 182.42
    Valid 4864 samples after epoch: 0098 lost = 6.251725 ppl = 518.907
    Epoch: 0099 Batch: 50 /134 lost = 5.361493 ppl = 213.043
    Epoch: 0099 Batch: 100 /134 lost = 5.199529 ppl = 181.187
    Valid 4864 samples after epoch: 0099 lost = 6.252495 ppl = 519.307
    Epoch: 0100 Batch: 50 /134 lost = 5.354817 ppl = 211.625
    Epoch: 0100 Batch: 100 /134 lost = 5.192796 ppl = 179.971
    Valid 4864 samples after epoch: 0100 lost = 6.253293 ppl = 519.721
    
    Test the LSTMLM……………………
    Test 5760 samples with models/2_layers_lstmlm_model_epoch100.ckpt……………………
    lost = 6.164685 ppl = 475.651
    
