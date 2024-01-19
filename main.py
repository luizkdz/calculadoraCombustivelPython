from calculo import Calculo

def main():
    calc = Calculo()

    print("O programa tem a finalidade de informar os valores gastos de 3 combustíveis")

    print("Os combustíveis disponíveis para este cálculo são:")
    print("\t° Álcool")
    print("\t° Díesel")
    print("\t° Gasolina")

    print(" ")
    try:
        distanciaInformada = float(input("Digite o valor da distancia "))
        consumoInformado = float(input(("Digite o valor do consumo em KM/L ")))

        calc.calcularValoresGastos(distanciaInformada,consumoInformado)
    except ValueError as Erro:
        print("Os valores informados não são válidos")

if __name__ == "__main__":
    main()