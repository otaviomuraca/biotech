#a = GAGCCTACTAACGGGAT
#b = CATCGTAATGACGGCCT
#Output 7

def dna(file):
    with open(file, "r") as f:
        a = f.readline()
        b = f.readline()

    return a, b

def pontosMutacao(a:str, b:str) -> int:
    resultado = 0
    contador = 0
    tamanho_a = len(a)

    while contador != tamanho_a:
        if a[contador] == b[contador]:
            pass
        else:
            resultado += 1

        contador += 1

    return print(int(resultado))

file = "files/dna.txt"

a,b = dna(file)

pontosMutacao(a,b)
