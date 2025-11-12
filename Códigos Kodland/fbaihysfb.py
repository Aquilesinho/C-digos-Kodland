import random
restart = "Sim"
lista = ["0","1","2","3","4","5","6","7","8","9"]
while restart == "Sim":
    a = random.choice(lista)
    b = random.choice(lista)
    c = random.choice(lista)
    print(a+b+c)
    if a == b == c:
        print("Você venceu com",a+b+c+"!!!")
    else:
        print("Você perdeu...")
    restart = input("Deseja jogar novamente? ")