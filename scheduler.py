
import threading
import heapq

class Scheduler:

    def __init__(self, n):
        self.n = n
        self.garfos = [True] * n  
        self.lock = threading.Lock()
        self.cond = threading.Condition(self.lock)

        self.heap = []  

    def pode_comer(self, id):
        esquerda = id
        direita = (id + 1) % self.n
        return self.garfos[esquerda] and self.garfos[direita]

    def pegar_garfos(self, id):
        self.garfos[id] = False
        self.garfos[(id + 1) % self.n] = False

    def devolver_garfos(self, id):
        self.garfos[id] = True
        self.garfos[(id + 1) % self.n] = True

    def request_to_eat(self, filosofo):
        with self.cond:
            heapq.heappush(self.heap, (filosofo.prioridade, filosofo.id, filosofo))

            while True:
                prioridade, _, f = self.heap[0]

                if f == filosofo and self.pode_comer(filosofo.id):
                    heapq.heappop(self.heap)
                    print(f"Filósofo {filosofo.id}: pegou os garfos")
                    self.pegar_garfos(filosofo.id)
                    return

                self.cond.wait()

    def done_eating(self, filosofo):
        with self.cond:
            self.devolver_garfos(filosofo.id)
            self.cond.notify_all()
