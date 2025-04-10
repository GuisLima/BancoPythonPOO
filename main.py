from abc import ABC

class Conta:
    def __init__(self, cliente, numero):
        self._cliente = cliente
        self._numero = numero
        self._agencia = '0001'
        self._saldo = 0
        self._historico = Historico()

    # Funções de retorno para atributos encapsulados
    @property
    def cliente(self):
        return self._cliente
        
    @property
    def numero(self):
        return self._numero
        
    @property
    def agencia(self):
        return self._agencia
        
    @property
    def saldo(self):
        return self._saldo
        
    @property
    def historico(self):
        return self._historico

    # Método de fábrica
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)
        
    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo

        if excedeu_saldo:
            print("Operação falhou! Excedeu o limite de saques diários")
        
        elif self.saldo > 0:
            self._saldo -= valor
            print("Operação realizada com sucesso")
            return True
        
        else:
            print("Operação falhou! Valor inválido")

        return False


    def depositar(self, valor):
        try:
            if valor > 0:
                self._saldo += valor
                print(f"Valor: {valor} depositado com sucesso!")

            else:
                print("Valor necessita ser positivo")
                return False
            
            return True
            
        except TypeError as exc:
                print(f"Ocorreu um erro! {exc}")
                


class ContaCorrente(Conta):
    def __init__(self, cliente, numero):
        super().__init__(cliente, numero)
        self._limite = 500
        self._limite_saques = 3

    def sacar(self):
        pass



class Cliente:
    pass

class PessoaFisica(Cliente):
    pass

# Interface
class Transacao(ABC):
    pass

class Deposito(Transacao):
    pass

class Saque(Transacao):
    pass

class Historico:
    pass




