import numpy as np
from claseNodo import Nodo
class Arbol:
    __tamano=0
    __LNV=[]#lista de nodos vivos
    __raiz=None 

    def __init__(self,n,lista=[]):
        self.__raiz=None
        self.__tamano=n
        self.__LNV=lista
        max=self.Beneficio()
        self.reinas(self.__raiz,max,0)
    def grado(self,nodo):
        grado=2
        if nodo.getDer()==None and nodo.getIzq()!=None or nodo.getDer()!=None and nodo.getIzq()==None: 
            grado=1
        elif nodo.getDer()==None and nodo.getIzq()==None:
            grado=0
        return grado

    def reinas(self,nodoR,nodo,nivel):
        if nivel==0: #tabla vacia
            self.__raiz=Nodo(4)
            
        elif nivel<self.__tamano:

            if self.grado(nodoR)==0 and nodo.getIzq()==None:
                nodoR.setIzq(nodo)

            elif self.grado(nodoR)==0 and nodo.getDer()==None:
                nodoR.setDer(nodo)

            else:
                self.reinas(nodoR.getDer(),nodo,nivel+1)
                
    def Beneficio(self):
        max=0
        indice = 0
        for i in range(len(self.__LNV)):
            if max<self.__LNV[i].getCosto():
                max=self.__LNV[i].getCosto()
                indice = i
        self.__LNV[indice]=None
        return max

    def ListaNV(self,nodo):
        self.__LNV.append(nodo)
    def getLNV(self):
        return self.__LNV
    def getRaiz(self):
        return self.__raiz
    def InOrden(self,nodo):
        if nodo!=None:
            self.InOrden(nodo.getIzq())
            
            self.InOrden(nodo.getDer())
            print(nodo.getCosto())
if __name__=='__main__':
    nodo1=Nodo(4,0,0)

    nodo2=Nodo(4,0,0)
    nodo2.setReina(2,1)

    nodo3=Nodo(4,0,0)
    nodo3.setReina(2,1)
    nodo3.setReina(3,1)
    arbol=Arbol(4,[nodo1,nodo2,nodo3])
    arbol.InOrden(arbol.getRaiz())
    for i in range(3):
        max=arbol.Beneficio()
        arbol.reinas(max)
