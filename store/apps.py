from django.apps import AppConfig


class StoreConfig(AppConfig):
    name = 'store'


#Need tp add more



class CartConfig(AppConfig):
    name = 'cart'

class CheckoutConfig(AppConfig):
    name = 'checkout'

class MainConfig(AppConfig):
    name = 'main'