# dd-masivo-python-mysql
Carga masiva a las tablas del catálogo de Mysql.

A partir de un diccionario de datos en un archivo de excel el cual tiene tres columnas, el nombre de la base de datos, el nombre de la columna y la descripción de la misma. 

Este script carga el archivo y linea a linea genera un sentencia Mysql de la forma :
(Ej ) ALTER TABLE banco CHANGE id_banco id_banco int(11) NOT NULL auto_increment COMMENT 'Aqui el comentario de la columna' ;


