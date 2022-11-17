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
    Epoch: 0001 Batch: 50 /134 lost = 8.843715 ppl = 6930.69
    Epoch: 0001 Batch: 100 /134 lost = 8.638642 ppl = 5645.66
    Valid 4864 samples after epoch: 0001 lost = 8.533294 ppl = 5081.16
    Epoch: 0002 Batch: 50 /134 lost = 8.315947 ppl = 4088.55
    Epoch: 0002 Batch: 100 /134 lost = 8.063635 ppl = 3176.82
    Valid 4864 samples after epoch: 0002 lost = 7.965967 ppl = 2881.21
    Epoch: 0003 Batch: 50 /134 lost = 7.724911 ppl = 2264.05
    Epoch: 0003 Batch: 100 /134 lost = 7.511007 ppl = 1828.05
    Valid 4864 samples after epoch: 0003 lost = 7.469049 ppl = 1752.94
    Epoch: 0004 Batch: 50 /134 lost = 7.244986 ppl = 1401.06
    Epoch: 0004 Batch: 100 /134 lost = 7.093092 ppl = 1203.62
    Valid 4864 samples after epoch: 0004 lost = 7.118874 ppl = 1235.06
    Epoch: 0005 Batch: 50 /134 lost = 6.918437 ppl = 1010.74
    Epoch: 0005 Batch: 100 /134 lost = 6.817809 ppl = 913.98
    Valid 4864 samples after epoch: 0005 lost = 6.899389 ppl = 991.668
    Epoch: 0006 Batch: 50 /134 lost = 6.712449 ppl = 822.582
    Epoch: 0006 Batch: 100 /134 lost = 6.643337 ppl = 767.652
    Valid 4864 samples after epoch: 0006 lost = 6.770566 ppl = 871.805
    Epoch: 0007 Batch: 50 /134 lost = 6.589432 ppl = 727.368
    Epoch: 0007 Batch: 100 /134 lost = 6.539042 ppl = 691.623
    Valid 4864 samples after epoch: 0007 lost = 6.697029 ppl = 809.995
    Epoch: 0008 Batch: 50 /134 lost = 6.514611 ppl = 674.932
    Epoch: 0008 Batch: 100 /134 lost = 6.469824 ppl = 645.37
    Valid 4864 samples after epoch: 0008 lost = 6.648476 ppl = 771.608
    Epoch: 0009 Batch: 50 /134 lost = 6.460711 ppl = 639.516
    Epoch: 0009 Batch: 100 /134 lost = 6.410820 ppl = 608.392
    Valid 4864 samples after epoch: 0009 lost = 6.601859 ppl = 736.463
    Epoch: 0010 Batch: 50 /134 lost = 6.416312 ppl = 611.743
    Epoch: 0010 Batch: 100 /134 lost = 6.360848 ppl = 578.737
    Valid 4864 samples after epoch: 0010 lost = 6.569289 ppl = 712.863
    Epoch: 0011 Batch: 50 /134 lost = 6.378457 ppl = 589.018
    Epoch: 0011 Batch: 100 /134 lost = 6.328974 ppl = 560.581
    Valid 4864 samples after epoch: 0011 lost = 6.550361 ppl = 699.497
    Epoch: 0012 Batch: 50 /134 lost = 6.353425 ppl = 574.457
    Epoch: 0012 Batch: 100 /134 lost = 6.305495 ppl = 547.572
    Valid 4864 samples after epoch: 0012 lost = 6.538499 ppl = 691.248
    Epoch: 0013 Batch: 50 /134 lost = 6.336658 ppl = 564.905
    Epoch: 0013 Batch: 100 /134 lost = 6.287929 ppl = 538.038
    Valid 4864 samples after epoch: 0013 lost = 6.526086 ppl = 682.721
    Epoch: 0014 Batch: 50 /134 lost = 6.317555 ppl = 554.217
    Epoch: 0014 Batch: 100 /134 lost = 6.265845 ppl = 526.286
    Valid 4864 samples after epoch: 0014 lost = 6.511079 ppl = 672.552
    Epoch: 0015 Batch: 50 /134 lost = 6.296829 ppl = 542.848
    Epoch: 0015 Batch: 100 /134 lost = 6.246230 ppl = 516.063
    Valid 4864 samples after epoch: 0015 lost = 6.500472 ppl = 665.456
    Epoch: 0016 Batch: 50 /134 lost = 6.276738 ppl = 532.05
    Epoch: 0016 Batch: 100 /134 lost = 6.225914 ppl = 505.685
    Valid 4864 samples after epoch: 0016 lost = 6.493263 ppl = 660.676
    Epoch: 0017 Batch: 50 /134 lost = 6.256526 ppl = 521.404
    Epoch: 0017 Batch: 100 /134 lost = 6.206602 ppl = 496.013
    Valid 4864 samples after epoch: 0017 lost = 6.484781 ppl = 655.096
    Epoch: 0018 Batch: 50 /134 lost = 6.236207 ppl = 510.917
    Epoch: 0018 Batch: 100 /134 lost = 6.184406 ppl = 485.125
    Valid 4864 samples after epoch: 0018 lost = 6.476981 ppl = 650.006
    Epoch: 0019 Batch: 50 /134 lost = 6.219322 ppl = 502.362
    Epoch: 0019 Batch: 100 /134 lost = 6.164897 ppl = 475.752
    Valid 4864 samples after epoch: 0019 lost = 6.469241 ppl = 644.994
    Epoch: 0020 Batch: 50 /134 lost = 6.202629 ppl = 494.046
    Epoch: 0020 Batch: 100 /134 lost = 6.148657 ppl = 468.088
    Valid 4864 samples after epoch: 0020 lost = 6.463837 ppl = 641.518
    Epoch: 0021 Batch: 50 /134 lost = 6.185874 ppl = 485.837
    Epoch: 0021 Batch: 100 /134 lost = 6.130955 ppl = 459.875
    Valid 4864 samples after epoch: 0021 lost = 6.454999 ppl = 635.873
    Epoch: 0022 Batch: 50 /134 lost = 6.170702 ppl = 478.522
    Epoch: 0022 Batch: 100 /134 lost = 6.113369 ppl = 451.858
    Valid 4864 samples after epoch: 0022 lost = 6.446517 ppl = 630.502
    Epoch: 0023 Batch: 50 /134 lost = 6.155285 ppl = 471.201
    Epoch: 0023 Batch: 100 /134 lost = 6.092510 ppl = 442.531
    Valid 4864 samples after epoch: 0023 lost = 6.435366 ppl = 623.51
    Epoch: 0024 Batch: 50 /134 lost = 6.138251 ppl = 463.243
    Epoch: 0024 Batch: 100 /134 lost = 6.073459 ppl = 434.18
    Valid 4864 samples after epoch: 0024 lost = 6.426488 ppl = 617.999
    Epoch: 0025 Batch: 50 /134 lost = 6.122128 ppl = 455.834
    Epoch: 0025 Batch: 100 /134 lost = 6.055735 ppl = 426.552
    Valid 4864 samples after epoch: 0025 lost = 6.418395 ppl = 613.018
    Epoch: 0026 Batch: 50 /134 lost = 6.104389 ppl = 447.819
    Epoch: 0026 Batch: 100 /134 lost = 6.030578 ppl = 415.955
    Valid 4864 samples after epoch: 0026 lost = 6.409686 ppl = 607.703
    Epoch: 0027 Batch: 50 /134 lost = 6.087724 ppl = 440.418
    Epoch: 0027 Batch: 100 /134 lost = 6.012424 ppl = 408.472
    Valid 4864 samples after epoch: 0027 lost = 6.402445 ppl = 603.318
    Epoch: 0028 Batch: 50 /134 lost = 6.070474 ppl = 432.886
    Epoch: 0028 Batch: 100 /134 lost = 5.993469 ppl = 400.802
    Valid 4864 samples after epoch: 0028 lost = 6.396380 ppl = 599.67
    Epoch: 0029 Batch: 50 /134 lost = 6.052166 ppl = 425.033
    Epoch: 0029 Batch: 100 /134 lost = 5.974955 ppl = 393.45
    Valid 4864 samples after epoch: 0029 lost = 6.390156 ppl = 595.95
    Epoch: 0030 Batch: 50 /134 lost = 6.037690 ppl = 418.924
    Epoch: 0030 Batch: 100 /134 lost = 5.957100 ppl = 386.488
    Valid 4864 samples after epoch: 0030 lost = 6.384069 ppl = 592.333
    Epoch: 0031 Batch: 50 /134 lost = 6.024184 ppl = 413.304
    Epoch: 0031 Batch: 100 /134 lost = 5.940439 ppl = 380.102
    Valid 4864 samples after epoch: 0031 lost = 6.378849 ppl = 589.249
    Epoch: 0032 Batch: 50 /134 lost = 6.010794 ppl = 407.807
    Epoch: 0032 Batch: 100 /134 lost = 5.924590 ppl = 374.125
    Valid 4864 samples after epoch: 0032 lost = 6.374377 ppl = 586.62
    Epoch: 0033 Batch: 50 /134 lost = 5.997336 ppl = 402.356
    Epoch: 0033 Batch: 100 /134 lost = 5.908958 ppl = 368.322
    Valid 4864 samples after epoch: 0033 lost = 6.370463 ppl = 584.328
    Epoch: 0034 Batch: 50 /134 lost = 5.983864 ppl = 396.971
    Epoch: 0034 Batch: 100 /134 lost = 5.893764 ppl = 362.768
    Valid 4864 samples after epoch: 0034 lost = 6.367448 ppl = 582.569
    Epoch: 0035 Batch: 50 /134 lost = 5.970423 ppl = 391.671
    Epoch: 0035 Batch: 100 /134 lost = 5.879231 ppl = 357.534
    Valid 4864 samples after epoch: 0035 lost = 6.364453 ppl = 580.827
    Epoch: 0036 Batch: 50 /134 lost = 5.957903 ppl = 386.798
    Epoch: 0036 Batch: 100 /134 lost = 5.865697 ppl = 352.728
    Valid 4864 samples after epoch: 0036 lost = 6.361648 ppl = 579.2
    Epoch: 0037 Batch: 50 /134 lost = 5.945900 ppl = 382.183
    Epoch: 0037 Batch: 100 /134 lost = 5.852846 ppl = 348.224
    Valid 4864 samples after epoch: 0037 lost = 6.358533 ppl = 577.398
    Epoch: 0038 Batch: 50 /134 lost = 5.933402 ppl = 377.436
    Epoch: 0038 Batch: 100 /134 lost = 5.840446 ppl = 343.933
    Valid 4864 samples after epoch: 0038 lost = 6.355370 ppl = 575.575
    Epoch: 0039 Batch: 50 /134 lost = 5.920762 ppl = 372.696
    Epoch: 0039 Batch: 100 /134 lost = 5.828030 ppl = 339.689
    Valid 4864 samples after epoch: 0039 lost = 6.351245 ppl = 573.206
    Epoch: 0040 Batch: 50 /134 lost = 5.909148 ppl = 368.392
    Epoch: 0040 Batch: 100 /134 lost = 5.815545 ppl = 335.474
    Valid 4864 samples after epoch: 0040 lost = 6.346842 ppl = 570.687
    Epoch: 0041 Batch: 50 /134 lost = 5.898091 ppl = 364.341
    Epoch: 0041 Batch: 100 /134 lost = 5.804039 ppl = 331.636
    Valid 4864 samples after epoch: 0041 lost = 6.343943 ppl = 569.035
    Epoch: 0042 Batch: 50 /134 lost = 5.886376 ppl = 360.098
    Epoch: 0042 Batch: 100 /134 lost = 5.792434 ppl = 327.81
    Valid 4864 samples after epoch: 0042 lost = 6.341492 ppl = 567.642
    Epoch: 0043 Batch: 50 /134 lost = 5.874391 ppl = 355.808
    Epoch: 0043 Batch: 100 /134 lost = 5.781433 ppl = 324.223
    Valid 4864 samples after epoch: 0043 lost = 6.339340 ppl = 566.423
    Epoch: 0044 Batch: 50 /134 lost = 5.863064 ppl = 351.801
    Epoch: 0044 Batch: 100 /134 lost = 5.771097 ppl = 320.89
    Valid 4864 samples after epoch: 0044 lost = 6.338037 ppl = 565.685
    Epoch: 0045 Batch: 50 /134 lost = 5.852191 ppl = 347.996
    Epoch: 0045 Batch: 100 /134 lost = 5.760936 ppl = 317.646
    Valid 4864 samples after epoch: 0045 lost = 6.336547 ppl = 564.843
    Epoch: 0046 Batch: 50 /134 lost = 5.841390 ppl = 344.257
    Epoch: 0046 Batch: 100 /134 lost = 5.750697 ppl = 314.41
    Valid 4864 samples after epoch: 0046 lost = 6.335559 ppl = 564.285
    Epoch: 0047 Batch: 50 /134 lost = 5.832946 ppl = 341.363
    Epoch: 0047 Batch: 100 /134 lost = 5.740684 ppl = 311.277
    Valid 4864 samples after epoch: 0047 lost = 6.334955 ppl = 563.944
    Epoch: 0048 Batch: 50 /134 lost = 5.822361 ppl = 337.768
    Epoch: 0048 Batch: 100 /134 lost = 5.730665 ppl = 308.174
    Valid 4864 samples after epoch: 0048 lost = 6.334254 ppl = 563.549
    Epoch: 0049 Batch: 50 /134 lost = 5.811670 ppl = 334.177
    Epoch: 0049 Batch: 100 /134 lost = 5.720865 ppl = 305.169
    Valid 4864 samples after epoch: 0049 lost = 6.333893 ppl = 563.345
    Epoch: 0050 Batch: 50 /134 lost = 5.800965 ppl = 330.619
    Epoch: 0050 Batch: 100 /134 lost = 5.711752 ppl = 302.401
    Valid 4864 samples after epoch: 0050 lost = 6.333117 ppl = 562.909
    Epoch: 0051 Batch: 50 /134 lost = 5.790381 ppl = 327.138
    Epoch: 0051 Batch: 100 /134 lost = 5.702773 ppl = 299.697
    Valid 4864 samples after epoch: 0051 lost = 6.333007 ppl = 562.846
    Epoch: 0052 Batch: 50 /134 lost = 5.779922 ppl = 323.734
    Epoch: 0052 Batch: 100 /134 lost = 5.694937 ppl = 297.358
    Valid 4864 samples after epoch: 0052 lost = 6.332424 ppl = 562.518
    Epoch: 0053 Batch: 50 /134 lost = 5.770305 ppl = 320.635
    Epoch: 0053 Batch: 100 /134 lost = 5.687570 ppl = 295.175
    Valid 4864 samples after epoch: 0053 lost = 6.331990 ppl = 562.275
    Epoch: 0054 Batch: 50 /134 lost = 5.761128 ppl = 317.707
    Epoch: 0054 Batch: 100 /134 lost = 5.679858 ppl = 292.908
    Valid 4864 samples after epoch: 0054 lost = 6.331528 ppl = 562.015
    Epoch: 0055 Batch: 50 /134 lost = 5.752284 ppl = 314.909
    Epoch: 0055 Batch: 100 /134 lost = 5.672358 ppl = 290.719
    Valid 4864 samples after epoch: 0055 lost = 6.331389 ppl = 561.936
    Epoch: 0056 Batch: 50 /134 lost = 5.743416 ppl = 312.129
    Epoch: 0056 Batch: 100 /134 lost = 5.665535 ppl = 288.743
    Valid 4864 samples after epoch: 0056 lost = 6.331335 ppl = 561.906
    Epoch: 0057 Batch: 50 /134 lost = 5.734848 ppl = 309.466
    Epoch: 0057 Batch: 100 /134 lost = 5.659121 ppl = 286.896
    Valid 4864 samples after epoch: 0057 lost = 6.331550 ppl = 562.027
    Epoch: 0058 Batch: 50 /134 lost = 5.725977 ppl = 306.733
    Epoch: 0058 Batch: 100 /134 lost = 5.652804 ppl = 285.09
    Valid 4864 samples after epoch: 0058 lost = 6.331431 ppl = 561.96
    Epoch: 0059 Batch: 50 /134 lost = 5.718431 ppl = 304.427
    Epoch: 0059 Batch: 100 /134 lost = 5.643909 ppl = 282.565
    Valid 4864 samples after epoch: 0059 lost = 6.325362 ppl = 558.56
    Epoch: 0060 Batch: 50 /134 lost = 5.715944 ppl = 303.671
    Epoch: 0060 Batch: 100 /134 lost = 5.639693 ppl = 281.376
    Valid 4864 samples after epoch: 0060 lost = 6.325811 ppl = 558.811
    
    Test the RNNLM……………………
    Test 5760 samples with models/1_layer_rnnlm_model_epoch60.ckpt……………………
    lost = 6.273175 ppl = 530.158
    
