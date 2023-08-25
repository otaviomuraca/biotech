#>Rosalind_6404
#CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
#TCCCACTAATAATTCTGAGG

file = "files/file.fasta"

def fasta(file):
    dicionario = {}
    chave = ""
    conteudo = ""
    lista = []

    with open(file, 'r') as f:
        for linha in f:
            linha = linha.strip()
            lista.append(linha)
        
        for i in lista:
            if i:
                if i[0] == ">":
                    #rotulo
                    chave = i[1:]
                    conteudo = ""

                else:
                    #conteudo
                    conteudo = "".join(conteudo + i)
                    
                dicionario[chave] = conteudo
            
        return dicionario


def frequencia(dicionario:dict):
    #freq Absoluta GC
    for i in dicionario:
        conteudo = dicionario[i]

        contador_total = len(conteudo)
        contador_gc = 0

        for l in conteudo:
            if (l == "C") or (l == "G"):
                contador_gc += 1

        #freq relativa %
        fre_relativa = round((contador_gc / contador_total) * 100,6)
        dicionario[i] = fre_relativa

    resultado = max(dicionario, key = dicionario.get)

    print(resultado)
    print(dicionario[resultado])
        

frequencia(fasta(file))
