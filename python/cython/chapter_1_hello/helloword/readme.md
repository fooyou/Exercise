# 说明

```
.
├── Makefile                # 使用 cypthon 和 gcc 构建，PS: C 程序员的选择
├── helloworld.pyx          # cython 文件
└── setup.py                # cython build 构建，方便
```

构建方法：

```
$ make
```

或者

```
$ python setup.py build_ext --inplace
```

然后，在 interpenter 中

```
>>> import helloworld 
```


> https://github.com/redbrain/cython-book

> 
