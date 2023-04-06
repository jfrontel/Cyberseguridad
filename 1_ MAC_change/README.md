<p>Con MAC_change cambiaremos nuestra dirección MAC.</p>

<p><b>¿Por qué cambiar la dirección MAC?</b></p>
Circunstancias que requieren el uso de una dirección específica o, alternativamente, una dirección elegida al azar. Éstas incluyen:</p>

<p> --> Uso de un servicio que ha sido bloqueado a una dirección MAC en particular;</p>
<p> --> Participación en un esquema de equilibrio de carga o conmutación por error que requiere el uso de la misma dirección MAC en múltiples interfaces;</p>
<p> --> Uso anónimo de una red donde se registran las direcciones MAC.</p>

<p><b>¿Qué es la dirección MAC?</b></p>
<p> La dirección MAC es un identificador único que cada fabricante le asigna a la tarjeta de red de sus dispositivos conectados, desde un ordenador o móvil hasta routers, impresoras u otros dispositivos como tu Chromecast. Sus siglas vienen del inglés, y significan Media Access Control.</p>

<p>Crearemos un programa en python 2.7 para esta misión, donde comenzaremos de una forma sencilla y sin cuidar para nada su seguridad ni eficiencia, y luego poco a poco
le hiremos dando optimizaciones hasta convertirse en un programa estructurado eficiente y seguro. Empecemos.</p>

<h2> 1_MAC_change</h2>
<div>
<p>import subprocess  #importamos libreria que nos permite correr comandos</p>

<p>subprocess.call("ifconfig eth0 down", shell=True)</p>
<p>subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44:66", shell=True)</p>
<p>subprocess.call("ifconfig eth0 up", shell=True)</p></div>

<p><b>Explicacion de comandos:</b></p>
<p>El módulo subprocess le permite generar nuevos procesos, conectarse a sus conductos de entrada/salida/error y obtener sus códigos de retorno.</p>
<p>Con subprocess.call() llamaremos a comandos como si lo hiciesemos en la terminal.</p>
<p>El comando " ifconfig " se utiliza para mostrar la información de configuración de red actual, configurar una dirección IP, máscara de red o dirección de transmisión a una interfaz de red, crear un alias para la interfaz de red, configurar la dirección de hardware y habilitar o deshabilitar las interfaces de red.</p>
<p>El comando " ifconfig " sin argumentos mostrará todos los detalles de las interfaces activas. El comando ifconfig también se usa para verificar la dirección IP asignada de un servidor.</p>
<p>El uso del nombre de la interfaz (eth0) como argumento con el comando " ifconfig " mostrará los detalles de la interfaz de red específica.</p>
<p>ifconfig eth0 up o down activará o desactivará la interfaz eth0 esto es una paso necesario para poder modificar nuestra MAC</p>
<p> En POSIX con shell=True, la shell predeterminada es /bin/sh. Si args es una cadena, ésta especifica la orden a ejecutar por la shell. Esto significa que la cadena tiene que tener el formato que tendría si se tecleara en la línea de órdenes. Esto incluye, por ejemplo, el entrecomillado y las secuencias de escape necesarias para los nombres de fichero que contengan espacios. </p>
<p><b> Advertencia Pasar shell=Truepuede ser un peligro para la seguridad si se combina con una entrada que no es de confianza. Consulte la advertencia en Argumentos de uso frecuente para obtener más información.</b></p>

<p>Si hacemos un ifconfig en nuestra terminal aparecerá algo parecido a esto:</p>
<div>
<p>eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500</p>
<p>&nbsp        inet 10.x.x.xx  netmask 255.xx.xxx.0  broadcast 10.0.x.xxx</p>
<p>&nbsp        inet6 fxx0::axx:xxxx:fxx3:xxxx  prefixlen 64  scopeid 0x20<link></p>
<p>&nbsp   <b>  ether 08:00:xx:xx:xx:xx </b> txqueuelen 1000  (Ethernet) </p>
<p>&nbsp        RX packets 36025  bytes 40582865 (38.7 MiB)</p>
<p>&nbsp        RX errors 0  dropped 0  overruns 0  frame 0</p>
<p>&nbsp        TX packets 15709  bytes 3132890 (2.9 MiB)</p>
<p>&nbsp        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0</p><br>

<p>lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536</p>
<p>&nbsp        inet xxx.0.xx.1  netmask 255.x.x.x</p>
<p>&nbsp        inet6 ::1  prefixlen 128  scopeid 0x10<host></p>
<p>&nbsp        loop  txqueuelen 1000  (Local Loopback)</p>
<p>&nbsp        RX packets 20  bytes 996 (996.0 B)</p>
<p>&nbsp        RX errors 0  dropped 0  overruns 0  frame 0</p>
<p>&nbsp        TX packets 20  bytes 996 (996.0 B)</p>
<p>&nbsp        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0</p><br>
</div>

<p> la llamada ifconfig eth0 hw ether 00:11:22:33:44:66 cambia nuestra direccion MAC por la aquí expuesta.</p>
<p> Por si os lo preguntáis y el miedo recorre vuestras manos a la hora de ejecurtar el programa, la nueva dirección MAC no aguantará un reinicio y volverá a su versión anterior</p>


<h2> 2_MAC_change_usar_variables</h2> 
<p>La primera optimización que haremos para seguir el camino del buen padawan es el uso de variables. Empecemos:</p>
  
<p><b> Ver archivo mac_change_variable.py</b></p>


<h2> 3_MAC_change_input_user</h2> 
<p> La siguiente optimizacion --> input de usuario, queremos que la interface y el mac sean establecidos por teclado.</p>

<p> si utilizas python 2 usar raw_input, para python 3 input
<p><b> Ver archivo mac_change_input_user.py</b></p>


<h2> 4_MAC_change_arguments_and_options</h2> 
<p>Nuestro programa funciona pero no es muy seguro, una persona que sabe hackear programas lo haria con gran facilidad y esto se debe a <b>shell=True</b>, si escribimos en la terminal cuando nos pide la interface eth0;(punto y coma para decirle a la terminal que queremos correr otro comando). </p>
<p> --> eth0;ls;pwd nos correra comandos que no deseamos.</p>

<p>Usaremos import optparse, para poder importar los comandos.</p>
<p>optparse es una biblioteca más conveniente, flexible y poderosa para analizar opciones de línea de comandos que el antiguo módulo getopt. optparse usa un estilo más declarativo: creas una instancia de OptionParser, le añades las opciones deseadas y realizas el análisis sintáctico de la línea de comandos. optparse permite a los usuarios especificar opciones siguiendo la sintaxis convencional de GNU/POSIX, además de generar mensajes de uso y de ayuda automáticamente.</p>





Para finalizar diremos que existe ya una herramienta para hacer esto: <b>MAC Changer</b> es una utilidad para ver/manipular la dirección MAC de las interfaces de red.</p>
<p>Su instalacion: $ sudo apt-get install macchanger</p>
<p>Pero nosotros tenemos la nuestra creada con sudor y muchas lágrimas, y por mi parte la usaré .
  
