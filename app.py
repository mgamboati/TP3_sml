'''________________________________________________________________________
					
					Instituto Tecnologico de Costa Rica
					     Lenguajes de Programacion	
					     Tercera Tarea Programada 
					     App Web en Python-SML
					
					Realizado por: 
					        * Josue Espinoza Castro 
							* Mauricio Gamboa Cubero
							* Andres Pacheco Quesada

					Junio del 2014
__________________________________________________________________________'''

#Imports del framework para la aplicacion web: Flask
from flask import Flask, request, redirect, url_for, abort, session, render_template, flash
from werkzeug.utils import secure_filename
import os

#Configuracion de guardar archivos
UPLOAD_FOLDER = '/home/josue/TP3_sml/Uploads'
ALLOWED_EXTENSIONS = set(['sml'])

#Nombre de la aplicacion: Bumbur
app = Flask("SML")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Para usar flash
#app.secret_key = 'josue'

#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------			FRONTEND	   ------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------

#URL y funcion para home
@app.route('/')
def home():
	return render_template('home.html')


@app.route('/felicidades', methods=['GET', 'POST'])
def felicidades():
	dinamico = [["x","999"],["y","True"]]
	estatico = [["x","int"],["y","boolean"]]
	if request.method == 'POST':
		file = request.files['file']
		if file and archivoPermitido(file.filename):
			nombre = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], nombre))
			#leersml(nombre) y generar las listas para las tablas
			#dinamico = leersml(nombre)[1] 
			#estatico = leersml(nombre)[2]
			#borrarArchivo(nombre)
			return render_template('felicidades.html',dinamico=dinamico,estatico=estatico)
		else:
			return redirect(url_for('error'))
	return render_template('felicidades.html')

@app.route('/error', methods=['GET', 'POST'])
def error():
	return render_template('error.html')


#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------			BACKEND		   --------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------

#Funcion que evalua la extension sml del archivo
def archivoPermitido(nombre):
	boolean = '.' in nombre and nombre.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
	return boolean

#Funcion para borrar un archivo en uploads despues de ser evaluado
def borrarArchivo(nombre):
	os.remove("/home/josue/TP3_sml/Uploads/"+nombre)

#Al comenzar, se borran los archivo en la carpeta Uploads
filelist = [ f for f in os.listdir("/home/josue/TP3_sml/Uploads") if f.endswith(".sml") ]
for f in filelist:
	borrarArchivo(f)

#Funcion que carga la base de conocimientos de un .txt al prolog interno        
def leersml(nombre):
    archi=open('/Uploads/'+nombre,'r+')
    linea=archi.readline()
    while linea!="":
		#hacer algo con la linea
        linea=archi.readline()
    archi.close()

#def esLista(lista):
	#lista es un string que puede o no ser una lista
	#if lista[0] == '['
#def esTupla(tupla):

#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------			MAIN				-----------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------

#main de la aplicacion
if __name__ == '__main__':
	#app.debug = True
	app.run(host='192.168.0.9') #CAMBIAR ESTE IP POR EL ACTUAL
