import multiprocessing as mp
import time
import os

def foo_pool(x):
    print('process id: %s' % os.getpid())
    result = []
    for _, v in x:
        time.sleep(0.3)
        print(v)
        result.append(v)
    return result

result_list = []

def log_result(result):
    # This is called whenever foo_pool(i) returns a result.
    # result_list is modified only by the main process, not the pool workers.
    result_list.append(result)


def gen_data():
    return [(i, i + 1) for i in range(100)]


def apply_async_with_callback():
    pool = mp.Pool(processes=3)
    data = gen_data()
    pool.apply_async(foo_pool, args = (data[:len(data) // 2], ), callback = log_result)
    pool.apply_async(foo_pool, args = (data[len(data) // 2:], ), callback = log_result)
    pool.close()
    pool.join()
    print(result_list)

if __name__ == '__main__':
    apply_async_with_callback()
