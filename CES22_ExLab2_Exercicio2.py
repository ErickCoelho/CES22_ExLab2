from abc import ABC, abstractmethod

class Acao(ABC): #Command

    @abstractmethod
    def execute(self):
        pass


class VerificarSaldo(Acao): #Concrete Command

    def __init__(self, banco):
        self.banco = banco
    
    def execute(self):
        self.banco.verificar()
        print("seu saldo.\n")


class VerificarExtrato(Acao): #Concrete Command

    def __init__(self, banco):
        self.banco = banco
    
    def execute(self):
        self.banco.verificar()
        print("seu extrato.\n")


class RelizarTransferencia(Acao): #Concrete Command

    def __init__(self, banco):
        self.banco = banco
    
    def execute(self):
        self.banco.realizar()
        print("uma transferencia.\n")


class Banco: #Receiver

    def verificar(self):
        print("Voce esta verificando")

    def realizar(self):
        print("Voce esta realizando")


class Cliente: #Invoker

    def __init__(self):
        self.__acao_quee = []

    def acao_bancaria(self, acao):
        self.acao = acao
        acao.execute()

banco = Banco()
verificar_saldo = VerificarSaldo(banco)
verificar_extrato = VerificarExtrato(banco)
realizar_transferencia = RelizarTransferencia(banco)

cliente = Cliente()
cliente.acao_bancaria(verificar_saldo)
cliente.acao_bancaria(verificar_extrato)
cliente.acao_bancaria(realizar_transferencia)