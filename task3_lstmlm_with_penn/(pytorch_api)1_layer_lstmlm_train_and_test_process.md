```python
!python (pytorch_api)1_layer_lstmlm_with_penn_assignment.py
```

    The size of the dictionary is: 7613
    The number of the train batch is: 134
    
    Train the LSTMLM……………………
    TextLSTM(
      (C): Embedding(7613, 128)
      (LSTM): LSTM(128, 5)
      (W): Linear(in_features=5, out_features=7613, bias=False)
    )
    Epoch: 0001 Batch: 50 /134 lost = 8.902255 ppl = 7348.53
    Epoch: 0001 Batch: 100 /134 lost = 8.807341 ppl = 6683.12
    Valid 4864 samples after epoch: 0001 lost = 8.722815 ppl = 6141.44
    Epoch: 0002 Batch: 50 /134 lost = 8.544079 ppl = 5136.25
    Epoch: 0002 Batch: 100 /134 lost = 8.298601 ppl = 4018.25
    Valid 4864 samples after epoch: 0002 lost = 8.135667 ppl = 3414.09
    Epoch: 0003 Batch: 50 /134 lost = 7.745963 ppl = 2312.22
    Epoch: 0003 Batch: 100 /134 lost = 7.423221 ppl = 1674.42
    Valid 4864 samples after epoch: 0003 lost = 7.317796 ppl = 1506.88
    Epoch: 0004 Batch: 50 /134 lost = 6.985383 ppl = 1080.72
    Epoch: 0004 Batch: 100 /134 lost = 6.817431 ppl = 913.635
    Valid 4864 samples after epoch: 0004 lost = 6.879521 ppl = 972.161
    Epoch: 0005 Batch: 50 /134 lost = 6.642229 ppl = 766.802
    Epoch: 0005 Batch: 100 /134 lost = 6.574686 ppl = 716.721
    Valid 4864 samples after epoch: 0005 lost = 6.725711 ppl = 833.565
    Epoch: 0006 Batch: 50 /134 lost = 6.509105 ppl = 671.226
    Epoch: 0006 Batch: 100 /134 lost = 6.480493 ppl = 652.292
    Valid 4864 samples after epoch: 0006 lost = 6.672270 ppl = 790.187
    Epoch: 0007 Batch: 50 /134 lost = 6.454483 ppl = 635.545
    Epoch: 0007 Batch: 100 /134 lost = 6.439851 ppl = 626.314
    Valid 4864 samples after epoch: 0007 lost = 6.651783 ppl = 774.163
    Epoch: 0008 Batch: 50 /134 lost = 6.427477 ppl = 618.611
    Epoch: 0008 Batch: 100 /134 lost = 6.416714 ppl = 611.989
    Valid 4864 samples after epoch: 0008 lost = 6.643033 ppl = 767.419
    Epoch: 0009 Batch: 50 /134 lost = 6.409840 ppl = 607.796
    Epoch: 0009 Batch: 100 /134 lost = 6.400077 ppl = 601.892
    Valid 4864 samples after epoch: 0009 lost = 6.638135 ppl = 763.67
    Epoch: 0010 Batch: 50 /134 lost = 6.397213 ppl = 600.17
    Epoch: 0010 Batch: 100 /134 lost = 6.385226 ppl = 593.019
    Valid 4864 samples after epoch: 0010 lost = 6.633861 ppl = 760.412
    Epoch: 0011 Batch: 50 /134 lost = 6.382553 ppl = 591.435
    Epoch: 0011 Batch: 100 /134 lost = 6.372360 ppl = 585.438
    Valid 4864 samples after epoch: 0011 lost = 6.630577 ppl = 757.919
    Epoch: 0012 Batch: 50 /134 lost = 6.366876 ppl = 582.236
    Epoch: 0012 Batch: 100 /134 lost = 6.347458 ppl = 571.039
    Valid 4864 samples after epoch: 0012 lost = 6.612564 ppl = 744.389
    Epoch: 0013 Batch: 50 /134 lost = 6.350230 ppl = 572.625
    Epoch: 0013 Batch: 100 /134 lost = 6.327637 ppl = 559.832
    Valid 4864 samples after epoch: 0013 lost = 6.607352 ppl = 740.519
    Epoch: 0014 Batch: 50 /134 lost = 6.335190 ppl = 564.076
    Epoch: 0014 Batch: 100 /134 lost = 6.310266 ppl = 550.192
    Valid 4864 samples after epoch: 0014 lost = 6.598221 ppl = 733.789
    Epoch: 0015 Batch: 50 /134 lost = 6.322818 ppl = 557.141
    Epoch: 0015 Batch: 100 /134 lost = 6.294872 ppl = 541.787
    Valid 4864 samples after epoch: 0015 lost = 6.593609 ppl = 730.412
    Epoch: 0016 Batch: 50 /134 lost = 6.310810 ppl = 550.49
    Epoch: 0016 Batch: 100 /134 lost = 6.281281 ppl = 534.473
    Valid 4864 samples after epoch: 0016 lost = 6.589000 ppl = 727.054
    Epoch: 0017 Batch: 50 /134 lost = 6.295695 ppl = 542.233
    Epoch: 0017 Batch: 100 /134 lost = 6.263443 ppl = 525.024
    Valid 4864 samples after epoch: 0017 lost = 6.582157 ppl = 722.095
    Epoch: 0018 Batch: 50 /134 lost = 6.280514 ppl = 534.063
    Epoch: 0018 Batch: 100 /134 lost = 6.249141 ppl = 517.568
    Valid 4864 samples after epoch: 0018 lost = 6.579259 ppl = 720.005
    Epoch: 0019 Batch: 50 /134 lost = 6.266355 ppl = 526.554
    Epoch: 0019 Batch: 100 /134 lost = 6.234742 ppl = 510.169
    Valid 4864 samples after epoch: 0019 lost = 6.576751 ppl = 718.202
    Epoch: 0020 Batch: 50 /134 lost = 6.253586 ppl = 519.874
    Epoch: 0020 Batch: 100 /134 lost = 6.220319 ppl = 502.864
    Valid 4864 samples after epoch: 0020 lost = 6.572276 ppl = 714.995
    Epoch: 0021 Batch: 50 /134 lost = 6.238779 ppl = 512.232
    Epoch: 0021 Batch: 100 /134 lost = 6.207247 ppl = 496.333
    Valid 4864 samples after epoch: 0021 lost = 6.570622 ppl = 713.814
    Epoch: 0022 Batch: 50 /134 lost = 6.227691 ppl = 506.585
    Epoch: 0022 Batch: 100 /134 lost = 6.195641 ppl = 490.606
    Valid 4864 samples after epoch: 0022 lost = 6.569817 ppl = 713.24
    Epoch: 0023 Batch: 50 /134 lost = 6.215829 ppl = 500.611
    Epoch: 0023 Batch: 100 /134 lost = 6.181947 ppl = 483.933
    Valid 4864 samples after epoch: 0023 lost = 6.566509 ppl = 710.884
    Epoch: 0024 Batch: 50 /134 lost = 6.200320 ppl = 492.907
    Epoch: 0024 Batch: 100 /134 lost = 6.168594 ppl = 477.514
    Valid 4864 samples after epoch: 0024 lost = 6.565988 ppl = 710.513
    Epoch: 0025 Batch: 50 /134 lost = 6.185235 ppl = 485.527
    Epoch: 0025 Batch: 100 /134 lost = 6.155624 ppl = 471.361
    Valid 4864 samples after epoch: 0025 lost = 6.565069 ppl = 709.861
    Epoch: 0026 Batch: 50 /134 lost = 6.170511 ppl = 478.431
    Epoch: 0026 Batch: 100 /134 lost = 6.128734 ppl = 458.855
    Valid 4864 samples after epoch: 0026 lost = 6.559743 ppl = 706.09
    Epoch: 0027 Batch: 50 /134 lost = 6.155087 ppl = 471.108
    Epoch: 0027 Batch: 100 /134 lost = 6.115776 ppl = 452.947
    Valid 4864 samples after epoch: 0027 lost = 6.558117 ppl = 704.943
    Epoch: 0028 Batch: 50 /134 lost = 6.142272 ppl = 465.109
    Epoch: 0028 Batch: 100 /134 lost = 6.101391 ppl = 446.478
    Valid 4864 samples after epoch: 0028 lost = 6.556617 ppl = 703.886
    Epoch: 0029 Batch: 50 /134 lost = 6.130114 ppl = 459.489
    Epoch: 0029 Batch: 100 /134 lost = 6.085809 ppl = 439.575
    Valid 4864 samples after epoch: 0029 lost = 6.556809 ppl = 704.021
    Epoch: 0030 Batch: 50 /134 lost = 6.117547 ppl = 453.75
    Epoch: 0030 Batch: 100 /134 lost = 6.069911 ppl = 432.642
    Valid 4864 samples after epoch: 0030 lost = 6.553248 ppl = 701.519
    Epoch: 0031 Batch: 50 /134 lost = 6.101085 ppl = 446.342
    Epoch: 0031 Batch: 100 /134 lost = 6.055584 ppl = 426.488
    Valid 4864 samples after epoch: 0031 lost = 6.553130 ppl = 701.436
    Epoch: 0032 Batch: 50 /134 lost = 6.087836 ppl = 440.467
    Epoch: 0032 Batch: 100 /134 lost = 6.048122 ppl = 423.317
    Valid 4864 samples after epoch: 0032 lost = 6.551393 ppl = 700.219
    Epoch: 0033 Batch: 50 /134 lost = 6.077395 ppl = 435.892
    Epoch: 0033 Batch: 100 /134 lost = 6.030842 ppl = 416.065
    Valid 4864 samples after epoch: 0033 lost = 6.547521 ppl = 697.513
    Epoch: 0034 Batch: 50 /134 lost = 6.068565 ppl = 432.06
    Epoch: 0034 Batch: 100 /134 lost = 6.014868 ppl = 409.472
    Valid 4864 samples after epoch: 0034 lost = 6.547415 ppl = 697.439
    Epoch: 0035 Batch: 50 /134 lost = 6.055888 ppl = 426.618
    Epoch: 0035 Batch: 100 /134 lost = 6.001537 ppl = 404.049
    Valid 4864 samples after epoch: 0035 lost = 6.548918 ppl = 698.488
    Epoch: 0036 Batch: 50 /134 lost = 6.045244 ppl = 422.101
    Epoch: 0036 Batch: 100 /134 lost = 5.989396 ppl = 399.173
    Valid 4864 samples after epoch: 0036 lost = 6.549320 ppl = 698.769
    Epoch: 0037 Batch: 50 /134 lost = 6.030765 ppl = 416.033
    Epoch: 0037 Batch: 100 /134 lost = 5.975854 ppl = 393.804
    Valid 4864 samples after epoch: 0037 lost = 6.550493 ppl = 699.589
    Epoch: 0038 Batch: 50 /134 lost = 6.015644 ppl = 409.789
    Epoch: 0038 Batch: 100 /134 lost = 5.965629 ppl = 389.798
    Valid 4864 samples after epoch: 0038 lost = 6.551441 ppl = 700.252
    Epoch: 0039 Batch: 50 /134 lost = 6.004798 ppl = 405.369
    Epoch: 0039 Batch: 100 /134 lost = 5.953871 ppl = 385.242
    Valid 4864 samples after epoch: 0039 lost = 6.552709 ppl = 701.141
    Epoch: 0040 Batch: 50 /134 lost = 5.994116 ppl = 401.062
    Epoch: 0040 Batch: 100 /134 lost = 5.942885 ppl = 381.033
    Valid 4864 samples after epoch: 0040 lost = 6.552086 ppl = 700.704
    Epoch: 0041 Batch: 50 /134 lost = 5.986573 ppl = 398.048
    Epoch: 0041 Batch: 100 /134 lost = 5.932364 ppl = 377.045
    Valid 4864 samples after epoch: 0041 lost = 6.553176 ppl = 701.468
    Epoch: 0042 Batch: 50 /134 lost = 5.976767 ppl = 394.164
    Epoch: 0042 Batch: 100 /134 lost = 5.921338 ppl = 372.91
    Valid 4864 samples after epoch: 0042 lost = 6.553870 ppl = 701.956
    Epoch: 0043 Batch: 50 /134 lost = 5.968225 ppl = 390.812
    Epoch: 0043 Batch: 100 /134 lost = 5.910091 ppl = 368.74
    Valid 4864 samples after epoch: 0043 lost = 6.556084 ppl = 703.511
    Epoch: 0044 Batch: 50 /134 lost = 5.959482 ppl = 387.409
    Epoch: 0044 Batch: 100 /134 lost = 5.900546 ppl = 365.237
    Valid 4864 samples after epoch: 0044 lost = 6.555719 ppl = 703.254
    Epoch: 0045 Batch: 50 /134 lost = 5.950495 ppl = 383.943
    Epoch: 0045 Batch: 100 /134 lost = 5.890555 ppl = 361.606
    Valid 4864 samples after epoch: 0045 lost = 6.558481 ppl = 705.2
    Epoch: 0046 Batch: 50 /134 lost = 5.939724 ppl = 379.83
    Epoch: 0046 Batch: 100 /134 lost = 5.876805 ppl = 356.668
    Valid 4864 samples after epoch: 0046 lost = 6.559002 ppl = 705.567
    Epoch: 0047 Batch: 50 /134 lost = 5.924415 ppl = 374.06
    Epoch: 0047 Batch: 100 /134 lost = 5.865352 ppl = 352.606
    Valid 4864 samples after epoch: 0047 lost = 6.560370 ppl = 706.533
    Epoch: 0048 Batch: 50 /134 lost = 5.913874 ppl = 370.137
    Epoch: 0048 Batch: 100 /134 lost = 5.854358 ppl = 348.751
    Valid 4864 samples after epoch: 0048 lost = 6.562788 ppl = 708.244
    Epoch: 0049 Batch: 50 /134 lost = 5.904059 ppl = 366.522
    Epoch: 0049 Batch: 100 /134 lost = 5.841793 ppl = 344.396
    Valid 4864 samples after epoch: 0049 lost = 6.564429 ppl = 709.407
    Epoch: 0050 Batch: 50 /134 lost = 5.895092 ppl = 363.25
    Epoch: 0050 Batch: 100 /134 lost = 5.830560 ppl = 340.549
    Valid 4864 samples after epoch: 0050 lost = 6.566981 ppl = 711.22
    Epoch: 0051 Batch: 50 /134 lost = 5.886898 ppl = 360.286
    Epoch: 0051 Batch: 100 /134 lost = 5.818709 ppl = 336.537
    Valid 4864 samples after epoch: 0051 lost = 6.569555 ppl = 713.053
    Epoch: 0052 Batch: 50 /134 lost = 5.879527 ppl = 357.64
    Epoch: 0052 Batch: 100 /134 lost = 5.810230 ppl = 333.696
    Valid 4864 samples after epoch: 0052 lost = 6.571628 ppl = 714.532
    Epoch: 0053 Batch: 50 /134 lost = 5.871787 ppl = 354.882
    Epoch: 0053 Batch: 100 /134 lost = 5.801166 ppl = 330.685
    Valid 4864 samples after epoch: 0053 lost = 6.574357 ppl = 716.485
    Epoch: 0054 Batch: 50 /134 lost = 5.861343 ppl = 351.196
    Epoch: 0054 Batch: 100 /134 lost = 5.791573 ppl = 327.528
    Valid 4864 samples after epoch: 0054 lost = 6.574254 ppl = 716.411
    Epoch: 0055 Batch: 50 /134 lost = 5.850592 ppl = 347.44
    Epoch: 0055 Batch: 100 /134 lost = 5.783313 ppl = 324.834
    Valid 4864 samples after epoch: 0055 lost = 6.576979 ppl = 718.366
    Epoch: 0056 Batch: 50 /134 lost = 5.840537 ppl = 343.964
    Epoch: 0056 Batch: 100 /134 lost = 5.773129 ppl = 321.542
    Valid 4864 samples after epoch: 0056 lost = 6.579079 ppl = 719.876
    Epoch: 0057 Batch: 50 /134 lost = 5.831630 ppl = 340.914
    Epoch: 0057 Batch: 100 /134 lost = 5.766088 ppl = 319.286
    Valid 4864 samples after epoch: 0057 lost = 6.581863 ppl = 721.883
    Epoch: 0058 Batch: 50 /134 lost = 5.824429 ppl = 338.468
    Epoch: 0058 Batch: 100 /134 lost = 5.760106 ppl = 317.382
    Valid 4864 samples after epoch: 0058 lost = 6.583244 ppl = 722.881
    Epoch: 0059 Batch: 50 /134 lost = 5.817660 ppl = 336.185
    Epoch: 0059 Batch: 100 /134 lost = 5.753476 ppl = 315.285
    Valid 4864 samples after epoch: 0059 lost = 6.585478 ppl = 724.497
    Epoch: 0060 Batch: 50 /134 lost = 5.809583 ppl = 333.48
    Epoch: 0060 Batch: 100 /134 lost = 5.741693 ppl = 311.592
    Valid 4864 samples after epoch: 0060 lost = 6.588805 ppl = 726.912
    
    Test the LSTMLM……………………
    Test 5760 samples with models/(pytorch_api)1_layer_lstmlm_model_epoch60.ckpt……………………
    lost = 6.472979 ppl = 647.41
    