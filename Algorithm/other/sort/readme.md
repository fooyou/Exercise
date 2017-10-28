# 排序算法汇总

## 定义

对一序列对象根据某个关键字进行排序:

- 输入: n 个数: a1, a2, a3, ..., an
- 输出: n 个数的排列: a1', a2', a3', ..., an'

再讲的形象点就是排排坐，调座位，高的站在后面，矮的站在前面咯。

## 算法优劣术语

**稳定**: 如果a原本在b前面，而a=b，排序之后a仍然在b的前面；
**不稳定**: 如果a原本在b的前面，而a=b，排序之后a可能会出现在b的后面；

**内排序**: 所有排序操作都在内存中完成；
**外排序**: 由于数据太大，因此把数据放在磁盘中，而排序通过磁盘和内存的数据传输才能进行；

**时间复杂度**: 一个算法执行所耗费的时间；
**空间复杂度**: 运行完一个程序所需内存的大小；


## 排序算法总结

 排序算法 | 平均时间复杂度 | 最好情况 | 最坏情况 | 空间复杂度 | 排序方式 | 稳定性
----------|----------------|----------|----------|------------|----------|-------------
 冒泡排序 | O(n^2)         | O(n)     | O(n^2)   | O(1)       | in-place | 稳定
 选择排序 | O(n^2)         | O(n^2)   | O(n^2)   | O(1)       | in-place | 不稳定
 插入排序 | O(n^2)         | O(n)     | O(n^2)   | O(1)       | in-place | 稳定
 希尔排序 | O(n log n)     | O(n log^2 n) | O(n log^2 n) | O(1) | in-place | 不稳定
 归并排序 | O(n log n)     | O(n log n) | O(n log n) | O(n)   | out-place | 稳定
 快速排序 | O(n log n)     | O(n log n) | O(n^2) | O(log n)   | in-place | 不稳定
 堆排序   | O(n log n)     | O(n log n) | O(n log n) | O(1)   | in-place | 不稳定
 计数排序 | O(n + k)       | O(n + k) | O(n + k) | O(k)       | out-place | 稳定
 桶排序   | O(n + k)       | O(n + k) | O(n^2)   | O(n + k)   | out-place | 稳定
 基数排序 | O(n * k)       | O(n * k) | O(n * k) | O(n + k)   | out-place | 稳定

**名词解释**

n: 数据规模
k: “桶”的个数
in-place: 占用常数内存，不占用额外内存
out-place: 占用额外内存

**排序分类**

```
├── 内部排序(使用内存)
│   ├── 插入排序
│   │   ├── 直接插入排序
│   │   └── 希尔排序
│   ├── 选择排序
│   │   ├── 简单选择排序
│   │   └── 堆排序
│   ├── 交换排序
│   │   ├── 冒泡排序
│   │   └── 快速排序
│   ├── 归并排序
│   └── 基数排序
└── 外部排序(内存外存结合使用)
```

好，下面开始详述各个算法的原理及实现

### 一、冒泡排序（Bubble Sort）

冒泡排序是 C 语言的入门算法，也是很多人接触的第一个排序算法。

#### 算法描述

冒泡排序是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

#### 算法过程

1. 比较相邻的元素。如果第一个比第二个大，就交换它们两个；
2. 对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素会是最大的数；
3. 针对所有的元素重复以上的步骤，除了最后一个
4. 重复 1~3，直到排序完成

![bubble sort](./img/bubble_sort.gif)

C 代码实现：

```C
int* bubbleSort(int* list, int len) {
    int i;
    int j;
    for (i = 0; i < len; ++i) {
        for (j = 0; j < len - 1 - i; ++j) {
            if (list[j] > list[j + 1]) {
                int temp = list[j + 1];
                list[j + 1] = list[j];
                list[j] = temp;
                printList(list, len);
            }
        }
        printf("\n");
    }
    return list;
}
```

**改进冒泡**

设置一标志性变量pos,用于记录每趟排序中最后一次进行交换的位置。由于pos位置之后的记录均已交换到位,故在进行下一趟排序时只要扫描到pos位置即可。

改进代码：

```C
void improvedBubble(int* list, int len) {
    int pos;
    int i;
    int end = len - 1;
    while (end > 0) {
        pos = 0;
        for (i = 0; i < end; ++i) {
            if (list[i] > list[i + 1]) {
                pos = i;
                int temp = list[i + 1];
                list[i] = list[i + 1];
                list[i + 1] = temp;
                printList(list, len);
            }
        }
        end = pos;
        printf("\n");
    }
}
```

**双冒泡**

传统冒泡排序中每一趟排序操作只能找到一个最大值或最小值,我们考虑利用在每趟排序中进行正向和反向两遍冒泡的方法一次可以得到两个最终值(最大者和最小者) , 从而使排序趟数几乎减少了一半。

改进后算法：

```C
void doubleBubble(int* list, int len) {
    int pos = 0;
    int neg = len - 1;
    int tmp;
    int i;
    while (pos < neg) {
        for (i = pos; i < neg; ++i) {
            if (list[i] > list[i + 1]) {
                tmp = list[i + 1];
                list[i + 1] = list[i];
                list[i] = tmp;
            }
        }
        --neg;
        for (i = neg; i > pos; --i) {
            if (list[i] < list[i - 1]) {
                tmp = list[i];
                list[i] = list[i - 1];
                list[i - 1] = tmp;
            }
        }
        ++pos;
    }
}
```
#### 算法分析

- 最佳情况：T(n) = O(n)，输入完全正序
- 最差情况：T(n) = O(n^2)，输入完全反序
- 平均情况：T(n) = O(n^2)

### 二、选择排序（Selection Sort）

表现最稳定的排序算法之一(这个稳定不是指算法层面上的稳定哈，相信聪明的你能明白我说的意思2333)，因为无论什么数据进去都是O(n²)的时间复杂度.....所以用到它的时候，数据规模越小越好。唯一的好处可能就是不占用额外的内存空间了吧。理论上讲，选择排序可能也是平时排序一般人想到的最多的排序方法了吧。

#### 算法简介

选择排序(Selection-sort)是一种简单直观的排序算法。它的工作原理：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

#### 算法过程

n个记录的直接选择排序可经过n-1趟直接选择排序得到有序结果。具体算法描述如下：

1. 初始状态：无序区为R[1..n]，有序区为空；
2. 第i趟排序(i=1,2,3...n-1)开始时，当前有序区和无序区分别为R[1..i-1]和R(i..n）。该趟排序从当前无序区中-选出关键字最小的记录 R[k]，将它与无序区的第1个记录R交换，使R[1..i]和R[i+1..n)分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区；
3. n-1趟结束，数组有序化了

![selection sort](./img/selection_sort.gif)

Python 代码实现：

```python
def select_sort(sequence):
    seq = sequence
    for i in range(len(seq) - 1):
        mi = i;
        for j in range(i + 1, len(seq)):
            if seq[j] < seq[mi]:
                mi = j
        seq[i], seq[mi] = seq[mi], seq[i]
    return seq
```


### 三、插入排序

插入排序的代码实现虽然没有冒泡排序和选择排序那么简单粗暴，但它的原理应该是最容易理解的了，因为只要打过扑克牌的人都应该能够秒懂。当然，如果你说你打扑克牌摸牌的时候从来不按牌的大小整理牌，那估计这辈子你对插入排序的算法都不会产生任何兴趣了.....

#### 算法简介

插入排序（Insertion-Sort）的算法描述是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。插入排序在实现上，通常采用in-place排序（即只需用到O(1)的额外空间的排序），因而在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。

#### 算法过程

1. 从第一个元素开始，该元素可以认为已经被排序；
2. 取出下一个元素，在已经排序的元素序列中从后向前扫描；
3. 如果该元素（已排序）大于新元素，将该元素移到下一位置；
4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
5. 将新元素插入到该位置后；
6. 重复步骤2~5。

![insection sort](./img/insertion_sort.gif)

Python 实现：

```python
def insertion_sort(sequence):
    seq = dc(sequence)
    for i in range(1, len(seq)):
        j = i - 1
        if j >= 0 and seq[j] > seq[j + 1]:
            seq[j], seq[j + 1] = seq[j + 1], seq[j]
            j -= 1
    return seq
```

**算法改进** 在插入位置时，使用二分查找的方式

```python
def insertion_dichotomy_sort(sequence):
    ''' 二分查找插入位置 '''
    seq = dc(sequence)
    for i in range(1, len(seq)):
        key = seq[i]
        left = 0
        right = i - 1
        while left <= right:
            mid = int((left + right) / 2)
            if key < seq[mid]:
                right = mid - 1
            else:
                left = mid + 1
        for j in range(i - 1, left - 1, -1):
            seq[j + 1] = seq[j]
        seq[left] = key
    return seq
```

#### 算法分析

- 最佳情况：输入为升序序列 T(n) = O(n)
- 最坏情况：输入为反序序列 T(n) = O(n^2)
- 平均情况：T(n) = O(n^2)


### 四、希尔排序（Shell Sort）

1959年Shell发明；

第一个突破O(n^2)的排序算法；是简单插入排序的改进版；它与插入排序的不同之处在于，它会优先比较距离较远的元素。希尔排序又叫缩小增量排序

#### 算法简介

希尔排序的核心在于间隔序列的设定。既可以提前设定好间隔序列，也可以动态的定义间隔序列。动态定义间隔序列的算法是《算法（第4版》的合著者Robert Sedgewick提出的。

该算法的基本思想是：先将整个待排元素序列分割成若干个子序列（由相隔某个“增量”的元素组成的）分别进行直接插入排序，然后依次缩减增量再进行排序，待整个序列中的元素基本有序（增量足够小）时，再对全体元素进行一次直接插入排序。因为直接插入排序在元素基本有序的情况下（接近最好情况），效率是很高的，因此希尔排序在时间效率上比前两种方法有较大提高。

#### 算法过程

先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，具体算法描述：

1. 选择一个增量序列 t1, t2, ..., tk，其中 ti > tj, tk=1；
2. 按增量序列个数 k，对序列进行 k 趟排序；
3. 每趟排序，根据对应的增量 ti，将待排序列分割为若干个长度为 m 的子序列，分别对各子表进行直接插入排序。仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。


希尔算法的严谨实现：

```python
def shell_sort(sequence):
    seq = dc(sequence)

    gap = int(len(seq) / 2)
    while gap > 0:
        for i in range(gap):
            for j in range(i + gap, len(seq), gap):
                if seq[j] < seq[j - gap]:
                    temp = seq[j]
                    k = j - gap
                    while k >= 0 and seq[k] > temp:
                        seq[k + gap] = seq[k]
                        k -= gap
                    seq[k + gap] = temp
        gap = int(gap / 2)
    return seq
```


更好的简明实现：

```python
def shell_simple_sort(sequence):
    seq = dc(sequence)
    gap = int(len(seq) / 2)
    while gap > 0:
        for i in range(gap, len(seq)):
            j = i - gap
            while j >= 0 and seq[j] > seq[j + gap]:
                seq[j], seq[j + gap] = seq[j + gap], seq[j]
                j -= gap
        gap = int(gap / 2)
    return seq
```


#### 算法分析

- 最佳情况：T(n) = O(n log^2 n)
- 最坏情况：T(n) = O(n log^2 n)
- 平均情况：T(n) = O(n log n)


### 五、归并排序（Merge Sort）

和选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好的多，因为始终都是O(n log n）的时间复杂度。代价是需要额外的内存空间。


#### 算法简介

归并排序是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。归并排序是一种稳定的排序方法。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为2-路归并。


#### 算法过程

1. 把长度为 n 的输入序列分成两个长度为 n/2 的子序列；
2. 对这两个子序列分别采用归并排序；
3. 将两个排序好的子序列合并成一个最终的排序序列。

![merge_sort](./img/merge_sort.gif)

Python 代码实现：

```python
def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left):
        result.extend(left)
    if len(right):
        result.extend(right)
    return result


def merge_sort(sequence):
    seq = sequence
    if len(seq) < 2:
        return seq
    mid = int(len(seq) / 2)
    left = seq[:mid]
    right = seq[mid:]
    return merge(merge_sort(left), merge_sort(right))
```


#### 算法分析

- 最佳情况：T(n) = O(n)
- 最差情况：T(n) = O(n log n)
- 平均情况：T(n) = O(n log n)


### 六、快速排序（Quick Sort）

快速排序的名字起的是简单粗暴，因为一听到这个名字你就知道它存在的意义，就是快，而且效率高! 它是处理大数据最快的排序算法之一了。

#### 算法分析

快速排序的基本思想：通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。

#### 算法过程

快速排序使用分治法来把一个串（list）分为两个子串（sub-lists）。具体算法描述如下：

1. 从数列中挑出一个元素，称为 "基准"（pivot）；
2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

![quick_sort](./img/quick_sort.gif)

Python 实现：

```python
def quick_sort(sequence):
    seq = sequence
    if len(seq) < 2:
        return seq
    pivot_idx = int(len(seq) / 2)
    pivot = seq.pop(pivot_idx)
    left = []
    right = []
    for i in range(len(seq)):
        if seq[i] < pivot:
            left.append(seq[i])
        else:
            right.append(seq[i])
    return quick_sort(left) + [pivot] + quick_sort(right)
```

#### 算法分析

- 最佳情况：T(n) = O(n log n)
- 最差情况：T(n) = O(n^2)
- 平均情况：T(n) = O(n log n)


### 七、堆排序（Heap Sort）

堆排序可以说是一种利用堆的概念来排序的选择排序。

#### 算法简介

堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。


#### 算法过程

1. 将初始待排序关键字序列(R1,R2....Rn)构建成大顶堆，此堆为初始的无序区；
2. 将堆顶元素R[1]与最后一个元素R[n]交换，此时得到新的无序区(R1,R2,......Rn-1)和新的有序区(Rn),且满足R[1,2...n-1]<=R[n]；
3. 由于交换后新的堆顶R[1]可能违反堆的性质，因此需要对当前无序区(R1,R2,......Rn-1)调整为新堆，然后再次将R[1]与无序区最后一个元素交换，得到新的无序区(R1,R2....Rn-2)和新的有序区(Rn-1,Rn)。不断重复此过程直到有序区的元素个数为n-1，则整个排序过程完成。


![heap_sort](./img/heap_sort.gif)

```python
def heapify(sequence, idx, length):
    seq = sequence
    l = 2 * idx + 1
    r = 2 * idx + 2
    mx = idx
    if l < length and seq[l] > seq[mx]:
        mx = l
    if r < length and seq[r] > seq[mx]:
        mx = r
    if mx != idx:
        seq[idx], seq[mx] = seq[mx], seq[idx]
        heapify(seq, mx, length)


def heap_sort(sequence):
    seq = dc(sequence)

    # 建堆
    heapsize= len(seq)
    for i in range(int(heapsize / 2) - 1, -1, -1):
        heapify(seq, i, heapsize)

    # 堆排序
    for i in range(heapsize - 1, 0, -1):
        seq[0], seq[i] = seq[i], seq[0]
        heapsize -= 1
        heapify(seq, 0, heapsize)
    return seq
```

#### 算法分析

- 最佳情况：T(n) = O(nlogn)
- 最差情况：T(n) = O(nlogn)
- 平均情况：T(n) = O(nlogn)


### 八、计数排序（Counting Sort）

计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。

作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。


