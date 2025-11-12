import random
elementos = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
elementosplus = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
tamanho = int(input("Digite o tamanho da senha: "))
abc = input("A senha deve ter caractéres especiais? ")
if abc == "Sim":
    choiced = elementosplus
if abc == "Não":
    choiced = elementos
senha = ""
for i in range(tamanho):
    senha += random.choice(choiced)

print("Senha gerada:", senha)