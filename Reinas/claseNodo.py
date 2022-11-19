import numpy as np
class Nodo:
    __costo=0# cantidad de reinas chocadas
    __arreglo=None
    __tamano=0
    __posicion=0
    __sigD=None
    __sigI=None

    def __init__(self,n=4,x=None,y=None):
        self.__costo=0
        self.__arreglo=np.full(n,-1)
        self.__tamano=n
        if x!=None and y!=None:
            self.__posicion=y
            self.__arreglo[x]=y
        self.__sigD=None
        self.__sigI=None

    def setDer(self,nodo):
        self.__sigD=nodo
    def setIzq(self,nodo):
        self.__sigI=nodo
    def getDer(self):
        return self.__sigD
    def getIzq(self):
        return self.__sigI
    def getArray(self):
        return self.__arreglo
    def getX(self):
        return self.__posicion
    def getY(self):
        return self.__arreglo[self.__posicion]
    def setCosto(self,costo):
        self.__costo=costo
    def setReina(self,x,y):
        self.__arreglo[x]=y
    def getCosto(self):
        espacios=0
        tabla=np.full((self.__tamano,self.__tamano),0)
        for i in range(self.__tamano):
            if self.__arreglo[i]!=-1:
                tabla[i][self.__arreglo[i]]=1
        i=0

        for i in range(self.__tamano):
            for j in range(self.__tamano):
                if not self.Choca(i,j):
                    espacios+=1

        self.setCosto=espacios
        return espacios
#if abs(x+y) != abs(i+j) and abs(x-y) != abs(i-j) and y != self.__arreglo[i]  and x!= i: #diagonal positiva, diagonal negativa, fila, columna
#                   pass

    def Choca(self,x,y):
        band=False
        for i in range(self.__tamano):
            j=self.__arreglo[i]
            if self.__arreglo[i]!=-1:
                if abs(i+j) != abs(x+y):
                    if abs(i-j) != abs(x-y): 
                        if i!=x and j!=y:
                            pass
                        else:
                            band=True
                    else:
                            band=True
                else:
                            band=True
        return band