import random
def sacarRes(letra,lstpal,lstres):
    cont=0
    if letra in lstpal:
        for l in lstpal:
            if l==letra:
                lstres[cont]=l
            cont+=1
    return lstres

def imprimir_(lstpal,lstres):
    cont=0
    for letra in lstpal:
        if lstres[cont]==letra:
            print(letra,end="")
        else:
            print("_",end="")
        cont+=1
    print()

def pasarAMinuscula(letra):
    if ord(letra) >=65 and ord(letra)<=90:
        return chr(ord(letra)+32)
    else:
        return letra

def palabraAMinuscula(pal):
    res=""
    for letra in pal:
        if ord(letra) >=65 and ord(letra)<=90:
            res+=chr(ord(letra)+32)
        else:
            res+=letra
    return res


def ahorcado(listaPalabras):
    #letra=input("Ingrese una letra: ")
    num=random.randint(0,len(listaPalabras)-1)
    palabra=listaPalabras[num]
    intentos=10
    intentospal=3
    print()
    print("Tus intentos para letras son:",intentos)
    print("Tus intentos para palabra son:",intentospal)
    print()   
    ganaste=False
    perdiste=False
    lstpal=[]
    lstres=[]
    for let in palabra:
        lstpal.append(let)
        lstres.append("")
    print("A ustdes le a tocado la siguiente palabra(",len(lstpal),"): ",end="")
    imprimir_(lstpal,lstres)
    opcion=int(input("Ingrese 1 si quiere arriegar una letra(10 intentos), ingrese 2 si quiere arriesgar la palabra(3 intentos): "))
    while (opcion==1 or opcion==2) and not(ganaste) and not(perdiste):
        if intentos>0 and not(ganaste) and opcion==1 and intentospal>0: #El juego sigue hasta que ganes o hasta que acabes tus intentos(10)
            letra=pasarAMinuscula(input("Ingrese una letra: "))
            if len(letra)==1:
                if letra in lstpal and letra not in lstres:
                    sacarRes(letra,lstpal,lstres)
                    imprimir_(lstpal,lstres)
                else:
                    print("Erraste")
                    intentos-=1
                    if intentos==0:
                        perdiste=True
            else:
                print("Ingrese una letra por favor.")
            if lstres==lstpal:
                ganaste=True
                
            if not(ganaste) and not(perdiste):
                opcion=int(input("Ingrese 1 si quiere arriegar una letra, ingrese 2 si quiere arriesgar la palabra: "))        #elif opcion==2:
            
            
        if intentos>0 and not(ganaste) and opcion==2:
            print("Recuerde que la palabra tiene",len(lstpal),"letras")
            imprimir_(lstpal,lstres)
            palabraintento=palabraAMinuscula(input("Ingrese la palabra que cree correcta: "))
            if palabraintento==palabra:
                ganaste=True
            else:
                intentospal=intentospal-1
                print("Esa no es la palabra")
                if intentospal==0:
                        perdiste=True
            if not(ganaste) and not(perdiste):
                opcion=int(input("Ingrese 1 si quiere arriegar una letra(10 intentos fallidos), ingrese 2 si quiere arriesgar la palabra(3 intentos fallidos): "))
        if not(ganaste) and not(perdiste):
            print("Tus intentos para letras son:",intentos)
            print("Tus intentos para palabra son:",intentospal)      

    return ganaste


def main():
    listaPal=["ajedrez","bonjour","renata","marcela","esquizofrenia","atleta","alterado","tintura","termotanque","cuaderno","saque","seis"]
    if ahorcado(listaPal):
        print("Ganaste!!!!!!")
    else:
       print("Perdiste!!!!!!!")
main()