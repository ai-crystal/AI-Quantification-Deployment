# 延伸阅读

这一册讲到的每一个方法都能追到一篇原始论文。下面按作者姓氏的字母序排列，只列出正文里真正引用过的，格式是作者、标题、年份、arXiv 编号。读原文时先看它的实验设置，尤其是量化配置和校准数据来源，很多方法的结论只在特定配置下成立。

## 量化

- Dettmers T., et al. The Case for 4-bit Precision: k-bit Inference Scaling Laws. 2022b. arXiv:2212.09720.
- Dettmers T., et al. LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale. 2022a. arXiv:2208.07339.
- Dettmers T., et al. QLoRA: Efficient Finetuning of Quantized LLMs. 2023. arXiv:2305.14314.
- Frantar E., et al. GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers. 2022. arXiv:2210.17323.
- Jacob B., et al. Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference. 2017. arXiv:1712.05877.
- Lin J., et al. AWQ: Activation-aware Weight Quantization for On-Device LLM Compression and Acceleration. 2023. arXiv:2306.00978.
- Liu S., et al. LLM-FP4: 4-Bit Floating-Point Quantized Transformers. 2023. arXiv:2310.16836.
- Micikevicius P., et al. Mixed Precision Training. 2017. arXiv:1710.03740.
- Micikevicius P., et al. FP8 Formats for Deep Learning. 2022. arXiv:2209.05433.
- Xiao G., et al. SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models. 2022. arXiv:2211.10438.
- Yao Z., et al. ZeroQuant: Efficient and Affordable Post-Training Quantization for Large-Scale Transformers. 2022. arXiv:2206.01861.

## 剪枝与稀疏

- Blalock D., et al. What is the State of Neural Network Pruning? 2020. arXiv:2003.03033.
- Frankle J., Carbin M. The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks. 2018. arXiv:1803.03635.
- Han S., et al. Learning both Weights and Connections for Efficient Neural Networks. 2015. arXiv:1506.02626.
- Li H., et al. Pruning Filters for Efficient ConvNets. 2016. arXiv:1608.08710.
- Mishra A., et al. Accelerating Sparse Deep Neural Networks. 2021. arXiv:2104.08378.
- Sanh V., et al. Movement Pruning: Adaptive Sparsity by Fine-Tuning. 2020. arXiv:2005.07683.

## 低秩分解与蒸馏

- Denton E., et al. Exploiting Linear Structure Within Convolutional Networks for Efficient Evaluation. 2014. arXiv:1404.0736.
- Hinton G., et al. Distilling the Knowledge in a Neural Network. 2015. arXiv:1503.02531.
- Hu E., et al. LoRA: Low-Rank Adaptation of Large Language Models. 2021. arXiv:2106.09685.
- Jaderberg M., et al. Speeding up Convolutional Neural Networks with Low Rank Expansions. 2014. arXiv:1405.3866.
- Jiao X., et al. TinyBERT: Distilling BERT for Natural Language Understanding. 2019. arXiv:1909.10351.
- Novikov A., et al. Tensorizing Neural Networks. 2015. arXiv:1509.06569.

## 数值与运行时

- Gupta S., et al. Deep Learning with Limited Numerical Precision. 2015. arXiv:1502.02551.
- Kwon W., et al. Efficient Memory Management for Large Language Model Serving with PagedAttention. 2023. arXiv:2309.06180.
- Zhou Z., et al. A Survey on Efficient Inference for Large Language Models. 2024. arXiv:2404.14294.

## 读论文时可以跳过的部分

这些论文里的性能数字大多在特定硬件、特定批大小下测得，直接搬到自己的场景往往会失望。比较有价值的是三部分，问题设定的形式化（比如 GPTQ 把量化写成带 Hessian 约束的最小化）、误差分析的方法（哪些量被近似、误差怎么传播）、以及消融实验（哪个组件真的起作用）。具体的加速比可以当参考，不要当承诺。
