# dd-masivo-python-mysql
Carga masiva a las tablas del catálogo de Mysql.

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////  Escenario : Es bastante típico que los desarrolladores y/o Dba's, creen las bases de datos sin documentarlas    /////////
/////////               mas sin embargo, la documentación es necesaria en procesos de mejoramiento tendiente a mas altos    /////////
/////////               niveles, por auditorías u otros procesos, y cargar ese tipo de información en una base de datos que /////////
/////////               está ya en producción aparte de los dispondioso que es en si mismo el proceso puede ser riesgoso.   /////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
A partir de un diccionario de datos en un archivo de excel el cual tiene tres columnas, el nombre de la base de datos, el nombre de la columna y la descripción de la misma. 

Este script carga el archivo y linea a linea genera un sentencia Mysql de la forma :
(Ej ) ALTER TABLE banco CHANGE id_banco id_banco int(11) NOT NULL auto_increment COMMENT 'Aqui el comentario de la columna' ;

Una vez creada la sentencia, la ejecuta con el fin de actualizar el diccionario de datos para la columna específica.


