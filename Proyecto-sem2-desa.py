#En este inicio encontraras todas funciones credas para las diferentes opciones del menú ofrecido.
# Esta funcion nos muestra la lista de estudiantes registrados con un ID asignado
def mostrar_lista(lista_calificaciones):                     
    print("======Estudiantes registrados======")
    for id_estudiantes, estudiante in lista_calificaciones.items():
        print(f" ID:{id_estudiantes} Nombre: {estudiante['Nombre']}, Nota: {estudiante['Nota']}")
 
 
#funcion creada para validar nota en case 5 
def validar_nota():
      while True:
        nota_buscada = input("Ingrese la nota que desea comparar, contar o eliminar en la lista: ")
        if nota_buscada.isdigit():
            nota = int(nota_buscada)
            if 0 <= nota <= 100:
                return nota
            else:
                print("La nota debe estar entre 0 y 100.")
        else:
            print("Por favor, ingrese solo números enteros.")
        
        
    #fin de la funcion 
 
 #creamos una funcion para el cálculo del promedio en el case 3   
def calcular_promedio(lista_calificaciones, id_ingresado2): 
    
    continuar = True
    if not lista_calificaciones:
        print("Aun no hay estudiantes registrados")
        continuar = False
        
    if id_ingresado2 not in lista_calificaciones:
        print("El ID del estudiante no existe.")
        continuar = False
        
        # Verificar si el ID existe en la lista de calificaciones
    if id_ingresado2 in lista_calificaciones:
        estudiante = lista_calificaciones[id_ingresado2]

        # Mostrar los datos del estudiante
        print(f"Estudiante seleccionado: {estudiante['Nombre']}")
        print("Notas actuales:", estudiante['Nota'])
     
     #creamos variables que extraigan los datos que necesitamos para los calculos y los print finales.   
    estudiante = lista_calificaciones[id_ingresado2]
    nombre = estudiante['Nombre']
    notas = estudiante['Nota']

    if not notas:
        print(f"El estudiante {nombre} no tiene notas registradas.")
        return
    #ahora calculamos, sum suma los valores dentro de la lista notas y la funcion len cuenta la cantidad de notas en la lista.
    promedio = sum(notas) / len(notas)
    print(f"Estudiante: {nombre}")
    print(f"Notas: {notas}")
    print(f"Promedio: {promedio:.2f}")    
    
    print("Promedio realizado con éxito")    

#fin de la funcion

#funcion para validar el ID ingresado
def validacion_id(lista_calificaciones, id_ingresado4):
    
    if not id_ingresado4.isdigit():  # esto nos ayuda a comprobar que sea solo numeros y no texto
        print("ID inválido, por favor ingrese solo números enteros")
        return None
    
    id_ingresado4 = int(id_ingresado4)

    if id_ingresado4 < 0:
        print("ID inválido, ingrese ID mayor o igual a 0")
        return None

    if id_ingresado4 not in lista_calificaciones:
        print("El ID del estudiante no existe.")
        return None
        
    return id_ingresado4  

              #fin de la funcion  
    
 #funcion para agregas notas a una lista existente          
def agregar_notas_existente(lista_calificaciones, id_ingresado4):
    if id_ingresado4 not in lista_calificaciones:
        print("El ID del estudiante no existe.")
        return

   
    nombre = lista_calificaciones[id_ingresado4].get("Nombre", "Desconocido") # usamos .get para q
    continuar = True

    while continuar:
        nota_estudiante = input("Ingrese nuevas notas separadas por comas (0 a 100). Para salir, escriba 'x': ")

        if nota_estudiante.lower() == "x":
            break

        comas = nota_estudiante.split(",")
        notas_temporales = []
        correcto = True

        #validamos que las notas ingresadas cumplan con algunos parametros, que no sea texto, ni numeros fuera de rango.
        for i in comas:
            if not i.isdigit():  # verificamos que sea un valor numerico
                print("Valores inválidos, ingrese números no decimales")
                correcto = False
                break
            i = int(i)
            if i < 0 or i > 100:
                print("Notas invalidas, ingrese notas entre 1 y 100: ")
                correcto = False
                break
            #ahora agregamos las notas captadas de i a la lista notas temporales
            notas_temporales.append(i)
            
        if not correcto:
            print("No se agrego ninuna nota, agrega nuevamente.")
            continue  # vuelve a pedir notas
           
        lista_calificaciones[id_ingresado4]["Nota"].extend(notas_temporales)
        print("Notas agregadas con éxito")
        
        op = int(input("Digite 1 para agregar más notas, digite 2 para volver al menú: "))
        if op == 2:
            notas_finales = lista_calificaciones[id_ingresado4]["Nota"]
            print(f"Datos finales del estudiante {nombre} (ID: {id_ingresado4}) Notas: {notas_finales}")
            break       
        #Fin de funcion
 
 #BLOQUE DE CODIGO PRINCIPAL      
continuar = True 
lista_calificaciones = {}
id_estudiantes = 1
estudiante = 0
while continuar:
    print("======Bienvenido al sistema======")
    print("======Opciones del programa======")
    print("1.Agregar estudiantes y nota")
    print("2.Agregar notas")
    print("3.Cálcular promedio de notas acumuladas")
    print("4.Comparar notas mayores")
    print("5.Contar la cantidad de veces que se repite una nota")
    print("6.Eliminar una nota")
    print("7.Salir del programa")

    opcion_menu= input("Elige una opcion: ")
    while continuar:
        if opcion_menu.isdigit():
            opcion_menu = int(opcion_menu)  # Convertimos a un número entero

            if 1 <= opcion_menu <= 7:
                print("Entrada válida. Continuamos...")
                break  
            else:
                print("Error: solo números del 1 al 7.")
        else:
            print("Error: ingresa solo números, no texto.")
            break
    #usamos un bucle por si elige opciones invalidas, continua hasta que ingrese valores correctos
         
    match opcion_menu:
        case 1:
            print("======Agrega un estudiante======")
            id = 0
            
            while continuar:
                print("Agregue estudiante")
                notas = []
                #agregar estudiante a la biblioteca
                nombre = str(input("Ingrese el nombre del estudiante: "))
                print("Agregue nota: ")
                while continuar:
                    nota_estudiante = input("Ingrese una nota (ENTRE 1 Y 100), si desea salir presione x: ")
                   
                    #ahora con un condicional validamos y asignamos la nota ingresada
                    if nota_estudiante.lower() == "x":
                        #asignamos str a nota_estudiante que es un formato texto
                        nota_estudiante = str(nota_estudiante)
                        print("Nota asignadas exitosamente")
                        break
                    #validamos que las notas ingresadas cumplan con algunos parametros, que no sea texto, ni numeros fuera de rango.
                    if "," in nota_estudiante:
                        print("Ingrese solo una nota por favor")
                        break
                    if not nota_estudiante.isdigit():  # verificamos que sea un numero
                        print("Notas inválidas, por favor ingrese solo un número del 0 al 100")
                        break
                    nota_estudiante = int(nota_estudiante)
                    if nota_estudiante < 1 or nota_estudiante > 100:
                        print("Notas invalidas, ingrese notas entre 1 y 100: ")
                        break
                    #agregamos las notas captadas a la lista notas
                    notas.append(float(nota_estudiante))  
                    #validamos si aprobó o reprobó
                    if nota_estudiante <= 50:
                        print(f"REPROBÓ")
                    else:
                        print(f"APROBÓ")
           
                # Validamos se haya ingresado una nota válida
                if not notas:
                    print("No se ingresó ninguna nota válida. El estudiante no fue registrado.")
                    continue

                # Si todo fue válido, agregamos al diccionario
                lista_calificaciones[id_estudiantes] = {"Nombre": nombre, "Nota": notas}
                id_estudiantes += 1
                print(f"{id_estudiantes} Estudiante ingresado: {nombre}, Nota: {notas}")

                
               #lo siguiente nos sirve para darle la opcion al usuario de agregar más estudiantes o volver al menú.
                op = int(input("Digite 1 para agregar más estudiantes, digite 2 para volver al menú: "))
                if op == 2:
                    mostrar_lista(lista_calificaciones)
                    break
                
        case 2:
            #primero validamos si hay estudiantes registrados
            continuar = True
            if not lista_calificaciones:
                print("Aun no hay estudiantes registrados")
                continue
            #mostramos la lista de estudiantes registrados y sus notas.
            mostrar_lista(lista_calificaciones)
            #le pedimos que elija el ID al cual desea gregar más notas.
            id_ingresado4 = input("Ingresa el ID del estudiante: ")
            id_valido = validacion_id(lista_calificaciones, id_ingresado4)

            if id_valido is None or id_valido not in lista_calificaciones:
                print("ID inválido o no existe en la lista.")
                break

            estudiante = lista_calificaciones[id_valido]
            # Mostrar los datos del estudiante
            print(f"Nombre del estudiante: {estudiante['Nombre']}")
            print("Notas:", estudiante['Nota'])
            #ahora traemos la funcion creada para ñadir notas al id ingresado
            agregar_notas_existente(lista_calificaciones, id_valido)
        
        case 3:
            #calcular promedio de notas acumuladas
            print("=====Cálculo de promedio======")
            #primero validamos si hay estudiantes registrados
            continuar = True
            if not lista_calificaciones:
                    print("Aun no hay estudiantes registrados")
                    continue
            mostrar_lista(lista_calificaciones)
            id_ingresado2 = int(input("Ingresa el ID del estudiante: "))
            
            calcular_promedio(lista_calificaciones, id_ingresado2)
               
        case 4:
            # Comparar notas mayores respecto a una ingresada
            print("===Buscar estudiante y notas mayores===")

            #primero validamos si hay estudiantes registrados
            if not lista_calificaciones:
                print("Aún no hay estudiantes registrados")
                continue

            #mostramos la lista de estudiantes
            mostrar_lista(lista_calificaciones)

            #solicitamos el ID
            id_ingresado4 = input("Ingresa el ID del estudiante: ")
            #validamos ID
            id_valido = validacion_id(lista_calificaciones, id_ingresado4)

            if id_valido is None or id_valido not in lista_calificaciones:
                print("ID inválido o no existe en la lista.")
                break
            #buscamos en el diccionario con el ID
            estudiante = lista_calificaciones[id_valido]
            print(f"Nombre del estudiante: {estudiante['Nombre']}")
            print("Notas:", estudiante['Nota'])

            #solicitamos el valor a comparar usando la funcion
            valor_valido = validar_nota()

            if valor_valido is None:
                print("Valor inválido, por favor ingrese una nota válida entre 1 y 100.")
                break

            #contamos las notas mayores al valor ingresado
            notas_mayores = []
            for nota in estudiante["Nota"]:
                if nota > valor_valido:
                    notas_mayores.append(nota)

            #mostramos resultados
            if len(notas_mayores) == 0:
                print(f"No hay notas mayores que {valor_valido} para el estudiante {estudiante['Nombre']}")
            else:
                print(f"Notas mayores que {valor_valido} para el {estudiante['Nombre']}: {notas_mayores}")

        case 5:
            #Contar la cantidad de veces que se repite una nota
            #primero validamos si hay estudiantes registrados
            continuar = True
            if not lista_calificaciones:
                    print("Aun no hay estudiantes registrados")
                    continue
            mostrar_lista(lista_calificaciones)   
               
            id_ingresado4 = input(" Eliga el estudiante correspondiente, ingresando el ID: ")
            #verificamos que el ID si exista y/o sea correcto
            id_correcto = validacion_id(lista_calificaciones, id_ingresado4)
            if id_correcto is None:
                print("ID no válido. Asegúrese de ingresar un ID correcto.")
                break
            
            lista_acceder = lista_calificaciones[id_correcto]["Nota"]
            print(lista_acceder)
            nota_buscada = validar_nota()
            contar_nota = lista_acceder.count(nota_buscada)
            print(f"La nota buscada se repite {contar_nota} veces, asociada al ID {id_ingresado4}")
            
        case 6:
            #primero validamos si hay estudiantes registrados
            if not lista_calificaciones:
                print("Aún no hay estudiantes registrados.")
                continue

            mostrar_lista(lista_calificaciones)
            id_ingresado = input("Ingrese el ID del estudiante: ")
            #usamos la funcion de validacion de ID
            id_correcto = validacion_id(lista_calificaciones, id_ingresado)

            if id_correcto is None:
                print("ID no válido.")
                break
             
            notas = lista_calificaciones[id_correcto]["Nota"]
            print(f"Notas actuales: {notas}")
            #despues de traer las  notas, el usuario elige la nota a eliminar 
            nota_a_eliminar = validar_nota() 

            if nota_a_eliminar in notas:
                notas.remove(nota_a_eliminar)
                print(f"Nota {nota_a_eliminar} eliminada. Nuevas notas: {notas}")
            else:
                print(f"La nota {nota_a_eliminar} no se encuentra en la lista.")

        case 7:
            #salir del sistema
            print("Nos vemos luego!")     
            continuar = False          
                


       
                    
            
    
    

    
        

