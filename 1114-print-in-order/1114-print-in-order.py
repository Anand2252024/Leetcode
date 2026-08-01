import threading

class Foo:
    def __init__(self):
        self.first_done = threading.Event()
        self.second_done = threading.Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        # Signal that first() is done
        self.first_done.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # Wait until first() has finished
        self.first_done.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        # Signal that second() is done
        self.second_done.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # Wait until second() has finished
        self.second_done.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
