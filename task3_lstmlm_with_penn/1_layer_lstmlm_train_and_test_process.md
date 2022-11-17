```python
!python 1_layer_lstmlm_with_penn_assignment.py
```

    The size of the dictionary is: 7613
    The number of the train batch is: 134
    
    Train the LSTMLM……………………
    TextLSTM(
      (C): Embedding(7613, 128)
      (W_xi): Linear(in_features=128, out_features=5, bias=False)
      (W_xf): Linear(in_features=128, out_features=5, bias=False)
      (W_xo): Linear(in_features=128, out_features=5, bias=False)
      (W_xc): Linear(in_features=128, out_features=5, bias=False)
      (W_hi): Linear(in_features=5, out_features=5, bias=False)
      (W_hf): Linear(in_features=5, out_features=5, bias=False)
      (W_ho): Linear(in_features=5, out_features=5, bias=False)
      (W_hc): Linear(in_features=5, out_features=5, bias=False)
      (sigmoid): Sigmoid()
      (tanh): Tanh()
      (W_hq): Linear(in_features=5, out_features=7613, bias=False)
    )
    Epoch: 0001 Batch: 50 /134 lost = 8.764113 ppl = 6400.39
    Epoch: 0001 Batch: 100 /134 lost = 8.560454 ppl = 5221.05
    Valid 4864 samples after epoch: 0001 lost = 8.393342 ppl = 4417.56
    Epoch: 0002 Batch: 50 /134 lost = 8.113312 ppl = 3338.62
    Epoch: 0002 Batch: 100 /134 lost = 7.861753 ppl = 2596.07
    Valid 4864 samples after epoch: 0002 lost = 7.739386 ppl = 2297.06
    Epoch: 0003 Batch: 50 /134 lost = 7.474248 ppl = 1762.08
    Epoch: 0003 Batch: 100 /134 lost = 7.300035 ppl = 1480.35
    Valid 4864 samples after epoch: 0003 lost = 7.262503 ppl = 1425.82
    Epoch: 0004 Batch: 50 /134 lost = 7.039638 ppl = 1140.97
    Epoch: 0004 Batch: 100 /134 lost = 6.926620 ppl = 1019.04
    Valid 4864 samples after epoch: 0004 lost = 6.959324 ppl = 1052.92
    Epoch: 0005 Batch: 50 /134 lost = 6.768075 ppl = 869.637
    Epoch: 0005 Batch: 100 /134 lost = 6.697480 ppl = 810.361
    Valid 4864 samples after epoch: 0005 lost = 6.784769 ppl = 884.276
    Epoch: 0006 Batch: 50 /134 lost = 6.612439 ppl = 744.296
    Epoch: 0006 Batch: 100 /134 lost = 6.568187 ppl = 712.078
    Valid 4864 samples after epoch: 0006 lost = 6.693582 ppl = 807.208
    Epoch: 0007 Batch: 50 /134 lost = 6.527956 ppl = 683.999
    Epoch: 0007 Batch: 100 /134 lost = 6.497767 ppl = 663.658
    Valid 4864 samples after epoch: 0007 lost = 6.648185 ppl = 771.383
    Epoch: 0008 Batch: 50 /134 lost = 6.482258 ppl = 653.445
    Epoch: 0008 Batch: 100 /134 lost = 6.459079 ppl = 638.473
    Valid 4864 samples after epoch: 0008 lost = 6.625099 ppl = 753.779
    Epoch: 0009 Batch: 50 /134 lost = 6.452636 ppl = 634.372
    Epoch: 0009 Batch: 100 /134 lost = 6.435332 ppl = 623.49
    Valid 4864 samples after epoch: 0009 lost = 6.611962 ppl = 743.942
    Epoch: 0010 Batch: 50 /134 lost = 6.430558 ppl = 620.52
    Epoch: 0010 Batch: 100 /134 lost = 6.417476 ppl = 612.455
    Valid 4864 samples after epoch: 0010 lost = 6.603872 ppl = 737.947
    Epoch: 0011 Batch: 50 /134 lost = 6.413572 ppl = 610.069
    Epoch: 0011 Batch: 100 /134 lost = 6.393893 ppl = 598.181
    Valid 4864 samples after epoch: 0011 lost = 6.590991 ppl = 728.502
    Epoch: 0012 Batch: 50 /134 lost = 6.395634 ppl = 599.223
    Epoch: 0012 Batch: 100 /134 lost = 6.378541 ppl = 589.068
    Valid 4864 samples after epoch: 0012 lost = 6.586955 ppl = 725.568
    Epoch: 0013 Batch: 50 /134 lost = 6.384496 ppl = 592.586
    Epoch: 0013 Batch: 100 /134 lost = 6.361850 ppl = 579.317
    Valid 4864 samples after epoch: 0013 lost = 6.583139 ppl = 722.805
    Epoch: 0014 Batch: 50 /134 lost = 6.375984 ppl = 587.563
    Epoch: 0014 Batch: 100 /134 lost = 6.350145 ppl = 572.576
    Valid 4864 samples after epoch: 0014 lost = 6.582147 ppl = 722.088
    Epoch: 0015 Batch: 50 /134 lost = 6.365971 ppl = 581.709
    Epoch: 0015 Batch: 100 /134 lost = 6.339929 ppl = 566.756
    Valid 4864 samples after epoch: 0015 lost = 6.581103 ppl = 721.334
    Epoch: 0016 Batch: 50 /134 lost = 6.356205 ppl = 576.056
    Epoch: 0016 Batch: 100 /134 lost = 6.329672 ppl = 560.973
    Valid 4864 samples after epoch: 0016 lost = 6.578187 ppl = 719.234
    Epoch: 0017 Batch: 50 /134 lost = 6.346712 ppl = 570.614
    Epoch: 0017 Batch: 100 /134 lost = 6.321855 ppl = 556.604
    Valid 4864 samples after epoch: 0017 lost = 6.577877 ppl = 719.011
    Epoch: 0018 Batch: 50 /134 lost = 6.338868 ppl = 566.155
    Epoch: 0018 Batch: 100 /134 lost = 6.314804 ppl = 552.694
    Valid 4864 samples after epoch: 0018 lost = 6.577877 ppl = 719.011
    Epoch: 0019 Batch: 50 /134 lost = 6.328376 ppl = 560.246
    Epoch: 0019 Batch: 100 /134 lost = 6.302441 ppl = 545.903
    Valid 4864 samples after epoch: 0019 lost = 6.571415 ppl = 714.38
    Epoch: 0020 Batch: 50 /134 lost = 6.319255 ppl = 555.159
    Epoch: 0020 Batch: 100 /134 lost = 6.296216 ppl = 542.515
    Valid 4864 samples after epoch: 0020 lost = 6.564849 ppl = 709.704
    Epoch: 0021 Batch: 50 /134 lost = 6.308022 ppl = 548.958
    Epoch: 0021 Batch: 100 /134 lost = 6.287255 ppl = 537.675
    Valid 4864 samples after epoch: 0021 lost = 6.563176 ppl = 708.519
    Epoch: 0022 Batch: 50 /134 lost = 6.298761 ppl = 543.898
    Epoch: 0022 Batch: 100 /134 lost = 6.270242 ppl = 528.605
    Valid 4864 samples after epoch: 0022 lost = 6.557936 ppl = 704.815
    Epoch: 0023 Batch: 50 /134 lost = 6.288295 ppl = 538.235
    Epoch: 0023 Batch: 100 /134 lost = 6.256631 ppl = 521.459
    Valid 4864 samples after epoch: 0023 lost = 6.553810 ppl = 701.913
    Epoch: 0024 Batch: 50 /134 lost = 6.276536 ppl = 531.943
    Epoch: 0024 Batch: 100 /134 lost = 6.242927 ppl = 514.362
    Valid 4864 samples after epoch: 0024 lost = 6.550958 ppl = 699.914
    Epoch: 0025 Batch: 50 /134 lost = 6.265718 ppl = 526.219
    Epoch: 0025 Batch: 100 /134 lost = 6.229879 ppl = 507.694
    Valid 4864 samples after epoch: 0025 lost = 6.548652 ppl = 698.302
    Epoch: 0026 Batch: 50 /134 lost = 6.253701 ppl = 519.933
    Epoch: 0026 Batch: 100 /134 lost = 6.217571 ppl = 501.484
    Valid 4864 samples after epoch: 0026 lost = 6.545985 ppl = 696.442
    Epoch: 0027 Batch: 50 /134 lost = 6.242042 ppl = 513.907
    Epoch: 0027 Batch: 100 /134 lost = 6.204174 ppl = 494.81
    Valid 4864 samples after epoch: 0027 lost = 6.535092 ppl = 688.897
    Epoch: 0028 Batch: 50 /134 lost = 6.216013 ppl = 500.703
    Epoch: 0028 Batch: 100 /134 lost = 6.185581 ppl = 485.695
    Valid 4864 samples after epoch: 0028 lost = 6.529415 ppl = 684.997
    Epoch: 0029 Batch: 50 /134 lost = 6.201210 ppl = 493.345
    Epoch: 0029 Batch: 100 /134 lost = 6.171102 ppl = 478.713
    Valid 4864 samples after epoch: 0029 lost = 6.524741 ppl = 681.803
    Epoch: 0030 Batch: 50 /134 lost = 6.191258 ppl = 488.46
    Epoch: 0030 Batch: 100 /134 lost = 6.156968 ppl = 471.995
    Valid 4864 samples after epoch: 0030 lost = 6.520941 ppl = 679.217
    Epoch: 0031 Batch: 50 /134 lost = 6.180199 ppl = 483.088
    Epoch: 0031 Batch: 100 /134 lost = 6.143183 ppl = 465.533
    Valid 4864 samples after epoch: 0031 lost = 6.517750 ppl = 677.053
    Epoch: 0032 Batch: 50 /134 lost = 6.169464 ppl = 477.93
    Epoch: 0032 Batch: 100 /134 lost = 6.129080 ppl = 459.014
    Valid 4864 samples after epoch: 0032 lost = 6.514021 ppl = 674.533
    Epoch: 0033 Batch: 50 /134 lost = 6.158387 ppl = 472.665
    Epoch: 0033 Batch: 100 /134 lost = 6.115629 ppl = 452.881
    Valid 4864 samples after epoch: 0033 lost = 6.512272 ppl = 673.355
    Epoch: 0034 Batch: 50 /134 lost = 6.147639 ppl = 467.612
    Epoch: 0034 Batch: 100 /134 lost = 6.101694 ppl = 446.614
    Valid 4864 samples after epoch: 0034 lost = 6.507977 ppl = 670.468
    Epoch: 0035 Batch: 50 /134 lost = 6.136068 ppl = 462.232
    Epoch: 0035 Batch: 100 /134 lost = 6.080598 ppl = 437.291
    Valid 4864 samples after epoch: 0035 lost = 6.505791 ppl = 669.004
    Epoch: 0036 Batch: 50 /134 lost = 6.122169 ppl = 455.852
    Epoch: 0036 Batch: 100 /134 lost = 6.060952 ppl = 428.784
    Valid 4864 samples after epoch: 0036 lost = 6.501891 ppl = 666.4
    Epoch: 0037 Batch: 50 /134 lost = 6.108071 ppl = 449.471
    Epoch: 0037 Batch: 100 /134 lost = 6.043548 ppl = 421.386
    Valid 4864 samples after epoch: 0037 lost = 6.499819 ppl = 665.021
    Epoch: 0038 Batch: 50 /134 lost = 6.093817 ppl = 443.109
    Epoch: 0038 Batch: 100 /134 lost = 6.026992 ppl = 414.466
    Valid 4864 samples after epoch: 0038 lost = 6.497140 ppl = 663.242
    Epoch: 0039 Batch: 50 /134 lost = 6.079057 ppl = 436.617
    Epoch: 0039 Batch: 100 /134 lost = 6.009484 ppl = 407.273
    Valid 4864 samples after epoch: 0039 lost = 6.493813 ppl = 661.039
    Epoch: 0040 Batch: 50 /134 lost = 6.063367 ppl = 429.82
    Epoch: 0040 Batch: 100 /134 lost = 5.992822 ppl = 400.543
    Valid 4864 samples after epoch: 0040 lost = 6.492877 ppl = 660.421
    Epoch: 0041 Batch: 50 /134 lost = 6.050817 ppl = 424.459
    Epoch: 0041 Batch: 100 /134 lost = 5.977750 ppl = 394.552
    Valid 4864 samples after epoch: 0041 lost = 6.490971 ppl = 659.163
    Epoch: 0042 Batch: 50 /134 lost = 6.035093 ppl = 417.838
    Epoch: 0042 Batch: 100 /134 lost = 5.962359 ppl = 388.526
    Valid 4864 samples after epoch: 0042 lost = 6.491395 ppl = 659.443
    Epoch: 0043 Batch: 50 /134 lost = 6.022286 ppl = 412.521
    Epoch: 0043 Batch: 100 /134 lost = 5.947373 ppl = 382.747
    Valid 4864 samples after epoch: 0043 lost = 6.493861 ppl = 661.071
    Epoch: 0044 Batch: 50 /134 lost = 6.010208 ppl = 407.568
    Epoch: 0044 Batch: 100 /134 lost = 5.933412 ppl = 377.44
    Valid 4864 samples after epoch: 0044 lost = 6.492045 ppl = 659.871
    Epoch: 0045 Batch: 50 /134 lost = 5.994466 ppl = 401.203
    Epoch: 0045 Batch: 100 /134 lost = 5.919090 ppl = 372.073
    Valid 4864 samples after epoch: 0045 lost = 6.493021 ppl = 660.516
    Epoch: 0046 Batch: 50 /134 lost = 5.982204 ppl = 396.313
    Epoch: 0046 Batch: 100 /134 lost = 5.904392 ppl = 366.644
    Valid 4864 samples after epoch: 0046 lost = 6.492120 ppl = 659.921
    Epoch: 0047 Batch: 50 /134 lost = 5.968430 ppl = 390.892
    Epoch: 0047 Batch: 100 /134 lost = 5.891328 ppl = 361.886
    Valid 4864 samples after epoch: 0047 lost = 6.491121 ppl = 659.262
    Epoch: 0048 Batch: 50 /134 lost = 5.953307 ppl = 385.025
    Epoch: 0048 Batch: 100 /134 lost = 5.877536 ppl = 356.929
    Valid 4864 samples after epoch: 0048 lost = 6.490247 ppl = 658.686
    Epoch: 0049 Batch: 50 /134 lost = 5.939493 ppl = 379.742
    Epoch: 0049 Batch: 100 /134 lost = 5.862689 ppl = 351.669
    Valid 4864 samples after epoch: 0049 lost = 6.490746 ppl = 659.015
    Epoch: 0050 Batch: 50 /134 lost = 5.925624 ppl = 374.512
    Epoch: 0050 Batch: 100 /134 lost = 5.848547 ppl = 346.73
    Valid 4864 samples after epoch: 0050 lost = 6.489280 ppl = 658.05
    Epoch: 0051 Batch: 50 /134 lost = 5.911274 ppl = 369.176
    Epoch: 0051 Batch: 100 /134 lost = 5.833873 ppl = 341.68
    Valid 4864 samples after epoch: 0051 lost = 6.487807 ppl = 657.081
    Epoch: 0052 Batch: 50 /134 lost = 5.896573 ppl = 363.788
    Epoch: 0052 Batch: 100 /134 lost = 5.820286 ppl = 337.069
    Valid 4864 samples after epoch: 0052 lost = 6.489392 ppl = 658.123
    Epoch: 0053 Batch: 50 /134 lost = 5.883865 ppl = 359.195
    Epoch: 0053 Batch: 100 /134 lost = 5.806839 ppl = 332.566
    Valid 4864 samples after epoch: 0053 lost = 6.490272 ppl = 658.702
    Epoch: 0054 Batch: 50 /134 lost = 5.869758 ppl = 354.163
    Epoch: 0054 Batch: 100 /134 lost = 5.795041 ppl = 328.666
    Valid 4864 samples after epoch: 0054 lost = 6.491751 ppl = 659.677
    Epoch: 0055 Batch: 50 /134 lost = 5.856802 ppl = 349.604
    Epoch: 0055 Batch: 100 /134 lost = 5.783404 ppl = 324.863
    Valid 4864 samples after epoch: 0055 lost = 6.492919 ppl = 660.449
    Epoch: 0056 Batch: 50 /134 lost = 5.842643 ppl = 344.689
    Epoch: 0056 Batch: 100 /134 lost = 5.772574 ppl = 321.364
    Valid 4864 samples after epoch: 0056 lost = 6.490127 ppl = 658.607
    Epoch: 0057 Batch: 50 /134 lost = 5.827961 ppl = 339.665
    Epoch: 0057 Batch: 100 /134 lost = 5.761318 ppl = 317.767
    Valid 4864 samples after epoch: 0057 lost = 6.492216 ppl = 659.984
    Epoch: 0058 Batch: 50 /134 lost = 5.818452 ppl = 336.451
    Epoch: 0058 Batch: 100 /134 lost = 5.751573 ppl = 314.685
    Valid 4864 samples after epoch: 0058 lost = 6.495927 ppl = 662.438
    Epoch: 0059 Batch: 50 /134 lost = 5.806273 ppl = 332.378
    Epoch: 0059 Batch: 100 /134 lost = 5.743273 ppl = 312.084
    Valid 4864 samples after epoch: 0059 lost = 6.497121 ppl = 663.229
    Epoch: 0060 Batch: 50 /134 lost = 5.796885 ppl = 329.272
    Epoch: 0060 Batch: 100 /134 lost = 5.733588 ppl = 309.076
    Valid 4864 samples after epoch: 0060 lost = 6.500774 ppl = 665.657
    
    Test the LSTMLM……………………
    Test 5760 samples with models/1_layer_lstmlm_model_epoch60.ckpt……………………
    lost = 6.401304 ppl = 602.63
    
