import time
import win32serviceutil


def service_agent_restart():
    service_name = "nddPrint.Agent"
    print('Reiniciando serviço do Agent...')
    win32serviceutil.RestartService(service_name)
    time.sleep(10)


def service_spool_restart():

    service_name = "Spooler"
    print('Reiniciando serviço Spool do Windows...')
    win32serviceutil.RestartService(service_name)
    time.sleep(1)