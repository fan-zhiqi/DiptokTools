import threading
threadLock = threading.Lock()
threads = []


import time

from datetime import datetime


import sys

from DiptokTools.message.eathFollow import eath_follow



'''動作'''
class Print():
    def print_time(self):
            print(datetime.now())
            time.sleep(6)

class PrintName():
    def __init__(self,name):
        self.name = name
    def return_name(self):
        print(self.name)

'''业务'''
class AddThreadNamePrint():
    def __init__(self,name,mobile):
        self.mobile = mobile
        self.ptime = Print()
        self.pname = PrintName(name)

    def print_name(self):
            self.pname.return_name()
            self.ptime.print_time()
            eath_follow(self.mobile)



# AddThreadNamePrint("业务").print_name()

'''重寫綫程run'''
class Threading(threading.Thread):
    def __init__(self,name,mobile):
        threading.Thread.__init__(self)
        self.name = name
        self.mobile = mobile

    def run(self):
        threadLock.acquire()
        AddThreadNamePrint(self.name,self.mobile).print_name()
        threadLock.release()



'''执行线程'''
class CreatThread(Threading):
    def __init__(self,name,mobile):
        super().__init__(name, mobile)

    def start_thread(self):
        self.start()
        self.join(1)


if __name__ == '__main__':
    '''实例线程'''
    n=0
    while n<5:
        CreatThread("线程1",13632422014).start_thread()

        CreatThread("线程2",13632422014).start_thread()
        n+=1
