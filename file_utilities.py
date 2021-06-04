import glob
import shutil
import os
import time
from service_restart import service_agent_restart


def extension_type(event):
    return event.src_path[event.src_path.rindex('.') + 1:]


def is_npl_file(event):
    if extension_type(event) in ('npl', 'NPL'):
        return True
    return False


def is_tmp_file(event):
    if extension_type(event) in ('txt', 'tmp'):

        return True
    return False


def make_folder(foldername):
    os.chdir('C:\\AgentTestes\\NPL')
    if os.path.exists(foldername):
        print('Folder already exists, skipping creation')
        return os.getcwd() + os.sep + str(foldername)
    else:
        os.mkdir(str(foldername))
        return os.getcwd() + os.sep + str(foldername)


def copy_to_new_corresponding_folder(event, path_to_new_folder):
    try:
        shutil.copy(event.src_path, path_to_new_folder)
        print('coping file')
    except:
        print('File already existed in target folder')
        pass


def wait_for_npl():
    dir_tpar = 'C:\\Windows\\System32\\tpar\\PrintLogs\\'
    os.chdir(dir_tpar)
    file = os.listdir()
    print('Arquivo da TPAR: ', file)
    while not file:
        print('Aguardando NPL')
        time.sleep(2)
        service_agent_restart()
        file = os.listdir()
        if not file == []:
            print('Arquivo da TPAR: ', file)
            break
    return True

def delete_files():
    os.chdir('c:\\AgentTestes\\NPL')
    time.sleep(3)
    npl_files = glob.glob('*.npl')
    xml_files = glob.glob('*.xml')
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
