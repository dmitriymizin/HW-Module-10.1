import time
from datetime import datetime
from threading import Thread

def wite_words(word_count, file_name):
    for i in range(1, word_count + 1):
        with open(file_name, 'a', encoding='utf8') as file:
            file_content = f'Какое-то слово № {i}\n'
            file.write(file_content)
            time.sleep(0.1)
    print(f'завершилась запись в файл {file_name}')

time_start1 = datetime.now()

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time_end1 = datetime.now()
time_res1 = time_end1 - time_start1
print(f'работа потоков {time_res1}')

time_start2 = datetime.now()
def wite_words(word_count, file_name):
    for i in range(1, word_count + 1):
        with open(file_name, 'a', encoding='utf8') as file:
            file_content = f'Какое-то слово № {i}\n'
            file.write(file_content)
            time.sleep(0.1)
    print(f'завершилась запись в файл {file_name}')

thr_first = Thread(target=wite_words, args=(10, 'exemple5.txt'))
thr_second = Thread(target=wite_words, args=(30, 'exemple6.txt'))
thr_third = Thread(target=wite_words, args=(200, 'exemple7.txt'))
thr_fourth = Thread(target=wite_words, args=(100, 'exemple8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

time_end2 = datetime.now()
time_res2 = time_end2 - time_start2
print(f'работа потоков {time_res2}')
