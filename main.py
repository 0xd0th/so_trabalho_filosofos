
from filosofo import Filosofo
from scheduler import Scheduler

NUM_FILOSOFOS = 5

if __name__ == "__main__":

    scheduler = Scheduler(NUM_FILOSOFOS)

    filosofos = [Filosofo(i, scheduler) for i in range(NUM_FILOSOFOS)]

    for f in filosofos:
        f.start()

