```python
!python n_layers_rnnlm_with_penn_assignment(default_n=3).py
```

    The size of the dictionary is: 7613
    The number of the train batch is: 134
    
    Train the RNNLM……………………
    TextRNN(
      (C): Embedding(7613, 128)
      (W_ax): Linear(in_features=128, out_features=5, bias=False)
      (tanh): Tanh()
      (W): Linear(in_features=5, out_features=7613, bias=False)
    )
    Epoch: 0001 Batch: 50 /134 lost = 8.767695 ppl = 6423.35
    Epoch: 0001 Batch: 100 /134 lost = 8.619022 ppl = 5535.97
    Valid 4864 samples after epoch: 0001 lost = 8.533462 ppl = 5082.01
    Saving best model
    Epoch: 0002 Batch: 50 /134 lost = 8.305187 ppl = 4044.8
    Epoch: 0002 Batch: 100 /134 lost = 8.170546 ppl = 3535.27
    Valid 4864 samples after epoch: 0002 lost = 8.112723 ppl = 3336.65
    Saving best model
    Epoch: 0003 Batch: 50 /134 lost = 7.863441 ppl = 2600.45
    Epoch: 0003 Batch: 100 /134 lost = 7.742763 ppl = 2304.83
    Valid 4864 samples after epoch: 0003 lost = 7.720596 ppl = 2254.3
    Saving best model
    Epoch: 0004 Batch: 50 /134 lost = 7.466867 ppl = 1749.12
    Epoch: 0004 Batch: 100 /134 lost = 7.363802 ppl = 1577.82
    Valid 4864 samples after epoch: 0004 lost = 7.389082 ppl = 1618.22
    Saving best model
    Epoch: 0005 Batch: 50 /134 lost = 7.139444 ppl = 1260.73
    Epoch: 0005 Batch: 100 /134 lost = 7.058592 ppl = 1162.81
    Valid 4864 samples after epoch: 0005 lost = 7.129408 ppl = 1248.14
    Saving best model
    Epoch: 0006 Batch: 50 /134 lost = 6.886751 ppl = 979.215
    Epoch: 0006 Batch: 100 /134 lost = 6.825836 ppl = 921.346
    Valid 4864 samples after epoch: 0006 lost = 6.937956 ppl = 1030.66
    Saving best model
    Epoch: 0007 Batch: 50 /134 lost = 6.702571 ppl = 814.498
    Epoch: 0007 Batch: 100 /134 lost = 6.657848 ppl = 778.873
    Valid 4864 samples after epoch: 0007 lost = 6.807841 ppl = 904.915
    Saving best model
    Epoch: 0008 Batch: 50 /134 lost = 6.579893 ppl = 720.462
    Epoch: 0008 Batch: 100 /134 lost = 6.542741 ppl = 694.187
    Valid 4864 samples after epoch: 0008 lost = 6.726735 ppl = 834.419
    Saving best model
    Epoch: 0009 Batch: 50 /134 lost = 6.502655 ppl = 666.91
    Epoch: 0009 Batch: 100 /134 lost = 6.472764 ppl = 647.27
    Valid 4864 samples after epoch: 0009 lost = 6.680600 ppl = 796.797
    Saving best model
    Epoch: 0010 Batch: 50 /134 lost = 6.456500 ppl = 636.828
    Epoch: 0010 Batch: 100 /134 lost = 6.432408 ppl = 621.669
    Valid 4864 samples after epoch: 0010 lost = 6.655293 ppl = 776.885
    Saving best model
    Epoch: 0011 Batch: 50 /134 lost = 6.430482 ppl = 620.473
    Epoch: 0011 Batch: 100 /134 lost = 6.405883 ppl = 605.396
    Valid 4864 samples after epoch: 0011 lost = 6.642588 ppl = 767.078
    Saving best model
    Epoch: 0012 Batch: 50 /134 lost = 6.415274 ppl = 611.108
    Epoch: 0012 Batch: 100 /134 lost = 6.388537 ppl = 594.986
    Valid 4864 samples after epoch: 0012 lost = 6.635537 ppl = 761.688
    Saving best model
    Epoch: 0013 Batch: 50 /134 lost = 6.404545 ppl = 604.587
    Epoch: 0013 Batch: 100 /134 lost = 6.376174 ppl = 587.675
    Valid 4864 samples after epoch: 0013 lost = 6.631826 ppl = 758.867
    Saving best model
    Epoch: 0014 Batch: 50 /134 lost = 6.396040 ppl = 599.466
    Epoch: 0014 Batch: 100 /134 lost = 6.366964 ppl = 582.287
    Valid 4864 samples after epoch: 0014 lost = 6.628215 ppl = 756.131
    Saving best model
    Epoch: 0015 Batch: 50 /134 lost = 6.387754 ppl = 594.52
    Epoch: 0015 Batch: 100 /134 lost = 6.357609 ppl = 576.866
    Valid 4864 samples after epoch: 0015 lost = 6.626400 ppl = 754.76
    Saving best model
    Epoch: 0016 Batch: 50 /134 lost = 6.381095 ppl = 590.574
    Epoch: 0016 Batch: 100 /134 lost = 6.350731 ppl = 572.911
    Valid 4864 samples after epoch: 0016 lost = 6.625156 ppl = 753.822
    Saving best model
    Epoch: 0017 Batch: 50 /134 lost = 6.374752 ppl = 586.84
    Epoch: 0017 Batch: 100 /134 lost = 6.344819 ppl = 569.534
    Valid 4864 samples after epoch: 0017 lost = 6.623570 ppl = 752.628
    Saving best model
    Epoch: 0018 Batch: 50 /134 lost = 6.367900 ppl = 582.833
    Epoch: 0018 Batch: 100 /134 lost = 6.339559 ppl = 566.546
    Valid 4864 samples after epoch: 0018 lost = 6.622302 ppl = 751.673
    Saving best model
    Epoch: 0019 Batch: 50 /134 lost = 6.361840 ppl = 579.311
    Epoch: 0019 Batch: 100 /134 lost = 6.334507 ppl = 563.691
    Valid 4864 samples after epoch: 0019 lost = 6.622089 ppl = 751.514
    Saving best model
    Epoch: 0020 Batch: 50 /134 lost = 6.356428 ppl = 576.185
    Epoch: 0020 Batch: 100 /134 lost = 6.326214 ppl = 559.036
    Valid 4864 samples after epoch: 0020 lost = 6.621774 ppl = 751.277
    Saving best model
    Epoch: 0021 Batch: 50 /134 lost = 6.352045 ppl = 573.665
    Epoch: 0021 Batch: 100 /134 lost = 6.320574 ppl = 555.892
    Valid 4864 samples after epoch: 0021 lost = 6.621957 ppl = 751.414
    Epoch: 0022 Batch: 50 /134 lost = 6.347836 ppl = 571.255
    Epoch: 0022 Batch: 100 /134 lost = 6.315464 ppl = 553.059
    Valid 4864 samples after epoch: 0022 lost = 6.622176 ppl = 751.579
    Epoch: 0023 Batch: 50 /134 lost = 6.344229 ppl = 569.198
    Epoch: 0023 Batch: 100 /134 lost = 6.310904 ppl = 550.542
    Valid 4864 samples after epoch: 0023 lost = 6.622562 ppl = 751.869
    Epoch: 0024 Batch: 50 /134 lost = 6.339936 ppl = 566.76
    Epoch: 0024 Batch: 100 /134 lost = 6.304591 ppl = 547.078
    Valid 4864 samples after epoch: 0024 lost = 6.621909 ppl = 751.378
    Epoch: 0025 Batch: 50 /134 lost = 6.335605 ppl = 564.311
    Epoch: 0025 Batch: 100 /134 lost = 6.299492 ppl = 544.296
    Valid 4864 samples after epoch: 0025 lost = 6.622849 ppl = 752.085
    Epoch: 0026 Batch: 50 /134 lost = 6.330453 ppl = 561.411
    Epoch: 0026 Batch: 100 /134 lost = 6.295497 ppl = 542.125
    Valid 4864 samples after epoch: 0026 lost = 6.615399 ppl = 746.502
    Saving best model
    Epoch: 0027 Batch: 50 /134 lost = 6.322875 ppl = 557.173
    Epoch: 0027 Batch: 100 /134 lost = 6.281405 ppl = 534.539
    Valid 4864 samples after epoch: 0027 lost = 6.612513 ppl = 744.351
    Saving best model
    Epoch: 0028 Batch: 50 /134 lost = 6.318082 ppl = 554.508
    Epoch: 0028 Batch: 100 /134 lost = 6.275888 ppl = 531.598
    Valid 4864 samples after epoch: 0028 lost = 6.612821 ppl = 744.581
    Epoch: 0029 Batch: 50 /134 lost = 6.313144 ppl = 551.777
    Epoch: 0029 Batch: 100 /134 lost = 6.270917 ppl = 528.962
    Valid 4864 samples after epoch: 0029 lost = 6.612834 ppl = 744.59
    Epoch: 0030 Batch: 50 /134 lost = 6.307557 ppl = 548.703
    Epoch: 0030 Batch: 100 /134 lost = 6.266397 ppl = 526.577
    Valid 4864 samples after epoch: 0030 lost = 6.613492 ppl = 745.08
    Epoch: 0031 Batch: 50 /134 lost = 6.302077 ppl = 545.704
    Epoch: 0031 Batch: 100 /134 lost = 6.262176 ppl = 524.359
    Valid 4864 samples after epoch: 0031 lost = 6.614067 ppl = 745.509
    Epoch: 0032 Batch: 50 /134 lost = 6.296577 ppl = 542.711
    Epoch: 0032 Batch: 100 /134 lost = 6.255343 ppl = 520.788
    Valid 4864 samples after epoch: 0032 lost = 6.614435 ppl = 745.783
    Epoch: 0033 Batch: 50 /134 lost = 6.292023 ppl = 540.245
    Epoch: 0033 Batch: 100 /134 lost = 6.250535 ppl = 518.29
    Valid 4864 samples after epoch: 0033 lost = 6.615695 ppl = 746.724
    Epoch: 0034 Batch: 50 /134 lost = 6.286271 ppl = 537.146
    Epoch: 0034 Batch: 100 /134 lost = 6.247342 ppl = 516.638
    Valid 4864 samples after epoch: 0034 lost = 6.615461 ppl = 746.549
    Epoch: 0035 Batch: 50 /134 lost = 6.284193 ppl = 536.031
    Epoch: 0035 Batch: 100 /134 lost = 6.243434 ppl = 514.623
    Valid 4864 samples after epoch: 0035 lost = 6.616403 ppl = 747.252
    Epoch: 0036 Batch: 50 /134 lost = 6.280647 ppl = 534.134
    Epoch: 0036 Batch: 100 /134 lost = 6.239960 ppl = 512.838
    Valid 4864 samples after epoch: 0036 lost = 6.617277 ppl = 747.906
    Epoch: 0037 Batch: 50 /134 lost = 6.278531 ppl = 533.005
    Epoch: 0037 Batch: 100 /134 lost = 6.236265 ppl = 510.946
    Valid 4864 samples after epoch: 0037 lost = 6.618516 ppl = 748.833
    Epoch: 0038 Batch: 50 /134 lost = 6.275411 ppl = 531.345
    Epoch: 0038 Batch: 100 /134 lost = 6.231481 ppl = 508.508
    Valid 4864 samples after epoch: 0038 lost = 6.619851 ppl = 749.834
    Epoch: 0039 Batch: 50 /134 lost = 6.272315 ppl = 529.702
    Epoch: 0039 Batch: 100 /134 lost = 6.227633 ppl = 506.555
    Valid 4864 samples after epoch: 0039 lost = 6.620247 ppl = 750.13
    Epoch: 0040 Batch: 50 /134 lost = 6.269044 ppl = 527.972
    Epoch: 0040 Batch: 100 /134 lost = 6.223034 ppl = 504.231
    Valid 4864 samples after epoch: 0040 lost = 6.621693 ppl = 751.216
    Epoch: 0041 Batch: 50 /134 lost = 6.262026 ppl = 524.28
    Epoch: 0041 Batch: 100 /134 lost = 6.219688 ppl = 502.546
    Valid 4864 samples after epoch: 0041 lost = 6.623392 ppl = 752.493
    Epoch: 0042 Batch: 50 /134 lost = 6.256196 ppl = 521.232
    Epoch: 0042 Batch: 100 /134 lost = 6.218229 ppl = 501.814
    Valid 4864 samples after epoch: 0042 lost = 6.625283 ppl = 753.917
    Epoch: 0043 Batch: 50 /134 lost = 6.252526 ppl = 519.323
    Epoch: 0043 Batch: 100 /134 lost = 6.215566 ppl = 500.479
    Valid 4864 samples after epoch: 0043 lost = 6.627102 ppl = 755.29
    Epoch: 0044 Batch: 50 /134 lost = 6.249140 ppl = 517.568
    Epoch: 0044 Batch: 100 /134 lost = 6.212819 ppl = 499.106
    Valid 4864 samples after epoch: 0044 lost = 6.628905 ppl = 756.653
    Epoch: 0045 Batch: 50 /134 lost = 6.246003 ppl = 515.946
    Epoch: 0045 Batch: 100 /134 lost = 6.210150 ppl = 497.776
    Valid 4864 samples after epoch: 0045 lost = 6.630363 ppl = 757.757
    Epoch: 0046 Batch: 50 /134 lost = 6.243699 ppl = 514.759
    Epoch: 0046 Batch: 100 /134 lost = 6.207486 ppl = 496.452
    Valid 4864 samples after epoch: 0046 lost = 6.631766 ppl = 758.821
    Epoch: 0047 Batch: 50 /134 lost = 6.241317 ppl = 513.534
    Epoch: 0047 Batch: 100 /134 lost = 6.204803 ppl = 495.122
    Valid 4864 samples after epoch: 0047 lost = 6.632874 ppl = 759.662
    Epoch: 0048 Batch: 50 /134 lost = 6.237376 ppl = 511.515
    Epoch: 0048 Batch: 100 /134 lost = 6.202425 ppl = 493.945
    Valid 4864 samples after epoch: 0048 lost = 6.634748 ppl = 761.088
    Epoch: 0049 Batch: 50 /134 lost = 6.233319 ppl = 509.444
    Epoch: 0049 Batch: 100 /134 lost = 6.200137 ppl = 492.817
    Valid 4864 samples after epoch: 0049 lost = 6.636430 ppl = 762.368
    Epoch: 0050 Batch: 50 /134 lost = 6.228939 ppl = 507.217
    Epoch: 0050 Batch: 100 /134 lost = 6.196623 ppl = 491.088
    Valid 4864 samples after epoch: 0050 lost = 6.637814 ppl = 763.425
    Epoch: 0051 Batch: 50 /134 lost = 6.225685 ppl = 505.569
    Epoch: 0051 Batch: 100 /134 lost = 6.192041 ppl = 488.843
    Valid 4864 samples after epoch: 0051 lost = 6.639985 ppl = 765.084
    Epoch: 0052 Batch: 50 /134 lost = 6.222658 ppl = 504.041
    Epoch: 0052 Batch: 100 /134 lost = 6.187325 ppl = 486.543
    Valid 4864 samples after epoch: 0052 lost = 6.642228 ppl = 766.802
    Epoch: 0053 Batch: 50 /134 lost = 6.219954 ppl = 502.68
    Epoch: 0053 Batch: 100 /134 lost = 6.184578 ppl = 485.208
    Valid 4864 samples after epoch: 0053 lost = 6.644382 ppl = 768.455
    Epoch: 0054 Batch: 50 /134 lost = 6.217173 ppl = 501.284
    Epoch: 0054 Batch: 100 /134 lost = 6.182134 ppl = 484.024
    Valid 4864 samples after epoch: 0054 lost = 6.646584 ppl = 770.149
    Epoch: 0055 Batch: 50 /134 lost = 6.214853 ppl = 500.122
    Epoch: 0055 Batch: 100 /134 lost = 6.179708 ppl = 482.851
    Valid 4864 samples after epoch: 0055 lost = 6.648670 ppl = 771.757
    Epoch: 0056 Batch: 50 /134 lost = 6.212487 ppl = 498.941
    Epoch: 0056 Batch: 100 /134 lost = 6.177235 ppl = 481.658
    Valid 4864 samples after epoch: 0056 lost = 6.650703 ppl = 773.328
    Epoch: 0057 Batch: 50 /134 lost = 6.209754 ppl = 497.579
    Epoch: 0057 Batch: 100 /134 lost = 6.174756 ppl = 480.466
    Valid 4864 samples after epoch: 0057 lost = 6.652829 ppl = 774.973
    Epoch: 0058 Batch: 50 /134 lost = 6.207550 ppl = 496.483
    Epoch: 0058 Batch: 100 /134 lost = 6.172235 ppl = 479.256
    Valid 4864 samples after epoch: 0058 lost = 6.654837 ppl = 776.532
    Epoch: 0059 Batch: 50 /134 lost = 6.205477 ppl = 495.455
    Epoch: 0059 Batch: 100 /134 lost = 6.169771 ppl = 478.077
    Valid 4864 samples after epoch: 0059 lost = 6.656833 ppl = 778.083
    Epoch: 0060 Batch: 50 /134 lost = 6.203075 ppl = 494.267
    Epoch: 0060 Batch: 100 /134 lost = 6.167260 ppl = 476.878
    Valid 4864 samples after epoch: 0060 lost = 6.657273 ppl = 778.426
    
    Test the RNNLM……………………
    Test 5760 samples with models/3_layers_rnnlm_model_best.ckpt……………………
    lost = 6.544725 ppl = 695.566
    
