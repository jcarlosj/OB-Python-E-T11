# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.
# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

import getpass
import sqlite3

db_name = 'db_alumnos'

def open_connection( filename ) :
    conn = sqlite3.connect( f'./{ filename }.db', isolation_level=None )   # Abre fichero y crea la conexion a la base de datos
    cursor = conn.cursor()   # Abrimos el cursor

    return cursor, conn

def close_connection( cursor, conn ) :
    cursor.close()      # Cierra el cursor (No es necesario, pero es una buena práctica])
    conn.close()        # Cierra el fichero y conexión a la base de datos
    

def buscar_por_nombre( first_name ) :
    table_name = 'alumnos'

    cursor, conn = open_connection( db_name )

    rows = cursor.execute(
        f'SELECT * FROM "{ table_name }" WHERE nombre="{ first_name.lower() }"'
    )
    data = rows.fetchall()

    close_connection( cursor, conn )

    return data

def is_table_exists( table_name ) :
    cursor, conn = open_connection( db_name )

    rows = cursor.execute(
        f'SELECT name FROM sqlite_master WHERE type="table" AND name="{ table_name }"'
    )
    data = rows.fetchone()

    close_connection( cursor, conn )

    return False if data == None else True

def insert_list( table_name, alumnos ) :
    cursor, conn = open_connection( db_name )

    for alumno in alumnos :
        cursor.execute( 
            f'INSERT INTO { table_name }( nombre, apellido ) VALUES ( ?, ? )',
            ( alumno[ 'first_name' ].lower(), alumno[ 'last_name' ].lower() )
        )

    close_connection( cursor, conn )

def create_table( table_name ) :
    cursor, conn = open_connection( db_name )

    cursor.execute( 
        f'''
            CREATE TABLE IF NOT EXISTS { table_name } (
                user_id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL
            );
        '''
    )

    close_connection( cursor, conn )


def main() :
    lista_alumnos = [
        { 'first_name': 'Luisa', 'last_name': 'Bazalar' },
        { 'first_name': 'Juliana', 'last_name': 'Puerta' },
        { 'first_name': 'Laura', 'last_name': 'Zapata' },
        { 'first_name': 'Melisa', 'last_name': 'Sanchez' },
        { 'first_name': 'Maura', 'last_name': 'Villanueva' },
        { 'first_name': 'Karen', 'last_name': 'Gonzalez' },
        { 'first_name': 'Ana', 'last_name': 'Fernandez' },
        { 'first_name': 'Ana', 'last_name': 'Castro' },
        { 'first_name': 'Carolina', 'last_name': 'Porras' }
    ]

    if not is_table_exists( 'alumnos' ) :
        create_table( 'alumnos' );
        insert_list( 'alumnos', lista_alumnos )

    print( 'Ingrese los datos solicitados' )
    name = input( '  nombre: ' )

    registros = buscar_por_nombre( name )

    if not registros :
        print( f'  > Lo sentimos, { name } no esta registrado!' )
    else :
        print( '  > Resultados coincidentes con la búsqueda' )

        for registro in registros :
            print( f'   - { registro[ 1 ].capitalize() } { registro[ 2 ].capitalize() }' )


if __name__ == "__main__" :
    main()