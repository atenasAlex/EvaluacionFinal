from api.models import Producto

class Cart():
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart


    def add(self, producto, quantity):
        producto_codigo = str(producto.codigo)
        producto_qty = str(quantity)

        if producto_codigo in self.cart:
            pass
        else:
            #self.cart[producto_codigo] = {'precio': str(producto.precio)}
            self.cart[producto_codigo] = int(producto_qty)

        self.session.modified = True





    def cart_total(self):
        producto_ids = self.cart.keys()
        productos = Producto.objects.filter(codigo__in = producto_ids)
        quantities = self.cart

        total = 0
        producto_ids = self.cart.keys()
        productos = Producto.objects.filter(codigo__in=producto_ids)

        total = sum(producto.precio * self.cart[str(producto.codigo)] for producto in productos)
    
        return total

        # for key, value in quantities.items():
        #     key = int(key)
        #     for producto in productos:
        #         if producto.codigo == key:
        #             total += (producto.price * value)
        # return total



    def __len__(self):
        return len(self.cart)
    

    def get_prods(self):
        producto_ids = self.cart.keys()
        productos = Producto.objects.filter(codigo__in = producto_ids)

        return productos
    

    def get_quants(self):
        quantities = self.cart
        return quantities



    def delete(self, producto):
        producto_codigo = str(producto)
        if producto_codigo in self.cart:
            del self.cart[producto_codigo]

        self.session.modified = True


