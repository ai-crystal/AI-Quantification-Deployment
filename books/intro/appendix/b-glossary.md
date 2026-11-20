# 术语表

下面按中文词条整理书中反复出现的术语，英文放在括号里。解释只求能读懂上下文，不追求严格定义。

**算术强度**（arithmetic intensity）　每读写一个字节做多少次浮点运算。强度低受带宽限制，强度高受算力限制。

**算子融合**（operator fusion）　把相邻的多个算子合成一个 kernel，减少中间结果的显存读写和 kernel 启动。

**计算图**（computational graph）　用节点表示算子、用边表示张量的有向无环图。部署时的图优化都在这一层进行。

**静态形状**（static shape）　推理时把输入形状固定下来，便于提前分配显存、选择 kernel、录制执行图。

**权重分块**（weight tiling）　把大权重切成块，只把当前需要的块放进显存，或把矩阵切成适合缓存的块。前者省显存，后者提带宽利用率。

**批处理**（batching）　把多个请求组成一批一起算。批越大吞吐越高，单请求延迟也越长。

**连续批处理**（continuous batching）　每一步都让完成的请求离开、新到的请求加入，而不是等整批结束。

**KV cache**　生成式模型缓存历史 token 的 Key 和 Value，避免每一步重复计算。它随序列长度线性增长。

**PagedAttention**　把 KV cache 切成固定大小的块，用块表映射逻辑位置和物理块，减少碎片并支持共享前缀。

**前缀缓存**（prefix caching）　把相同 prompt 前缀的 KV cache 复用，省掉重复的 prefill。

**prefill 与 decode**　prefill 一次算完整段输入，计算密集；decode 逐 token 生成，访存密集。

**TTFT 与 TPOT**　首 token 延迟（time to first token）和每 token 延迟（time per output token），衡量生成服务体验的两个核心指标。

**MQA / GQA / MLA**　三种减少 KV cache 的注意力结构。MQA 所有查询头共享一套 K/V，GQA 分组共享，MLA 把 K/V 压成潜向量。

**投机解码**（speculative decoding）　用小模型先猜几个 token，再用大模型一次验证，接受猜对的前缀。不改变输出分布，低并发时收益最大。

**量化**（quantization）　用更少的位表示权重或激活。常见格式有 int8、int4、fp8、fp4。

**PTQ 与 QAT**　PTQ 在训练后量化，靠校准确定范围；QAT 在训练时模拟量化，让模型适应误差。

**校准**（calibration）　用一批代表性数据统计激活范围，确定量化的 scale 和 zero point。

**per-tensor / per-channel / per-group**　量化的粒度。整个张量一个 scale、每个通道一个、每组若干元素一个。粒度越细精度越好，元数据越多。

**GPTQ / AWQ / SmoothQuant**　三种大模型量化方法。GPTQ 用二阶误差补偿压权重，AWQ 保护显著通道，SmoothQuant 把激活的 outlier 迁移到权重。

**FP8 / FP4 / MX**　低比特浮点格式与微缩放格式。FP8 有 e4m3、e5m2 两种；FP4 常配合 MX 或 NVFP4 的块缩放使用。

**剪枝**（pruning）　去掉不重要的权重、通道、头或层。非结构化剪枝省存储，结构化剪枝省计算。

**2:4 稀疏**　每 4 个权重最多保留 2 个非零，特定 Tensor Core 可以跳过零，理论算力翻倍。

**低秩分解**（low-rank decomposition）　用两个瘦长矩阵近似一个大矩阵，减少参数量和计算量。

**蒸馏**（distillation）　用大模型的输出分布教一个小模型，让小模型接近大模型的行为。

**LoRA**　冻结基础模型，只训练低秩适配器。一个基础模型可以挂很多个 LoRA，服务多个定制版本。

**MoE**（mixture of experts）　把 FFN 拆成很多专家，每个 token 只激活少数几个，参数量大但单 token 计算量可控。

**张量并行 / 流水并行 / 专家并行**　三种多卡切法。张量并行切一层内的矩阵，流水并行切层，专家并行切 MoE 的专家。

**PD 分离**（prefill-decode disaggregation）　把 prefill 和 decode 放到不同的机器池，各自扩缩容，中间传 KV cache。

**CUDA Graph**　把一串 kernel 启动录下来重放，减少 CPU 侧启动开销和 GPU 空隙。

**roofline**　用算术强度和硬件带宽、算力画出的性能上界模型，用来判断一个算子受带宽还是算力限制。

**SLO**（service level objective）　服务等级目标，比如 P99 延迟小于 300 毫秒、可用性 99.9%。

**Agent**　让模型在循环里决定下一步、调用工具、读取结果，直到完成任务。一次请求可能包含多轮模型调用和工具调用。

**约束解码**（constrained decoding）　在生成时屏蔽不符合语法或 schema 的 token，保证输出是合法 JSON、SQL 等结构。

**扩散模型**（diffusion model）　从噪声开始，迭代去噪生成图像或视频。步数是主要成本，步数蒸馏可以把它压到几步。

**步数蒸馏**（step distillation）　用多步教师模型教少步学生模型，让少步生成接近多步质量。

**HBM 与 NVLink**　HBM 是 GPU 的高带宽显存；NVLink 是卡间高速互联，决定多卡并行的通信效率。

**Hopper 与 Blackwell**　NVIDIA 的两代数据中心 GPU 架构。Hopper 把 FP8 带进主流，Blackwell 增加了 FP4 支持。
