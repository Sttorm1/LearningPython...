#ih papai, um gerador de senhas

import random
import string
# random é obviamente pra geração de caracteres aleatorios, e string pra ter letras maiusculas e minusculas
def gerar_senha(tamanho=12):
    #def define a função, =12 é caso nenhum numero for especificado após solicitar o tamanho para o usuario, então o padrão é 12
    caracteres = string.ascii_letters + string.digits 
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha
#string.ascii_letters é letra maiuscula e minuscula, e o digits são os digitos

def main():
    #o main chama a função gerar_senha e mostra a senha gerada
    tamanho = int(input("digite o tamanho da senha:"))
    senha = gerar_senha(tamanho)
    print(f"sua senha gerada é: {senha}")
    
    #aqui pede o tamanho da senha, 