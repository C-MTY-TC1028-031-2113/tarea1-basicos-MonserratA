#def main():
    #escribe tu código abajo de esta línea
def kilos_por_mes():
    pesoinicial= float(input("Dame el peso inicial: "))
    pesofinal= float(input("Dame el peso final: "))
    meses= int(input("Dame la cantidad de meses: "))
    bajarpormes= (pesoinicial - pesofinal)/meses
    
    print("Lo que debes bajar por mes es: " + str(bajarpormes))
    
kilos_por_mes()
