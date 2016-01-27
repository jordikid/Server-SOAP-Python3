from pysimplesoap.client import SoapClient, SoapFault

client = SoapClient(
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/', # SOAPAction
    namespace = "http://example.com/sample.wsdl",
    soap_ns='soap',
    trace = True,
    ns = False)
    
response = client.BETA(call="something")
result = response.Result
print (result)
