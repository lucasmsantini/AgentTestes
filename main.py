
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
import glob
import xmltodict, json
import untangle


print('Instalando Agent...')
os.system('c:\\projlucas\\nddPrintAgentSetup-x64_5.50.0.msi /q')
print('Instalação do Agent concluída')


def imprime():
    filename = tempfile.mktemp(prefix="prefix_", suffix="_suffix" '.txt')
    print('Imprimindo teste na impressora padrão do Windows...')
    open(filename, 'w').write('Teste de impressão na impressora '
                              'padrão do sistema com esta escrita '
                              'para que o Agent não descarte o '
                              'arquivo por estar com tamanho muito '
                              'pequeno')

    for i in range(3):
        os.startfile(filename, "print")


def imprime2():
    arquivo = open("teste" + ".txt", "w")
    arquivo.write("linha escrita. \n")
    print(arquivo)


def serviceRestart():
    serviceName = "nddPrint.Agent"
    print('Reiniciando serviço do Agent...')
    win32serviceutil.RestartService(serviceName)
    time.sleep(10)


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
        arquivo_NPL = 'C:\\Windows\\System32\\Tpar\\PrintLogs\\'+nomearquivo
        print('------->', arquivo_NPL)
        os.system(f'copy "{arquivo_NPL}" "C:\\ProjLucas\\NPL"')
        os.system(f'C:\\projLucas\\nddPrint.Agent.NPLToXML.exe C:\\projLucas\\NPL\\{nomearquivo}')
        print('Um arquivo XML foi extraído do .NPL')
        #os.remove(arquivo_NPL)
        #print('Arquivo ', arquivo_NPL, 'removido')
        return

    @staticmethod
    def on_deleted(event):
        print('e= ', event)
        print('Arquivo NPL enviado ao Host')
        return

def xmlfiletoOBJECT():

    npl_files = glob.glob('c:/projLucas/NPL/*.NPL')
    #xml_files = glob.glob('c:\\projLucas\\NPL*.xml')
    diretorio = "C:\\projLucas\\NPL\\"
    arquivos_da_pasta = os.listdir(diretorio)
    xml_file = (diretorio + arquivos_da_pasta[1])
    # for file in os.listdir(diretorio):
    #     print('Arquivos do diretótio: '+ file)
    # arquivo_XML = f'C:\\projLucas\\NPL\\{file}'
    print('Arquivo que vai para o Parser: ', xml_file)
    obj = untangle.parse(xml_file)

    # path = Path(npl_files)
    # print('path.suffix: ', path.suffix)
    # print('path.stem: ', path.stem)

    print('------PRINTLOG-------')
    print('Versão: ', obj.ROOT.PrintLog.Version.cdata)
    print('EnterpriseKey: ', obj.ROOT.PrintLog.EnterpriseKey.cdata)
    print('CreateQueues: ', obj.ROOT.PrintLog.CreateQueues.cdata)
    print('CreatedDate: ', obj.ROOT.PrintLog.CreatedDate.cdata)
    print('ProductName: ', obj.ROOT.PrintLog.ProductName.cdata)
    print('ProductVersion: ', obj.ROOT.PrintLog.ProductVersion.cdata)
    print('IsEmbedded: ', obj.ROOT.PrintLog.IsEmbedded.cdata)

    print('------ComputerMetaData-------')
    print('OperationalSystem: ', obj.ROOT.PrintLog.ComputerMetaData.OperationalSystem.cdata)
    print('StrongName: ', obj.ROOT.PrintLog.ComputerMetaData.StrongName.cdata)
    print('ComputerName: ', obj.ROOT.PrintLog.ComputerMetaData.ComputerName.cdata)
    print('IP: ', obj.ROOT.PrintLog.ComputerMetaData.NetworkAddresses.NetworkAddress.IP.cdata)
    print('Mask: ', obj.ROOT.PrintLog.ComputerMetaData.NetworkAddresses.NetworkAddress.Mask.cdata)
    print('MacAddress: ', obj.ROOT.PrintLog.ComputerMetaData.NetworkAddresses.NetworkAddress.MacAddress.cdata)

    print('------PRINTERS-------')
    print('Impressoras detectadas: ', len(obj.ROOT.PrintLog.Printers.Printer))
    x = range(len(obj.ROOT.PrintLog.Printers.Printer))
    for n in x:
        print('Printer ID: ', obj.ROOT.PrintLog.Printers.Printer[n]['ID'])
        print('Printer AddressMAC: ', obj.ROOT.PrintLog.Printers.Printer[n].AddressMAC.cdata)
        print('Printer AddressName: ', obj.ROOT.PrintLog.Printers.Printer[n].AddressName.cdata)
        print('Printer AddressPort: ', obj.ROOT.PrintLog.Printers.Printer[n].AddressPort.cdata)
        print('Printer DeviceManufacturer: ', obj.ROOT.PrintLog.Printers.Printer[n].DeviceManufacturer.cdata)
        print('Printer DeviceModelName: ', obj.ROOT.PrintLog.Printers.Printer[n].DeviceModelName.cdata)
        print('Printer DeviceSerialNumber: ', obj.ROOT.PrintLog.Printers.Printer[n].DeviceSerialNumber.cdata)
        print('Printer IsColor: ', obj.ROOT.PrintLog.Printers.Printer[n].IsColor.cdata)
        print('Printer IsCopier: ', obj.ROOT.PrintLog.Printers.Printer[n].IsCopier.cdata)
        print('Printer IsDuplex: ', obj.ROOT.PrintLog.Printers.Printer[n].IsDuplex.cdata)
        print('Printer IsFax: ', obj.ROOT.PrintLog.Printers.Printer[n].IsFax.cdata)
        print('Printer IsScan: ', obj.ROOT.PrintLog.Printers.Printer[n].IsScan.cdata)
        print('Printer PrinterType: ', obj.ROOT.PrintLog.Printers.Printer[n].PrinterType.cdata)
        print('Printer QueueDriverName: ', obj.ROOT.PrintLog.Printers.Printer[n].QueueDriverName.cdata)
        print('Printer QueueName: ', obj.ROOT.PrintLog.Printers.Printer[n].QueueName.cdata)
        print('Printer QueuePort: ', obj.ROOT.PrintLog.Printers.Printer[n].QueuePort.cdata)
        print('--------- Fim Printer ID: ', obj.ROOT.PrintLog.Printers.Printer[n]['ID'])

    print('------PRINTJOBS-------')
    print('Documentos impressos: ', len(obj.ROOT.PrintLog.PrintJobs.PrintJob))
    y = range(len(obj.ROOT.PrintLog.PrintJobs.PrintJob))
    for n in y:
        job_data = (obj.ROOT.PrintLog.PrintJobs.PrintJob[0].Data.cdata.replace('Â','').split('¬'))
        print('PrintJob.Data: ', job_data)
        print('Título do Job: ', job_data[23])
        print('Hostname do Job: ', job_data[22])
        print('PrinterID do Job: ', job_data[4])
        print('Data do Job: ', job_data[12])
        print('Hora do Job: ', job_data[13])
        print('Tamanho do Job: ', job_data[11])
        print('Tipo de papel do Job: ', job_data[5])
        print('Qualidade do Job: ', job_data[5])

# 1¬1¬0¬600¬672¬9¬1¬1¬0¬0¬0¬50738¬2021/04/27¬08:52:39¬0¬0¬0¬¬¬0¬0¬¬NDD-VM-TES4919¬prefix_xxvwlp1w_suffix.txt - Notepad
#       3   4   5           11    12         13                    22             23

    print('------USERS-------')
    print('UserID: ', obj.ROOT.PrintLog.Users.User.UserID.cdata)
    print('LogonName: ', obj.ROOT.PrintLog.Users.User.LogonName.cdata)
    print('FullName: ', obj.ROOT.PrintLog.Users.User.FullName.cdata)
    print('DomainName: ', obj.ROOT.PrintLog.Users.User.DomainName.cdata)
    print('DomainType: ', obj.ROOT.PrintLog.Users.User.DomainType.cdata)

    # os.remove(arquivo_XML)
    # print('Arquivo xml removido')

    xml_files = glob.glob('c:/projLucas/NPL/*.xml')
    xml_files2 = glob.glob('c:/projLucas/NPL/*.xml')

    for npl in npl_files:
        try:
            os.remove(npl)
            print('Arquivo npl removido')
        except OSError as e:
            print(f"Error:{e.strerror}")

    for xml in xml_files:
        try:
            os.remove(xml)
            print('Arquivo xml removido')
        except OSError as e:
            print(f"Error:{e.strerror}")


file_change_handler = Handler()
observer = Observer()
os.chdir('C:\\Windows\\System32\\Tpar\\PrintLogs')
print(os.getcwd())
observer.schedule(file_change_handler, os.getcwd(), recursive=False, )
observer.start()

imprime()
time.sleep(5)
serviceRestart()

xmlfiletoOBJECT()


# try:
#     while True:
#         time.sleep(1)
# except KeyboardInterrupt:
#     observer.stop()
# observer.join()

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
