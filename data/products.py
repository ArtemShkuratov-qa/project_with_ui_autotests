from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: str
    add_id: str
    remove_id: str
    #id: str


t_shirt = Product(
    name='Sauce Labs Bolt T-Shirt',
    price='15.99',
    add_id='#add-to-cart-sauce-labs-bolt-t-shirt',
    remove_id='#remove-sauce-labs-bolt-t-shirt'
    #id='#item_4_title_link'
)

fleece_jacket = Product(
    name='Sauce Labs Fleece Jacket',
    price='49.99',
    add_id='#add-to-cart-sauce-labs-fleece-jacket',
    remove_id='#remove-sauce-labs-fleece-jacket'
    #id='#item_0_title_link'
)

bike_light = Product(
    name='Sauce Labs Bike Light',
    price='$9.99',
    add_id='#add-to-cart-sauce-labs-bike-light',
    remove_id='#remove-sauce-labs-bike-light'
)

