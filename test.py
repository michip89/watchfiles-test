import time
import signal

# https://stackoverflow.com/questions/1112343/how-do-i-capture-sigint-in-python
class GracefulInterruptHandler(object):
    def __init__(self, signals=(signal.SIGINT, signal.SIGTERM)):
        self.signals = signals
        self.original_handlers = {}
        self.signum = None

    def __enter__(self):
        self.interrupted = False
        self.released = False

        for sig in self.signals:
            self.original_handlers[sig] = signal.getsignal(sig)
            signal.signal(sig, self.handler)

        return self

    def handler(self, signum, frame):
        self.signum = signum
        self.release()
        self.interrupted = True

    def __exit__(self, type, value, tb):
        self.release()

    def release(self):
        if self.released:
            return False

        for sig in self.signals:
            signal.signal(sig, self.original_handlers[sig])

        self.released = True
        return True


if __name__ == '__main__':
    i = 0
    with GracefulInterruptHandler() as h:
        while True:
            print(i)
            i += 1
            time.sleep(1)
            if h.interrupted:
                break
    print("Shutdown")

