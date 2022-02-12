#-*- coding: utf-8 -*-

from time import perf_counter


class Duration:
    def __init__(self):
        self.start    : float = 0.0
        self.stop     : float = 0.0
        self.duration : float = 0.0

    def start_timer(self):
        self.start = perf_counter()

    def stop_timer(self):
        self.stop = perf_counter()
        self.duration = self.stop - self.start

    @property
    def result(self):
        return self.duration

if __name__ == "__main__":
    print("Not to be tested directly")
