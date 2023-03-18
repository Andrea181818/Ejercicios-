#Pregunta N°1
__name__=='__main__'

#Pregunta N°2
class Producto:
    def __init__(self, nombre):
        self.nombre = nombre
        print("Se agrego el producto ", self.nombre)
        print("")

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(f"producto: {producto.nombre}")

#Ejemplo
catalogo = Catalogo()

producto1 = Producto("Llanta")
catalogo.agregar_producto(producto1)

producto2 = Producto("Bujía")
catalogo.agregar_producto(producto2)

catalogo.mostrar_productos()

#Pregunta N°3
import modulos_N3 as mod

mod.dividir(10,2)

#Pregunta N°4
class Producto:
    def __init__(self, nombre,pais,lote,anio):
        self.nombre = nombre
        self.pais = pais.upper()
        self.lote = lote
        self.anio = anio
        print("Se agrego el producto ", self.nombre, f"codigo: {self.pais}-{self.lote}-{self.anio}")
        print("")
    def __str__(self):
        return (f'producto: {self.nombre}, Codigo: {self.pais}-{self.lote}-{self.anio} con pais de origen: {self.pais} y lote {self.lote}')

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

#Ejemplo
catalogo = Catalogo()

producto1 = Producto("Muñecas","Brasil","0001",2014)
catalogo.agregar_producto(producto1)

producto2 = Producto("Pelotas", "Chile", "0045",2020)
catalogo.agregar_producto(producto2)

catalogo.mostrar_productos()

#Pregunta N°5
import os

catalogo = Catalogo()
while(True):
    try:
        producto3 = Producto("Mesas","Argentina","0004",2019)
        catalogo.agregar_producto(producto3)
    except:
        print("Ha ocurrido un error, introduce bien el producto")
    else:
        print(os.getcwd())
        break
    finally:
        print("Proceso terminado")

#Pregunta N°6
class Product:
    id=""
    nombre=""
    precio=""
    tipo=""
    stock=""
    release=""
    def __init__(self,id,nombre,precio,tipo,stock,release) -> None:
        self.id=id
        self.nombre=nombre
        self.precio=precio
        self.tipo=tipo
        self.stock=stock
        self.release=release
        pass
    def __str__(self) -> str:
        return f"el producto {self.nombre} con {self.id}  de {self.precio} cuenta con {self.stock} stock"
    def updateStock(self,stock):
        self.stock=stock
    
class CarritoCompra:
    def __init__(self):
        self.listaProductos=[]
        self.precioTotal=0
    def agregarProducto(self,product:Product,cantidad=1):
        if self.validarStock(product):
            print("agregando producto")
            self.listaProductos.append(product)
            product.updateStock(product.stock-1)
        else:
            print("el producto no tienen stock")
         
    def quitarProdcut(self,product,id):
        print("Quitando producto")
        self.listaProductos.remove(product)
        product.updateStock(product.stock+1)
    def calcularPrecio(self):
        for i in self.listaProductos:
            self.precioTotal+=i.precio
        print(self.precioTotal)
    def validarStock(self,product:Product):
        existe=False
        if product.stock>0:
            existe=True
        return existe
    def mostrarProductos(self):
        print(len(self.listaProductos))
        if len(self.listaProductos)>0:
            for i in self.listaProductos:
                print(i)
        else:
            print("carrito vacio")

message="""
    1)Agregar Producto
    2)Mostrar Productos
    3)Quitar Producto
    4)Salir
"""
id=0
carrito=CarritoCompra()
while True:

    print(message)
    opcion=int(input("ingrese la opcion a realizar:"))
    if opcion==1:
        try:
            id=id+1
            name=input("ingrese el nombre del producto:")
            precio=float(input("ingrese el precio del producto:"))
            tipo=input("ingrese el tipo del prodcuto:")
            stock=int(input("ingrese el stock del prodcuto:"))
            release=int(input("ingrese el release del prodcuto:"))
            px=Product(id,name,precio,tipo,stock,release)
            carrito.agregarProducto()
        except Exception as Error:
                print("sucedio un error")
        else:
            print("agregando en el menu")
    if opcion==2:
        carrito.mostrarProductos()
        carrito.precioTotal
    if opcion == 3:
        carrito.quitarProdcut()
    if opcion==4:
        break

#Pregunta N°7

##usar modulos
## manejo de errores
## clases -> pacientes ,doctores(especialidades),agenda
#from lib.users import Pacientes,Doctores


### registrar doctores -> menu iteractio
## registar sus horarios
## ver sus horarios
## registramos pacientes-> menu iteractio

##logica de enviar solicitud

especialidad="" # input
## mostrar horarios de doctores por especialiadad 
hora=""         #input