import sqlite3

#conexxion ala base de datos 
conn = sqlite3.connect('database.db')
cursor =conn.cursor()

#crear tabla si no exite 
cursor.execute(
    """
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT ,
                    apellido TEXT ,
                    edad int
                )"""
)

conn.commit()
#crear registro -> C

def crear_usuario(nombre: str,apellido:str,edad: int) -> str:
    cursor.execute("INSERT INTO usuarios (nombre, apellido, edad) VALUES (?,?,?)", (nombre,apellido,edad))
    conn.commit() 
    return "usuario Agregado"

#obtener registros -> R
def  obtener_registros() -> list:
    cursor.execute("SELECT nombre,apellido,edad FROM usuarios")
    usuarios = cursor.fetchall()            
                
    lista_usuarios =[]            
    for usuarios in usuarios:
        lista_usuarios.append(usuarios)      
        
    return lista_usuarios

 #Actualizar usuario por id  -> U
def actualizar_usuario(id:int,nombre:str,apellido:str,edad:int) -> str:
    cursor.execute("UPDATE usuarios SET nombre =?, apellido =?, edad =? WHERE id =?", (nombre, apellido, edad, id))
    conn.commit()
    return "Usuario actualizado"
          
#eeliminar usuario 
def eliminar_usuario(id) -> str:
    cursor.execute("DELETE FROM usuarios WHERE id =?", (id,))
    conn.commit()
    return "usuario eliminado"
    
    
#leer registro por su id 
def obtener_usuario(id: int) -> list:
    cursor.execute("SELECT id,nombre,apellido,edad FROM usuarios WHERE id =?", (id,))
    usuario = cursor.fetchall()
    
    if usuario:
        return usuario
    return "usuario no encontrado"

#crear usuario
# crear_usuario("joshua","rivas",27)
# crear_usuario("jcva","velasquez",28)
# crear_usuario("carmen","barranza",22)
# crear_usuario("joel","fernando",25)
# crear_usuario("belaunde","terry",27)


#obtener usuarios

print(obtener_registros())