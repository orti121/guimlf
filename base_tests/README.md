# Tests de funcionalidad básica

En esta carpeta se encuentran pequeños test para probar algunas funcionalidades básicas del programa.

A continuación se detalla cada archivo.

## **Demo_Keyboard.py**
Al ejecutar este script se genera una ventana que captura eventos de teclado y scrolling, mostrando su nombre. Utilizado para comprobar si se puede ejecutar código específico dependiente de la tecla presionada. 

De funcionar correctamente, debería imprimir en consola la dirección correspondiente al presionar dichas teclas de flecha o W, A, S, D. 

## **testgen.py**

Prueba la generación y decodificación de comando para enviar coordenadas a la Raspberry.
Al ejecutar el script, pedirá tres valores. Mientras éstos sean válidos para json, debiera imprimir en consola el comando construido para enviar, seguido de la extracción de sus valores, que será realizada de lado del servidor. 

## **SSHtest.py**

Corresponde a un test de conexión SSH de una vez utilizando Paramiko. Tanto host como usuario se encuentran predeterminados en el código, correspondientes a *rainbowdash*. 

Al ejecutar el script, solicitará la contraseña en consola. De ser correcta, se ejecutará el comando `ls` una vez y se cerrará la conexión. Si es incorrecta, entregará un mensaje de autenticación fallida y finalizará.

## **SSHtest2.py**

Muy similar a SSHtest, pero esta vez no cierra la sesión luego de ejecutado un solo comando, sino que pide permanentemente input de usuario. 

Si se inicia sesión correctamente, pedirá constantemente input hasta presionar Ctrl+C o enviar `exit`. Si la contraseña es incorrecta, arrojará un mensaje de autenticación fallida y terminará.

Se observa que luego de cada comando se vuelve al directorio base.