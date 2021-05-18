import time
from service_restart import serviceRestart
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import xml_converter
from file_utilities import *
from print_it_for_me import imprime2
from nddPrintAgent_install import install_agent


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        print('event on_created: ', event)
        if os.path.isdir(event.src_path):
            print('return isdir')
            return

        elif is_tmp_file(event) == True:
            print('Detectado arquivo TMP criado na pasta PrintLogs')
            return

    @staticmethod
    def on_moved(event):
        print('event on_moved: ', event)
        return

    @staticmethod
    def on_modified(event):
        print('event on_modified: ', event)
        nomearquivo = str(event.src_path[35:79])
        arquivo_NPL = 'C:\\Windows\\System32\\Tpar\\PrintLogs\\'+nomearquivo
        print('------->', arquivo_NPL)
        os.system(f'copy "{arquivo_NPL}" "C:\\ProjLucas\\NPL"')
        os.system(f'C:\\projLucas\\nddPrint.Agent.NPLToXML.exe C:\\projLucas\\NPL\\{nomearquivo}')
        print('Um arquivo XML foi extraído do .NPL')
        return

    @staticmethod
    def on_deleted(event):
        print('event on_deleted: ', event)
        print('Arquivo NPL enviado ao Host')
        return


file_change_handler = Handler()
observer = Observer()
os.chdir('C:\\Windows\\System32\\Tpar\\PrintLogs')
print(os.getcwd())
observer.schedule(file_change_handler, os.getcwd(), recursive=False, )
observer.start()

install_agent()
imprime2()
time.sleep(5)
serviceRestart()
xml_converter.xmlfiletoOBJECT()
delete_files()

#

# obj = untangle.parse('C:\\projLucas\\NPL\\09-11-20210514085936545-172031249105-LLF.xml')
#
# for printer in obj.ROOT.PrintLog.Printers.Printer:
#     print(printer)
#     print('AddressMAC: ', printer.AddressMAC.cdata)
#     print(printer.AddressName.cdata)
