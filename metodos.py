# -*- coding: utf-8 -*-

class MetodoDePago:
    def cobrar(self):
        pass

class Stripe(MetodoDePago):
    """
        Esta clase es la encargada de cobrar con Stripe.
        implementa la interfaz de Método de pago.
    """

    token = 'asdfghjk'
    correo ='asdf@sdfgh.com'

    @classmethod
    def cobrar(cls, cantidad):
        '''
        Esta es la funcion que cobra
        '''
        
        # Hice todos los metodos necesarios para cobrar
        print('cobré con stripe %s' % cantidad)
    @staticmethod
    def un_metodo_statico():


class Efectivo(MetodoDePago):
    def cobrar(self, cantidad):
        print('Envié correo al cliente para que prepre el dinero')

class Bitcoin(MetodoDePago):
    def cobrar(self, cantidad):
        print('Cobré %s bitcoins' % cantidad)
