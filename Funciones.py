import random


#inicializa variables 
diccionario={}


cont=0


#definicion de funcion de diagnostico 
def diagnostico(eritrocitos,hemoglobina,VCM):
    listaDiagnostico =[]
    resultadoDiagnostico = ""
   
    if (VCM >= 60 and VCM <=77): #verifica que la VCM este en los rangos
      resulVCM = "Normacita"
    elif VCM >77:
       resulVCM = "Macrocita"
    else:
       resulVCM = "Microcita"

    if (eritrocitos >= 5.5 and eritrocitos <=8.5 ):
        if(hemoglobina >= 12 and hemoglobina <= 19):
            resulEritroHemo = "Normocromico"
        elif (hemoglobina < 12):
           resulEritroHemo ="Hipocromia"
           
    elif (eritrocitos <=5.5): resulEritroHemo = "Hipercromia"

    else: resulEritroHemo = "Se requieren examenes complementarios"

    resultadoDiagnostico = resulVCM + "-" + resulEritroHemo
    listaDiagnostico.append(eritrocitos)
    listaDiagnostico.append(hemoglobina)
    listaDiagnostico.append(VCM)
    listaDiagnostico.append(resultadoDiagnostico)
    return listaDiagnostico 
       
    
#definicion de funcion para verificar 
def validar_numero(mensaje):
    intentos = 0 #contador de cada uno de los intentos, en total son 4
    while intentos < 4:
        try:
            valor = float(input(mensaje)) #recibe el input de la persona y convierte en flotante
            if valor.is_integer(): #se verifica si el número ingresado es un entero 
                valor = int(valor) # Si es un entero, se convierte a int, de lo contrario, se deja como flotante.
            return valor # devuelve el valor paa que posteriormente pueda ser usado en agregar paciente
        except ValueError:
            print("Error: Debes ingresar un número válido.")
            intentos += 1# va aumenta la cantidad de intentos
    print("Has excedido el número de intentos. Volviendo al menú principal.")



def validar_fecha(mensaje):
    intentos = 0#contador de cada uno de los intentos, en total son 4
    while intentos < 4:
        try:
            fecha = input(mensaje)#recibe el input de la persona 
            if len(fecha) >= 5: 
                if fecha[0:2].isdigit():
                    if fecha[3:5].isdigit():
                        if fecha[6:11].isdigit():
                            return fecha ## devuelve el valor paa que posteriormente pueda ser usado en agregar paciente
            
        except ValueError:
            print("Error: Debes ingresar una fecha en formato dd/mm/aaaa.")
            
            intentos += 1 # va aumenta la cantidad de intentos
    print("Has excedido el número de intentos. Volviendo al menú principal.")


       
#definicion de funcion de codigo 
def codigoPerros(raza):
    global cont
    cont=cont+1 # aumenta a medida que entra a la funcion 
    codigodepaciente="" #inicializa la variable en vacio 

    numeroGenerado =  random.randint(0, 1000) # genera un nuemero aleatorio 
    
    codigodepaciente = str(numeroGenerado) + "_Pe_" + raza + "_" + str(cont) #concatena para mandar el codigo generado

    return codigodepaciente
    


#definicion de la funcion que se encarga de agregar pacientes
def agregarPaciente(identificacion, nombre, edad, fecha, raza, eritrocitos, hemoglobina, VCM):
  
  
  lista=[]
  #agrega los dato sdel paciente a la lista 
  lista.append(identificacion)
  lista.append(nombre)
  lista.append(edad)
  lista.append(fecha)

#llama la funcion para generar el codigo 
  codigo = codigoPerros(raza) 
  lista.append(codigo)

#llama la funcion para generar el diagnostico
  diagnostico_paciente = diagnostico(eritrocitos,hemoglobina,VCM)
  lista.append(diagnostico_paciente)

  #guarda la lista en el diccionario
  diccionario[identificacion] = lista
  print(diccionario)
  
  return "Paciente "+ nombre+" identificado con el documento de identidad " + str(identificacion) + " ingresado exitosamente , su resultado es "+ diagnostico_paciente[3]




def buscarPaciente(identificacion):

    if identificacion in diccionario: #busca que la identificacion este en el diccionario
        var =  diccionario[identificacion] #se alamcena en una variable la lista con los datos  y se procede a sacar cada uno de los datos
        print("identificacion: ", str(var[0]))
        print("nombre: ", var[1])
        print("edad: ", str(var[2]))
        print("fecha: ", str(var[3]))
        print("codigo: ", var[4])
        print("Diagnostico: ", var[5][3])
    else:
        return print('El paciente con identificacion '+ str(identificacion) +' no se encuentra en el sistema \n')




def cantidadPacientes():
     # Utilizamos la función filter para filtrar los pacientes cuya edad esté entre 3 y 6 años
    pacientes_filtrados = filter(lambda paciente: 3 <= paciente[2] <= 6, diccionario.values())
    
    # Contamos la cantidad de pacientes filtrados
    cantidad_pacientes = len(list(pacientes_filtrados))

    # Imprimimos la cantidad de pacientes entre 3 y 6 años
    print("\nLa cantidad de pacientes entre 3 y 6 años es:", cantidad_pacientes)


def examenesComplementarios():

     # Utilizamos la función filter para filtrar los pacientes que requieren exámenes complementarios
    pacientes_filtrados = filter(lambda paciente: paciente[5][3].split("-")[1] == "Se requieren examenes complementarios", diccionario.values())
    
    # Contamos la cantidad de pacientes filtrados
    cantidad_pacientes = len(list(pacientes_filtrados))

    # Imprimimos la cantidad de pacientes que requieren exámenes complementarios
    print("\nLa cantidad de pacientes que requieren exámenes complementarios son:", cantidad_pacientes)

def BorrarPaciente(identificacion):
    if identificacion in diccionario: # busca al paciente
        del(diccionario[identificacion]) #elimina al paciente teniendo su llave
        print(diccionario)
        print("El paciente con documento "+ str(identificacion) +" ha sido eliminado de la base de datos")
    else:
        print("El paciente con documento "+ str(identificacion) +" no se encuentra en la base de datos")



