lis = [8,5,2,6,9,3,1,0,4,0,7] #[6,7,9,5,1,8,3] #  #6,0,9,1 #8,5,2,6,9,3,1,4,0,7
def sortSel (lista):
    print("Orden original", lista)
    for i in range (len(lista)-1):
    #    print("\n","*"*40,"\nIteración",i,"\n")
    #    print()
        min = lista[i]
        for j in range (i+1, (len(lista))):
    #        print("Comparando si",lista[j],"es menor que",min)
            if lista[j] < min:
                min = lista[j]
    #           print(lista[j],"es menor que",lista[i])
    #           print("**** El menor de momento es:",lista[j],"****")
                lista[i],lista[j]=lista[j],lista[i]
    #        else:
    #           print(lista[j],"no es menor que",min)
    #   print("El mínimo en esta iteración es",lista[i],"se mueve a hacia atrás")
    #   print("El orden actual de la lista es",lista)
    #   print("El mínimo en la sgte iteración será:",lista[i+1])
    return lista
print(sortSel(lis))