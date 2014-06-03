lista=[["x",3,"int","global"],["z",5,"int","global"],["y","false","bool","global"]]


#Inserta datos al inicio de la lista.  
def agregardatos(lista,variable,valor,tipo,scope):
     temp_list=[[variable,valor,tipo,scope]]
     lista=temp_list+lista
     return lista

     
## resuelve operaciones elementales
def operacion(valor1,operando,valor2):
     if (isinstance(valor1,int) and isinstance(valor2,int)) : 
          if operando=="+":
               return (valor1+valor2)
          elif operando=="-":
               return (valor1-valor2)
          elif operando=="*":
               return (valor1*valor2)
          elif operando=="div": #operando=="/" 
               return (valor1/valor2)
          elif operando=="mod": #operando=="%" 
               return (valor1%valor2)
          else:
               print ("Operacion no permitida")
     elif (isinstance(valor1,int) and verificar_int(valor2)):
          if operando=="+":
               return (valor1+(obtener(valor2)))
          elif operando=="-":
               return (valor1-(obtener(valor2)))
          elif operando=="*":
               return (valor1*(obtener(valor2)))
          elif operando=="div": #operando=="/"
               return (valor1/(obtener(valor2)))
          elif operando=="mod": #operando=="%" 
               return (valor1%(obtener(valor2)))
          else:
               print ("Operacion no permitida")
     elif (verificar_int(valor1) and isinstance(valor2,int)):
          if operando=="+":
               return ((obtener(valor1))+valor2)
          elif operando=="-":
               return ((obtener(valor1))-valor2)
          elif operando=="*":
               return ((obtener(valor1))*valor2)
          elif operando=="div": #operando=="/"
               return ((obtener(valor1))/valor2)
          elif operando=="mod": #operando=="%"
               return ((obtener(valor1))%valor2)
          else:
               print ("Operacion no permitida")

     elif (verificar_int(valor1) and verificar_int(valor2)):
          if operando=="+":
               return ((obtener(valor1))+(obtener(valor2)))
          elif operando=="-":
               return ((obtener(valor1))-(obtener(valor2)))
          elif operando=="*":
               return ((obtener(valor1))*(obtener(valor2)))
          elif operando=="div": #operando=="/"
               return ((obtener(valor1))/(obtener(valor2)))
          elif operando=="mod": #operando=="%"
               return ((obtener(valor1))%(obtener(valor2)))
          else:
               print ("Operacion no permitida")
     else:
          print ("operacion fallida")



#La lista que recibe debe ser asi [2,3,4] o [true,false,true,false] o [[2,1],[3,6],[5,6]] o [(5,4),(8,9),(3,6)]
#Los tipos de datos se tuvieron que convertir anteriormente  
def analizador_lista(Llista):
     if Llista==[]:
          return ("list")
     elif isinstance (Llista[0],int):
          return ("int list")
     elif Llista[0]=="false" or Llista[0]=="true":
          return ("bool list")
     elif isinstance(Llista[0],list):
          return (analizador_lista(Llista[0])+" list")
     elif isinstance(Llista[0],tuple):
          return (analizador_tupla(Llista[0])+" list")
     else:
          print ("Errorrsh")
          

def analizador_tupla(Ttupla):
     if len(Ttupla)==0:
          return ("()")
     respuesta="("
     if isinstance (Ttupla[0],int):
          respuesta=respuesta+"int"     
     elif Ttupla[0]=="false" or Ttupla[0]=="true":
          respuesta=respuesta+"bool"
     elif isinstance (Ttupla[0],list):
          respuesta=respuesta+analizador_lista(Ttupla[0])
     elif isinstance (Ttupla[0],tuple):
          respuesta=respuesta+analizador_tupla(Ttupla[0])
     for e in Ttupla[1:]:
          if isinstance (e,int):
               respuesta=respuesta+"*int"
          elif e=="false" or e=="true":
               respuesta=respuesta+"*bool"
          elif isinstance (e,list):
               respuesta=respuesta+"*"+analizador_lista(e)
          elif isinstance (e,tuple):
               respuesta=respuesta+"*"+analizador_tupla(e)
     respuesta+=")"
     return respuesta

# Verificar si la variable es un int
def verificar_int(valor):
     if lista==[]:
          return False
     for e in lista:
          if ((e[0]==valor) and (e[2]=="int")):
               return True
     return False

#Obtener el valor del dato almacenado en la lista siempre y cuando sean GLOBALES
def obtener(valor):
     for e in lista:
          if (e[0]==valor) and (e[3]=="global"):
               return (e[1])

#Si se identifica tl
def tl(lista):
     return (lista[1:])

#Si de identifica hd
def hd(lista):
     return (lista[0])
