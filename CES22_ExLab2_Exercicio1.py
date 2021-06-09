class Pizza(): #Componente

    def getDescription(self):
        return self.__class__.__name__

    def getTotalCost(self):
        return self.__class__.cost


class Massa(Pizza): #Componente Concreto
    cost = 0.0


class Decorator(Pizza): #Decorador

    def __init__(self, Pizza):
        self.component = Pizza

    def getDescription(self):
        return self.component.getDescription() + ' ' + Pizza.getDescription(self)

    def getTotalCost(self):
        return self.component.getTotalCost() + Pizza.getTotalCost(self)


class Mussarela(Decorator): #Decorador Concreto
    cost = 30.0
    def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)


class Milho(Decorator): #Decorador Concreto
    cost = 27.0
    def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)


class Marguerita(Decorator): #Decorador Concreto
    cost = 35.0
    def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)


class Calabresa(Decorator): #Decorador Concreto
    cost = 40.0
    def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)


class Atum(Decorator): #Decorador Concreto
    cost = 20.0
    def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)



aleatoria  = Mussarela(Atum(Calabresa(Massa())))
print(aleatoria.getDescription() + ' - R$' + str(aleatoria.getTotalCost()))