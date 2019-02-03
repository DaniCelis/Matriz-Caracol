def leer_archivo(archivo):
    return ([x.split(" ") for x in [y.strip("\n") for y in open(archivo).readlines()]])

def derecha(matriz, pos, tam, x, y, end):
    if(end<(len(leer_archivo("caracol.txt"))*len(leer_archivo("caracol.txt")))):
        if(pos<=tam):
            print matriz[x][y]
            pos+=1
            y+=1
            end+=1
            derecha(matriz, pos, tam, x, y, end)
        else:
            abajo(matriz, 0, tam-1, x+1, y-1, end)


def abajo(matriz, pos, tam, x, y, end):
    if(pos<=tam):
        print matriz[x][y]
        pos+=1
        x+=1
        end+=1
        abajo(matriz, pos, tam, x, y, end)
        
    else:
        izquierda(matriz, 0, tam, x-1, y-1, end)


def izquierda(matriz, pos, tam, x, y, end):
    if(pos<=tam):
        print matriz[x][y]
        pos+=1
        y-=1
        end+=1
        izquierda(matriz, pos, tam, x, y, end)
    else:
        arriba(matriz, 0, tam-1, x-1, y+1, end)


def arriba(matriz, pos, tam, x, y, end):
    if(pos<=tam):
        print matriz[x][y]
        pos+=1
        x-=1
        end+=1
        arriba(matriz, pos, tam, x, y, end)
    else:
        derecha(matriz, 0, tam, x+1, y+1, end)

        
def main():
    print derecha(leer_archivo("caracol.txt"), 0, len(leer_archivo("caracol.txt"))-1, 0, 0, 0)

main()








