class incendioForestal:
    
    def __init__(self,L):
        self.bosque=np.ones((L,L))
        self.p=0.7
    
   def muere(self,aux,i,j):
    # Esta función cumple que el arbol muera si se esta quemando.

        if self.bosque[i,j]==2:
            aux[i,j] = 0
        else:
            aux[i,j] = self.bosque[i,j]

        return aux[i,j]
    
    def revive(self,aux,i,j):
    # Esta función determina si el arbol revive de manera aleatoria. 
    # La probabilidad de revivir esta dada por p.

        if self.bosque[i,j] == 0 and 0.01*randint(0,100)<=self.p: #por que no random.random()
            aux[i,j]= 1
        else:
            aux[i,j] = self.bosque[i,j]

        return aux[i,j]
    
    def fuego(self,aux,i,j): #vecinos
        if bosque[i,j+1]==2 or bosque[i+1,j+1]==2 or bosque[i+1,j]==2 or bosque[i-1,j]==2 or bosque[i,j-1]==2 or bosque[i-1,j-1]==2 or bosque[i+1,j-1]==2 or bosque[i-1,j+1]:
            aux[i,j] = 2                      
        else: 
            aux[i,j] = 1

        return aux[i,j]

    
    def incendio(self):
    """
    esto es un solo paso, una sola unidad de tiempo
    """
        aux =np.zeros((self.L,self.L))
    
        for i in xrange(1,self.L-1):
            for j in xrange(1,self.L-1):
                if bosque[i,j]==1:
                    fuego(aux,i,j,)
                elif bosque[i,j]==2:
                    muere(aux,i,j)
                elif bosque[i,j]==0:
                    revive(aux,i,j)
                    
        self.bosque=aux
    
    def loop(self, steps=10):
        """Ejecuta el número especificado de pasos."""
        [self.step() for i in xrange(steps)]

    def step(self):
        """Avanza un paso t -> t+1."""
        self.incendio()