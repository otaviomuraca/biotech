#n <= 40 meses
#k <= 5 reprodução
# Fn= Fn−1 + Fn−2
# Saida = 19

def coelhos(n:int, k:int):
    
    contador = 0

    while contador == 0:
        if (n <=40) and (k <=5):
            contador = 1
        else:
            print("Valores fora de limite.")
            break

    while contador == 1:
        lista = []
        lista.append(1)
        lista.append(1)

        for i in range(2,n):
            formula = lista[-1] + lista[-2] * k
            lista.append(formula)

        print(lista[-1]) 
        contador = 2

coelhos(36, 5)
