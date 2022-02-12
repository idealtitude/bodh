#!/usr/bin/env python3.10
#-*- coding: utf-8 -*-

import sys
from time import sleep

from timing import Duration


def worker(laps: int = 5, dur: int|float = 1):
    print(f"Starting test with params: {laps=}, {dur=}\n")
    for i in range(0, laps):
        print(f"lap #{i}")
        sys.stdout.flush()
        sleep(dur)
        print(f"lap end, next: {i+i}")
        sys.stdout.flush()
    print("\nEnd of test...")

def do_test():
    timer = Duration()
    timer.start_timer()
    worker(laps=3, dur=0.75)
    timer.stop_timer()
    print(f"Duration, {timer.result=}")

if __name__ == "__main__":
    do_test()

