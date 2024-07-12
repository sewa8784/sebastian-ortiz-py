import random
import csv


sueldos = []
s_asignado= []

trabajadores = ['Juan Pérez','María García', 'Carlos López','Ana Martínez','Pedro Rodríguez','Laura Hernández','Miguel Sánchez','Isabel Gómez','Francisco Díaz', 'Elena Fernández']


def sueldo_random():
    
    for i in range(0,(len(trabajadores))):
        sueldo = random.randint(300000, 2500000)
        sueldos.append(sueldo)
        s_asignado.append([trabajadores[i], sueldo])
    return s_asignado



def clasificar_sueldos():
    if not s_asignado:
        print("")
        print("no hay sueldos que clasificar aun")
        print("")
    else:
        sueldosMenores=[]
        sueldosMedianos=[]
        sueldosMayores=[]
        for i in range(len(s_asignado)):
            if (s_asignado[i][1] <800000):
                sueldosMenores.append(s_asignado[i])
            elif (s_asignado[i][1] >= 800000) and (s_asignado[i][1] <=2000000):
                sueldosMedianos.append(s_asignado[i])
            elif (s_asignado[i][1]) >2000000:
                sueldosMayores.append(s_asignado[i])
        totalsueldo= sum(sueldos)
        print("")       
        print(f"sueldos menores a $800.000 TOTAL: {len(sueldosMenores)}")
        print(sueldosMenores)
        print("")
        print(f"sueldos mayores a $800.000 y menores a $2.000.000 TOTAL: {len(sueldosMedianos)}")
        print(sueldosMedianos)
        print("")
        print(f"sueldos mayores a $2.000.000 TOTAL: {len(sueldosMayores)}")
        print(sueldosMayores)
        print("")
        print(f"TOTAL SUELDOS: ${totalsueldo} ")
    

    

def ver_estadisticas():
    print("")
    print("en mantencion, dificultades tecnicas han ocurrido")
    print("")
           
def salirse_del_programa():
    print("Finalizando programa...")
    print("Desarrollado por Sebastián Ortiz")
    print("21.856.852-1")
    
    
def reporte_de_sueldos():
    print("")
    print("funcion no terminada aun, intentelo en un futuro lejano nuevamente")
    print("")
  
    
     
    
    
while True:
    
    print("="*17)
    print("Menu De Opciones")
    print("="*17)
    print("1.- asignar sueldos aleatorios")
    print("2.- clasificar sueldos ")
    print("3.- ver estadisticas ")
    print("4.- reporte de sueldos")
    print("5.- salirse del programa ")
    print("")
    opc=input("ingrese la opción que desea: ")
    
    if opc == "1":
        s_asignado=sueldo_random()
        print(s_asignado)
        
    elif opc == "2":
        clasificar_sueldos()
        
    elif opc == "3":
        ver_estadisticas()
        
    elif opc == "4":
        reporte_de_sueldos()
        
        
    elif opc == "5":
        salirse_del_programa()
        break
 
    else:
        print("")
        print("opcion no valida, por favor intentelo nuevamente")
        print("")