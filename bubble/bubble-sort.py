arr = [8,5,2,6,9,3,1,4,0,7]
def bubblesort(lista):
    contador = 0
    #print("Orden original :",lista)
    for j in range (len(lista)-1):
    #    print("\n","-"*60,"\nIteración número n",j,"(Desde",lista[0],"hasta",lista[len(lista)-1-j],")")
        for i in range (len(lista)-1-j): # Al colocar "-j", estoy indicando que revise desde el anterior al último número, 
                                            # pues ese siempre será el número más grande bajo la priemra iteración
            contador += 1
            #print("\n","*"*80,"\nindex",i,"valor",lista[i])
    #        print("\n","*"*80,"\ncomparando ",lista[i],"con",lista[i+1])
            if lista[i] > lista[i+1]:
                lista[i],lista[i+1]=lista[i+1],lista[i]
    #           print(lista[i+1],"Es mayor que " ,lista[i])
    #           print("Se cambia ",lista[i],"por -->",lista[i+1])
    #           print("El arreglo ahora queda así :",lista)
    #       else: 
    #           print("No se cambia porque ",lista[i+1],"no es mayor que",lista[i])
    #   print("\nLista al final de esta iteración: ",lista)
    #print("\n","-"*80,"\nLista final :",lista)
    print("Cantidad de evaluaciones :",contador) # sin "j" en (len(lista)-1-j), en el segundo for, 
                                                    #la cantidad de evaluaciones casi se duplica, esto consume muchos más recrusos
    return(lista)
print(bubblesort(arr))