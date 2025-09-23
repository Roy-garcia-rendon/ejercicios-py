class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # atributo privado

    def depositar(self, monto):
        self.__saldo += monto

    def ver_saldo(self):
        return self.__saldo


cuenta = CuentaBancaria(100)
cuenta.depositar(50)
print(cuenta.ver_saldo())  # 150
