"""
 Dining philosophers, 5 Phillies with 5 forks. Must have two forks to eat.

 Deadlock is avoided by never waiting for a fork while holding a fork (locked)
 Procedure is to do block while waiting to get first fork, and a nonblocking
 acquire of second fork.  If failed to get second fork, release first fork,
 swap which fork is first and which is second and retry until getting both.
"""
import threading
import random
import time


class Philosopher(threading.Thread):

    running = True

    def __init__(self, xname: str, fork_on_left: threading.Lock, fork_on_right: threading.Lock):
        super().__init__()
        self.name = xname
        self.fork_on_left = fork_on_left
        self.fork_on_right = fork_on_right

    def run(self):
        while self.running:
            #  Philosopher is thinking (but really is sleeping).
            time.sleep(random.uniform(3, 13))
            print(f"{self.name} is hungry")
            self.dine()

    def dine(self):
        fork1, fork2 = self.fork_on_left, self.fork_on_right

        while self.running:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked:
                break
            fork1.release()
            print(f"{self.name} swaps forks")
            fork1, fork2 = fork2, fork1  # ?
        else:
            return

        self.dining()
        fork2.release()
        fork1.release()

    def dining(self):
        print(f"{self.name} starts eating")
        time.sleep(random.uniform(1, 10))
        print(f"{self.name} finishes eating and leaves to think")


if __name__ == "__main__":
    forks = [threading.Lock() for _ in range(5)]
    philosopher_names = ('Aristotle', 'Kant', 'Buddha', 'Marx', 'Russel')

    philosophers = [Philosopher(
        philosopher_names[i], forks[i % 5], forks[(i+1) % 5]) for i in range(5)]

    # random.seed(2137)
    for p in philosophers:
        p.start()
    time.sleep(15)
    print("Now we're finishing")
    Philosopher.running = False
