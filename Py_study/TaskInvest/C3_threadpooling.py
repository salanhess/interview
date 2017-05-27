#refer to https://www.ibm.com/developerworks/cn/aix/library/au-threadingpython/?ca=drs-tp3008
http://www.dongwm.com/archives/%E4%BD%BF%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B-%E7%BA%BF%E7%A8%8B%E7%AF%87/
  
  
# -*-coding:utf-8-*-
# Python 2.7
#refer to  http://codingpy.com/article/python-201-a-tutorial-on-threads/
# https://stackoverflow.com/questions/3033952/threading-pool-similar-to-the-multiprocessing-pool

from threading import Thread
from Queue import Queue
import time
import logging

def get_logger():
    logger = logging.getLogger("threading_example")
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler("threading.log")
    fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

def doubler(number,logger):
    logger.debug('doubler function executing')
    result = number * 2
    logger.debug('doubler function ended with: {}'.format(result))

class Worker(Thread):
    def __init__(self, work_queue):
        #super(Worker, self).__init__()
        Thread.__init__(self)
        self.__work_queue = work_queue
        self.daemon = True
        self.start()
    def run(self):
        while True:
            func, args, kwargs = self.__work_queue.get()
            try:
                func(*args, **kwargs)
                time.sleep(0.01)
            except Exception as e:
                print (str(e))
            finally:
                self.__work_queue.task_done()


class ThreadPool(object):
    def __init__(self, num_threads=8):
        self.__work_queue = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.__work_queue)

    def add_job(self, func, *args, **kwargs):
        self.__work_queue.put((func, args, kwargs))

    def check_queue(self):
        return self.__work_queue.qsize

    def join_all(self):
        self.__work_queue.join()


def func2(a):
    logger.debug('func2 executing')
    result = a
    logger.debug('func2 ended with: {}'.format(result))

if __name__ == '__main__':
    logger = get_logger()
    pool = ThreadPool(4)
    for i in range(20):
        pool.add_job(func2,i)
    pool.join_all()
