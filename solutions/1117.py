"""
Question 1117: https://leetcode.com/problems/building-h2o/

Not so challenging if you know if you could use Lock.
Basically, when you call either one of the functions hydrogen or oxygen, lock the state and just catch up with
the calls that have been enqueued when there was not enough of either hydrogen or oxygen.
"""

from threading import Lock

class H2O:
    def __init__(self):
        self.h = 0
        self.o = 0
        
        self.lock = Lock()
        
        self.releaseHydrogen = None
        self.releaseOxygen = None

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.releaseHydrogen = releaseHydrogen
        
        self.lock.acquire()

        self.h = self.h + 1
        
        while self.h >= 2 and self.o > 0:
            # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()
            releaseHydrogen()
            if self.releaseOxygen:
                self.releaseOxygen()

            self.h = self.h - 2
            self.o = self.o - 1
        
        self.lock.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.releaseOxygen = releaseOxygen
        
        self.lock.acquire()
        
        self.o = self.o + 1
        
        while self.h >= 2 and self.o > 0:
            # releaseOxygen() outputs "O". Do not change or remove this line.
            releaseOxygen()
            
            if self.releaseHydrogen:
                self.releaseHydrogen()
                self.releaseHydrogen()

            self.h = self.h - 2
            self.o = self.o - 1            
        
        self.lock.release()
        
