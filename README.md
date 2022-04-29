# ¿Qué es?

El proyecto GuiMLF presenta una interfaz gráfica sencilla para facilitar el control de los brazos robóticos de My Little Factory. 

# Por qué?
Hasta el momento el control de estos brazos se realiza conectándose vía línea de comando por SSH a su respectiva Raspberry Pi para ejecutar un script que permite controlar, vía comunicación serial, el arduino que a su vez controla uno de los brazos robóticos de My Little Factory en el FabLab de la Facultad de Ciencias Físicas y Matemáticas de la universidad de Chile.

# Cómo funciona?
Se establece un nuevo script de lado del servidor, ubicado en `guimlf/main_pi/test_onpi.py`, el cual recibe un comando sencillo con estructura json, `\{"mode" : --, "x0" : -- , "x1" : -- , "x2" : -- \}`.

A nivel de cliente, se utiliza la librería Paramiko para establecer la conexión vía SSH a través del script de Python `guimlf/main_client/GUI_MLF.py`.  
Éste cuenta con una sencilla interfaz gráfica que permite tanto enviar coordenadas específicas en modo X,Y,Z o angular, como moverse gradualmente utilizando el teclado.

## Librerías utilizadas

Para poder ejecutar el script sin problemas, es necesario contar con algunas librerías instaladas y archivos presentes en el directorio.

- **Paramiko**
- **PySimpleGUI**
- **NumPy**
- MK2Robot

Las primeras tres librerías pueden ser instaladas vía **pip**. Para esto basta con ingresar `pip install paramiko`, `pip install pysimplegui` y `pip install numpy` en la consola de comandos. MK2Robot.py debe estar en el mismo directorio que GUI_MLF.py

En caso de no tener pip ya instalado, entrar [aquí](https://pip.pypa.io/en/stable/installation/) para instrucciones de instalación.  
Si al instalarlo no es posible ejecutar el comando directamente desde la consola, puede ser necesario agregarlo manualmente a las variables de entorno, cuyas instrucciones se pueden encontrar [aquí](https://medium.com/swlh/solved-windows-pip-command-not-found-or-pip-is-not-recognized-as-an-internal-or-external-command-dd34f8b2938f)

# Cómo usar?

Al ejecutar main_client/GUI_MLF.py, se abrirá la ventana principal:

![mainwindow][mainwindow]

[mainwindow]: img/main.PNG

En ella se encuentran las siguientes funcionalidades:

### **Selección de modo de coordenadas (XYZ o Angular)** 
    
![mode][mode]

[mode]: img/modo.png

### **Última posición ingresada:** 
Si no ha sido establecida la conexión, esta información no se condecirá con la posición real.

### **Input de posición deseada:**
Aquí se ingresa el valor de cada coordenada a la cual se desea llevar el brazo.
### **Conexión/Cierre:**

Al presionar el botón de conexión se abrirá una ventana de login, donde se debe ingresar la información necesaria:

![connect][connect]

[connect]: img/login.PNG

- Host: Dirección IP a la cual nos conectaremos (192.168.0.11-18).
- Username: pi
- Password: Contraseña correspondiente

Si la conexión resulta exitosa, aparecerá su mensaje correspondiente, junto con la respuesta de la ejecución del comando `ls` en el servidor de destino, así como también se avisará en caso de conexión fallida.

![success][success]

[success]: img/exitosa.PNG

![fail][fail]

[fail]: img/fallida.PNG

Al día 29-04-2022, por problemas en la forma que se están manejando las sesiones SSH desde el script de cliente, aún no resulta posible ir al directorio correspondiente, ejecutar e interactuar remotamente con el script necesario.

### **Control con teclado**

Es posible establecer cambios incrementales en la posición mediante el teclado. Cada coordenada (cuyo modo se determina en el selector correspondiente) puede ser manejada por los siguientes pares de teclas:

- X / q0 : A-D o Flecha Izquierda-Flecha Derecha
- Y / q1 : W-S o Flecha Arriba-Flecha Abajo
- Z / q2 : Q-E

Los incrementos se encuentran actualmente configurados para ser de 1mm en modo XYZ o de 1° en modo angular.

Cada comando generado se muestra en consola para propósitos de debug, independiente sea o no enviado vía SSH.

# Trabajo Futuro

Aún quedan algunas aristas por pulir para asegurar el correcto funcionamiento del proyecto.

Dentro de las funcionalidades básicas y de máxima prioridad a implementar, se encuentran:

- Corrección de conexión SSH para ejecutar e interactuar correctamente con el script en la Raspberry de destino.

- Detección de inputs fuera de rango, los cuales deben ser verificados y configurados en base a los brazos in-situ. De momento, su correcto funcionamiento depende de que el usuario ingrese correctamente la posición deseada.

- Validación de funciones de conversión utilizadas mediante MK2Robot.

En cuanto a adiciones/modificaciones deseables:

- Visualización de stream de cámara.
- Funcionalidad con joystick
- Reordenamiento general del código para facilitar su mantención/actualización.


