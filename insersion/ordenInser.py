a=[4,7,1,32,9,5,5,65,1,0,81,2.4] #6,7,9,5,1,8,3 #0,2.4,7,1,32,9,5,5,65,1,81
def sortIns(lista):
    print("Orden original", lista)
    for i in range (1, (len(lista))):
    #    print("\n","*"*40,"\nIteración",i,"\n")
        for j in range (i,0,-1): # El segundo ciclo se recorre de adelanta a atrás empezando por el valor de i
                                    # de este modo, el numero menor será movido hasta el puesto que le corresponde,
                                    # además, estamos guardando siempre la parte ordenada lista al principio 
                                    # y en la próxima iteración, se evalúa desde el siguiente número de la lista
                                    # resultante de esa itaración nuevamente hacia atrás.
    #        print("Comparando si",lista[j],"es menor que",lista[j-1])
            if lista[j-1] > lista[j]:
                aux = lista[j]
                lista[j] = lista[j-1]
                lista[j-1] = aux
    #        print(lista[j-1],"es menor que",lista[j],"se guarda en aux y se switchea con el puesto anterior")
    #       print("El orden momentaneo de la lista es",lista)
    #        else:
    #            print(lista[j],"no es menor que",lista[j-1])
    #    print("El orden de la lista al final de este ciclo es",lista)
    print("Orden final de la lista", lista)
    return lista
sortIns(a) 