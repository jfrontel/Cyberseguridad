<p>Con MAC_change cambiaremos nuestra dirección MAC, más adelante veremos para que nos sirve esto.</p>
<p> ¿Qué es la dirección MAC?
<p> La dirección MAC es un identificador único que cada fabricante le asigna a la tarjeta de red de sus dispositivos conectados, desde un ordenador o móvil hasta routers, impresoras u otros dispositivos como tu Chromecast. Sus siglas vienen del inglés, y significan Media Access Control.</p>

<p>Crearemos un programa en python 2.7 para esta misión, donde comenzaremos de una forma sencilla y sin cuidar para nada su seguridad ni eficiencia, y luego poco a poco
le hiremos dando optimizaciones hasta convertirse en un programa estructurado eficiente y seguro. Empecemos.</p>

<h2> 1_MAC_change</h2>
<div>
import subprocess  #importamos libreria que nos permite correr comandos

subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44:66", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)</div>

<p><b>Explicacion de comandos:</b></p>
<p>El módulo subprocess le permite generar nuevos procesos, conectarse a sus conductos de entrada/salida/error y obtener sus códigos de retorno.</p>
<p>Con subprocess.call() llamaremos a comandos como si lo hiciesemos en la terminal.</p>
<p>El comando " ifconfig " se utiliza para mostrar la información de configuración de red actual, configurar una dirección IP, máscara de red o dirección de transmisión a una interfaz de red, crear un alias para la interfaz de red, configurar la dirección de hardware y habilitar o deshabilitar las interfaces de red.</p>
<p>El comando " ifconfig " sin argumentos mostrará todos los detalles de las interfaces activas. El comando ifconfig también se usa para verificar la dirección IP asignada de un servidor.</p>
<p>El uso del nombre de la interfaz (eth0) como argumento con el comando " ifconfig " mostrará los detalles de la interfaz de red específica.</p>
<p>ifconfig eth0 up o down activará o desactivará la interfaz eth0 esto es una paso necesario para poder modificar nuestra MAC</p>
<p>si hacemos un ifconfig en nuestra terminal aparecerá algo parecido a esto:</p>
<div>
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.x.x.xx  netmask 255.xx.xxx.0  broadcast 10.0.x.xxx
        inet6 fxx0::axx:xxxx:fxx3:xxxx  prefixlen 64  scopeid 0x20<link>
   <b>  ether 08:00:xx:xx:xx:xx </b> txqueuelen 1000  (Ethernet) 
        RX packets 36025  bytes 40582865 (38.7 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 15709  bytes 3132890 (2.9 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet xxx.0.xx.1  netmask 255.x.x.x
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 20  bytes 996 (996.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 20  bytes 996 (996.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
</div>
<p> la llamada ifconfig eth0 hw ether 00:11:22:33:44:66 cambia nuestra direccion MAC por la aquí expuesta.</p>
<p> Por si os lo preguntáis y el miedo recorre vuestras manos a la hora de ejecurtar el programa, la nueva dirección MAC no aguantará un reinicio y volverá a su versión anterior</p>

<h2> 2_MAC_change_usar_variables</h2> 
<p>La primera optimización que haremos para seguir el camino del buen padawan es el uso de variables. Empecemos:</p>
  

  
  
  
  

Para finalizar diremos que existe ya una herramienta para hacer esto: <b>MAC Changer</b> es una utilidad para ver/manipular la dirección MAC de las interfaces de red.</p>
<p>Su instalacion: $ sudo apt-get install macchanger</p>
<p>Pero nosotros tenemos la nuestra creada con sudor y muchas lágrimas, y por mi parte la usaré .
  
