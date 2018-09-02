import random
from builtins import sum

from pythonds.basic.queue import Queue


class Printer:
    """
    打印机类：判断当前是否有任务
    """
    def __init__(self, ppm):
        # 打印速度
        self.pagerate = ppm
        # 当前任务
        self.currentTask = None
        # 剩余时间
        self.timeRemaining = 0

    # 定时器
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    # 判断是否空闲
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate


class Task:
    """
    任务类：表示单个任务，随机生成1-20页的任务长度
    """
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    # 记录时间戳
    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    # 打印任务队列
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averagewait = sum(waitingtimes) / len(waitingtimes)
    print('Average Wait %6.2f secs %3d tasks remaining.' % (averagewait, printQueue.size()))


def newPrintTask():
    """决定是否创建一个新的打印任务"""
    # num表示任务发生的机会
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


for i in range(10):
    simulation(3600, 10)