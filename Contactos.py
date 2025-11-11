import os 

CARPETA = 'contactos/' #Carpeta de contactos

def app():
    
    crear_directorio()
    
def crear_directorio():
    if not os.path.exists(CARPETA): #Carpeta para revisar
        #crear una carpeta
        os.makedirs(CARPETA) 
    else:
        print('La carpeta ya existe')
        
app()