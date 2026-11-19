# 延伸阅读

这一册引用到的论文不多，都是正文里真正用到结论的那几篇。读的时候可以配合各章末尾提到的官方文档，Nsight、CUDA、CUTLASS、Triton 的细节以文档为准，逐年更新，不适合写进书里。

- Chen T., et al. TVM: An Automated End-to-End Optimizing Compiler for Deep Learning. 2018. arXiv:1802.04799.
- Chetlur S., et al. cuDNN: Efficient Primitives for Deep Learning. 2014. arXiv:1410.0759.
- Dao T., et al. FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness. 2022. arXiv:2205.14135.
- Dao T. FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning. 2023. arXiv:2307.08691.
- Kwon W., et al. Efficient Memory Management for Large Language Model Serving with PagedAttention. 2023. arXiv:2309.06180.
- Lavin A., Gray S. Fast Algorithms for Convolutional Neural Networks. 2015. arXiv:1509.09308.
- Micikevicius P., et al. Mixed Precision Training. 2017. arXiv:1710.03740.
- Micikevicius P., et al. FP8 Formats for Deep Learning. 2022. arXiv:2209.05433.
- Vaswani A., et al. Attention Is All You Need. 2017. arXiv:1706.03762.

想要往下走，有三个方向。想理解硬件，去读各代 GPU 的架构白皮书，里面有时钟、缓存、张量核心形状的具体数字，比任何二手资料都准。想理解算子，去读 CUTLASS 的文档和源码，它把一个 GEMM 拆成了模块，每一块都有对应的注释。想理解系统，去读《引擎》那一册，那里讲怎么把这些 kernel 组织成一条流水线。
