import numpy as np

def convolucion(a,b):
    matriz2 = np.zeros([len(a)-2,len(a[0])-2])
    for f in range(len(matriz2)):
        for c in range(len(matriz2[0])):
            val1 = (a[f][c]*b[0][0])+(a[f][c+1]*b[0][1])+(a[f][c+2]*b[0][2])
            val2 = (a[f+1][c]*b[1][0])+(a[f+1][c+1]*b[1][1])+(a[f+1][c+2]*b[1][2])
            val3 = (a[f+2][c]*b[2][0])+(a[f+2][c+1]*b[2][1])+(a[f+2][c+2]*b[2][2])
            matriz2[f][c] = val1 + val2 +val3
    print(matriz2)
                                                    
matriz1 = [[6,9,0,3],[8,4,9,1],[4,1,3,12],[3,2,1,100]]
filtro = [[1,0,2],[5,0,9],[6,2,1]]
convolucion(matriz1, filtro)

