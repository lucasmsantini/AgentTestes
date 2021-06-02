from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import xml_converter
import time
from file_utilities import *
from print_it_for_me import imprime1, imprime2, imprime3
from service_restart import *
from nddPrintAgent_install import install_agent
from wait_for_npl import wait_for_npl


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        print('event on_created: ', event)
        if os.path.isdir(event.src_path):
            return
        elif is_tmp_file(event) == True:
            print('Detectado arquivo TMP criado na pasta PrintLogs')
            return
    #
    # @staticmethod
    # def on_moved(event):
    #     return

    @staticmethod
    def on_modified(event):

        time.sleep(0.1)
        name_file = str(event.src_path[35:79])
        npl_file = 'C:\\Windows\\System32\\Tpar\\PrintLogs\\'+name_file
        print('Arquivo NPL', npl_file)
        os.system(f'copy "{npl_file}" "c:\\AgentTestes\\NPL\\"')
        time.sleep(1)
        os.system(f'c:\\AgentTestes\\nddPrint.Agent.NPLToXML.exe c:\\AgentTestes\\npl\\{name_file}')
        print('Um arquivo XML foi extra do .NPL')
        return

    @staticmethod
    def on_deleted(event):
        print('Arquivo NPL enviado ao Host')
        return


file_change_handler = Handler()
observer = Observer()
os.chdir('C:\\Windows\\System32\\Tpar\\PrintLogs')
print(os.getcwd())
observer.schedule(file_change_handler, os.getcwd(), recursive=False, )
observer.start()

install_agent()
jobs_for_print = 5
imprime1(jobs_for_print)
wait_for_npl()
# time.sleep(jobs_for_print + 1)
service_agent_restart()
xml_converter.xml_file_to_object()
time.sleep(5)

