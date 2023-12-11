import user

usuarios = {
    "gabriel": "00",  # Substitua pelos hashes reais
    "menino": "01",
    "menina": "02"
}

def hash_senha(senha):
    # Use uma função de hash segura, como hashlib, para armazenar senhas de forma segura.
    return user.sha256(senha.encode('utf-8')).hexdigest()

usuario = input("Escreva seu Usuário: ")
senha = input("Escreva sua Senha: ")

try:
    if usuario in usuarios and hash_senha(senha) == usuarios[usuario]:
        print("Login Bem Sucedido!")
    else:
        print("Usuário ou Senha Incorreta. Tente Novamente!")
except Exception as e:
    print(f"Ocorreu um erro: {e}")