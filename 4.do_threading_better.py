# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech
import time
import threading

start = time.perf_counter()


# do something -> function
def what_you_want_the_computer_to_do():
    print('-------开始执行某一个程序了（程序执行需要1秒钟）-------\n')
    time.sleep(1)
    print('----------------程序已经执行完毕-------------------\n')


the_pool_of_threads = []
how_many_threads_do_you_want = 10
for _ in range(how_many_threads_do_you_want):
    every_thread = threading.Thread(target=what_you_want_the_computer_to_do)
    every_thread.start()
    the_pool_of_threads.append(every_thread)

# print(the_pool_of_threads)

for thread in the_pool_of_threads:
    thread.join()

finish = time.perf_counter()

print(f'整个项目花费 【{round(finish - start, 2)} 】秒完成')
