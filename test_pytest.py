import getpass
import win32print
import main
from file_utilities import delete_files
from xml_converter import xml_file_to_object
import wmi
import socket
from getmac import get_mac_address as gma

def test_install():
    pass


def test_verify_os():
    # Pegar os dados do XML:
    obj = xml_file_to_object()
    computer_operational_system = obj['computer_OperationalSystem']
    print(computer_operational_system[8:12])
    # Pegar os dados do Windows:
    c = wmi.WMI()
    for os_name in c.Win32_OperatingSystem():
        print(os_name.Caption)
    assert computer_operational_system[8:12] in os_name.Caption
    delete_files()


def test_verify_hostname():
    obj = xml_file_to_object()
    computer_computer_name = obj['computer_ComputerName']
    print(computer_computer_name)
    print(socket.gethostname())
    assert socket.gethostname() == computer_computer_name
    delete_files()


def test_verify_computer_ip():
    obj = xml_file_to_object()
    computer_ip = obj['computer_IP']
    print(computer_ip)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(ip_address)
    assert computer_ip == ip_address
    delete_files()


def test_verify_computer_address_mac():
    obj = xml_file_to_object()
    xml_computer_mac = obj['computer_AddressMac']
    print(xml_computer_mac)
    get_computer_mac = gma().replace(':', '-')
    print(get_computer_mac)
    assert get_computer_mac == xml_computer_mac
    delete_files()


def test_verify_printer_queue_name():
    obj = xml_file_to_object()
    printer_queue_name = obj['printer_QueueName']
    print(printer_queue_name)
    print(win32print.GetDefaultPrinter())
    assert win32print.GetDefaultPrinter() == printer_queue_name
    delete_files()


def test_verify_user_logon_name():
    obj = xml_file_to_object()
    user_logon_name = obj['user_LogonName']
    print(user_logon_name)
    print(getpass.getuser())
    assert getpass.getuser() == user_logon_name
    delete_files()


def test_verify_total_jobs():
    obj = xml_file_to_object()
    total_jobs = obj['total_jobs']
    print(total_jobs)
    print(main.jobs_for_print)
    assert total_jobs == main.jobs_for_print
    delete_files()
