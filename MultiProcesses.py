"""
Created on Jul 29 2020

@author: ricky
"""
import multiprocessing as mp
from time import sleep


class journeys(object):
    def __init__(self, *args, **kwargs):
        pass

    def say_journeys(self, i):
        print("journey {} process.".format(i+1))

    def run(self):
        processes = list()

        for i in range(3):
            proc = mp.Process(target=self.say_journeys, args=(i,))
            processes.append(proc)

        for proc in processes:
            proc.start()
            proc.join()

if __name__ == "__main__":
    journey = journeys()
    journey.run()

