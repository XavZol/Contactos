import os 

CARPETA = 'contactos/' #Carpeta de contactos
EXTENSION = '.txt' #Agrega la extension del tipo de documento

#Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    # Revisa si la carpeta existe o no
    crear_directorio()
    
    #Muestra el menú de opciones 
    mostrar_menu()
    
    #Preguntar al Usuario la acción a realizar
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opcion: \r\n')
        opcion = int(opcion)
        
        #Ejecutar las opciones 
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else: 
            print('Opcion no valida, digite otra opcion:')
            
def eliminar_contacto():
    nombre = input('Seleccione el Contacto que desea eliminar: \r\n')
    
    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\nEliminado correctamente')
    except FileNotFoundError:
        print('No existe ese contacto')
        
    #reiniciar la app
    app()

            
def buscar_contacto():
    nombre = input('Seleccione el Contacto que desea buscar: \r\n')
    
    try:
            with open(CARPETA + nombre + EXTENSION) as contacto:
                print('\r\n Información del Contacto: \r\n')
                for linea in contacto: 
                    print(linea.rstrip())
                print('\r\n')
    except IOError as e:
        print('El archivo no existe')
        print(e)
        
#Consultar datos de un archivo txt que ya hemos creado
def mostrar_contactos():
    archivos = os.listdir(CARPETA)
    
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    
    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                #Imprime los contenidos
                print(linea.rsplit())
           #Imprime el separador     
            print('\r\n')
            
def editar_contacto():
    print('Escribe el nombre del contacto a editar')         
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')   

    #Revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_anterior)
    
    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w' ) as archivo:
        
            #resto del campo 
            nombre_contacto = input('Agrega Nuevo Nombre: \r\n')
            telefono_contacto = input('Agrega Nuevo Telefono: \r\n')
            categoria_contacto = input('Agrega Nueva Categoria: \r\n')

            #Instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            
            #Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')
            
            #renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
            
            #Mostrar mensaje de exito
            print('\r\nContacto creado correctamente\r\n')
            
    else:
        print('Ese contacto no existe')
        
    #reiniciar la aplicación 
    app()
    

def agregar_contacto():
    print('Escribe los datos para agregar el nuevo contacto')
    nombre_contacto = input('Nombre del Contacto:\r\n')
    
    #Revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto)
    
    if not existe:
    
    #contactos/Javier.txt
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
                
                #Resto de los campos
                telefono_contacto = input('Agrega el Telefono:\r\n')
                categoria_contacto = input('Categoria Contacto: \r\n')
                
                #Instanciar clase
                contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
                
                #Escribir en el archivo
                archivo.write('Nombre: ' + contacto.nombre + '\r\n')
                archivo.write('Telefono: ' + contacto.telefono + '\r\n')
                archivo.write('Categoria: ' + contacto.categoria + '\r\n')
                
                #Mostrar un mensaje de éxito
                print('\r\nContacto creado correctamente\r\n')
                
    else: 
        print('Ese contacto ya existe')
        
    #Reiniciar la app 
    app()
    
def mostrar_menu():
    
    print('Seleccione del Menú lo que desea hacer:')
    print('1) Agregar nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')
    
def crear_directorio():
    # Crear la carpeta de contactos si no existe
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)
def existe_contacto(nombre):
    #Revisar si el archivo ya existe antes de crearlo
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()