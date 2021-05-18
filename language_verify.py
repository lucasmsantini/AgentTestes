from winreg import ConnectRegistry, OpenKey, QueryValueEx


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