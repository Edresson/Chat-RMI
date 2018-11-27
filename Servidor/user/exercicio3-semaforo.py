import threading
import time

class myThread(threading.Thread):
    def __init__(self, name, tvd,tam,tvm,estadoinicial):
        threading.Thread.__init__(self)
        self.name = name
        self.tempovd= tvd
        self.tempoam= tam
        self.tempovm= tvm
        self.estadoinicial = estadoinicial

    def run(self):
        if self.estadoinicial == 1:#inicia o semaforo no verde

            while(True):
                print('Estado '+str(self.name)+': VERDE')
                time.sleep(self.tempovd)
                print('Estado '+str(self.name)+': AMARELO')
                time.sleep(self.tempoam)
                print('Estado '+str(self.name)+': VERMELHO')
                time.sleep(self.tempovm)

        else:#inicia no vermelho
            while(True):
                print('Estado '+str(self.name)+': VERMELHO')
                time.sleep(self.tempovm)
                print('Estado '+str(self.name)+': VERDE')
                time.sleep(self.tempovd)
                print('Estado '+str(self.name)+': AMARELO')
                time.sleep(self.tempoam)
                

        print(str(self.name)+' Fim')
        #currentTreadname = threading.currentThread()
        #print( "running in", currentTreadname  )
        #print( 'threading.main_thread()', threading.main_thread())



thread = myThread("R1 ",0.3,0.1,0.4,1)
thread2 = myThread("R2 ",0.3,0.1,0.4,2)

thread.start()
thread2.start()
thread.join()
thread2.join()

