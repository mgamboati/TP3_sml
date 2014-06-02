lista=[["x",3,"int"],["z",5,"int"],["y","false","bool"]]



def agregardatos(lista,variable,valor,tipo):
     temp_list=[variable,valor,tipo]
     lista.append(temp_list)




     
## resuelve operaciones elementales
def operacion(valor1,operando,valor2):
     if (isinstance(valor1,int) and isinstance(valor2,int)) : 
          if operando=="+":
               return (valor1+valor2)
          elif operando=="-":
               return (valor1-valor2)
          elif operando=="*":
               return (valor1*valor2)
          elif operando=="/":
               return (valor1/valor2)
          else:
               print ("Operacion no permitida")
     elif (isinstance(valor1,int) and verificar_int(valor2)):
          if operando=="+":
               return (valor1+(obtener(valor2)))
          elif operando=="-":
               return (valor1-(obtener(valor2)))
          elif operando=="*":
               return (valor1*(obtener(valor2)))
          elif operando=="/":
               return (valor1/(obtener(valor2)))
          else:
               print ("Operacion no permitida")
     elif (verificar_int(valor1) and isinstance(valor2,int)):
          if operando=="+":
               return ((obtener(valor1))+valor2)
          elif operando=="-":
               return ((obtener(valor1))-valor2)
          elif operando=="*":
               return ((obtener(valor1))*valor2)
          elif operando=="/":
               return ((obtener(valor1))/valor2)
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
          print ("Errorrrrrrrrrrrrsh")
          

##def analizador_tupla(Ttupla):
##     if Ttupla==():
##          return ("()")
##     respuesta="("
##     elif isinstance (Ttupla[0],int):
##          return respuesta+("int ")
##  

def verificar_int(valor):
     if lista==[]:
          return False
     for e in lista:
          if ((e[0]==valor) and (e[2]=="int")):
               return True
     return False


def obtener(valor):
     for e in lista:
          if (e[0]==valor):
               return (e[1])
