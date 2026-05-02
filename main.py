
import threading
import time

from filosofo import Filosofo
from scheduler import Scheduler

NUM_FILOSOFOS = 5

stop_event = threading.Event()


if __name__ == "__main__":

    scheduler = Scheduler(NUM_FILOSOFOS)

    filosofos = [Filosofo(i, scheduler, stop_event) for i in range(NUM_FILOSOFOS)]

    for f in filosofos:
        f.start()

    try:
        while True:
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nCtrl+C detectado! Encerrando...")

        stop_event.set()

        with scheduler.cond:
            scheduler.cond.notify_all()

        resultados = [0]*NUM_FILOSOFOS
        for idx,f in enumerate(filosofos):
            f.join()
            resultados[idx] = f.prioridade
        

        print(f"\n{15*'-'} resutados {15*'-'}\n")
        for idx,f in enumerate(resultados): 
            print(f"Filósofo {idx} comeu {f} vezes")

        print("\nPrograma encerrado corretamente.")