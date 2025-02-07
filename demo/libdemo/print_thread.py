from threading import *


class PrintThread(Thread):
    def run(self):
        for i in range(1, 6):
            print(f"Print Thread : {i}")


pt = PrintThread()
pt.start()
# Main Thread
for i in range(1, 6):
    print(f"Main Thread : {i}")