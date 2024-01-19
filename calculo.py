class Calculo:

    def __init__(self):
        self.__valorAlcool = 3
        self.__valorDiesel = 4
        self.__valorGasolina = 5

    def calcularValoresGastos(self, distancia,consumo):
        if(distancia <=0 or consumo <=0):
            raise Exception("Os valores informados são inválidos")
        else:
            valorGastoGasolina = round((distancia / consumo) * self.__valorGasolina, 2)
            valorGastoDiesel = round((distancia / consumo) * self.__valorDiesel, 2)
            valorGastoAlcool = round((distancia / consumo) * self.__valorAlcool, 2)
            print("""
            O VALOR GASTO COM A GASOLINA FOI DE R$: {}
            O VALOR GASTO COM O DIESEL FOI DE R$: {}
            O VALOR GASTO COM O ALCOOL FOI DE R$: {}""".format(
            valorGastoGasolina,valorGastoDiesel,valorGastoAlcool))
