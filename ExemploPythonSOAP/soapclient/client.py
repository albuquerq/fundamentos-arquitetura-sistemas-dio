from zeep import Client

client = Client('http://soapclient.com/xml/soapresponder.wsdl')

response = client.service.Method1(bstrParam1='oi', bstrParam2='tchau')

print(response)