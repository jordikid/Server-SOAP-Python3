# Server-SOAP-Python3
Servidor SOAP en Python 3

Para crear un servidor SOAP con Python 3 una librería bastante buena y sencilla de utilizar es <b>pysimplesoap</b>.

<h2>Instalación</h2>

<code>pip3 install pysimplesoap</code>

<h2>Código</h2>

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
