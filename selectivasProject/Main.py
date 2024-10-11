from queue import PriorityQueue
from xml.dom.minidom import ProcessingInstruction

uno=" Estructura Simple y Doble ";print(uno.center(50,"•"))
a = 200
b = 200

if b > a:
    print(b,"es mayor que ",a)
else:
    print(b,"no es mayor que ",a)
print("\n")
dos= " ESTRUCTURA MULTIPLE "; print(dos.center(50,"•"))
if a>b:
    print(a,"es mayor que ",b)
elif a<b:
    print(a,"es menor que ",b)
else:
    print(a,"es igual a ",b)
print("\n")
tres=" CONDICIONES ENLAZADAS ";print(tres.center(50,"•"))
x=18

if x>10:
    print("Por encima de diez,")
    if x>20:
        print("También por encima de 20!")
    else:
        print("pero no por encima de 20.")
print("\n")
cuatro=" PARAMETROS END Y SEP ";print(cuatro.center(50,"•"))
print("END \n")
print("Estudiar los sábados",end=' ') #para en linea 1 las lineas  1 y 2
print("es genial")
#print("Estudiar los sábados",end=' ')
#print("es genial")
print("\SEP Y END\n")
print("Daniela","Luis","Carlos","Camila")#Agrega un espacio por defecto
print("Daniela","Luis","Carlos","Camila",sep="")#Quita el espacio
print("Daniela","Luis","Carlos","Camila",sep=",")#Agrega una camisa

print("Daniela","Luis","Carlos","Camila",sep="_", end="_Curso_Pyton")#implementacion 


