print("informe qual o veiculo dentre as opcoes vc pode escolher carro, moto e bike")

distancia= float(input("qual a distancia para o destino"))
veiculo= str(input("moto, bike e carro escolha apenas um veiculo"))

if veiculo == "moto":
    custo= distancia * 0.20
    print("o valor é:",custo)

elif veiculo == "carro":
    custo= distancia * 0.50
    print("o valor é:",custo)

elif veiculo == "bike":
    custo= distancia * 0.50
    print("o valor é:",custo)


