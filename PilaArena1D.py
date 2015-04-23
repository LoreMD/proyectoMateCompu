class PilaArena1D:
    
    def __init__ (self, L, n=1):
        """ 
        L es el numero de columnas que hay
        """
        self.L = L
        self.n = n
        self.array = np.zeros((self.n,self.L))
        self.pendienteCritica=7
    
    def dinamicaArena(self):
        """
        dinamica explicada en las instrucciones
        """
        aux=np.zeros((self.n, self.L))
        bandera=True
        j=0
        while bandera:
            pendiente=self.array[0,j]+self.array[0,j+1]
            if pendiente>self.pendienteCritica or j==L-2:
                bandera=False   
            j+=1
        if pendiente>self.pendienteCritica:
            for i in xrange(0,self.L,1):
                aux[0,i]=self.array[0,i]-1
                aux[0,i]=self.array[0,i]+1
                """
                se desparrama
                por ahora es circular (ups)
                """
            self.array=aux
        else:
            """
            crece
            """
            self.array[0,randint(0,self.L-1)]+=1
    
    """
    codigo siguiente modificado de lo que se vió en clase
    """
    def startSingle(self):
        """solo un granito de arena a la mitad del arreglo"""
        self.array[0, self.L/2] = 1

    def startRandom(self):
        """Valores aleatorios en el tiempo t_0"""
        for i in xrange(0,self.L,1):
            self.array[0,i]=randint(1,10)
        
    def loop(self, steps=10):
        """Ejecuta el número especificado de pasos."""
        [self.step() for i in xrange(steps)]

    def step(self):
        """Avanza un paso t -> t+1."""
        self.dinamicaArena()