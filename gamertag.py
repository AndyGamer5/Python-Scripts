def cabecera():
    """Muestra la cabecera de la aplicacion"""
    titulo= """ 
                /$$$$$$$                                                     /$$                       /$$  
                | $$__  $$                                                   | $$                     /$$$$  
                | $$  \ $$ /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$       |_  $$  
                | $$$$$$$//$$__  $$ /$$__  $$| $$  | $$ /$$__  $$ /$$_____/|_  $$_/   /$$__  $$        | $$  
                | $$____/| $$  \__/| $$  \ $$| $$  | $$| $$$$$$$$| $$        | $$    | $$  \ $$        | $$  
                | $$     | $$      | $$  | $$| $$  | $$| $$_____/| $$        | $$ /$$| $$  | $$        | $$  
                | $$     | $$      |  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$  |  $$$$/|  $$$$$$/       /$$$$$$
                |__/     |__/       \______/  \____  $$ \_______/ \_______/   \___/   \______/       |______/
                                            /$$  | $$                                                      
                                            |  $$$$$$/                                                      
                                            \______/                                                       """    
    print(titulo)

cabecera()                                    


def crear_tag_basico(nombre):
    """
    Crea un tag basico usando las primeras 4 letras.

    Parametro:
    nombre (str): El nombre del usario

    Returna:
    str:gamer tag basico

    """
    tag= nombre[:4]
    return tag

tag_basico = crear_tag_basico("Santiago")
print("TAG BASICO:",tag_basico)

#Invertido

def crear_tag_invertido(nombre):
    tag=nombre[::-1]
    return tag

tag_invertido= crear_tag_invertido("Santiago")
print("TAG INVERTIDO:", tag_invertido)

#Intercalado

def crear_tag_intercalado(nombre, apellido):
    tag=nombre[0]+apellido[0]+nombre[1::]+apellido[1::]
    return tag

tag_intercalado= crear_tag_intercalado("Santiago","Hernandez")
print("TAG INTERCALADO:", tag_intercalado)

#Elite

def crear_tag_elite(nombre):
    tag=nombre[:2]+nombre[-2:]
    return tag

tag_elite= crear_tag_elite("Santiago")
print("TAG ELITE:", tag_elite)

#Numero Tag

def crear_tag_con_numero(nombre, numero_favorito):
    tag=nombre[:5]+numero_favorito
    return tag

tag_numero= crear_tag_con_numero("Santiago","777")
print("TAG NUMERO:", tag_numero)

