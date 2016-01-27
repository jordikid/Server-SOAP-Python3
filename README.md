
<h2>Instalación</h2>

<pre>
clone https://github.com/jordikid/Server-SOAP-Python3.git
cd Server-SOAP-Python3/
</pre>

<h2>Iniciar Servidor SOAP</h2>
<pre>python3 server.py</pre>

<h2>Iniciar Cliente SOAP</h2>
<pre>python3 client.py</pre>

<h1>Servidor SOAP Python 3 con pysimplesoap</h1>

Para crear un servidor SOAP con Python 3 una librería bastante buena y sencilla de utilizar es <b>pysimplesoap</b>.

<ul>
<li>Primero importamos de la librería pysimplesoap lo que vamos a utilizar, en este caso <i>SoapDispatcher</i> y <i>SOAPHandler</i></li>
</ul>

<pre>from pysimplesoap.server import SoapDispatcher, SOAPHandler
import http.server</pre>


<ul>
<li>Esta es la función a la que llamamos desde nuestro Dispatcher, siempre debe devolver un return</li>
</ul>
<pre>def name_function(call):
  return "Response"</pre>

<ul>
<li>Configuración</li>
</ul>
<pre>dispatcher = SoapDispatcher(
    'soap',
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/', # SOAPAction
    namespace = "http://example.com/sample.wsdl", prefix="ns0",
    trace = True,
    ns = True)</pre>

<ul>
<li>El dispatcher es el que recibe la llamada del cliente. En este caso <i>BETA</i> lo declaramos como un elemento del WSDL y name_function es la función que hemos declarado anteriormente.</li>
</ul>
<pre>dispatcher.register_function('BETA', name_function,
    returns={'Result': str},
    args={'call': str})</pre>

<ul>
<li>Iniciamos el servidor.</li>
</ul>
<pre>print( "Starting server...")
httpd = http.server.HTTPServer(("localhost", 8008), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()</pre>


<h1>Cliente SOAP Python 3 con pysimplesoap</h1>

Para crear un cliente SOAP con Python 3 una librería bastante buena y sencilla de utilizar es <b>pysimplesoap</b>.

<ul>
<li>Primero importamos de la librería pysimplesoap lo que vamos a utilizar, en este caso <i>SoapDispatcher</i> y <i>SOAPHandler</i></li>
</ul>
<pre>from pysimplesoap.client import SoapClient, SoapFault</pre>

<ul>
<li>Creamos el cliente de una forma muy sencilla</li>
</ul>
<pre>client = SoapClient(
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/', # SOAPAction
    namespace = "http://example.com/sample.wsdl",
    soap_ns='soap',
    trace = True,
    ns = False)</pre>
    
<ul>
<li>Llamamos al servidor SOAP e imprimimos la respuesta que nos devuelve.</li>
</ul>
<pre>response = client.OTA_VehRes(call=ota)
result = response.Result
print (result)</pre>

