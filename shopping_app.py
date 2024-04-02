from ownable import Ownable
from customer import Customer
from item import Item
from seller import Seller

seller = Seller("TIENDA DIC ")
for i in range(10):
    Item("CPU", 40830, seller)
    Item("MEMORIA", 13880, seller)
    Item("TARJETA MADRE", 28980, seller)
    Item("UNIDAD DE FUENTE DE ALIMENTACION", 8980, seller)
    Item("GABINETE", 8727, seller)
    Item("3.5DISCO DURO HDD", 10980, seller)
    Item("2.5DISCO DURO HDD", 13370, seller)
    Item("M.2 SSD", 12980, seller)
    Item("CPU ENFRIADOR", 13400, seller)
    Item("TABLERO GRAFICO", 23800, seller)

print("🤖 POR FAVOR DIME TU NOMBRE")
customer = Customer(input())

print("🏧 POR FAVOR INGRESA EL MONTO A CARGAR EN TU BILLETERA")
customer.wallet.deposit(int(input()))

print("🛍️ EMPIEZA A COMPRAR")
end_shopping = False
while not end_shopping:
    print("📜 LISTA DE PRODUCTOS")
    seller.show_items()

    print("️️⛏ POR FAVOR INGRESE NUMERO DEL PRODUCTO")
    number = int(input())

    print("⛏ POR FAVOR INGRESE LA CANTIDAD DEL PRODUCTO")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 CONTENIDO DEL CARRITO")
    customer.cart.show_items()
    print(f"🤑 CANTIDAD TOTAL: {customer.cart.total_amount()}")

    print("😭 QUIERES TERMINAR DE COMPRAR? (yes/no)")
    end_shopping = input() == "yes"

print("💸 CONFIRMAR TU COMPRA? (yes/no)")
if input() == "yes":
    customer.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈RESULTADO┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️{customer.name}PROPIEDAD DE")
customer.show_items()
print(f"😱👛 {customer.name}SALDO DE BILLETERA DE: {customer.wallet.balance}")

print(f"📦 {seller.name}ESTADO DEL INVENTARIO")
seller.show_items()
print(f"😻👛 {seller.name}SALDO DE BILLETERA DE: {seller.wallet.balance}")

print("🛒 CONTENIDO DEL CARRITO")
customer.cart.show_items()
print(f"🌚 CANTIDAD TOTAL: {customer.cart.total_amount()}")

print("🎉 FIN")
