import numpy as np 
#CREACIÓN CONTADORES Y ACUMULADORES
contadorComun = 0
acumuladorComun = 0
contadorPiernas = 0
acumuladorPiernas = 0
contadorReclina = 0
acumuladorReclina = 0
acumuladorTotal = 0
contadorTotal = 0
#CREACIÓN MATRIZ
matrizAsientos = np.empty((6,28),dtype="U2")
matrizRUT = np.zeros((6,28),dtype="int")
#ASIGNACIÓN ASIENTOS MATRIZ
#ESPACIO PIERNAS
matrizAsientos[:,0] = "P"
matrizAsientos[:,1] = "P"
matrizAsientos[:,2] = "P" 
matrizAsientos[:,3] = "P" 
matrizAsientos[:,4] = "P" 
matrizAsientos[:,11] = "P" 
#ASIENTO COMÚN
matrizAsientos[:,5] = "C"
matrizAsientos[:,6] = "C"
matrizAsientos[:,7] = "C"
matrizAsientos[:,8] = "C"
matrizAsientos[:,12] = "C"
matrizAsientos[:,13] = "C"
matrizAsientos[:,14] = "C"
matrizAsientos[:,15] = "C"
matrizAsientos[:,16] = "C"
matrizAsientos[:,17] = "C"
matrizAsientos[:,18] = "C"
matrizAsientos[:,19] = "C"
matrizAsientos[:,20] = "C"
matrizAsientos[:,21] = "C"
matrizAsientos[:,22] = "C"
matrizAsientos[:,23] = "C"
matrizAsientos[:,24] = "C"
matrizAsientos[:,25] = "C"
matrizAsientos[:,26] = "C"
matrizAsientos[:,27] = "C"
#ASIENTO NO RECLINA
matrizAsientos[:,9] = "NR"
matrizAsientos[:,10] = "NR"
#CREACIÓN FUNCIONES
def mostrarAvion():
    print("COLUMNA   01 02 03 04 05 06 07 08 09  10  17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33")
    print("FILA")
    print(f"F         {matrizAsientos[0,0]}  {matrizAsientos[0,1]}  {matrizAsientos[0,2]}  {matrizAsientos[0,3]}  {matrizAsientos[0,4]}  {matrizAsientos[0,5]}  {matrizAsientos[0,6]}  {matrizAsientos[0,7]}  {matrizAsientos[0,8]}  {matrizAsientos[0,9]}  {matrizAsientos[0,10]}  {matrizAsientos[0,11]}  {matrizAsientos[0,12]}  {matrizAsientos[0,13]}  {matrizAsientos[0,14]}  {matrizAsientos[0,15]}  {matrizAsientos[0,16]}  {matrizAsientos[0,17]}  {matrizAsientos[0,18]}  {matrizAsientos[0,19]}  {matrizAsientos[0,20]}  {matrizAsientos[0,21]}  {matrizAsientos[0,22]}  {matrizAsientos[0,23]}  {matrizAsientos[0,24]}  {matrizAsientos[0,25]}  {matrizAsientos[0,26]}")
    print(f"E         {matrizAsientos[1,0]}  {matrizAsientos[1,1]}  {matrizAsientos[1,2]}  {matrizAsientos[1,3]}  {matrizAsientos[1,4]}  {matrizAsientos[1,5]}  {matrizAsientos[1,6]}  {matrizAsientos[1,7]}  {matrizAsientos[1,8]}  {matrizAsientos[1,9]}  {matrizAsientos[1,10]}  {matrizAsientos[1,11]}  {matrizAsientos[1,12]}  {matrizAsientos[1,13]}  {matrizAsientos[1,14]}  {matrizAsientos[1,15]}  {matrizAsientos[1,16]}  {matrizAsientos[1,17]}  {matrizAsientos[1,18]}  {matrizAsientos[1,19]}  {matrizAsientos[1,20]}  {matrizAsientos[1,21]}  {matrizAsientos[1,22]}  {matrizAsientos[1,23]}  {matrizAsientos[1,24]}  {matrizAsientos[1,25]}  {matrizAsientos[1,26]}")
    print(f"D         {matrizAsientos[1,0]}  {matrizAsientos[2,1]}  {matrizAsientos[2,2]}  {matrizAsientos[2,3]}  {matrizAsientos[2,4]}  {matrizAsientos[2,5]}  {matrizAsientos[2,6]}  {matrizAsientos[2,7]}  {matrizAsientos[2,8]}  {matrizAsientos[2,9]}  {matrizAsientos[2,10]}  {matrizAsientos[2,11]}  {matrizAsientos[2,12]}  {matrizAsientos[2,13]}  {matrizAsientos[2,14]}  {matrizAsientos[2,15]}  {matrizAsientos[2,16]}  {matrizAsientos[2,17]}  {matrizAsientos[2,18]}  {matrizAsientos[2,19]}  {matrizAsientos[2,20]}  {matrizAsientos[2,21]}  {matrizAsientos[2,22]}  {matrizAsientos[2,23]}  {matrizAsientos[2,24]}  {matrizAsientos[2,25]}  {matrizAsientos[2,26]}")
    print(f"C         {matrizAsientos[3,0]}  {matrizAsientos[3,1]}  {matrizAsientos[3,2]}  {matrizAsientos[3,3]}  {matrizAsientos[3,4]}  {matrizAsientos[3,5]}  {matrizAsientos[3,6]}  {matrizAsientos[3,7]}  {matrizAsientos[3,8]}  {matrizAsientos[3,9]}  {matrizAsientos[3,10]}  {matrizAsientos[3,11]}  {matrizAsientos[3,12]}  {matrizAsientos[3,13]}  {matrizAsientos[3,14]}  {matrizAsientos[3,15]}  {matrizAsientos[3,16]}  {matrizAsientos[3,17]}  {matrizAsientos[3,18]}  {matrizAsientos[3,19]}  {matrizAsientos[3,20]}  {matrizAsientos[3,21]}  {matrizAsientos[3,22]}  {matrizAsientos[3,23]}  {matrizAsientos[3,24]}  {matrizAsientos[3,25]}  {matrizAsientos[3,26]}")
    print(f"B         {matrizAsientos[4,0]}  {matrizAsientos[4,1]}  {matrizAsientos[4,2]}  {matrizAsientos[4,3]}  {matrizAsientos[4,4]}  {matrizAsientos[4,5]}  {matrizAsientos[4,6]}  {matrizAsientos[4,7]}  {matrizAsientos[4,8]}  {matrizAsientos[4,9]}  {matrizAsientos[4,10]}  {matrizAsientos[4,11]}  {matrizAsientos[4,12]}  {matrizAsientos[4,13]}  {matrizAsientos[4,14]}  {matrizAsientos[4,15]}  {matrizAsientos[4,16]}  {matrizAsientos[4,17]}  {matrizAsientos[4,18]}  {matrizAsientos[4,19]}  {matrizAsientos[4,20]}  {matrizAsientos[4,21]}  {matrizAsientos[4,22]}  {matrizAsientos[4,23]}  {matrizAsientos[4,24]}  {matrizAsientos[4,25]}  {matrizAsientos[4,26]}")
    print(f"A         {matrizAsientos[5,0]}  {matrizAsientos[5,1]}  {matrizAsientos[5,2]}  {matrizAsientos[5,3]}  {matrizAsientos[5,4]}  {matrizAsientos[5,5]}  {matrizAsientos[5,6]}  {matrizAsientos[5,7]}  {matrizAsientos[5,8]}  {matrizAsientos[5,9]}  {matrizAsientos[5,10]}  {matrizAsientos[5,11]}  {matrizAsientos[5,12]}  {matrizAsientos[5,13]}  {matrizAsientos[5,14]}  {matrizAsientos[5,15]}  {matrizAsientos[5,16]}  {matrizAsientos[5,17]}  {matrizAsientos[5,18]}  {matrizAsientos[5,19]}  {matrizAsientos[5,20]}  {matrizAsientos[5,21]}  {matrizAsientos[5,22]}  {matrizAsientos[5,23]}  {matrizAsientos[5,24]}  {matrizAsientos[5,25]}  {matrizAsientos[5,26]}")
def validarMenu(menu):
    if menu >= 1 and menu <= 7:
        return False
    else:
        print("ERROR!")
        print("Ingresar opción de menú válida.\n")
def validarColumna(columna):
    if columna >= 0 and columna <= 26:
        return False
    else:
        print("ERROR!")
        print("Ingresar columna válida.\n")
def validarFila(fila):
    if fila >= 0 and fila <= 6:
        return False
    else:
        print("ERROR!")
        print("Ingresar fila válida.\n")
        return True
def validarRut(rut):
    if rut >= 7 and rut <= 8:
        return False
        print(" ")
    else:
        print("ERROR!")
        print("Ingresar RUT sin puntos ni código verificador.\n")
        return True
def guardarRut(fila,columna,rut):
    matrizRUT[fila,columna] = rut
def validarAsiento(fila,columna):
    if matrizAsientos[fila,columna] == "P" or matrizAsientos[fila,columna] == "C" or matrizAsientos[fila,columna] == "NR":
        print("-----------------------------------")
        print("Asiento seleccionado disponible.")
        print("-----------------------------------")
        return False
    else:
        print("ERROR!")
        print("Asiento seleccionado no disponible.\n")
        return True
def realizarCompra(fila,columna,rut):
    matrizRUT[fila,columna] = rut
    matrizAsientos[fila,columna] = "X"
    print("----------------------------------------")
    print("LA COMPRA SE HA REALIZADO CON ÉXITO.")
    print("----------------------------------------") 
def listaPasajeros():
    listaPasajerosAvion = np.unique(matrizRUT)
    print("----------------------------------------")
    print("La lista de pasajeros es la siguiente:")
    print("----------------------------------------")
    for i in range(len(listaPasajerosAvion)):
        if not listaPasajerosAvion[i] == 0:
            print(f"RUT PASAJERO:   {listaPasajerosAvion[i]}")
def validarReasignacion(fila,columna):
    if matrizAsientos[fila,columna] == "X":
        print("-------------------------------------")
        print("Asiento disponible para reasignación.")
        print("-------------------------------------")
        return False
    else:
        print("ERROR!")
        print("Asiento no disponible para reasignación.\n")
        return True
def realizarReasignacion(fila,columna,rut):
    matrizRUT[fila,columna] = rut
    print("-------------------------------------------------------")
    print("La reasignación del asiento se ha realizado con éxito.")
    print("-------------------------------------------------------")
    return False     
#INICIO MENÚ
while True:
    #VALIDACIÓN MENÚ
    whileMenu = True
    while whileMenu == True:
        print("-----------------------------------------\n           MENÚ AEROLÍNEA FLASH\n-----------------------------------------")
        try:
            print("1) Comprar pasajes.\n2) Mostrar ubicaciones disponibles.\n3) Ver listado de pasajeros.\n4) Buscar pasajero.\n5) Reasignar asiento.\n6) Mostrar ganancias totales.\n7) Salir.\n-----------------------------------------")
            opcionMenu = int(input())
            whileMenu = validarMenu(opcionMenu)
        except:
            print("Ingresar caracteres válidos.")
    #INGRESO MENÚ OPCIÓN 1
    if opcionMenu == 1:
        print("Ingresar la cantidad de pasajes que desea comprar.")
        cantidadPasajes = int(input())
        for i in range(0,cantidadPasajes):
            print("--------------------------------------------------")
            print("TIPO ASIENTO                        PRECIO")
            print("(C)   Asiento Común                 $60.000.-")
            print("(P)   Asiento Espacio Piernas       $80.000.-")
            print("(NR)  Asiento No Reclina            $50.000.-")
            print("--------------------------------------------------")
            mostrarAvion()
            #VALIDACIÓN FILA
            verificacionColumna = True
            while verificacionColumna == True:
                try:
                    print("Ingresar número de columna.")
                    numeroColumna = int(input())
                    busquedaColumna = numeroColumna
                    if numeroColumna == 1:
                        numeroColumna = 0
                    if numeroColumna == 2:
                        numeroColumna = 1
                    if numeroColumna == 3:
                        numeroColumna = 2
                    if numeroColumna == 4:
                        numeroColumna = 3
                    if numeroColumna == 5:
                        numeroColumna = 4
                    if numeroColumna == 6:
                        numeroColumna = 5
                    if numeroColumna == 7:
                        numeroColumna = 6
                    if numeroColumna == 8:
                        numeroColumna = 7
                    if numeroColumna == 9:
                        numeroColumna = 8
                    if numeroColumna == 10:
                        numeroColumna = 9
                    if numeroColumna == 17:
                        numeroColumna = 10
                    if numeroColumna == 18:
                        numeroColumna = 11
                    if numeroColumna == 19:
                        numeroColumna = 12
                    if numeroColumna == 20:
                        numeroColumna = 13
                    if numeroColumna == 21:
                        numeroColumna = 14
                    if numeroColumna == 22:
                        numeroColumna = 15
                    if numeroColumna == 23:
                        numeroColumna = 16
                    if numeroColumna == 24:
                        numeroColumna = 17
                    if numeroColumna == 25:
                        numeroColumna = 18
                    if numeroColumna == 26:
                        numeroColumna = 19
                    if numeroColumna == 27:
                        numeroColumna = 20
                    if numeroColumna == 28:
                        numeroColumna = 21
                    if numeroColumna == 29:
                        numeroColumna = 22
                    if numeroColumna == 30:
                        numeroColumna = 23
                    if numeroColumna == 31:
                        numeroColumna= 24
                    if numeroColumna == 32:
                        numeroColumna = 25
                    if numeroColumna == 33:
                        numeroColumna = 26
                    verificacionColumna = validarColumna(numeroColumna)
                except ValueError:
                    print("Ingresar caracteres válidos.\n")
            verificacionFila = True
            while verificacionFila == True:
                print("Ingresar letra de fila.")
                letraFila = input()
                letraFila = letraFila.upper()
                busquedaFila = letraFila
                if letraFila == "A":
                    letraFila = 5
                if letraFila == "B":
                    letraFila = 4
                if letraFila == "C":
                    letraFila = 3
                if letraFila == "D":
                    letraFila = 2
                if letraFila == "E":
                    letraFila = 1
                if letraFila == "F":
                    letraFila = 0
                if matrizAsientos[letraFila, numeroColumna] == "P":
                    contadorPiernas = contadorPiernas + 1
                    acumuladorPiernas = acumuladorPiernas + 80000
                if matrizAsientos[letraFila,numeroColumna] == "C":
                    contadorComun = contadorComun + 1
                    acumuladorComun = acumuladorComun + 60000
                if matrizAsientos[letraFila,numeroColumna] == "NR":
                    contadorReclina = contadorReclina + 1
                    acumuladorReclina = acumuladorReclina + 50000
                acumuladorTotal = acumuladorComun + acumuladorPiernas + acumuladorReclina
                contadorTotal = contadorComun + contadorPiernas + contadorReclina
                verificacionFila = validarFila(letraFila)
            verificacionAsiento = validarAsiento(letraFila,numeroColumna)
            if verificacionAsiento == False:
                verificacionRut = True
                while verificacionRut == True:
                    print("Ingresar RUT sin puntos ni código verificador.")
                    rutCliente = input()
                    rutClienteLen = len(rutCliente)
                    verificacionRut = validarRut(rutClienteLen)
                registrarRut = guardarRut(letraFila,numeroColumna,rutCliente)
                realizarCompra(letraFila,numeroColumna,rutCliente)
    #INGRESO MENÚ OPCIÓN 2
    if opcionMenu == 2:
        mostrarAvion()
    #INGRESO MENÚ OPCIÓN 3
    if opcionMenu == 3:
        listaPasajeros()
    #INGRESO MENÚ OPCIÓN 4
    if opcionMenu == 4:
        busquedaRut = True
        while busquedaRut == True:
            print("Ingresar el RUT del pasajero que desea buscar (sin puntos ni código verificador.)")
            buscarPasajero = int(input())
            if len(str(buscarPasajero)) >= 7 and len(str(buscarPasajero)) <= 8:
                busquedaRut = False
            else:
                print("Ingresar RUT sin puntos ni código verificador.")
            for i in range(0,6):
                for j in range(0,28):
                    if matrizRUT[i,j] == buscarPasajero:                  
                        print(f"El pasajero esta en el asiento: {busquedaFila,busquedaColumna}")
    if opcionMenu == 5:
        validarRut2 = True
        while validarRut2 == True:
            print("Ingresar el RUT original del asiento (sin puntos ni código verificador).")
            rutOriginal = int(input())
            if len(str(rutOriginal)) >= 7 and len(str(rutOriginal)) <= 8:
                validarRut2 = False
            else:
                print("Ingresar RUT sin puntos ni código verificador.")            
        validarRut3 = True
        while validarRut3 == True:
            print("Ingresar RUT del nuevo pasajero.")
            nuevoRut = int(input())              
            if len(str(nuevoRut)) >= 7 and len(str(nuevoRut)) <= 8:
                    validarRut3 = False
            else:
                print("Ingrese rut valido 8 digitos!!!")
            for i in range(0,6):
                for j in range(0,28):
                    if matrizRUT[i,j] == rutOriginal:
                        matrizRUT[i,j] = nuevoRut
                        print("---------------------------------------------")
                        print("EL ASIENTO HA SIDO REASIGNADO ÉXITOSAMENTE.")
                        print("---------------------------------------------")
    #INGRESO MENÚ OPCIÓN 6
    if opcionMenu == 6:
        print("Tipo de asiento           PRECIO           Cantidad            Total")
        print(f"Asiento común             $60.000          {contadorComun}                   ${acumuladorComun}")
        print(f"Espacio para piernas      $80.000          {contadorPiernas}                   ${acumuladorPiernas}")
        print(f"No reclina                $50.000          {contadorReclina}                   ${acumuladorReclina}")
        print(f"TOTAL                                      {contadorTotal}                   ${acumuladorTotal}")
    #INGRESO MENÚ OPCION 7
    if opcionMenu == 7:
        break