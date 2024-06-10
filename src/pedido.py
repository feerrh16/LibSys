from asyncio import log
from logger_base import * 

class pedido:
    def __init__(self, id_Proveedor = None, ISBN = None, Fecha_Pedido = None,
                 Fecha_Entrega = None, Cantidad_Pedida = None, Precio_Total = None):
        self._id_Proveedor = id_Proveedor
        self._ISBN = ISBN
        self._Fecha_Pedido = Fecha_Pedido
        self._Fecha_Entrega = Fecha_Entrega
        self._Cantidad_Pedida = Cantidad_Pedida
        self._Precio_Total = Precio_Total

    def __str__(self):
        return  f'''
                ID Proveedor: {self._id_Proveedor}
                ISBN: {self._ISBN}
                Fecha_Pedido = {self._Fecha_Pedido}
                Fecha_Entrega: {self._Fecha_Entrega}
                Cantidad_Pedida: {self._Cantidad_Pedida}
                Precio_Total: {self._Precio_Total}
                '''
    
    @property
    def id_Proveedor(self):
        return self._id_Proveedor
    
    @id_Proveedor.setter
    def id_Proveedor(self, id_Proveedor):
        self._id_Proveedor = id_Proveedor

    @property
    def ISBN(self):
        return self._ISBN

    @ISBN.setter
    def ISBN(self, ISBN):
        self._ISBN = ISBN

    @property
    def Fecha_Pedido(self):
        return self.Fecha_Pedido
    
    @Fecha_Pedido.setter
    def Fecha_Pedido(self, Fecha_Pedido):
        self._Fecha_Pedido = Fecha_Pedido

    @property
    def Fecha_Entrega(self):
        return self._Fecha_Entrega
    
    @Fecha_Entrega.setter
    def Fecha_Entrega(self, Fecha_Entrega):
        self._Fecha_Entrega = Fecha_Entrega

    @property
    def Cantidad_Pedida(self):
        return self._Cantidad_Pedida
    
    @Cantidad_Pedida.setter
    def Cantidad_Pedida(self, Cantidad_Pedida):
        self._Cantidad_Pedida = Cantidad_Pedida
    
    @property
    def Precio_Total(self):
        return self._Precio_Total
    
    @Precio_Total.setter
    def Precio_Total(self, Precio_Total):
        self._Precio_Total = Precio_Total

if __name__ == '__main__':
    pedido1 = pedido(1, '05762', '03/03/02', '04/03/02', 2, '$290')
    log.debug(pedido1)

    # Simular un INSERT INTO
    pedido1 = pedido(id_Proveedor= 1, ISBN= '05762', Fecha_Pedido= '03/03/02', Fecha_Entrega= '04/03/02', 
                        Cantidad_Pedida= '2', Precio_Total='$290')
    log.debug(pedido1)

    #Simular un DELETE
    pedido1 = pedido(id_Proveedor=1)
    log.debug(pedido1)

