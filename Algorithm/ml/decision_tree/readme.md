# 决策树（decision tree）

专家系统最常用的机器学习过程。决策树可以使用不熟悉的数据集合，并从中提取出一系列规则，机器根据数据创建规则时，就是机器学习过程。

## 算法分析

- 优点：计算复杂度不高，输出结果易于理解，对中间值缺失不敏感，可以处理不相关特征数据；
- 缺点：可能产生过度匹配的问题
- 使用数据类型：数值型和标称型

在构造决策树时，我们需要解决的第一个问题就是，当前数据集上哪个特征在划分数据分类时起决定性作用。为了找到决定性的特征，划分出最好的结果，我们必须评估每个特征。完成测试之后，原始数据集就被划分为几个数据子集。这些数据子集会分布在第一个决策点的所有分支上。如果某个分支下的数据属于同一类型，则当前无需阅读的垃圾邮件已经正确地划分数据分类，无需进一步对数据集进行分割。如果数据子集内的数据不属于同一类型，则需要重复划分数据子集的过程。如何划分数据子集的算法和划分原始数据集的方法相同，直到所有具有相同类型的数据均在一个数据子集内。


## 信息增益和熵（information gain & entropy）

划分数据集的大原则是：将无序的数据变得更加有序。我们可以使用多种方法划分数据集，但是每种方法都有各自的优缺点。组织杂乱无章数据的一种方法就是使用信息论度量信息，信息论是量化处理信息的分支科学。我们可以在划分数据前后使用信息论量化度量信息的内容。

