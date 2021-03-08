"""
script : dd-python-mysql.python-mysql
Utilidad : Este script documenta las descripciones (comments) de las columnas en una base de datos Mysql a partir de un archivo plano con la siguiente estructura
la 1a clumna es la tabla, la 2a es la columna y la 3a es la descipción que el desarrollador de la aplicación ha registrado en un archivo Excel del cual hemos obtenido
el archivo plano.
profiles;active;Indica si el perfil del proyecto radicado se encuentra activo.
remember_tokens;id;Identificador de la tabla remember_tokens
Desarrolló : Ing. Martin Alfonso Nieto Prada
             DBA - Agencia de Desarrollo Rural
Fecha : Marzo 7 de 2021
"""
import mysql.connector
import csv

bd='perfiles'
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("use perfiles")  

contador=0
archivo_nombre='a.csv'		
print("<<<<<<<<<<<<<<<<<<<   INICIAMOS PROCESO >>>>>>>>>>>>>>>>>>>>>")
with open(archivo_nombre) as File:
	reader = csv.reader(File, delimiter=';', quoting=csv.QUOTE_MINIMAL) # quotechar=',',
	# Vamos a generar un ALTER TABLE ... por cada trio BD - Tabla - Columna, para registrar el comment de la columna
	for row in reader:
		contador=contador+1
		print("**************************************************************************************************************************************")
		print("<<<======  ",contador,")  Tabla : ",row[0]," Columna : ",row[1]," Descripcion -->> ",row[2], "   ===========>>>")
		cadena = "SELECT table_name, column_name,CONCAT('ALTER TABLE "+ row[0] + " CHANGE " + row[1] + "   " + row[1] + "   ',column_type,  "
		cadena = cadena + " IF(is_nullable = 'YES', '  ' , '  NOT NULL '), IF(column_default IS NOT NULL, concat('  DEFAULT ', IF(column_default = 'CURRENT_TIMESTAMP', column_default, "
		cadena = cadena + "	CONCAT(column_default) ), ' '), ''), "
		cadena = cadena + " IF(column_default IS NULL AND is_nullable = 'YES' AND column_key = '' AND column_type = 'timestamp','  NULL ', ' '), "
		cadena = cadena + " IF(column_default IS NULL AND is_nullable = 'YES' AND column_key = '','  DEFAULT NULL ', ' '), "
		cadena = cadena + "extra, ' COMMENT \"" + row[2] + "\";') as script FROM information_schema.columns WHERE table_schema = '" + bd + "' and table_name='"+row[0]+"'  "
		cadena = cadena + " and column_name='" + row[1] + "' ORDER BY table_name , column_name"
		""" 
		ALTER TABLE banco CHANGE id_banco id_banco int(11) NOT NULL auto_increment COMMENT '' ;
		"""
		print(cadena)
		mycursor.execute(cadena)
		for x in mycursor:
			print ("Sentencia de documentación a ejecutar : ")
			print(x[2])
			mycursor.execute(x[2])
			mycursor.fetchall()
			
print ("!!!  Terminé, documenté ",contador," columnas. !!!!")