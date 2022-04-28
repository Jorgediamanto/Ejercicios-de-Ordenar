#import numpy as np
array_condiciones=[[2,1],[3,1],[4,2],[3,4],[0,2],[0,3]]

array_ayuda=[1,1,1,1,1]  #usas para calcular por que elmentos has pasado

array_ayuda2=[]  #usas para calcular no hay escapatoria

array_ayuda3=[]
#n=4 #numero de elementos-1


def buscarsinsalida(x):
  
  array_ayuda[x]=0
  for y in range(len(array_condiciones)): #del 0 al 5
    
    
    if(array_condiciones[y][0]==x):
      
      if(array_ayuda[array_condiciones[y][1]]==1):
        
        buscarsinsalida(array_condiciones[y][1])
        
        
      
    
      

    
  array_ayuda2.append(x) #meter el ultimo numero en array  

  


  
  

for barna in range(len(array_condiciones)-1):
  
  
  buscarsinsalida(barna)
  if(len(array_ayuda2)>len(array_ayuda3)):
    array_ayuda3=array_ayuda2
  array_ayuda2=[]

print(array_ayuda3[::-1])