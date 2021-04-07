
import os
import tempfile
import time
import subprocess
import win32service
import win32serviceutil
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
from file_utilities import *
from winreg import *
from pathlib import Path
import xmltodict, json
import untangle


# print('Instalando Agent...')
# os.system('c:\\projlucas\\nddPrintAgentSetup-x64_5.50.0.msi /q')
# print('Instalação do Agent concluída')


def imprime():
    filename = tempfile.mktemp(prefix="prefix", suffix="suffix" '.txt')
    print('Imprimindo teste na impressora padrão do Windows...')
    open(filename, 'w').write('Teste de impressão na impressora '
                              'padrão do sistema com esta escrita '
                              'para que o Agent não descarte o '
                              'arquivo por estar com tamanho muito '
                              'pequeno')
    time.sleep(1)
    for i in range(10):
        os.startfile(filename, "print")

def imprime2():
    arquivo = open("teste" + ".txt", "w")
    arquivo.write("Essa é a primeira linha escrita por nós. \n")
    print(arquivo)


def serviceRestart():
    serviceName = "nddPrint.Agent"
    print('Reiniciando serviço do Agent...')
    time.sleep(10)
    win32serviceutil.RestartService(serviceName)


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        print('e= ', event)
        if os.path.isdir(event.src_path):
            print('return isdir')
            return

        elif is_tmp_file(event) == True:
            print('Detectado arquivo TMP criado na pasta PrintLogs')

            # nomearquivo = str(event.src_path[35:])
            # os.system('Copy * C:\\Windows\\System32\\Tpar\\')
            # with open(f'C:/Windows/System32/Tpar/PrintLogs/{nomearquivo}', "rb") as f:
            #     print (f)
            # #os.chmod(f'C:/Windows/System32/Tpar/PrintLogs/{nomearquivo}',0o777)
            # #shutil.copy2(Path(f'C:/Windows/System32/Tpar/PrintLogs/{nomearquivo}'),Path(f'C:/Windows/System32/Tpar/{nomearquivo}')
            # print('Arquivo copiado: ', nomearquivo)
            return

    @staticmethod
    def on_moved(event):
        print('e===== ', event)
        return

    @staticmethod
    def on_modified(event):
        print('e==modified== ', event)
        nomearquivo = str(event.src_path[35:79])
        npl = 'C:\\Windows\\System32\\Tpar\\PrintLogs\\'+nomearquivo
        print('------->', npl)
        os.system(f'copy "{npl}" "C:\\ProjLucas\\NPL"')
        os.system(f'C:\\projLucas\\nddPrint.Agent.NPLToXML.exe C:\\projLucas\\NPL\\{nomearquivo}')
        print('Um arquivo XML foi extraído do .NPL')
        return

    @staticmethod
    def on_deleted(event):
        print('e= ', event)
        print('Arquivo NPL enviado ao Host')
        return

def xmlfiletoOBJECT():

    diretorio = "C:\\projLucas\\NPL\\"
    for file in os.listdir(diretorio):
        print('Arquivos do diretótio: '+ file)
    arquivo = f'C:\\projLucas\\NPL\\{file}'
    obj = untangle.parse(arquivo)
    print('Versão: ', obj.ROOT.PrintLog.Version.cdata)
    print('EnterpriseKey: ', obj.ROOT.PrintLog.EnterpriseKey.cdata)
    print('CreateQueues: ', obj.ROOT.PrintLog.CreateQueues.cdata)
    print('CreatedDate: ', obj.ROOT.PrintLog.CreatedDate.cdata)
    print('ProductName: ', obj.ROOT.PrintLog.ProductName.cdata)
    print('ProductVersion: ', obj.ROOT.PrintLog.ProductVersion.cdata)
    print('IsEmbedded: ', obj.ROOT.PrintLog.IsEmbedded.cdata)
    print('OperationalSystem: ', obj.ROOT.PrintLog.ComputerMetaData.OperationalSystem.cdata)
    print('StrongName: ', obj.ROOT.PrintLog.ComputerMetaData.StrongName.cdata)
    print('ComputerName: ', obj.ROOT.PrintLog.ComputerMetaData.ComputerName.cdata)
    print('EnterpriseKey: ', obj.ROOT.PrintLog.ComputerMetaData.NetworkAddresses.NetworkAddress.IP.cdata)
    print('EnterpriseKey: ', obj.ROOT.PrintLog.ComputerMetaData.NetworkAddresses.NetworkAddress.Mask.cdata)
    print('EnterpriseKey: ', obj.ROOT.PrintLog.ComputerMetaData.NetworkAddresses.NetworkAddress.MacAddress.cdata)


file_change_handler = Handler()
observer = Observer()
os.chdir('C:\\Windows\\System32\\Tpar\\PrintLogs')
print(os.getcwd())
observer.schedule(file_change_handler, os.getcwd(), recursive=False, )
observer.start()

imprime()
serviceRestart()
time.sleep(5)
xmlfiletoOBJECT()



try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()




def agent_ini_portugues():
    print('Escrevendo arquivo Agent.ini...')
    agent_ini = open('Agent.ini', 'w')
    agent_ini.write('[Settings]\n'
                    'DestinationType=1\n'
                    'DestinationAddress=127.0.0.1\n'
                    'Language=pt-br')
    agent_ini.close()


def agent_ini_ingles():
    print('Escrevendo arquivo Agent.ini...')
    agent_ini = open('Agent.ini', 'w')
    agent_ini.write('[Settings]\n'
                    'DestinationType=1\n'
                    'DestinationAddress=127.0.0.1\n'
                    'Language=en-us')
    agent_ini.close()


def agent_ini_espanhol():
    print('Escrevendo arquivo Agent.ini...')
    agent_ini = open('Agent.ini', 'w')
    agent_ini.write('[Settings]\n'
                    'DestinationType=1\n'
                    'DestinationAddress=127.0.0.1\n'
                    'Language=es-es')
    agent_ini.close()


def test_verifica_linguagem_ptbr():
    cReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
    aReg = OpenKey(cReg, 'SOFTWARE\\NDDigital\\nddPrint\\MF\\HP')
    valorChave = QueryValueEx(aReg, 'InstallerLanguage')
    print('valor da chave:', valorChave)
    assert '1033' in str(valorChave)