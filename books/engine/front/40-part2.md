# 第二篇　编译

图优化到一定程度，剩下的工作交给编译器：为每一层选实现，为整张图排内存，把高层算子逐步下降到机器码。TensorRT、TVM、MLIR、XLA、torch.compile 走的是不同的路线，但都在做这件事。

这一篇讲编译：TensorRT 的两阶段构建，TVM/MLIR/XLA 的下降路径，torch.compile 的捕获与生成，以及量化怎么落到图上。
