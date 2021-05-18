import time
import win32serviceutil


def serviceRestart():
    serviceName = "nddPrint.Agent"
    print('Reiniciando serviço do Agent...')
    win32serviceutil.RestartService(serviceName)
    time.sleep(10)
