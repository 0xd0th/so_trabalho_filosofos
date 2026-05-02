import threading
import time
import random

class Filosofo(threading.Thread):

    def __init__(self, id, scheduler, stopevent):
        super().__init__()
        self.id = id
        self.scheduler = scheduler
        self.stopevent = stopevent
        self.prioridade = 0

    def pensar(self):
        print(f"Filósofo {self.id}: pensando")
        time.sleep(random.uniform(1, 2))

    def comer(self):
        print(f"Filósofo {self.id}: comendo")
        time.sleep(random.uniform(1, 2))

    def run(self):
        while not self.stopevent.is_set():
 
            self.pensar()

            if self.stopevent.is_set():
                break

            print(f"Filósofo {self.id}: pedindo para comer")
            self.scheduler.request_to_eat(self)

            self.comer()
            self.prioridade += 1

            
            print(f"Filósofo {self.id}: abaixando os garfos")
            self.scheduler.done_eating(self)
