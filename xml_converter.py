import untangle
import os


def xmlfiletoOBJECT():

    try:
        dir = "C:\\projLucas\\NPL\\"
        arquivos_da_pasta = os.listdir(dir)
        print("arquivos_da_pasta: ", arquivos_da_pasta)
        xml_file = str(dir + arquivos_da_pasta[1])
        print('Arquivo que vai para o Parser: ', xml_file)
        obj = untangle.parse(xml_file)
        print("OBJETO: ", obj)

        print('------PRINTLOG-------')
        printlog_version = obj.ROOT.PrintLog.Version.cdata
        printlog_enterpriseKey = obj.ROOT.PrintLog.EnterpriseKey.cdata
        printlog_createQueues = obj.ROOT.PrintLog.CreateQueues.cdata
        printlog_createdDate = obj.ROOT.PrintLog.CreatedDate.cdata
        printlog_productName = obj.ROOT.PrintLog.ProductName.cdata
        printlog_productVersion = obj.ROOT.PrintLog.ProductVersion.cdata
        printlog_isEmbedded = obj.ROOT.PrintLog.IsEmbedded.cdata

        print('Versão: ', obj.ROOT.PrintLog.Version.cdata)
        print('EnterpriseKey: ', obj.ROOT.PrintLog.EnterpriseKey.cdata)
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

            print('Impressoras detectadas: ', len(obj.ROOT.PrintLog.Printers))
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
            print('--------- Fim Printer ID: ', printer['ID'])


        print('------PRINTJOBS-------')
        for printjob in obj.ROOT.PrintLog.PrintJobs.PrintJob:
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
            print('Documentos impressos: ', len(obj.ROOT.PrintLog.PrintJobs.PrintJob))
            print('PrintJob.Data: ', job_data)
            print('Título do Job: ', job_data_converted[23])
            print('Hostname do Job: ', job_data_converted[22])
            print('PrinterID do Job: ', job_data_converted[4])
            print('Data do Job: ', job_data_converted[12])
            print('Hora do Job: ', job_data_converted[13])
            print('Tamanho do Job: ', job_data_converted[11])
            print('Tipo de papel do Job: ', job_data_converted[5])
            print('Qualidade do Job: ', job_data_converted[3])

        # Fatiamento utilizado:
        # 1¬1¬0¬600¬672¬9¬1¬1¬0¬0¬0¬50738¬2021/04/27¬08:52:39¬0¬0¬0¬¬¬0¬0¬¬NDD-VM-TES4919¬prefix_xxvwlp1w_suffix.txt - Notepad
        #       3   4   5           11    12         13                    22             23

        # ['1', '1', '0', '-1', '675', '9', '1', '0', '1', '0', '0', '62031', '2021/05/14', '08:57:21', '0', '0', '1', '', '', '0', '0', '', 'NDD-VM-TES4919', 'Test Page']
        #                        4      5                             11       12            13                                               22                23

        print('------USERS-------')
        user_UserID = obj.ROOT.PrintLog.Users.User.UserID.cdata
        user_LogonName = obj.ROOT.PrintLog.Users.User.LogonName.cdata
        user_FullName = obj.ROOT.PrintLog.Users.User.FullName.cdata
        user_DomainName = obj.ROOT.PrintLog.Users.User.DomainName.cdata
        user_DomainType = obj.ROOT.PrintLog.Users.User.DomainType.cdata

        print('UserID: ', obj.ROOT.PrintLog.Users.User.UserID.cdata)
        print('LogonName: ', obj.ROOT.PrintLog.Users.User.LogonName.cdata)
        print('FullName: ', obj.ROOT.PrintLog.Users.User.FullName.cdata)
        print('DomainName: ', obj.ROOT.PrintLog.Users.User.DomainName.cdata)
        print('DomainType: ', obj.ROOT.PrintLog.Users.User.DomainType.cdata)

    except Exception as e:
        print(e)
