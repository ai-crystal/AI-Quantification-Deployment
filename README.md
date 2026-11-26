# AI 推理部署与量化技术

> 从模型文件到线上服务

训练好的模型要在别人的机器上稳定跑起来，中间隔着很长一段路：延迟、吞吐、显存、算子融合、量化、剪枝、推理引擎、批处理、KV cache 与服务调度。

这套书按入门、算力、精度、引擎四个层次拆开。第一册建立全景，后面三册分别深入 GPU 与算子、数值精度与压缩、计算图与推理服务，每一册都可以单独读。

作者：Dr. Dezeming　·　2026

**在线阅读**：[在线阅读站](https://ai-crystal.github.io/AI-Quantification-Deployment/)　·　**仓库**：[GitHub 仓库](https://github.com/ai-crystal/AI-Quantification-Deployment)

## 分册

| 册 | 书名 | 一句话 | 页数 | 在线阅读 | PDF |
| --- | --- | --- | ---: | --- | --- |
| 01 | [入门](books/intro/README.md) | 从模型文件到线上服务 | 158 | [阅读](books/intro/README.md) | <a href="output/v1-intro.pdf" target="_blank" rel="noopener" data-router-ignore>下载</a> |
| 02 | [算力](books/compute/README.md) | GPU、CUDA 与算子性能 | 94 | [阅读](books/compute/README.md) | <a href="output/v2-compute.pdf" target="_blank" rel="noopener" data-router-ignore>下载</a> |
| 03 | [精度](books/precision/README.md) | 量化、剪枝与低秩分解 | 96 | [阅读](books/precision/README.md) | <a href="output/v3-precision.pdf" target="_blank" rel="noopener" data-router-ignore>下载</a> |
| 04 | [引擎](books/engine/README.md) | 计算图、编译与推理服务 | 88 | [阅读](books/engine/README.md) | <a href="output/v4-engine.pdf" target="_blank" rel="noopener" data-router-ignore>下载</a> |

## 怎么读

- 没有部署经验：先读入门册，建立从模型文件到线上服务的整体地图。
- 要调 GPU 与算子：读算力册，从 SM 与存储层次讲到 GEMM、卷积与 FlashAttention。
- 要把模型压小：读精度册，覆盖 PTQ / QAT、GPTQ / AWQ、剪枝与蒸馏。
- 要搭推理服务：读引擎册，覆盖图优化、TensorRT、torch.compile、批处理与调度。

## 许可

本系列文字与插图采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 许可发布，转载请注明作者与出处。书中引用的论文、数据集与模型归各自作者所有。

---

作者：Dr. Dezeming　·　2026
