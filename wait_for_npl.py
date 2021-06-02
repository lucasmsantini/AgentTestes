import os
import time


def wait_for_npl():
    dir_tpar = 'C:\\Windows\\System32\\tpar\\PrintLogs\\'
    os.chdir(dir_tpar)
    file = os.listdir()
    print('Arquivo da TPAR: ', file)
    while not file:
        print('Aguardando NPL')
        time.sleep(4)
        file = os.listdir()
        if not file == []:
            print('Arquivo da TPAR: ', file)
            break
