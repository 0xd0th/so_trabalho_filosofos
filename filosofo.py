import threading
import time
import random

class Filosofo(threading.Thread):

    def __init__(self, id, scheduler):
        super().__init__()
        self.id = id
        self.scheduler = scheduler
        self.prioridade = 0

    def pensar(self):
        print(f"Filósofo {self.id} está pensando")
        time.sleep(random.uniform(1, 2))

    def comer(self):
        print(f"Filósofo {self.id} está comendo")
        time.sleep(random.uniform(1, 2))

    def run(self):
        while True:
            self.pensar()

            self.scheduler.request_to_eat(self)

            self.comer()
            self.prioridade += 1

            self.scheduler.done_eating(self)