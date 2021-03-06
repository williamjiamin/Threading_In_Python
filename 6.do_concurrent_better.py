# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech
import time
import concurrent.futures

start = time.perf_counter()


# do something -> function
def what_you_want_the_computer_to_do(seconds):
    print('-------开始执行某一个程序了（程序执行需要1秒钟）-------\n')
    time.sleep(seconds)
    return '----------------程序已经执行完毕-------------------\n'


with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(what_you_want_the_computer_to_do, 1) for _ in range(10)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f'整个项目花费 【{round(finish - start, 2)} 】秒完成')
