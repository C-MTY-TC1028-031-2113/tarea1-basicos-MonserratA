#def main():
    #escribe tu código abajo de esta línea
def calcular_saldofinal():
    saldodelmesanterior= float(input("Dame el saldo del mes anterior: "))
    ingresos= float(input("Dame los ingresos: "))
    egresos= float(input("Dame los egresos: "))
    cheques= int (input("Dame el número de cheques: "))
    saldofinal= (saldodelmesanterior+ingresos-egresos-cheques*13)
    saldof= (saldofinal*7.5/100)
    total= (saldofinal-saldof)
    
    print("El saldo final de la cuenta es: " + str(total))

calcular_saldofinal()