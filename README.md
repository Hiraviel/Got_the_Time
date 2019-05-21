# Got_the_Time
Trying an Andon system

v1

El sistema tiene la intención de:

1.- Generar un cronometro en cuanto se ingresen un par de parametros (Timer.py & Tkinter_Timer.py):

         VIN: 17 caracteres alfanúmericos, no signos/simbolos.
      MODELO: 6 caracteres alfanúmericos, no signos/simbolos.

2.- El Cronometro cambia de color y estatus de acuerdo a los limites de tiempo:
      
       0 - 26 minutos:  VERDE
      27 - 51 minutos:  AMARILLO
        >= 52 minutos:  ROJO

3.- Generar un archivo ".txt" que contiene varios parametros:

      FECHA
      VIN
      MODELO
      HORA DE INICIO
      HORA DE FIN
      DIFERENCIA EN TIEMPOS
      OK/NOK

4.- El archivo ".txt" tendra el nombre de acuerdo al VIN + FECHA:

      ESTEESUNCODIGOVIN_2019-05-19.txt

3.- El proceso se ejecuta de manera constante regreseando siempre a la solicitud de los parametros VIN/MODELO.


v1.1

1.- Sistema realiza continuamente su función, mediante Threading, pero muestra errores en línea de comandos.
2.- No es necesario el archivo Tkinter_Timer.py, el Script se incorpora directamente a Timer.py.
3.- En v1 se sobreescribia el contenido si se reutilizaba el VIN, se mejora añadiendo hora de inicio al nombre del .txt.
