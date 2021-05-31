import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import xml_converter
from file_utilities import *
from print_it_for_me import imprime1, imprime2, imprime3
from service_restart import *
from nddPrintAgent_install import install_agent


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        print('event on_created: ', event)
        if os.path.isdir(event.src_path):
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
        time.sleep(3)
        print('event on_modified: ', event)
        # while not event:
        #     time.sleep(1)
        #     print('Aguardando NPL')
        # else:
        #     print('Arquivo NPL encontrado')

        name_file = str(event.src_path[35:79])
        npl_file = 'C:\\Windows\\System32\\Tpar\\PrintLogs\\'+name_file
        print('Arquivo NPL', npl_file)
        os.system(f'copy "{npl_file}" "C:\\NPL"')
        os.system(f'C:\\AgentTestes\\nddPrint.Agent.NPLToXML.exe c:\\npl\\{name_file}')
        print('Um arquivo XML foi extra do .NPL')
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

#install_agent()
#imprime2()

jobs_for_print = 10
imprime1(jobs_for_print)
time.sleep(jobs_for_print + 5)

# dir_tpar = os.listdir('C:\\Windows\\System32\\tpar\\PrintLogs')
# print('dir_tpar', dir_tpar)
# while dir_tpar == []:
#     print('Aguardando NPL')
#     print('dir_tpar- while', dir_tpar)
#     time.sleep(4)
#     # service_agent_restart()
#     if not dir_tpar == []:
#         print('dir_tpar- while - IF', dir_tpar)
#         break
# else:
#     print("fim while")

# service_agent_restart()
xml_converter.xml_file_to_object()
time.sleep(15)
#service_spool_restart()
delete_files()

# obj = untangle.parse('C:\\projLucas\\NPL\\09-11-20210514085936545-172031249105-LLF.xml')
#
# for printer in obj.ROOT.PrintLog.Printers.Printer:
#     print(printer)
#     print('AddressMAC: ', printer.AddressMAC.cdata)
#     print(printer.AddressName.cdata)
