import xmltodict, json

def xmlfiletojson():
    with open('C:\\projLucas\\NPL\\09-11-20210403163353686-172031249105-XVJ.xml', 'r') as xmlfile:
        obj = xmltodict.parse(xmlfile.read())
    print(json.dumps(obj))
