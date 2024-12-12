
from abc import ABC, abstractmethod

class Employee(ABC):
    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Managers job.....")


class Developer(Employee):

    def doJob(self):
        print("Write code......")


def BankJob(emp):
    print("Bankjob Started........")
    emp.doJob()
    print("Bankjob ended..........")
    print("-" * 60)


mike = Manager()
dave = Developer()

BankJob(mike)
BankJob(dave)

