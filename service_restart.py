import time
import win32serviceutil


def service_agent_restart():
    serviceName = "nddPrint.Agent"
    print('Reiniciando serviço do Agent...')
    win32serviceutil.RestartService(serviceName)
    # time.sleep(10)


def service_spool_restart():
    serviceName = "Spooler"
    print('Reiniciando serviço Spool do Windows...')
    win32serviceutil.RestartService(serviceName)
    time.sleep(1)