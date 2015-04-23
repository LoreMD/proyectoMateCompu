class montonArena:
    
    def __init__ (self, L):
        self.L=L
        self.array=self.startRandom()
        self.pendienteCritica=15
        
    def dinamicaArena(self):
        aux=np.zeros((self.L, self.L))
        bandera=True
        j=1
        while bandera==True:
            for i in xrange(1, self.L-1):
                if j==self.L-1:
                    bandera=False
                else:
                    pendiente=self.array[i,j]+self.array[i,j+1]
                    pendiente+=self.array[i, j-1]
                    pendiente+=self.array[i+1, j]
                    pendiente+=self.array[i-1, j-1]
                    if pendiente>self.pendienteCritica:
                        bandera=False
                    """la bandera es para sacarte del while, porque tiene que checar que la pila completa sea estable/inestable"""
            j+=1
        if pendiente>self.pendienteCritica:
            for j in xrange(0, self.L, 1):
                for i in xrange(0,self.L-1,1):
                    aux[j,i]=self.array[j,i]-1
                    aux[j,i+1]=self.array[j,i+1]+1
                """
                se desparrama
                """
            self.array=aux
        else:
            """
            crece
            """
            pass
            
    def a(self):
        return self.array
    
     """
    codigo siguiente copiado de lo de clase, y modificado para 2 dimensiones
    """
    def startSingle(self):
        """solo un granito de arena/fuego a la mitad del arreglo"""
        self.array[self.L/2, self.L/2] = 1

    def startRandom(self):
        """Valores aleatorios en el tiempo t_0"""
        array=np.zeros([self.L, self.L])
        for i in xrange(0,self.L,1):
            for j in xrange(0, self.L,1):
                array[i,j]=randint(1,10)
        return array
        
    def loop(self, steps=1):
        """Ejecuta el número especificado de pasos."""
        [self.step() for i in xrange(steps)]

    def step(self):
        """Avanza un paso t -> t+1."""
        pass