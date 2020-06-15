# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech
import time
import concurrent.futures

start = time.perf_counter()


# do something -> function
def what_you_want_the_computer_to_do(seconds):
    print(f'-------开始执行某一个程序了（程序执行需要【{seconds}】秒钟）-------\n')
    time.sleep(seconds)
    return f'---------------程序已经执行完毕,花费【{seconds}】秒钟-----------\n'


with concurrent.futures.ThreadPoolExecutor() as executor:
    execution_time_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    results = executor.map(what_you_want_the_computer_to_do,execution_time_list)
    #
    # for result in results:
    #     print(result)

finish = time.perf_counter()

print(f'整个项目花费 【{round(finish - start, 2)} 】秒完成')
