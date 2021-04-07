import xmltodict, json

def parserxml():
    obj = xmltodict.parse("""
    <ROOT>
        <PrintLog>
            <Version>9</Version>
            <EnterpriseKey/>
            <CreateQueues>false</CreateQueues>
            <QueuesSync>false</QueuesSync>
            <CreatedDate>2021/04/03 16:33:53</CreatedDate>
            <ProductName>nddPrint Agent</ProductName>
            <ProductVersion>5.51.7</ProductVersion>
            <IsEmbedded>0</IsEmbedded>
            <ComputerMetaData>
                <OperationalSystem>Windows 2016</OperationalSystem>
                <StrongName>FE4317B97C02C2693EE5B831F6D8CD9B</StrongName>
                <ComputerName>NDD-VM-TES4919</ComputerName>
                <NetworkAddresses>
                    <NetworkAddress>
                        <IP>172.31.249.105</IP>
                        <Mask>255.255.0.0</Mask>
                        <MacAddress>00-0C-29-F9-D9-61</MacAddress>
                    </NetworkAddress>
                </NetworkAddresses>
            </ComputerMetaData>
            <Printers/>
            <PrintJobs/>
            <Users/>
        </PrintLog>
    </ROOT>

    """)
    print(json.dumps(obj))


def parserxml2():
    obj = xmltodict.parse("""

<ROOT xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
<PrintLog>
<Version>9</Version>
<EnterpriseKey/>
<CreateQueues>false</CreateQueues>
<QueuesSync>false</QueuesSync>
<CreatedDate>2021/04/03 16:33:53</CreatedDate>
<ProductName>nddPrintAgent</ProductName>
<ProductVersion>5.51.7</ProductVersion>
<IsEmbedded>0</IsEmbedded>
<ComputerMetaData>
<OperationalSystem>Windows 2016</OperationalSystem>
<StrongName>FE4317B97C02C2693EE5B831F6D8CD9B</StrongName>
<ComputerName>NDD-MTES4919</ComputerName>
<NetworkAddresses>
<NetworkAddress>
<IP>172.31.249.105</IP>
<Mask>255.255.0.0</Mask>
<MacAddress>00-0C-29-F9-D9-61</MacAddress>
</NetworkAddress>
</NetworkAddresses>
</ComputerMetaData>
<Printers />
<PrintJobs />
<Users />
</PrintLog>
</ROOT>

    """)
    print(json.dumps(obj))