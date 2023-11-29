usuario = input("digite seu nome:")
print("ola", usuario)
idade = int (input("digite sua idade"))
print(idade)

if idade < 13:
    print ("usuario é criança")

elif 13<= idade <18 :
    print("usuario é adolescente: ")

elif 18<= idade <60: 
    print ("usuario é adulto:")

elif idade >= 60:
    print ("usuario é coroa: ")