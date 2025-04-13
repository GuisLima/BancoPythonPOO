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
            print("\nOperação falhou! Você não possui saldo o suficiente")
        
        elif self.saldo > 0:
            self._saldo -= valor
            print("\nOperação realizada com sucesso! Valor sacado: R$ {valor}")
            return True
        
        else:
            print("\nOperação falhou! Valor inválido")

        return False


    def depositar(self, valor):
        try:
            if valor > 0:
                self._saldo += valor
                print(f"\nValor: {valor} depositado com sucesso!")

            else:
                print("\nValor necessita ser positivo")
                return False
            
            return True
            
        except TypeError as exc:
                print(f"\nOcorreu um erro! {exc}")
                


class ContaCorrente(Conta):
    def __init__(self, cliente, numero):
        super().__init__(cliente, numero)
        self._limite = 500
        self._limite_saques = 3

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transcao["tipo" == Saque.__name__]])

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\nOperação falhou! Excedeu o limite de R$ 500,00 reais diários")
        
        elif excedeu_saques:
            print("\nOperação falhou! VocÊ excedeu o limite de saques diários")
        
        else:
            return super().sacar(valor)

        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Cliente:
    def __init__(self, endereco):
        self_endereco = endereco
        self._contas = []

    @property
    def endereco(self):
        return self._endereco
    
    @property
    def contas(self):
        return self._contas

    def realizar_transcao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

# Interface
class Transacao(ABC):
    pass

class Deposito(Transacao):
    pass

class Saque(Transacao):
    pass

class Historico:
    pass




