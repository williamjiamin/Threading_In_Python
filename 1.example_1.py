# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

import time

start = time.perf_counter()


# do something -> function
def what_you_want_the_computer_to_do():
    print('-------开始执行某一个程序了（程序执行需要1秒钟）-------')
    time.sleep(1)
    print('----------------程序已经执行完毕-------------------')


what_you_want_the_computer_to_do()
what_you_want_the_computer_to_do()
what_you_want_the_computer_to_do()
what_you_want_the_computer_to_do()
what_you_want_the_computer_to_do()
what_you_want_the_computer_to_do()
what_you_want_the_computer_to_do()
what_you_want_the_computer_to_do()
what_you_want_the_computer_to_do()
what_you_want_the_computer_to_do()

finish = time.perf_counter()

print(f'整个项目花费 【{round(finish - start, 2)} 】秒完成')
