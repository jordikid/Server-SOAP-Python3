""" SOAP """
from pysimplesoap.server import SoapDispatcher, SOAPHandler
import http.server

""" Función a la que llamamos desde el dispatcher """
def name_function(call):
  return "Response"

dispatcher = SoapDispatcher(
    'soap',
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/', # SOAPAction
    namespace = "http://example.com/sample.wsdl", prefix="ns0",
    trace = True,
    ns = True)

""" BETA es el miembro del WSDL, el cliente SOAP entrará por ahí """
dispatcher.register_function('BETA', name_function,
    returns={'Result': str},
    args={'call': str})
    
print( "Starting server...")
httpd = http.server.HTTPServer(("localhost", 8008), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()
