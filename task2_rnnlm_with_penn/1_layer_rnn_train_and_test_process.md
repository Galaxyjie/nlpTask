```python
!python rnnlm_with_penn_assignment_1.py
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
    Epoch: 0001 Batch: 50 /134 lost = 8.848632 ppl = 6964.85
    Epoch: 0001 Batch: 100 /134 lost = 8.639423 ppl = 5650.07
    Valid 4864 samples after epoch: 0001 lost = 8.477308 ppl = 4804.5
    Epoch: 0002 Batch: 50 /134 lost = 8.261154 ppl = 3870.56
    Epoch: 0002 Batch: 100 /134 lost = 7.997774 ppl = 2974.33
    Valid 4864 samples after epoch: 0002 lost = 7.845099 ppl = 2553.19
    Epoch: 0003 Batch: 50 /134 lost = 7.631029 ppl = 2061.17
    Epoch: 0003 Batch: 100 /134 lost = 7.439372 ppl = 1701.68
    Valid 4864 samples after epoch: 0003 lost = 7.370788 ppl = 1588.89
    Epoch: 0004 Batch: 50 /134 lost = 7.183162 ppl = 1317.07
    Epoch: 0004 Batch: 100 /134 lost = 7.053770 ppl = 1157.21
    Valid 4864 samples after epoch: 0004 lost = 7.054325 ppl = 1157.86
    Epoch: 0005 Batch: 50 /134 lost = 6.880682 ppl = 973.29
    Epoch: 0005 Batch: 100 /134 lost = 6.794115 ppl = 892.579
    Valid 4864 samples after epoch: 0005 lost = 6.852796 ppl = 946.524
    Epoch: 0006 Batch: 50 /134 lost = 6.690525 ppl = 804.745
    Epoch: 0006 Batch: 100 /134 lost = 6.623251 ppl = 752.387
    Valid 4864 samples after epoch: 0006 lost = 6.730730 ppl = 837.759
    Epoch: 0007 Batch: 50 /134 lost = 6.572710 ppl = 715.305
    Epoch: 0007 Batch: 100 /134 lost = 6.519270 ppl = 678.083
    Valid 4864 samples after epoch: 0007 lost = 6.662661 ppl = 782.631
    Epoch: 0008 Batch: 50 /134 lost = 6.503142 ppl = 667.235
    Epoch: 0008 Batch: 100 /134 lost = 6.457843 ppl = 637.684
    Valid 4864 samples after epoch: 0008 lost = 6.626312 ppl = 754.694
    Epoch: 0009 Batch: 50 /134 lost = 6.458957 ppl = 638.395
    Epoch: 0009 Batch: 100 /134 lost = 6.418542 ppl = 613.109
    Valid 4864 samples after epoch: 0009 lost = 6.604624 ppl = 738.502
    Epoch: 0010 Batch: 50 /134 lost = 6.433177 ppl = 622.147
    Epoch: 0010 Batch: 100 /134 lost = 6.391558 ppl = 596.785
    Valid 4864 samples after epoch: 0010 lost = 6.595797 ppl = 732.012
    Epoch: 0011 Batch: 50 /134 lost = 6.408435 ppl = 606.943
    Epoch: 0011 Batch: 100 /134 lost = 6.369542 ppl = 583.79
    Valid 4864 samples after epoch: 0011 lost = 6.585053 ppl = 724.19
    Epoch: 0012 Batch: 50 /134 lost = 6.383768 ppl = 592.155
    Epoch: 0012 Batch: 100 /134 lost = 6.343710 ppl = 568.903
    Valid 4864 samples after epoch: 0012 lost = 6.573444 ppl = 715.831
    Epoch: 0013 Batch: 50 /134 lost = 6.360076 ppl = 578.291
    Epoch: 0013 Batch: 100 /134 lost = 6.317438 ppl = 554.152
    Valid 4864 samples after epoch: 0013 lost = 6.558413 ppl = 705.152
    Epoch: 0014 Batch: 50 /134 lost = 6.336107 ppl = 564.594
    Epoch: 0014 Batch: 100 /134 lost = 6.290372 ppl = 539.354
    Valid 4864 samples after epoch: 0014 lost = 6.545053 ppl = 695.793
    Epoch: 0015 Batch: 50 /134 lost = 6.311266 ppl = 550.742
    Epoch: 0015 Batch: 100 /134 lost = 6.259381 ppl = 522.895
    Valid 4864 samples after epoch: 0015 lost = 6.526104 ppl = 682.733
    Epoch: 0016 Batch: 50 /134 lost = 6.277253 ppl = 532.324
    Epoch: 0016 Batch: 100 /134 lost = 6.226046 ppl = 505.752
    Valid 4864 samples after epoch: 0016 lost = 6.509124 ppl = 671.238
    Epoch: 0017 Batch: 50 /134 lost = 6.249893 ppl = 517.957
    Epoch: 0017 Batch: 100 /134 lost = 6.193617 ppl = 489.614
    Valid 4864 samples after epoch: 0017 lost = 6.492952 ppl = 660.47
    Epoch: 0018 Batch: 50 /134 lost = 6.224148 ppl = 504.793
    Epoch: 0018 Batch: 100 /134 lost = 6.167305 ppl = 476.899
    Valid 4864 samples after epoch: 0018 lost = 6.481194 ppl = 652.75
    Epoch: 0019 Batch: 50 /134 lost = 6.201616 ppl = 493.546
    Epoch: 0019 Batch: 100 /134 lost = 6.142966 ppl = 465.432
    Valid 4864 samples after epoch: 0019 lost = 6.467988 ppl = 644.187
    Epoch: 0020 Batch: 50 /134 lost = 6.178551 ppl = 482.293
    Epoch: 0020 Batch: 100 /134 lost = 6.118488 ppl = 454.177
    Valid 4864 samples after epoch: 0020 lost = 6.457004 ppl = 637.149
    Epoch: 0021 Batch: 50 /134 lost = 6.157422 ppl = 472.209
    Epoch: 0021 Batch: 100 /134 lost = 6.097614 ppl = 444.795
    Valid 4864 samples after epoch: 0021 lost = 6.445961 ppl = 630.152
    Epoch: 0022 Batch: 50 /134 lost = 6.135948 ppl = 462.177
    Epoch: 0022 Batch: 100 /134 lost = 6.077685 ppl = 436.019
    Valid 4864 samples after epoch: 0022 lost = 6.434838 ppl = 623.181
    Epoch: 0023 Batch: 50 /134 lost = 6.117792 ppl = 453.862
    Epoch: 0023 Batch: 100 /134 lost = 6.058665 ppl = 427.804
    Valid 4864 samples after epoch: 0023 lost = 6.425155 ppl = 617.176
    Epoch: 0024 Batch: 50 /134 lost = 6.100302 ppl = 445.992
    Epoch: 0024 Batch: 100 /134 lost = 6.038069 ppl = 419.083
    Valid 4864 samples after epoch: 0024 lost = 6.416443 ppl = 611.823
    Epoch: 0025 Batch: 50 /134 lost = 6.083096 ppl = 438.384
    Epoch: 0025 Batch: 100 /134 lost = 6.018194 ppl = 410.836
    Valid 4864 samples after epoch: 0025 lost = 6.408552 ppl = 607.014
    Epoch: 0026 Batch: 50 /134 lost = 6.063943 ppl = 430.068
    Epoch: 0026 Batch: 100 /134 lost = 5.998146 ppl = 402.682
    Valid 4864 samples after epoch: 0026 lost = 6.400947 ppl = 602.415
    Epoch: 0027 Batch: 50 /134 lost = 6.046067 ppl = 422.448
    Epoch: 0027 Batch: 100 /134 lost = 5.980003 ppl = 395.442
    Valid 4864 samples after epoch: 0027 lost = 6.394003 ppl = 598.247
    Epoch: 0028 Batch: 50 /134 lost = 6.031278 ppl = 416.247
    Epoch: 0028 Batch: 100 /134 lost = 5.962341 ppl = 388.519
    Valid 4864 samples after epoch: 0028 lost = 6.387710 ppl = 594.494
    Epoch: 0029 Batch: 50 /134 lost = 6.016594 ppl = 410.179
    Epoch: 0029 Batch: 100 /134 lost = 5.944685 ppl = 381.719
    Valid 4864 samples after epoch: 0029 lost = 6.382061 ppl = 591.145
    Epoch: 0030 Batch: 50 /134 lost = 6.002218 ppl = 404.324
    Epoch: 0030 Batch: 100 /134 lost = 5.929065 ppl = 375.803
    Valid 4864 samples after epoch: 0030 lost = 6.375952 ppl = 587.544
    Epoch: 0031 Batch: 50 /134 lost = 5.988615 ppl = 398.862
    Epoch: 0031 Batch: 100 /134 lost = 5.911656 ppl = 369.317
    Valid 4864 samples after epoch: 0031 lost = 6.369353 ppl = 583.68
    Epoch: 0032 Batch: 50 /134 lost = 5.974663 ppl = 393.335
    Epoch: 0032 Batch: 100 /134 lost = 5.895440 ppl = 363.377
    Valid 4864 samples after epoch: 0032 lost = 6.364480 ppl = 580.843
    Epoch: 0033 Batch: 50 /134 lost = 5.961120 ppl = 388.044
    Epoch: 0033 Batch: 100 /134 lost = 5.880411 ppl = 357.956
    Valid 4864 samples after epoch: 0033 lost = 6.360156 ppl = 578.337
    Epoch: 0034 Batch: 50 /134 lost = 5.947966 ppl = 382.973
    Epoch: 0034 Batch: 100 /134 lost = 5.866528 ppl = 353.021
    Valid 4864 samples after epoch: 0034 lost = 6.355946 ppl = 575.907
    Epoch: 0035 Batch: 50 /134 lost = 5.933496 ppl = 377.472
    Epoch: 0035 Batch: 100 /134 lost = 5.847979 ppl = 346.533
    Valid 4864 samples after epoch: 0035 lost = 6.350863 ppl = 572.987
    Epoch: 0036 Batch: 50 /134 lost = 5.919797 ppl = 372.336
    Epoch: 0036 Batch: 100 /134 lost = 5.829162 ppl = 340.074
    Valid 4864 samples after epoch: 0036 lost = 6.347180 ppl = 570.881
    Epoch: 0037 Batch: 50 /134 lost = 5.906757 ppl = 367.512
    Epoch: 0037 Batch: 100 /134 lost = 5.815102 ppl = 335.326
    Valid 4864 samples after epoch: 0037 lost = 6.343758 ppl = 568.93
    Epoch: 0038 Batch: 50 /134 lost = 5.893281 ppl = 362.593
    Epoch: 0038 Batch: 100 /134 lost = 5.798654 ppl = 329.855
    Valid 4864 samples after epoch: 0038 lost = 6.339971 ppl = 566.78
    Epoch: 0039 Batch: 50 /134 lost = 5.878427 ppl = 357.247
    Epoch: 0039 Batch: 100 /134 lost = 5.784951 ppl = 325.366
    Valid 4864 samples after epoch: 0039 lost = 6.337403 ppl = 565.326
    Epoch: 0040 Batch: 50 /134 lost = 5.865041 ppl = 352.497
    Epoch: 0040 Batch: 100 /134 lost = 5.772004 ppl = 321.181
    Valid 4864 samples after epoch: 0040 lost = 6.335118 ppl = 564.036
    Epoch: 0041 Batch: 50 /134 lost = 5.852897 ppl = 348.242
    Epoch: 0041 Batch: 100 /134 lost = 5.760087 ppl = 317.376
    Valid 4864 samples after epoch: 0041 lost = 6.333008 ppl = 562.847
    Epoch: 0042 Batch: 50 /134 lost = 5.842158 ppl = 344.522
    Epoch: 0042 Batch: 100 /134 lost = 5.748622 ppl = 313.758
    Valid 4864 samples after epoch: 0042 lost = 6.332166 ppl = 562.373
    Epoch: 0043 Batch: 50 /134 lost = 5.831809 ppl = 340.975
    Epoch: 0043 Batch: 100 /134 lost = 5.737619 ppl = 310.325
    Valid 4864 samples after epoch: 0043 lost = 6.330807 ppl = 561.61
    Epoch: 0044 Batch: 50 /134 lost = 5.822556 ppl = 337.834
    Epoch: 0044 Batch: 100 /134 lost = 5.727365 ppl = 307.159
    Valid 4864 samples after epoch: 0044 lost = 6.330448 ppl = 561.408
    Epoch: 0045 Batch: 50 /134 lost = 5.813122 ppl = 334.662
    Epoch: 0045 Batch: 100 /134 lost = 5.718082 ppl = 304.321
    Valid 4864 samples after epoch: 0045 lost = 6.330132 ppl = 561.231
    Epoch: 0046 Batch: 50 /134 lost = 5.803871 ppl = 331.581
    Epoch: 0046 Batch: 100 /134 lost = 5.708791 ppl = 301.506
    Valid 4864 samples after epoch: 0046 lost = 6.330431 ppl = 561.399
    Epoch: 0047 Batch: 50 /134 lost = 5.794374 ppl = 328.446
    Epoch: 0047 Batch: 100 /134 lost = 5.700220 ppl = 298.933
    Valid 4864 samples after epoch: 0047 lost = 6.330692 ppl = 561.545
    Epoch: 0048 Batch: 50 /134 lost = 5.785478 ppl = 325.537
    Epoch: 0048 Batch: 100 /134 lost = 5.691474 ppl = 296.33
    Valid 4864 samples after epoch: 0048 lost = 6.331603 ppl = 562.057
    Epoch: 0049 Batch: 50 /134 lost = 5.776742 ppl = 322.706
    Epoch: 0049 Batch: 100 /134 lost = 5.682734 ppl = 293.752
    Valid 4864 samples after epoch: 0049 lost = 6.332820 ppl = 562.741
    Epoch: 0050 Batch: 50 /134 lost = 5.768481 ppl = 320.051
    Epoch: 0050 Batch: 100 /134 lost = 5.673819 ppl = 291.144
    Valid 4864 samples after epoch: 0050 lost = 6.334804 ppl = 563.859
    Epoch: 0051 Batch: 50 /134 lost = 5.760114 ppl = 317.385
    Epoch: 0051 Batch: 100 /134 lost = 5.664709 ppl = 288.504
    Valid 4864 samples after epoch: 0051 lost = 6.335940 ppl = 564.5
    Epoch: 0052 Batch: 50 /134 lost = 5.752951 ppl = 315.119
    Epoch: 0052 Batch: 100 /134 lost = 5.654006 ppl = 285.432
    Valid 4864 samples after epoch: 0052 lost = 6.337858 ppl = 565.584
    Epoch: 0053 Batch: 50 /134 lost = 5.745444 ppl = 312.763
    Epoch: 0053 Batch: 100 /134 lost = 5.645479 ppl = 283.009
    Valid 4864 samples after epoch: 0053 lost = 6.338811 ppl = 566.123
    Epoch: 0054 Batch: 50 /134 lost = 5.739111 ppl = 310.788
    Epoch: 0054 Batch: 100 /134 lost = 5.637916 ppl = 280.877
    Valid 4864 samples after epoch: 0054 lost = 6.341327 ppl = 567.549
    Epoch: 0055 Batch: 50 /134 lost = 5.732170 ppl = 308.638
    Epoch: 0055 Batch: 100 /134 lost = 5.630563 ppl = 278.819
    Valid 4864 samples after epoch: 0055 lost = 6.342824 ppl = 568.399
    Epoch: 0056 Batch: 50 /134 lost = 5.726415 ppl = 306.867
    Epoch: 0056 Batch: 100 /134 lost = 5.624272 ppl = 277.071
    Valid 4864 samples after epoch: 0056 lost = 6.345532 ppl = 569.941
    Epoch: 0057 Batch: 50 /134 lost = 5.720031 ppl = 304.914
    Epoch: 0057 Batch: 100 /134 lost = 5.618255 ppl = 275.408
    Valid 4864 samples after epoch: 0057 lost = 6.341509 ppl = 567.652
    Epoch: 0058 Batch: 50 /134 lost = 5.716419 ppl = 303.815
    Epoch: 0058 Batch: 100 /134 lost = 5.607723 ppl = 272.523
    Valid 4864 samples after epoch: 0058 lost = 6.341242 ppl = 567.501
    Epoch: 0059 Batch: 50 /134 lost = 5.710314 ppl = 301.966
    Epoch: 0059 Batch: 100 /134 lost = 5.602506 ppl = 271.105
    Valid 4864 samples after epoch: 0059 lost = 6.341184 ppl = 567.468
    Epoch: 0060 Batch: 50 /134 lost = 5.705699 ppl = 300.575
    Epoch: 0060 Batch: 100 /134 lost = 5.597611 ppl = 269.781
    Valid 4864 samples after epoch: 0060 lost = 6.343233 ppl = 568.632
    
    Test the RNNLM……………………
    Test 5760 samples with models/rnnlm_only_one_layer_model_epoch60.ckpt……………………
    lost = 6.260655 ppl = 523.562
    