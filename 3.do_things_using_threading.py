# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech
import time
import threading

start = time.perf_counter()


# do something -> function
def what_you_want_the_computer_to_do():
    print('-------开始执行某一个程序了（程序执行需要1秒钟）-------\n')
    time.sleep(1)
    print('----------------程序已经执行完毕-------------------\n')


threading_1 = threading.Thread(target=what_you_want_the_computer_to_do)
threading_2 = threading.Thread(target=what_you_want_the_computer_to_do)
threading_3 = threading.Thread(target=what_you_want_the_computer_to_do)
threading_4 = threading.Thread(target=what_you_want_the_computer_to_do)
threading_5 = threading.Thread(target=what_you_want_the_computer_to_do)
threading_6 = threading.Thread(target=what_you_want_the_computer_to_do)
threading_7 = threading.Thread(target=what_you_want_the_computer_to_do)
threading_8 = threading.Thread(target=what_you_want_the_computer_to_do)
threading_9 = threading.Thread(target=what_you_want_the_computer_to_do)
threading_10 = threading.Thread(target=what_you_want_the_computer_to_do)

threading_1.start()
threading_2.start()
threading_3.start()
threading_4.start()
threading_5.start()
threading_6.start()
threading_7.start()
threading_8.start()
threading_9.start()
threading_10.start()

# 这里必须要加上让每个线程完全运行完毕后再继续执行下方的代码的命令
threading_1.join()
threading_2.join()
threading_3.join()
threading_4.join()
threading_5.join()
threading_6.join()
threading_7.join()
threading_8.join()
threading_9.join()
threading_10.join()



finish = time.perf_counter()

print(f'整个项目花费 【{round(finish - start, 2)} 】秒完成')
