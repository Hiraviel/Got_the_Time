import datetime
import re
from time import sleep
import Tkinter_Timer

global stage1


def cronometro():
    Tkinter_Timer.root.mainloop()


def captura():

    stage1 = 0

    while stage1 <= 0:
        VIN = input("Put VIN: ")
        pkykVIN = bool(re.match("^[A-Z0-9]*$", VIN)) #OK
        print(pkykVIN)
        if len(VIN) != 17:
            print("Error with the lenght ({}) of the VIN.".format(len(VIN)))
        else:
            if pkykVIN != False:
                print(stage1)   #OK
                print("\n")

                MODEL = input("Put MODEL: ")
                    
                if len(MODEL) != 6:
                    print(len(MODEL))
                    print(stage1)
                    print("\n")
                    print("Error with the lenght ({}) of the MODEL.".format(len(MODEL)))
                else:
                    stage1 = 1

                if stage1 == 1:
                    fecha = datetime.datetime.today().strftime("%Y-%d-%m")

                    start = datetime.datetime.now()
                    inicio = str(start)

                    #sleep(2)

                    #Cronometro aquí
                    cronometro()


                    end = datetime.datetime.now()
                    fin = str(end)

                    duration = end - start
                    tt = str(duration)
                    print(duration)

                    if tt != "00:54:00":
                        estatus = "OK"
                        print("OK")
                    else:
                        estatus = "NOK"
                        print("NOK")


                    datos = (str(fecha),str(VIN), str(inicio[11:19]), str(fin[11:19]), str(tt[0:7]), str(estatus))
                    print("Creating file..."+"\n")
                    file = open(VIN + "_" + fecha + ".txt", "w+")

                    for i in range(len(datos)):
                        file.write(datos[i]+", ")
                    file.close()

                    print("Done..."+"\n")

                    rfile = open(VIN + "_" + fecha + ".txt", "r")
                    if rfile.mode == "r":
                        contents = rfile.read()
                        print(contents)

                    stage1 = 0

                    print(stage1)

if __name__ == "__main__":
    while True:
        captura()
    

