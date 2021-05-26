import os
import tempfile
from datetime import time
import time

# jobs_for_print = 10
# object_xml = {'jobs_for_print': jobs_for_print}
# print('obj_print_t_for_me: ', object_xml)


def imprime2(n_jobs):
    filename = tempfile.mktemp(prefix="prefix_", suffix="_suffix" '.txt')
    print('Imprimindo teste na impressora padrão do Windows...')
    open(filename, 'w').write('Teste de impressão na impressora '
                              'padrão do sistema com esta escrita '
                              'para que o Agent não descarte o '
                              'arquivo por estar com tamanho muito '
                              'pequeno')
    for i in range(n_jobs):
        os.startfile(filename, "print")
        time.sleep(1)


def imprime():
    print('Imprimindo um arquivo texto a ser utilizado nos testes...')
    os.chdir('C:\\Windows\\System32\\Tpar')
    arquivo = open("teste" + ".txt", "w")
    arquivo.write("linha escrita.linha escrita.linha escrita.linha escrita.linha escrita. \n")
    os.startfile('teste.txt', 'print')
