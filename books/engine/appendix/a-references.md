# 延伸阅读

按作者姓氏字母排列。正文里提到的数字与结论，凡来自这些文献的都标注了作者与年份，其余为量级估算。

## 论文

- Chen T., et al. TVM: An Automated End-to-End Optimizing Compiler for Deep Learning. 2018. arXiv:1802.04799.
- Dao T., et al. FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness. 2022. arXiv:2205.14135.
- Jacob B., et al. Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference. 2017. arXiv:1712.05877.
- Kwon W., et al. Efficient Memory Management for Large Language Model Serving with PagedAttention. 2023. arXiv:2309.06180.
- Lattner C., et al. MLIR: A Compiler Infrastructure for the End of Moore's Law. 2020. arXiv:2002.11054.
- Pope R., et al. Efficiently Scaling Transformer Inference. 2022. arXiv:2211.05102.

## 官方文档与规范

这些材料没有固定版本可引，正文提到它们时只说产品名，不写版本号。

- NVIDIA. TensorRT Developer Guide.
- NVIDIA. CUDA C++ Programming Guide.
- PyTorch. torch.compile 与 torch.export 文档.
- ONNX. Operators 与 IR 规范.
- Open Neural Network Exchange. ONNX Runtime 文档.
- Triton. Triton Language 文档.
- vLLM. 项目文档与 PagedAttention 实现说明.

## 怎么读这些材料

TVM 和 MLIR 两篇是编译器方向的入口。前者讲清楚“写什么”和“怎么算”为什么要分开，后者讲清楚为什么需要多层 IR。读这两篇不需要跟着实现，看懂它们各自解决的问题就够了。

PagedAttention 那一篇是这一册里性价比最高的一篇，它把一个显存管理问题讲得非常具体，块表和共享前缀的设计可以直接对应到你在服务里看到的那些参数。Pope 等那篇讨论的是推理的硬件效率边界，读完会对“为什么解码阶段总是访存受限”有更清楚的判断。

FlashAttention 与量化那两篇属于“知道结论即可”的类型，具体推导可以留给专门讲算子和精度的资料。它们在这一册里出现，主要是解释某些融合为什么不是简单的算子拼接，以及 QDQ 这种图表示从哪来。
