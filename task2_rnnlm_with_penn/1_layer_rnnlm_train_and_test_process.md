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
    Epoch: 0001 Batch: 50 /134 lost = 8.828547 ppl = 6826.36
    Epoch: 0001 Batch: 100 /134 lost = 8.620298 ppl = 5543.04
    Valid 4864 samples after epoch: 0001 lost = 8.475018 ppl = 4793.51
    Saving best model
    Epoch: 0002 Batch: 50 /134 lost = 8.206701 ppl = 3665.43
    Epoch: 0002 Batch: 100 /134 lost = 7.972886 ppl = 2901.22
    Valid 4864 samples after epoch: 0002 lost = 7.834972 ppl = 2527.46
    Saving best model
    Epoch: 0003 Batch: 50 /134 lost = 7.571381 ppl = 1941.82
    Epoch: 0003 Batch: 100 /134 lost = 7.397242 ppl = 1631.48
    Valid 4864 samples after epoch: 0003 lost = 7.338874 ppl = 1538.98
    Saving best model
    Epoch: 0004 Batch: 50 /134 lost = 7.116129 ppl = 1231.67
    Epoch: 0004 Batch: 100 /134 lost = 6.997710 ppl = 1094.12
    Valid 4864 samples after epoch: 0004 lost = 7.014088 ppl = 1112.19
    Saving best model
    Epoch: 0005 Batch: 50 /134 lost = 6.817903 ppl = 914.066
    Epoch: 0005 Batch: 100 /134 lost = 6.737115 ppl = 843.125
    Valid 4864 samples after epoch: 0005 lost = 6.817340 ppl = 913.552
    Saving best model
    Epoch: 0006 Batch: 50 /134 lost = 6.637103 ppl = 762.881
    Epoch: 0006 Batch: 100 /134 lost = 6.577186 ppl = 718.514
    Valid 4864 samples after epoch: 0006 lost = 6.707323 ppl = 818.377
    Saving best model
    Epoch: 0007 Batch: 50 /134 lost = 6.531134 ppl = 686.176
    Epoch: 0007 Batch: 100 /134 lost = 6.482541 ppl = 653.63
    Valid 4864 samples after epoch: 0007 lost = 6.647630 ppl = 770.955
    Saving best model
    Epoch: 0008 Batch: 50 /134 lost = 6.465350 ppl = 642.489
    Epoch: 0008 Batch: 100 /134 lost = 6.418269 ppl = 612.941
    Valid 4864 samples after epoch: 0008 lost = 6.608139 ppl = 741.102
    Saving best model
    Epoch: 0009 Batch: 50 /134 lost = 6.419223 ppl = 613.526
    Epoch: 0009 Batch: 100 /134 lost = 6.372218 ppl = 585.355
    Valid 4864 samples after epoch: 0009 lost = 6.583450 ppl = 723.03
    Saving best model
    Epoch: 0010 Batch: 50 /134 lost = 6.386536 ppl = 593.796
    Epoch: 0010 Batch: 100 /134 lost = 6.332651 ppl = 562.646
    Valid 4864 samples after epoch: 0010 lost = 6.563710 ppl = 708.897
    Saving best model
    Epoch: 0011 Batch: 50 /134 lost = 6.361369 ppl = 579.038
    Epoch: 0011 Batch: 100 /134 lost = 6.303811 ppl = 546.651
    Valid 4864 samples after epoch: 0011 lost = 6.546490 ppl = 696.794
    Saving best model
    Epoch: 0012 Batch: 50 /134 lost = 6.337354 ppl = 565.299
    Epoch: 0012 Batch: 100 /134 lost = 6.282200 ppl = 534.964
    Valid 4864 samples after epoch: 0012 lost = 6.533525 ppl = 687.819
    Saving best model
    Epoch: 0013 Batch: 50 /134 lost = 6.318511 ppl = 554.747
    Epoch: 0013 Batch: 100 /134 lost = 6.254858 ppl = 520.535
    Valid 4864 samples after epoch: 0013 lost = 6.522715 ppl = 680.423
    Saving best model
    Epoch: 0014 Batch: 50 /134 lost = 6.298895 ppl = 543.971
    Epoch: 0014 Batch: 100 /134 lost = 6.228705 ppl = 507.099
    Valid 4864 samples after epoch: 0014 lost = 6.513601 ppl = 674.25
    Saving best model
    Epoch: 0015 Batch: 50 /134 lost = 6.279442 ppl = 533.491
    Epoch: 0015 Batch: 100 /134 lost = 6.206190 ppl = 495.808
    Valid 4864 samples after epoch: 0015 lost = 6.504941 ppl = 668.436
    Saving best model
    Epoch: 0016 Batch: 50 /134 lost = 6.257855 ppl = 522.098
    Epoch: 0016 Batch: 100 /134 lost = 6.182185 ppl = 484.049
    Valid 4864 samples after epoch: 0016 lost = 6.495266 ppl = 662.0
    Saving best model
    Epoch: 0017 Batch: 50 /134 lost = 6.234365 ppl = 509.977
    Epoch: 0017 Batch: 100 /134 lost = 6.158048 ppl = 472.505
    Valid 4864 samples after epoch: 0017 lost = 6.485704 ppl = 655.701
    Saving best model
    Epoch: 0018 Batch: 50 /134 lost = 6.211925 ppl = 498.66
    Epoch: 0018 Batch: 100 /134 lost = 6.137548 ppl = 462.917
    Valid 4864 samples after epoch: 0018 lost = 6.476875 ppl = 649.937
    Saving best model
    Epoch: 0019 Batch: 50 /134 lost = 6.190399 ppl = 488.041
    Epoch: 0019 Batch: 100 /134 lost = 6.118356 ppl = 454.118
    Valid 4864 samples after epoch: 0019 lost = 6.468736 ppl = 644.668
    Saving best model
    Epoch: 0020 Batch: 50 /134 lost = 6.173689 ppl = 479.954
    Epoch: 0020 Batch: 100 /134 lost = 6.101280 ppl = 446.429
    Valid 4864 samples after epoch: 0020 lost = 6.460623 ppl = 639.459
    Saving best model
    Epoch: 0021 Batch: 50 /134 lost = 6.157946 ppl = 472.457
    Epoch: 0021 Batch: 100 /134 lost = 6.083850 ppl = 438.715
    Valid 4864 samples after epoch: 0021 lost = 6.453252 ppl = 634.763
    Saving best model
    Epoch: 0022 Batch: 50 /134 lost = 6.141352 ppl = 464.681
    Epoch: 0022 Batch: 100 /134 lost = 6.067672 ppl = 431.674
    Valid 4864 samples after epoch: 0022 lost = 6.446609 ppl = 630.56
    Saving best model
    Epoch: 0023 Batch: 50 /134 lost = 6.124587 ppl = 456.956
    Epoch: 0023 Batch: 100 /134 lost = 6.052974 ppl = 425.376
    Valid 4864 samples after epoch: 0023 lost = 6.439329 ppl = 625.987
    Saving best model
    Epoch: 0024 Batch: 50 /134 lost = 6.110154 ppl = 450.408
    Epoch: 0024 Batch: 100 /134 lost = 6.038228 ppl = 419.15
    Valid 4864 samples after epoch: 0024 lost = 6.433625 ppl = 622.426
    Saving best model
    Epoch: 0025 Batch: 50 /134 lost = 6.097142 ppl = 444.585
    Epoch: 0025 Batch: 100 /134 lost = 6.023822 ppl = 413.155
    Valid 4864 samples after epoch: 0025 lost = 6.429106 ppl = 619.62
    Saving best model
    Epoch: 0026 Batch: 50 /134 lost = 6.085153 ppl = 439.287
    Epoch: 0026 Batch: 100 /134 lost = 6.008904 ppl = 407.037
    Valid 4864 samples after epoch: 0026 lost = 6.424444 ppl = 616.738
    Saving best model
    Epoch: 0027 Batch: 50 /134 lost = 6.074033 ppl = 434.429
    Epoch: 0027 Batch: 100 /134 lost = 5.993049 ppl = 400.634
    Valid 4864 samples after epoch: 0027 lost = 6.420992 ppl = 614.613
    Saving best model
    Epoch: 0028 Batch: 50 /134 lost = 6.061695 ppl = 429.102
    Epoch: 0028 Batch: 100 /134 lost = 5.973692 ppl = 392.954
    Valid 4864 samples after epoch: 0028 lost = 6.416902 ppl = 612.104
    Saving best model
    Epoch: 0029 Batch: 50 /134 lost = 6.050913 ppl = 424.501
    Epoch: 0029 Batch: 100 /134 lost = 5.958521 ppl = 387.037
    Valid 4864 samples after epoch: 0029 lost = 6.413756 ppl = 610.181
    Saving best model
    Epoch: 0030 Batch: 50 /134 lost = 6.038111 ppl = 419.1
    Epoch: 0030 Batch: 100 /134 lost = 5.943460 ppl = 381.252
    Valid 4864 samples after epoch: 0030 lost = 6.412888 ppl = 609.652
    Saving best model
    Epoch: 0031 Batch: 50 /134 lost = 6.028360 ppl = 415.034
    Epoch: 0031 Batch: 100 /134 lost = 5.929807 ppl = 376.082
    Valid 4864 samples after epoch: 0031 lost = 6.411748 ppl = 608.957
    Saving best model
    Epoch: 0032 Batch: 50 /134 lost = 6.018884 ppl = 411.119
    Epoch: 0032 Batch: 100 /134 lost = 5.916839 ppl = 371.236
    Valid 4864 samples after epoch: 0032 lost = 6.410852 ppl = 608.412
    Saving best model
    Epoch: 0033 Batch: 50 /134 lost = 6.008741 ppl = 406.971
    Epoch: 0033 Batch: 100 /134 lost = 5.903532 ppl = 366.329
    Valid 4864 samples after epoch: 0033 lost = 6.409265 ppl = 607.447
    Saving best model
    Epoch: 0034 Batch: 50 /134 lost = 5.997005 ppl = 402.222
    Epoch: 0034 Batch: 100 /134 lost = 5.890610 ppl = 361.626
    Valid 4864 samples after epoch: 0034 lost = 6.407321 ppl = 606.267
    Saving best model
    Epoch: 0035 Batch: 50 /134 lost = 5.987088 ppl = 398.253
    Epoch: 0035 Batch: 100 /134 lost = 5.878755 ppl = 357.364
    Valid 4864 samples after epoch: 0035 lost = 6.405745 ppl = 605.312
    Saving best model
    Epoch: 0036 Batch: 50 /134 lost = 5.977859 ppl = 394.595
    Epoch: 0036 Batch: 100 /134 lost = 5.865984 ppl = 352.829
    Valid 4864 samples after epoch: 0036 lost = 6.404194 ppl = 604.375
    Saving best model
    Epoch: 0037 Batch: 50 /134 lost = 5.969205 ppl = 391.195
    Epoch: 0037 Batch: 100 /134 lost = 5.854802 ppl = 348.906
    Valid 4864 samples after epoch: 0037 lost = 6.402370 ppl = 603.273
    Saving best model
    Epoch: 0038 Batch: 50 /134 lost = 5.960011 ppl = 387.615
    Epoch: 0038 Batch: 100 /134 lost = 5.842927 ppl = 344.787
    Valid 4864 samples after epoch: 0038 lost = 6.401077 ppl = 602.494
    Saving best model
    Epoch: 0039 Batch: 50 /134 lost = 5.950181 ppl = 383.823
    Epoch: 0039 Batch: 100 /134 lost = 5.830447 ppl = 340.511
    Valid 4864 samples after epoch: 0039 lost = 6.399262 ppl = 601.401
    Saving best model
    Epoch: 0040 Batch: 50 /134 lost = 5.941453 ppl = 380.488
    Epoch: 0040 Batch: 100 /134 lost = 5.817968 ppl = 336.288
    Valid 4864 samples after epoch: 0040 lost = 6.396554 ppl = 599.774
    Saving best model
    Epoch: 0041 Batch: 50 /134 lost = 5.933867 ppl = 377.612
    Epoch: 0041 Batch: 100 /134 lost = 5.806744 ppl = 332.535
    Valid 4864 samples after epoch: 0041 lost = 6.394467 ppl = 598.524
    Saving best model
    Epoch: 0042 Batch: 50 /134 lost = 5.925776 ppl = 374.569
    Epoch: 0042 Batch: 100 /134 lost = 5.795638 ppl = 328.862
    Valid 4864 samples after epoch: 0042 lost = 6.393652 ppl = 598.037
    Saving best model
    Epoch: 0043 Batch: 50 /134 lost = 5.917878 ppl = 371.622
    Epoch: 0043 Batch: 100 /134 lost = 5.785364 ppl = 325.501
    Valid 4864 samples after epoch: 0043 lost = 6.393250 ppl = 597.796
    Saving best model
    Epoch: 0044 Batch: 50 /134 lost = 5.910451 ppl = 368.872
    Epoch: 0044 Batch: 100 /134 lost = 5.775240 ppl = 322.222
    Valid 4864 samples after epoch: 0044 lost = 6.393069 ppl = 597.688
    Saving best model
    Epoch: 0045 Batch: 50 /134 lost = 5.903023 ppl = 366.143
    Epoch: 0045 Batch: 100 /134 lost = 5.765365 ppl = 319.056
    Valid 4864 samples after epoch: 0045 lost = 6.392904 ppl = 597.589
    Saving best model
    Epoch: 0046 Batch: 50 /134 lost = 5.895513 ppl = 363.403
    Epoch: 0046 Batch: 100 /134 lost = 5.755445 ppl = 315.906
    Valid 4864 samples after epoch: 0046 lost = 6.392969 ppl = 597.629
    Saving best model
    Epoch: 0047 Batch: 50 /134 lost = 5.888353 ppl = 360.81
    Epoch: 0047 Batch: 100 /134 lost = 5.746165 ppl = 312.988
    Valid 4864 samples after epoch: 0047 lost = 6.393300 ppl = 597.826
    Saving best model
    Epoch: 0048 Batch: 50 /134 lost = 5.881489 ppl = 358.342
    Epoch: 0048 Batch: 100 /134 lost = 5.737065 ppl = 310.153
    Valid 4864 samples after epoch: 0048 lost = 6.393300 ppl = 597.826
    Saving best model
    Epoch: 0049 Batch: 50 /134 lost = 5.874820 ppl = 355.961
    Epoch: 0049 Batch: 100 /134 lost = 5.728673 ppl = 307.561
    Valid 4864 samples after epoch: 0049 lost = 6.393372 ppl = 597.869
    Saving best model
    Epoch: 0050 Batch: 50 /134 lost = 5.868149 ppl = 353.594
    Epoch: 0050 Batch: 100 /134 lost = 5.720470 ppl = 305.048
    Valid 4864 samples after epoch: 0050 lost = 6.393535 ppl = 597.967
    Saving best model
    Epoch: 0051 Batch: 50 /134 lost = 5.861605 ppl = 351.287
    Epoch: 0051 Batch: 100 /134 lost = 5.712708 ppl = 302.69
    Valid 4864 samples after epoch: 0051 lost = 6.393709 ppl = 598.071
    Saving best model
    Epoch: 0052 Batch: 50 /134 lost = 5.854908 ppl = 348.943
    Epoch: 0052 Batch: 100 /134 lost = 5.704972 ppl = 300.357
    Valid 4864 samples after epoch: 0052 lost = 6.393973 ppl = 598.229
    Saving best model
    Epoch: 0053 Batch: 50 /134 lost = 5.848343 ppl = 346.659
    Epoch: 0053 Batch: 100 /134 lost = 5.697444 ppl = 298.105
    Valid 4864 samples after epoch: 0053 lost = 6.394167 ppl = 598.345
    Saving best model
    Epoch: 0054 Batch: 50 /134 lost = 5.841337 ppl = 344.239
    Epoch: 0054 Batch: 100 /134 lost = 5.690028 ppl = 295.902
    Valid 4864 samples after epoch: 0054 lost = 6.394450 ppl = 598.514
    Saving best model
    Epoch: 0055 Batch: 50 /134 lost = 5.834790 ppl = 341.993
    Epoch: 0055 Batch: 100 /134 lost = 5.682937 ppl = 293.811
    Valid 4864 samples after epoch: 0055 lost = 6.394761 ppl = 598.7
    Saving best model
    Epoch: 0056 Batch: 50 /134 lost = 5.828619 ppl = 339.889
    Epoch: 0056 Batch: 100 /134 lost = 5.675129 ppl = 291.526
    Valid 4864 samples after epoch: 0056 lost = 6.395071 ppl = 598.886
    Saving best model
    Epoch: 0057 Batch: 50 /134 lost = 5.822982 ppl = 337.979
    Epoch: 0057 Batch: 100 /134 lost = 5.667756 ppl = 289.384
    Valid 4864 samples after epoch: 0057 lost = 6.395251 ppl = 598.994
    Saving best model
    Epoch: 0058 Batch: 50 /134 lost = 5.817715 ppl = 336.203
    Epoch: 0058 Batch: 100 /134 lost = 5.659528 ppl = 287.013
    Valid 4864 samples after epoch: 0058 lost = 6.395913 ppl = 599.39
    Saving best model
    Epoch: 0059 Batch: 50 /134 lost = 5.813040 ppl = 334.635
    Epoch: 0059 Batch: 100 /134 lost = 5.652571 ppl = 285.023
    Valid 4864 samples after epoch: 0059 lost = 6.396841 ppl = 599.947
    Saving best model
    Epoch: 0060 Batch: 50 /134 lost = 5.808358 ppl = 333.072
    Epoch: 0060 Batch: 100 /134 lost = 5.645984 ppl = 283.152
    Valid 4864 samples after epoch: 0060 lost = 6.397878 ppl = 600.569
    Saving best model
    
    Test the RNNLM……………………
    Test 5760 samples with models/1_layer_rnnlm_model_best.ckpt……………………
    lost = 6.319994 ppl = 555.57
    
