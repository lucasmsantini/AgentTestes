import os
import tempfile
from datetime import time


def imprime():
    filename = tempfile.mktemp(prefix="prefix_", suffix="_suffix" '.txt')
    print('Imprimindo teste na impressora padrão do Windows...')
    open(filename, 'w').write('Teste de impressão na impressora '
                              'padrão do sistema com esta escrita '
                              'para que o Agent não descarte o '
                              'arquivo por estar com tamanho muito '
                              'pequeno')

    for i in range(10):
        os.startfile(filename, "print")
        time.sleep(1)


def imprime2():
    print('Imprimindo um arquivo texto a ser utilizado nos testes...')
    os.chdir('C:\\Windows\\System32\\Tpar')
    arquivo = open("teste" + ".txt", "w")
    arquivo.write("linha escrita.linha escrita.linha escrita.linha escrita.linha escrita. \n")
    os.startfile('teste.txt', 'print')

