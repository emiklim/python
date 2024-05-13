class Cliente ():
    
    def __init__(self, nombre, apellido, edad, dni):

        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni

    def __str__(self):
        return f"Hola, me llamo {self.nombre} {self.apellido} y tengo {self.edad} años.\n"

    def demanda(self, prod, tipo_caja, cant):
        print(f"Quiero comprar {cant} {tipo_caja} de {prod}.\n")

    def metodo_pago(self):
        while True:
            print("Seleccione el número de su método de pago:\n1: Efectivo\n2: Tarjeta de débito\n3: Tarjeta de crédito\n4: Transferencia Bancaria")
            try:
                metodo_pago = int(input("Elija su método de pago: "))
                if metodo_pago == 1:
                    return print("Usted ha elegido pagar con efectivo.\n")
                elif metodo_pago == 2:
                    return print("Usted ha elegido pagar con tarjeta de débito.\n")
                elif metodo_pago == 3:
                    return print("Usted ha elegido pagar con tarjeta de crédito.\n")
                elif metodo_pago == 4:
                    return print("Usted ha elegido pagar con transferencia bancaria.\n")
                else:
                    print("Método de pago incorrecto, por favor, intente nuevamente.\n")
            except ValueError:
                print("Debe elegir una opción numérica válida.\n")