import time

class Countdown():
    def __init__(self):
        self.my_timer = 60
        self.start = False

    def starterd(self):
        while self.my_timer > 0:
            self.start = True
            time.sleep(1)
            self.my_timer -= 1
        self.start = False
        
    def reset(self):
        self.my_timer = 60
        self.start = False
