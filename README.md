# 落地

> AI 推理部署与量化技术

从一次前向开始，把模型文件、算子、计算图、数值精度和线上服务串成一条线。四册正文，一册实战。

作者　Dr. Dezeming　2026

## 这套书讲什么

训练好的模型要在别人的机器上稳定地跑起来，中间隔着很长一段路：延迟、吞吐、显存、算子融合、量化、剪枝、推理引擎、批处理、KV cache、服务调度。这套书按“入门 → 算力 → 精度 → 引擎”的顺序拆开，每一册都可以单独读。

| 册 | 书名 | 一句话 | 页数 | 阅读 | 下载 |
|---|---|---|---|---|---|
| 01 | 落地：AI 推理部署与量化入门 | 建立全景地图，覆盖全部技术，不深入公式 | 113 | [在线阅读](books/intro/README.md) | [PDF](output/landing-01-intro.pdf ':ignore') |
| 02 | 算力：GPU、CUDA 与算子性能 | 从 SM 与存储层次讲到 GEMM、卷积、FlashAttention | 83 | [在线阅读](books/compute/README.md) | [PDF](output/landing-02-compute.pdf ':ignore') |
| 03 | 精度：量化、剪枝与低秩分解 | 浮点、定点、PTQ/QAT、GPTQ/AWQ、剪枝与蒸馏 | 82 | [在线阅读](books/precision/README.md) | [PDF](output/landing-03-precision.pdf ':ignore') |
| 04 | 引擎：计算图、编译与推理服务 | 图优化、TensorRT、torch.compile、批处理与服务 | 74 | [在线阅读](books/engine/README.md) | [PDF](output/landing-04-engine.pdf ':ignore') |
| 05 | 实战：一个真实项目的优化记录 | 拿到项目后按真实数据撰写 | — | [说明](books/practice/README.md) | — |

## 适合谁

能写 Python、训练过小模型、但没有部署经验的工程师。第一册不要求 CUDA，也不要求数学推导；后面三册会逐步深入，读者可以按工作需要挑一本。

## 在线阅读

站点：<https://ai-crystal.github.io/AI-Inference-Deployment/>

每一章都有独立地址，可以直接分享。侧栏可以切换分册，右上角可以搜索全书。也可以从[全书目录](TOC.md)进入任意一章。

## 说明

书里的图都由代码绘制，性能数字来自公开论文或明确标注的估算，没有实测来源的对比不会画成图表。示例中的模型、硬件和配置用于讲解原理，不代表任何产品的实际表现。
