'''

from decimal import Decimal 
from django.conf import settings 
from ecom.models import Product 

class Cart():
    def __init__(self,request):
        self.session=request.session
        cart=self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart=self.session[settings.CART_SESSION_ID]={}
        self.cart=cart 
        
    def add(self,product,quantity=1):
        product_id=str(product.id)#retreve prudct id 
        if product_id not in self.cart:#check if product is in cart 
            self.cart[product_id]={'quantity':0,#create the product
                                   'price':str(product.price)}
       # if override_quantity:
        self.cart[product_id]['quantity']=int(quantity)
        #else:
         #   self.cart[product_id]['quantity']+=quantity#updateng the product quantity
        self.save() #mdoifiy the cart
        
    def save(self):
        self.session.modified=True
        
        
    def remove(self,product):
        product_id=str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()
        
    def __iter__(self):
        product_ids=self.cart.keys()
        products=Product.objects.filter(id__in=product_ids)
        cart=self.cart.copy()
        for product in products:
            cart[str(product.id)]['product']=product
        for item in cart.values():
            item['price']=Decimal(item['price'])
            item['total_price']=Decimal(item['price'])*item['quantity']
            yield item 
        
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

                
    def get_sub_total_price(self):
    
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())


'''

from decimal import Decimal
from django.conf import settings
from ecom.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity']=int(quantity)# Ensure quantity is integer
        else:
            self.cart[product_id]['quantity']=int(quantity)# Convert to integer
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = item['price']  # Ensure price is Decimal
            item['total_price'] = float(item['price'])* int(item['quantity'])  # Correct calculation
            yield item

    def __len__(self):
        return sum(int(item['quantity']) for item in self.cart.values())

    def get_sub_total_price(self):
        return sum(float(item['price']) * int(item['quantity']) 
                           for item in self.cart.values())

    def clear(self):
        self.cart = {}
        self.save()
