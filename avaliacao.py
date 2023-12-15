#funcao1
conta = {
    'saldo': 125,
    'senha': 12, 
}
print('saldo 1', conta ['saldo'])
print('senha 1', conta ['senha']) 

#funcao2

senha = input("me informe sua senha: ")

try:
    if conta in conta and senha(senha) == conta[conta]:
        print("Login Bem Sucedido!")
    else:
        print("Usuário ou Senha Incorreta. Tente Novamente!")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

#funcao3
saldo= input("me informe seu saldo")
def menu_caixa_eletronico (self):
    print("Verficar saldo")
if saldo== 125:
    print("saldo correto")
else:
    print("deu merda nego")
