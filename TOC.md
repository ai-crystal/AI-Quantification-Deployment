# 全书目录

按四册排列，章节顺序与 PDF 一致。每一章都链接到仓库里的 Markdown，GitHub 网页端可以直接阅读。

## 入门：从模型文件到线上服务

- 第 1 章　[训练结束之后](books/intro/chapters/ch01.md)
- 第 2 章　[延迟、吞吐与显存的账](books/intro/chapters/ch02.md)
- 第 3 章　[一个模型文件里有什么](books/intro/chapters/ch03.md)
- 第 4 章　[硬件的脾气](books/intro/chapters/ch04.md)
- 第 5 章　[算子的真面目](books/intro/chapters/ch05.md)
- 第 6 章　[融合：一次算完，少搬几趟](books/intro/chapters/ch06.md)
- 第 7 章　[图上的清理：常量、死代码与静态形状](books/intro/chapters/ch07.md)
- 第 8 章　[换一种算法：注意力、GELU 与那些被删掉的层](books/intro/chapters/ch08.md)
- 第 9 章　[编译器与推理引擎](books/intro/chapters/ch09.md)
- 第 10 章　[看懂一次性能分析](books/intro/chapters/ch10.md)
- 第 11 章　[数字的几种写法](books/intro/chapters/ch11.md)
- 第 12 章　[量化的基本做法](books/intro/chapters/ch12.md)
- 第 13 章　[量化做到更低比特](books/intro/chapters/ch13.md)
- 第 14 章　[剪枝：从权重到通道](books/intro/chapters/ch14.md)
- 第 15 章　[低秩、蒸馏与稀疏](books/intro/chapters/ch15.md)
- 第 16 章　[批处理与 KV cache](books/intro/chapters/ch16.md)
- 第 17 章　[推理服务是怎么搭起来的](books/intro/chapters/ch17.md)
- 第 18 章　[云、端、边：部署形态的选择](books/intro/chapters/ch18.md)
- 第 19 章　[一次完整的优化：从基线到上线](books/intro/chapters/ch19.md)
- 第 20 章　[注意力变体：MQA、GQA、MLA 与更省的注意力](books/intro/chapters/ch20.md)
- 第 21 章　[投机解码：用小模型换大模型的速度](books/intro/chapters/ch21.md)
- 第 22 章　[并行与分离：一张卡放不下之后](books/intro/chapters/ch22.md)
- 第 23 章　[多模型与多 LoRA：一个服务装下很多个版本](books/intro/chapters/ch23.md)
- 第 24 章　[长上下文与多模态：输入变长之后](books/intro/chapters/ch24.md)
- 第 25 章　[推理模型、Agent 与结构化输出](books/intro/chapters/ch25.md)
- 第 26 章　[扩散模型与视频生成：另一类推理负载](books/intro/chapters/ch26.md)
- 第 27 章　[新一代硬件与数值格式](books/intro/chapters/ch27.md)
- 第 28 章　[技术地图与学习路径](books/intro/chapters/ch28.md)

- [延伸阅读](books/intro/appendix/a-references.md)
- [术语表](books/intro/appendix/b-glossary.md)
- [本册 PDF](output/ai-inference-01-intro.pdf ':ignore')

## 算力：GPU、CUDA 与算子性能

- 第 1 章　[一块 GPU 的构造](books/compute/chapters/ch01.md)
- 第 2 章　[存储的阶梯](books/compute/chapters/ch02.md)
- 第 3 章　[用 roofline 判断瓶颈](books/compute/chapters/ch03.md)
- 第 4 章　[Tensor Core 与矩阵指令](books/compute/chapters/ch04.md)
- 第 5 章　[GEMM：分块与流水](books/compute/chapters/ch05.md)
- 第 6 章　[卷积的几种算法](books/compute/chapters/ch06.md)
- 第 7 章　[归一化、激活与逐元素运算](books/compute/chapters/ch07.md)
- 第 8 章　[Attention 与 FlashAttention](books/compute/chapters/ch08.md)
- 第 9 章　[融合算子的写法与边界](books/compute/chapters/ch09.md)
- 第 10 章　[并行、流与 CUDA Graph](books/compute/chapters/ch10.md)
- 第 11 章　[用 Nsight 找瓶颈](books/compute/chapters/ch11.md)
- 第 12 章　[带宽、布局与权重分块](books/compute/chapters/ch12.md)
- 第 13 章　[算子库与自动调优](books/compute/chapters/ch13.md)
- 第 14 章　[从 kernel 到端到端延迟](books/compute/chapters/ch14.md)

- [延伸阅读](books/compute/appendix/a-references.md)
- [本册 PDF](output/ai-inference-02-compute.pdf ':ignore')

## 精度：量化、剪枝与低秩分解

- 第 1 章　[浮点数的内部](books/precision/chapters/ch01.md)
- 第 2 章　[定点数与整数运算](books/precision/chapters/ch02.md)
- 第 3 章　[误差从哪里来](books/precision/chapters/ch03.md)
- 第 4 章　[均匀量化：scale 与 zero point](books/precision/chapters/ch04.md)
- 第 5 章　[校准：怎么确定范围](books/precision/chapters/ch05.md)
- 第 6 章　[PTQ：逐层替换与敏感度](books/precision/chapters/ch06.md)
- 第 7 章　[QAT：伪量化与直通估计](books/precision/chapters/ch07.md)
- 第 8 章　[低比特：int4、fp8 与微缩放](books/precision/chapters/ch08.md)
- 第 9 章　[大模型量化的三条路](books/precision/chapters/ch09.md)
- 第 10 章　[激活与 KV cache 的量化](books/precision/chapters/ch10.md)
- 第 11 章　[剪枝的几种形态](books/precision/chapters/ch11.md)
- 第 12 章　[通道裁剪与重训练](books/precision/chapters/ch12.md)
- 第 13 章　[低秩分解](books/precision/chapters/ch13.md)
- 第 14 章　[蒸馏与稀疏](books/precision/chapters/ch14.md)
- 第 15 章　[精度评估与上线监控](books/precision/chapters/ch15.md)

- [延伸阅读](books/precision/appendix/a-references.md)
- [本册 PDF](output/ai-inference-03-precision.pdf ':ignore')

## 引擎：计算图、编译与推理服务

- 第 1 章　[计算图与中间表示](books/engine/chapters/ch01.md)
- 第 2 章　[图优化：折叠、消除与重写](books/engine/chapters/ch02.md)
- 第 3 章　[算子融合的规则](books/engine/chapters/ch03.md)
- 第 4 章　[形状、动态性与静态化](books/engine/chapters/ch04.md)
- 第 5 章　[TensorRT：从网络到 engine](books/engine/chapters/ch05.md)
- 第 6 章　[TVM、MLIR 与 XLA](books/engine/chapters/ch06.md)
- 第 7 章　[torch.compile：捕获与生成](books/engine/chapters/ch07.md)
- 第 8 章　[量化在图上的落地](books/engine/chapters/ch08.md)
- 第 9 章　[内存规划与复用](books/engine/chapters/ch09.md)
- 第 10 章　[执行调度与 CUDA Graph](books/engine/chapters/ch10.md)
- 第 11 章　[批处理与 KV cache 管理](books/engine/chapters/ch11.md)
- 第 12 章　[推理服务系统](books/engine/chapters/ch12.md)
- 第 13 章　[部署流水线](books/engine/chapters/ch13.md)
- 第 14 章　[选型与取舍](books/engine/chapters/ch14.md)

- [延伸阅读](books/engine/appendix/a-references.md)
- [本册 PDF](output/ai-inference-04-engine.pdf ':ignore')
