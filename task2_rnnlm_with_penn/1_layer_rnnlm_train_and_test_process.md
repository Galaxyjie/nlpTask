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
    Epoch: 0001 Batch: 50 /134 lost = 8.770793 ppl = 6443.28
    Epoch: 0001 Batch: 100 /134 lost = 8.561597 ppl = 5227.02
    Valid 4864 samples after epoch: 0001 lost = 8.372887 ppl = 4328.12
    Saving best model
    Epoch: 0002 Batch: 50 /134 lost = 8.086017 ppl = 3248.72
    Epoch: 0002 Batch: 100 /134 lost = 7.888824 ppl = 2667.31
    Valid 4864 samples after epoch: 0002 lost = 7.757512 ppl = 2339.08
    Saving best model
    Epoch: 0003 Batch: 50 /134 lost = 7.493163 ppl = 1795.72
    Epoch: 0003 Batch: 100 /134 lost = 7.362891 ppl = 1576.39
    Valid 4864 samples after epoch: 0003 lost = 7.306516 ppl = 1489.98
    Saving best model
    Epoch: 0004 Batch: 50 /134 lost = 7.069048 ppl = 1175.03
    Epoch: 0004 Batch: 100 /134 lost = 6.984200 ppl = 1079.44
    Valid 4864 samples after epoch: 0004 lost = 6.996054 ppl = 1092.31
    Saving best model
    Epoch: 0005 Batch: 50 /134 lost = 6.781522 ppl = 881.409
    Epoch: 0005 Batch: 100 /134 lost = 6.729634 ppl = 836.841
    Valid 4864 samples after epoch: 0005 lost = 6.802506 ppl = 900.1
    Saving best model
    Epoch: 0006 Batch: 50 /134 lost = 6.607311 ppl = 740.489
    Epoch: 0006 Batch: 100 /134 lost = 6.577558 ppl = 718.782
    Valid 4864 samples after epoch: 0006 lost = 6.699119 ppl = 811.691
    Saving best model
    Epoch: 0007 Batch: 50 /134 lost = 6.516552 ppl = 676.243
    Epoch: 0007 Batch: 100 /134 lost = 6.499075 ppl = 664.527
    Valid 4864 samples after epoch: 0007 lost = 6.653679 ppl = 775.633
    Saving best model
    Epoch: 0008 Batch: 50 /134 lost = 6.475573 ppl = 649.091
    Epoch: 0008 Batch: 100 /134 lost = 6.462999 ppl = 640.98
    Valid 4864 samples after epoch: 0008 lost = 6.637138 ppl = 762.908
    Saving best model
    Epoch: 0009 Batch: 50 /134 lost = 6.457710 ppl = 637.599
    Epoch: 0009 Batch: 100 /134 lost = 6.443057 ppl = 628.325
    Valid 4864 samples after epoch: 0009 lost = 6.626290 ppl = 754.677
    Saving best model
    Epoch: 0010 Batch: 50 /134 lost = 6.446610 ppl = 630.561
    Epoch: 0010 Batch: 100 /134 lost = 6.432212 ppl = 621.548
    Valid 4864 samples after epoch: 0010 lost = 6.623178 ppl = 752.332
    Saving best model
    Epoch: 0011 Batch: 50 /134 lost = 6.438458 ppl = 625.442
    Epoch: 0011 Batch: 100 /134 lost = 6.420478 ppl = 614.297
    Valid 4864 samples after epoch: 0011 lost = 6.618684 ppl = 748.959
    Saving best model
    Epoch: 0012 Batch: 50 /134 lost = 6.424472 ppl = 616.755
    Epoch: 0012 Batch: 100 /134 lost = 6.401260 ppl = 602.604
    Valid 4864 samples after epoch: 0012 lost = 6.607340 ppl = 740.511
    Saving best model
    Epoch: 0013 Batch: 50 /134 lost = 6.407441 ppl = 606.34
    Epoch: 0013 Batch: 100 /134 lost = 6.380885 ppl = 590.45
    Valid 4864 samples after epoch: 0013 lost = 6.601230 ppl = 736.0
    Saving best model
    Epoch: 0014 Batch: 50 /134 lost = 6.389877 ppl = 595.783
    Epoch: 0014 Batch: 100 /134 lost = 6.366470 ppl = 582.0
    Valid 4864 samples after epoch: 0014 lost = 6.593928 ppl = 730.645
    Saving best model
    Epoch: 0015 Batch: 50 /134 lost = 6.372251 ppl = 585.374
    Epoch: 0015 Batch: 100 /134 lost = 6.349784 ppl = 572.369
    Valid 4864 samples after epoch: 0015 lost = 6.586628 ppl = 725.331
    Saving best model
    Epoch: 0016 Batch: 50 /134 lost = 6.352564 ppl = 573.962
    Epoch: 0016 Batch: 100 /134 lost = 6.334500 ppl = 563.687
    Valid 4864 samples after epoch: 0016 lost = 6.578950 ppl = 719.783
    Saving best model
    Epoch: 0017 Batch: 50 /134 lost = 6.332828 ppl = 562.746
    Epoch: 0017 Batch: 100 /134 lost = 6.317489 ppl = 554.18
    Valid 4864 samples after epoch: 0017 lost = 6.571645 ppl = 714.544
    Saving best model
    Epoch: 0018 Batch: 50 /134 lost = 6.313169 ppl = 551.791
    Epoch: 0018 Batch: 100 /134 lost = 6.292450 ppl = 540.476
    Valid 4864 samples after epoch: 0018 lost = 6.563096 ppl = 708.462
    Saving best model
    Epoch: 0019 Batch: 50 /134 lost = 6.294964 ppl = 541.837
    Epoch: 0019 Batch: 100 /134 lost = 6.273080 ppl = 530.108
    Valid 4864 samples after epoch: 0019 lost = 6.556206 ppl = 703.597
    Saving best model
    Epoch: 0020 Batch: 50 /134 lost = 6.277239 ppl = 532.317
    Epoch: 0020 Batch: 100 /134 lost = 6.253585 ppl = 519.873
    Valid 4864 samples after epoch: 0020 lost = 6.545735 ppl = 696.268
    Saving best model
    Epoch: 0021 Batch: 50 /134 lost = 6.253945 ppl = 520.06
    Epoch: 0021 Batch: 100 /134 lost = 6.234339 ppl = 509.963
    Valid 4864 samples after epoch: 0021 lost = 6.538597 ppl = 691.316
    Saving best model
    Epoch: 0022 Batch: 50 /134 lost = 6.236287 ppl = 510.958
    Epoch: 0022 Batch: 100 /134 lost = 6.215533 ppl = 500.463
    Valid 4864 samples after epoch: 0022 lost = 6.531371 ppl = 686.338
    Saving best model
    Epoch: 0023 Batch: 50 /134 lost = 6.219816 ppl = 502.611
    Epoch: 0023 Batch: 100 /134 lost = 6.196913 ppl = 491.23
    Valid 4864 samples after epoch: 0023 lost = 6.524163 ppl = 681.409
    Saving best model
    Epoch: 0024 Batch: 50 /134 lost = 6.202456 ppl = 493.961
    Epoch: 0024 Batch: 100 /134 lost = 6.177282 ppl = 481.681
    Valid 4864 samples after epoch: 0024 lost = 6.517388 ppl = 676.808
    Saving best model
    Epoch: 0025 Batch: 50 /134 lost = 6.185370 ppl = 485.593
    Epoch: 0025 Batch: 100 /134 lost = 6.156902 ppl = 471.964
    Valid 4864 samples after epoch: 0025 lost = 6.509671 ppl = 671.605
    Saving best model
    Epoch: 0026 Batch: 50 /134 lost = 6.166934 ppl = 476.722
    Epoch: 0026 Batch: 100 /134 lost = 6.134532 ppl = 461.523
    Valid 4864 samples after epoch: 0026 lost = 6.501756 ppl = 666.311
    Saving best model
    Epoch: 0027 Batch: 50 /134 lost = 6.152033 ppl = 469.671
    Epoch: 0027 Batch: 100 /134 lost = 6.113041 ppl = 451.71
    Valid 4864 samples after epoch: 0027 lost = 6.494234 ppl = 661.318
    Saving best model
    Epoch: 0028 Batch: 50 /134 lost = 6.137086 ppl = 462.703
    Epoch: 0028 Batch: 100 /134 lost = 6.092947 ppl = 442.724
    Valid 4864 samples after epoch: 0028 lost = 6.488594 ppl = 657.598
    Saving best model
    Epoch: 0029 Batch: 50 /134 lost = 6.124274 ppl = 456.813
    Epoch: 0029 Batch: 100 /134 lost = 6.073693 ppl = 434.282
    Valid 4864 samples after epoch: 0029 lost = 6.481085 ppl = 652.679
    Saving best model
    Epoch: 0030 Batch: 50 /134 lost = 6.111003 ppl = 450.791
    Epoch: 0030 Batch: 100 /134 lost = 6.054439 ppl = 426.0
    Valid 4864 samples after epoch: 0030 lost = 6.475716 ppl = 649.184
    Saving best model
    Epoch: 0031 Batch: 50 /134 lost = 6.098607 ppl = 445.237
    Epoch: 0031 Batch: 100 /134 lost = 6.037934 ppl = 419.027
    Valid 4864 samples after epoch: 0031 lost = 6.471529 ppl = 646.471
    Saving best model
    Epoch: 0032 Batch: 50 /134 lost = 6.085277 ppl = 439.341
    Epoch: 0032 Batch: 100 /134 lost = 6.018664 ppl = 411.029
    Valid 4864 samples after epoch: 0032 lost = 6.466325 ppl = 643.116
    Saving best model
    Epoch: 0033 Batch: 50 /134 lost = 6.071483 ppl = 433.323
    Epoch: 0033 Batch: 100 /134 lost = 6.003676 ppl = 404.915
    Valid 4864 samples after epoch: 0033 lost = 6.461208 ppl = 639.834
    Saving best model
    Epoch: 0034 Batch: 50 /134 lost = 6.059709 ppl = 428.251
    Epoch: 0034 Batch: 100 /134 lost = 5.983340 ppl = 396.763
    Valid 4864 samples after epoch: 0034 lost = 6.454667 ppl = 635.662
    Saving best model
    Epoch: 0035 Batch: 50 /134 lost = 6.043020 ppl = 421.163
    Epoch: 0035 Batch: 100 /134 lost = 5.965352 ppl = 389.69
    Valid 4864 samples after epoch: 0035 lost = 6.450855 ppl = 633.243
    Saving best model
    Epoch: 0036 Batch: 50 /134 lost = 6.026217 ppl = 414.146
    Epoch: 0036 Batch: 100 /134 lost = 5.949403 ppl = 383.524
    Valid 4864 samples after epoch: 0036 lost = 6.446988 ppl = 630.8
    Saving best model
    Epoch: 0037 Batch: 50 /134 lost = 6.011363 ppl = 408.039
    Epoch: 0037 Batch: 100 /134 lost = 5.934320 ppl = 377.783
    Valid 4864 samples after epoch: 0037 lost = 6.442561 ppl = 628.013
    Saving best model
    Epoch: 0038 Batch: 50 /134 lost = 5.997071 ppl = 402.249
    Epoch: 0038 Batch: 100 /134 lost = 5.920073 ppl = 372.439
    Valid 4864 samples after epoch: 0038 lost = 6.438325 ppl = 625.359
    Saving best model
    Epoch: 0039 Batch: 50 /134 lost = 5.983297 ppl = 396.746
    Epoch: 0039 Batch: 100 /134 lost = 5.906170 ppl = 367.297
    Valid 4864 samples after epoch: 0039 lost = 6.434287 ppl = 622.838
    Saving best model
    Epoch: 0040 Batch: 50 /134 lost = 5.970162 ppl = 391.569
    Epoch: 0040 Batch: 100 /134 lost = 5.892750 ppl = 362.401
    Valid 4864 samples after epoch: 0040 lost = 6.430565 ppl = 620.524
    Saving best model
    Epoch: 0041 Batch: 50 /134 lost = 5.956279 ppl = 386.171
    Epoch: 0041 Batch: 100 /134 lost = 5.877945 ppl = 357.075
    Valid 4864 samples after epoch: 0041 lost = 6.426337 ppl = 617.906
    Saving best model
    Epoch: 0042 Batch: 50 /134 lost = 5.943121 ppl = 381.123
    Epoch: 0042 Batch: 100 /134 lost = 5.864865 ppl = 352.435
    Valid 4864 samples after epoch: 0042 lost = 6.422388 ppl = 615.471
    Saving best model
    Epoch: 0043 Batch: 50 /134 lost = 5.928915 ppl = 375.746
    Epoch: 0043 Batch: 100 /134 lost = 5.850887 ppl = 347.543
    Valid 4864 samples after epoch: 0043 lost = 6.419045 ppl = 613.417
    Saving best model
    Epoch: 0044 Batch: 50 /134 lost = 5.915370 ppl = 370.692
    Epoch: 0044 Batch: 100 /134 lost = 5.837161 ppl = 342.805
    Valid 4864 samples after epoch: 0044 lost = 6.414581 ppl = 610.685
    Saving best model
    Epoch: 0045 Batch: 50 /134 lost = 5.901915 ppl = 365.737
    Epoch: 0045 Batch: 100 /134 lost = 5.824375 ppl = 338.45
    Valid 4864 samples after epoch: 0045 lost = 6.411085 ppl = 608.554
    Saving best model
    Epoch: 0046 Batch: 50 /134 lost = 5.889960 ppl = 361.391
    Epoch: 0046 Batch: 100 /134 lost = 5.812039 ppl = 334.3
    Valid 4864 samples after epoch: 0046 lost = 6.407852 ppl = 606.589
    Saving best model
    Epoch: 0047 Batch: 50 /134 lost = 5.878444 ppl = 357.253
    Epoch: 0047 Batch: 100 /134 lost = 5.798316 ppl = 329.744
    Valid 4864 samples after epoch: 0047 lost = 6.404383 ppl = 604.489
    Saving best model
    Epoch: 0048 Batch: 50 /134 lost = 5.865512 ppl = 352.663
    Epoch: 0048 Batch: 100 /134 lost = 5.785517 ppl = 325.55
    Valid 4864 samples after epoch: 0048 lost = 6.400980 ppl = 602.435
    Saving best model
    Epoch: 0049 Batch: 50 /134 lost = 5.854443 ppl = 348.78
    Epoch: 0049 Batch: 100 /134 lost = 5.774087 ppl = 321.85
    Valid 4864 samples after epoch: 0049 lost = 6.399302 ppl = 601.425
    Saving best model
    Epoch: 0050 Batch: 50 /134 lost = 5.842885 ppl = 344.773
    Epoch: 0050 Batch: 100 /134 lost = 5.763921 ppl = 318.595
    Valid 4864 samples after epoch: 0050 lost = 6.398500 ppl = 600.943
    Saving best model
    Epoch: 0051 Batch: 50 /134 lost = 5.833116 ppl = 341.421
    Epoch: 0051 Batch: 100 /134 lost = 5.754312 ppl = 315.548
    Valid 4864 samples after epoch: 0051 lost = 6.397336 ppl = 600.244
    Saving best model
    Epoch: 0052 Batch: 50 /134 lost = 5.822306 ppl = 337.75
    Epoch: 0052 Batch: 100 /134 lost = 5.744219 ppl = 312.38
    Valid 4864 samples after epoch: 0052 lost = 6.395475 ppl = 599.128
    Saving best model
    Epoch: 0053 Batch: 50 /134 lost = 5.812698 ppl = 334.52
    Epoch: 0053 Batch: 100 /134 lost = 5.734116 ppl = 309.239
    Valid 4864 samples after epoch: 0053 lost = 6.393117 ppl = 597.717
    Saving best model
    Epoch: 0054 Batch: 50 /134 lost = 5.803108 ppl = 331.328
    Epoch: 0054 Batch: 100 /134 lost = 5.725191 ppl = 306.492
    Valid 4864 samples after epoch: 0054 lost = 6.392687 ppl = 597.46
    Saving best model
    Epoch: 0055 Batch: 50 /134 lost = 5.793920 ppl = 328.297
    Epoch: 0055 Batch: 100 /134 lost = 5.717430 ppl = 304.122
    Valid 4864 samples after epoch: 0055 lost = 6.392482 ppl = 597.337
    Saving best model
    Epoch: 0056 Batch: 50 /134 lost = 5.784971 ppl = 325.373
    Epoch: 0056 Batch: 100 /134 lost = 5.710590 ppl = 302.049
    Valid 4864 samples after epoch: 0056 lost = 6.391772 ppl = 596.913
    Saving best model
    Epoch: 0057 Batch: 50 /134 lost = 5.775783 ppl = 322.397
    Epoch: 0057 Batch: 100 /134 lost = 5.703177 ppl = 299.818
    Valid 4864 samples after epoch: 0057 lost = 6.391376 ppl = 596.677
    Saving best model
    Epoch: 0058 Batch: 50 /134 lost = 5.767227 ppl = 319.65
    Epoch: 0058 Batch: 100 /134 lost = 5.695836 ppl = 297.625
    Valid 4864 samples after epoch: 0058 lost = 6.390845 ppl = 596.36
    Saving best model
    Epoch: 0059 Batch: 50 /134 lost = 5.758789 ppl = 316.964
    Epoch: 0059 Batch: 100 /134 lost = 5.688883 ppl = 295.563
    Valid 4864 samples after epoch: 0059 lost = 6.390691 ppl = 596.269
    Saving best model
    Epoch: 0060 Batch: 50 /134 lost = 5.750678 ppl = 314.404
    Epoch: 0060 Batch: 100 /134 lost = 5.680879 ppl = 293.207
    Valid 4864 samples after epoch: 0060 lost = 6.390280 ppl = 596.023
    Saving best model
    
    Test the RNNLM……………………
    Test 5760 samples with models/1_layer_rnnlm_model_best.ckpt……………………
    lost = 6.299852 ppl = 544.491
    
