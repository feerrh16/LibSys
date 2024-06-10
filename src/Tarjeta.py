from logger_base import *


class Tarjeta:
    def __init__(self, num_tarjeta=None, id_cliente=None, cvv=None, fecha_vencimiento=None, banco=None):
        self._num_tarjeta = num_tarjeta
        self._id_cliente = id_cliente
        self._cvv = cvv
        self._fecha_vencimiento = fecha_vencimiento
        self._banco = banco

    def __str__(self):
        return f'''
                Numero de Tarjeta: {self._num_tarjeta}
                ID Cliente: {self._id_cliente}
                CVV: {self._cvv}
                Fecha de Vencimiento: {self._fecha_vencimiento}
                Banco: {self._banco}
                '''

    @property
    def num_tarjeta(self):
        return self._num_tarjeta

    @num_tarjeta.setter
    def num_tarjeta(self, num_tarjeta):
        self._num_tarjeta = num_tarjeta

    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self._id_cliente = id_cliente

    @property
    def cvv(self):
        return self._cvv

    @cvv.setter
    def cvv(self, cvv):
        self._cvv = cvv

    @property
    def fecha_vencimiento(self):
        return self._fecha_vencimiento

    @fecha_vencimiento.setter
    def fecha_vencimiento(self, fecha_vencimiento):
        self._fecha_vencimiento = fecha_vencimiento

    @property
    def banco(self):
        return self._banco

    @banco.setter
    def banco(self, banco):
        self._banco = banco


if __name__ == '__main__':
    tarjeta = Tarjeta(543527364591827, 457876, 577, '23/12/29', 'Santander')
    log.debug(tarjeta)

    # Simular un INSERT INTO
    tarjeta = Tarjeta(num_tarjeta=5354435634522345, id_cliente=233, cvv=332, fecha_vencimiento='24/01/24',
                      banco='Santander')
    log.debug(tarjeta)

    # Simular un DELETE
    tarjeta1 = Tarjeta(num_tarjeta=552673872771972)
    log.debug(tarjeta)
