
# importa la funciones que estan en otro archivo de python
import Funciones
from Funciones import * 


#CONTEXTO
#Hemoglobina Proteína del interior de los glóbulos rojos que transporta oxígeno desde los pulmones a los tejidos y órganos del cuerpo
#Un recuento bajo de hemoglobina puede estar asociado con una enfermedad o afección que hace que el cuerpo tenga muy pocos glóbulos rojos o eritrocitos
# Por lo que la hemoglobina estaria baja en el cuerpo, teniendo encuenta esto sera necesario verificar primero la cantidad de eritrocitos 
#para posteriormente revisar la cantidad de hemoglobina haciendo uso de condicionales, los cuales se encargaran de realizar el analisis de que
#se pase de los rangos establecidos.





#se aplicara un while que hara que siempre se ejecute el menu hasta que yo decida que no se realice mas 
#se mostrara un menu en pantalla y con un if se buscara verificar la seleccion del usuario 

#


# una variable que se encargara de que mientras sea verdad se haga pero cuando se de salir sera falsa
x=True 
while x:

    print("__MENU__")

    val=validar_numero("ingrese una de las opciones\n 1.ingresar un paciente\n 2.informe de pacientes almacenados \n 3.borrar paciente \n 4. salir \n")
    if val==1:
        # ingreso de datos del perro
        identificacion= validar_numero("ingrese numero de identificacion: ")

        nombre= input("ingrese nombre: ")

        edad= validar_numero("ingrese edad: ")

        fecha= validar_fecha ("ingrese fecha de la siguiente manera dd/mm/aaaa: ")

        raza = input("ingrese la raza del perro: ")

        eritrocitos = validar_numero("ingrese el valor de eritrocitos, sin letras: ")
        hemoglobina = validar_numero("ingrese el valor de hemoglobina: ")
        VCM = validar_numero("ingrese el valor de VCM: ")
        print(Funciones.agregarPaciente(identificacion, nombre, edad, fecha, raza, eritrocitos, hemoglobina, VCM))


    elif val ==2:
        vari = True

        while vari:
            a=validar_numero("\ningrese una de las opciones\n 1.Buscar paciente \n 2.Ver cantidad de pacientes entre 3 y 6 años \n 3.Ver cantidad de pacientes que requieren exámenes complementarios \n 4. Regresar \n")
            if a == 1:
                identificacion= validar_numero("\ningrese numero de identificacion: ")
                Funciones.buscarPaciente(identificacion)
            elif a == 2:
                Funciones.cantidadPacientes()
            elif a == 3:

                Funciones.examenesComplementarios()
            elif a == 4:
                vari = False
            else:
    
                print("No ingreso ninguna de las opciones")

    elif val == 3:
        identificacion= validar_numero("\ningrese numero de identificacion: ")
        Funciones.BorrarPaciente(identificacion)

    elif val == 4: 
        x=False

    else: print("No ingreso ninguna de las opciones")

