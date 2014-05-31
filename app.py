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
	#flash('Archivo subido con exito.','message')
	table1 = [[1,1],[2,2],[3,3]]
	table2 = [[4,4],[5,5],[6,6]]
	if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			#flash('Archivo subido con exito.','success')
			return render_template('felicidades.html',dinamico=table1,estatico=table2)
		else:
			#flash('Debe ingresar un archivo de extension .sml unicamente.','error')
			return redirect(url_for('error'))
	return render_template('felicidades.html',dinamico=table1,estatico=table2)

@app.route('/error', methods=['GET', 'POST'])
def error():
	#flash('Debe ingresar un archivo de extension .sml unicamente.','error')
	return render_template('error.html')


#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------			BACKEND		   --------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------

#Funcion que evalua la extension sml del archivo
def allowed_file(filename):
	var = '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
	return var

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

#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------			MAIN				-----------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------

#main de la aplicacion
if __name__ == '__main__':
	#app.debug = True
	app.run(host='192.168.43.93') #CAMBIAR ESTE IP POR EL ACTUAL
