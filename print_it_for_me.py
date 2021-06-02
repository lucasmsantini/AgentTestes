import os
import sys
import tempfile
from datetime import time
import time
import win32print


def imprime1(n_jobs):
    # http://timgolden.me.uk/python/win32_how_do_i/print.html
    for i in range(n_jobs):
        printer_name = win32print.GetDefaultPrinter()
        if sys.version_info >= (3,):
            raw_data = bytes('Teste de impressão na impressora '
                             'padrão do sistema com esta escrita '
                             'para que o Agent não descarte o '
                             'arquivo por estar com tamanho muito '
                             'pequeno', "utf-8")
        else:
            raw_data = ('Teste de impressão na impressora '
                        'padrão do sistema com esta escrita '
                        'para que o Agent não descarte o '
                        'arquivo por estar com tamanho muito '
                        'pequeno')
        h_printer = win32print.OpenPrinter(printer_name)
        print('Imprimindo teste na impressora padrão do Windows...')
        try:
            hJob = win32print.StartDocPrinter(h_printer, 1, (
                'Teste de impressão na impressora '
                'padrão do sistema com esta escrita '
                'para que o Agent não descarte o '
                'arquivo por estar com tamanho muito '
                'pequeno', None, "RAW"))
            try:
                win32print.StartPagePrinter(h_printer)
                win32print.WritePrinter(h_printer, raw_data)
                win32print.EndPagePrinter(h_printer)
            finally:
                win32print.EndDocPrinter(h_printer)
        finally:
            win32print.ClosePrinter(h_printer)


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


def imprime3():
    print('Imprimindo um arquivo texto a ser utilizado nos testes...')
    os.chdir('C:\\Windows\\System32\\Tpar')
    arquivo = open("teste" + ".txt", "w")
    arquivo.write("linha escrita.linha escrita.linha escrita.linha escrita.linha escrita. \n")
    os.startfile('teste.txt', 'print')
