import untangle

def xmlfiletoOBJECT():

    obj = untangle.parse('C:\\projLucas\\NPL\\09-11-20210403163353686-172031249105-XVJ.xml')
    print('Versão: ', obj.ROOT.PrintLog.Version.cdata)
    print('EnterpriseKey: ', obj.ROOT.PrintLog.EnterpriseKey.cdata)
    print('CreateQueues: ', obj.ROOT.PrintLog.CreateQueues.cdata)
    print('QueuesSync: ', obj.ROOT.PrintLog.QueuesSync.cdata)
    print('CreatedDate: ', obj.ROOT.PrintLog.CreatedDate.cdata)
    print('ProductName: ', obj.ROOT.PrintLog.ProductName.cdata)
    print('ProductVersion: ', obj.ROOT.PrintLog.ProductVersion.cdata)
    print('IsEmbedded: ', obj.ROOT.PrintLog.IsEmbedded.cdata)
    print('OperationalSystem: ', obj.ROOT.PrintLog.ComputerMetaData.OperationalSystem.cdata)
    print('StrongName: ', obj.ROOT.PrintLog.ComputerMetaData.StrongName.cdata)
    print('ComputerName: ', obj.ROOT.PrintLog.ComputerMetaData.ComputerName.cdata)
    print('EnterpriseKey: ', obj.ROOT.PrintLog.ComputerMetaData.NetworkAddresses.NetworkAddress.IP.cdata)
    print('EnterpriseKey: ', obj.ROOT.PrintLog.ComputerMetaData.NetworkAddresses.NetworkAddress.Mask.cdata)
    print('EnterpriseKey: ', obj.ROOT.PrintLog.ComputerMetaData.NetworkAddresses.NetworkAddress.MacAddress.cdata)