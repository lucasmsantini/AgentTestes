import untangle
import os
import win32print
import time


def xml_file_to_object():
    try:

        dir_npl = "c:\\AgentTestes\\NPL\\"
        files_to_convert = os.listdir(dir_npl)
        print("Arquivos da pasta: ", files_to_convert)
        xml_file = str(dir_npl + files_to_convert[1])
        print('Arquivo que vai para o Parser: ', xml_file)
        obj = untangle.parse(xml_file)

        print('------PRINTLOG-------')
        printlog_version = obj.ROOT.PrintLog.Version.cdata
        #printlog_enterpriseKey = obj.ROOT.PrintLog.EnterpriseKey.cdata
        printlog_createQueues = obj.ROOT.PrintLog.CreateQueues.cdata
        printlog_createdDate = obj.ROOT.PrintLog.CreatedDate.cdata
        printlog_productName = obj.ROOT.PrintLog.ProductName.cdata
        printlog_productVersion = obj.ROOT.PrintLog.ProductVersion.cdata
        printlog_isEmbedded = obj.ROOT.PrintLog.IsEmbedded.cdata

        print('Versão: ', obj.ROOT.PrintLog.Version.cdata)
        #print('EnterpriseKey: ', obj.ROOT.PrintLog.EnterpriseKey.cdata)
        print('CreateQueues: ', obj.ROOT.PrintLog.CreateQueues.cdata)
        print('CreatedDate: ', obj.ROOT.PrintLog.CreatedDate.cdata)
        print('ProductName: ', obj.ROOT.PrintLog.ProductName.cdata)
        print('ProductVersion: ', obj.ROOT.PrintLog.ProductVersion.cdata)
        print('IsEmbedded: ', obj.ROOT.PrintLog.IsEmbedded.cdata)

        print('------ComputerMetaData-------')
        computer_OperationalSystem = obj.ROOT.PrintLog.ComputerMetaData.OperationalSystem.cdata
        computer_StrongName = obj.ROOT.PrintLog.ComputerMetaData.StrongName.cdata
        computer_ComputerName = obj.ROOT.PrintLog.ComputerMetaData.ComputerName.cdata
        computer_IP = obj.ROOT.PrintLog.ComputerMetaData.NetworkAddresses.NetworkAddress.IP.cdata
        computer_Mask = obj.ROOT.PrintLog.ComputerMetaData.NetworkAddresses.NetworkAddress.Mask.cdata
        computer_MacAddress = obj.ROOT.PrintLog.ComputerMetaData.NetworkAddresses.NetworkAddress.MacAddress.cdata

        print('OperationalSystem: ', obj.ROOT.PrintLog.ComputerMetaData.OperationalSystem.cdata)
        print('StrongName: ', obj.ROOT.PrintLog.ComputerMetaData.StrongName.cdata)
        print('ComputerName: ', obj.ROOT.PrintLog.ComputerMetaData.ComputerName.cdata)
        print('IP: ', obj.ROOT.PrintLog.ComputerMetaData.NetworkAddresses.NetworkAddress.IP.cdata)
        print('Mask: ', obj.ROOT.PrintLog.ComputerMetaData.NetworkAddresses.NetworkAddress.Mask.cdata)
        print('MacAddress: ', obj.ROOT.PrintLog.ComputerMetaData.NetworkAddresses.NetworkAddress.MacAddress.cdata)

        print('------PRINTERS-------')
        for printer in obj.ROOT.PrintLog.Printers.Printer:
            print('Impressoras detectadas: ', len(obj.ROOT.PrintLog.Printers))
            if win32print.GetDefaultPrinter() in printer.QueueName.cdata:
                printers_on_log = len(obj.ROOT.PrintLog.Printers)
                #Printer_ID = obj.ROOT.PrintLog.Printers.Printer['ID']
                printer_AddressMAC = printer.AddressMAC.cdata
                printer_AddressName = printer.AddressName.cdata
                printer_AddressPort = printer.AddressPort.cdata
                printer_DeviceManufacturer = printer.DeviceManufacturer.cdata
                printer_DeviceModelName = printer.DeviceModelName.cdata
                printer_DeviceSerialNumber = printer.DeviceSerialNumber.cdata
                printer_IsColor = printer.IsColor.cdata
                printer_IsCopier = printer.IsCopier.cdata
                printer_IsDuplex = printer.IsDuplex.cdata
                printer_IsFax = printer.IsFax.cdata
                printer_IsScan = printer.IsScan.cdata
                printer_PrinterType = printer.PrinterType.cdata
                printer_QueueDriverName = printer.QueueDriverName.cdata
                printer_QueueName = printer.QueueName.cdata
                printer_QueuePort = printer.QueuePort.cdata

                print('INFO: Esta é a impressora padrão do Windows')
                print('Printer ID: ', printer['ID'])
                print('Printer AddressMAC: ', printer.AddressMAC.cdata)
                print('Printer AddressName: ', printer.AddressName.cdata)
                print('Printer AddressPort: ', printer.AddressPort.cdata)
                print('Printer DeviceManufacturer: ', printer.DeviceManufacturer.cdata)
                print('Printer DeviceModelName: ', printer.DeviceModelName.cdata)
                print('Printer DeviceSerialNumber: ', printer.DeviceSerialNumber.cdata)
                print('Printer IsColor: ', printer.IsColor.cdata)
                print('Printer IsCopier: ', printer.IsCopier.cdata)
                print('Printer IsDuplex: ', printer.IsDuplex.cdata)
                print('Printer IsFax: ', printer.IsFax.cdata)
                print('Printer IsScan: ', printer.IsScan.cdata)
                print('Printer PrinterType: ', printer.PrinterType.cdata)
                print('Printer QueueDriverName: ', printer.QueueDriverName.cdata)
                print('Printer QueueName: ', printer.QueueName.cdata)
                print('Printer QueuePort: ', printer.QueuePort.cdata)
                print('Fim Printer ID: ', printer['ID'])
            else:
                _printer_AddressMAC_ = printer.AddressMAC.cdata
                _printer_AddressName = printer.AddressName.cdata
                _printer_AddressPort = printer.AddressPort.cdata
                _printer_DeviceManufacturer = printer.DeviceManufacturer.cdata
                _printer_DeviceModelName = printer.DeviceModelName.cdata
                _printer_DeviceSerialNumber = printer.DeviceSerialNumber.cdata
                _printer_IsColor = printer.IsColor.cdata
                _printer_IsCopier = printer.IsCopier.cdata
                _printer_IsDuplex = printer.IsDuplex.cdata
                _printer_IsFax = printer.IsFax.cdata
                _printer_IsScan = printer.IsScan.cdata
                _printer_PrinterType = printer.PrinterType.cdata
                _printer_QueueDriverName = printer.QueueDriverName.cdata
                _printer_QueueName = printer.QueueName.cdata
                _printer_QueuePort = printer.QueuePort.cdata

                print('Outras impresoras:')
                print('Printer ID: ', printer['ID'])
                print('Printer AddressMAC: ', printer.AddressMAC.cdata)
                print('Printer AddressName: ', printer.AddressName.cdata)
                print('Printer AddressPort: ', printer.AddressPort.cdata)
                print('Printer DeviceManufacturer: ', printer.DeviceManufacturer.cdata)
                print('Printer DeviceModelName: ', printer.DeviceModelName.cdata)
                print('Printer DeviceSerialNumber: ', printer.DeviceSerialNumber.cdata)
                print('Printer IsColor: ', printer.IsColor.cdata)
                print('Printer IsCopier: ', printer.IsCopier.cdata)
                print('Printer IsDuplex: ', printer.IsDuplex.cdata)
                print('Printer IsFax: ', printer.IsFax.cdata)
                print('Printer IsScan: ', printer.IsScan.cdata)
                print('Printer PrinterType: ', printer.PrinterType.cdata)
                print('Printer QueueDriverName: ', printer.QueueDriverName.cdata)
                print('Printer QueueName: ', printer.QueueName.cdata)
                print('Printer QueuePort: ', printer.QueuePort.cdata)
                print('Fim Printer ID: ', printer['ID'])

        print('------PRINTJOBS-------')
        for printjob in obj.ROOT.PrintLog.PrintJobs.PrintJob:
            total_jobs = len(obj.ROOT.PrintLog.PrintJobs.PrintJob)
            job_data = printjob.Data.cdata
            job_data_converted = (str(job_data).replace('Â', '').split('¬'))
            print_job_title = job_data[23]
            print_job_hostname = job_data[22]
            print_job_printerID = job_data[4]
            print_job_date = job_data[12]
            print_job_time = job_data[13]
            print_job_size = job_data[11]
            print_job_paperType = job_data[5]
            print_job_quality = job_data[3]
            print('Total Jobs: ', len(obj.ROOT.PrintLog.PrintJobs.PrintJob))
            print('Título do Job: ', job_data_converted[23])
            print('Hostname do Job: ', job_data_converted[22])
            print('PrinterID do Job: ', job_data_converted[4])
            print('Data do Job: ', job_data_converted[12])
            print('Hora do Job: ', job_data_converted[13])
            print('Tamanho do Job: ', job_data_converted[11])
            print('Tipo de papel do Job: ', job_data_converted[5])
            print('Qualidade do Job: ', job_data_converted[3])

        print('------USERS-------')
        user_UserID = obj.ROOT.PrintLog.Users.User.UserID.cdata
        user_LogonName = obj.ROOT.PrintLog.Users.User.LogonName.cdata
        #user_FullName = obj.ROOT.PrintLog.Users.User.FullName.cdata
        user_DomainName = obj.ROOT.PrintLog.Users.User.DomainName.cdata
        user_DomainType = obj.ROOT.PrintLog.Users.User.DomainType.cdata

        print('UserID: ', obj.ROOT.PrintLog.Users.User.UserID.cdata)
        print('LogonName: ', obj.ROOT.PrintLog.Users.User.LogonName.cdata)
        #print('FullName: ', obj.ROOT.PrintLog.Users.User.FullName.cdata)
        print('DomainName: ', obj.ROOT.PrintLog.Users.User.DomainName.cdata)
        print('DomainType: ', obj.ROOT.PrintLog.Users.User.DomainType.cdata)
        object_xml = {
            'printlog_version': printlog_version,
            #'printlog_enterpriseKey': printlog_enterpriseKey,
            'printlog_createQueues': printlog_createQueues,
            'printlog_createdDate': printlog_createdDate,
            'printlog_productName': printlog_productName,
            'printlog_productVersion': printlog_productVersion,
            'printlog_isEmbedded': printlog_isEmbedded,
            'computer_OperationalSystem': computer_OperationalSystem,
            'computer_ComputerName': computer_ComputerName,
            'computer_StrongName': computer_StrongName,
            'computer_IP': computer_IP,
            'computer_Mask': computer_Mask,
            'computer_MacAddress': computer_MacAddress,
            'printers_on_log': printers_on_log,
            'printer_AddressMAC': printer_AddressMAC,
            'printer_AddressName': printer_AddressName,
            'printer_AddressPort': printer_AddressPort,
            'printer_DeviceManufacturer': printer_DeviceManufacturer,
            'printer_DeviceModelName': printer_DeviceModelName,
            'printer_DeviceSerialNumber': printer_DeviceSerialNumber,
            'printer_IsColor': printer_IsColor,
            'printer_IsCopier': printer_IsCopier,
            'printer_IsDuplex': printer_IsDuplex,
            'printer_IsFax': printer_IsFax,
            'printer_IsScan': printer_IsScan,
            'printer_PrinterType': printer_PrinterType,
            'printer_QueueDriverName': printer_QueueDriverName,
            'printer_QueueName': printer_QueueName,
            'printer_QueuePort': printer_QueuePort,
            'job_data': job_data,
            'job_data_converted': job_data_converted,
            'print_job_title': print_job_title,
            'print_job_hostname': print_job_hostname,
            'print_job_printerID': print_job_printerID,
            'print_job_date': print_job_date,
            'print_job_time': print_job_time,
            'print_job_size': print_job_size,
            'print_job_paperType': print_job_paperType,
            'print_job_quality': print_job_quality,
            'user_UserID': user_UserID,
            'user_LogonName': user_LogonName,
            #'user_FullName': user_FullName,
            'user_DomainName': user_DomainName,
            'user_DomainType': user_DomainType,
            'total_jobs': total_jobs
        }
        return object_xml
    except Exception as e:
        print(e)
