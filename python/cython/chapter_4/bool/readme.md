# 使用说明

1. Makefile
    cython c++, 把 pyx 编译为 c 文件，然后用 g++ 编译
2. setup.py
    python3 直接编译 pyx 为 cpp 文件


## 用法

```
$ make
$ ./example
$ make clean
```

或 python3

```
$ python setup.py build_ext --inplace
$ python setup.py clean
$ python
>>> import cycode
>>> cycode.run()
False
```
