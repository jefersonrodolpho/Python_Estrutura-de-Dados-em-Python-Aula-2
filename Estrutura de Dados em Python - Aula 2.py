####  ####  ####     ##   #### #     #
   #  #__   #__      / #  #__   #   #
#  #  #     #   --- /  #  #      # #
 ##   ####  #       ###   ####    #

#### Cálculo de Média referente as notas das Provas 
def ValorLista():
    for i in range(1,5):
        list.append(int(input(f'Digite o valor da sua prova {i}')))

def Media():
    s=0
    for i in range(len(list)):
        s = s+ list[i]
    m= s / 4
    return m

list = []
ValorLista()
m= Media()
print(m)



#### Modelo de Busca Sequencial em uma lista (pode ser utilizado para qualquer tipo de lista)
## Faz uma busca completa em toda lista
def BuscaSeq(list, item):
    pos = 0
    x = False

    while pos<len(list) and not x:
        if list[pos]== item:
            x= True
        else:
            pos = pos +1
    return x


lista = [5,6,8,12,1,5,7]
print(BuscaSeq(lista, 8))
print(BuscaSeq(lista, 13))

#### Modelo de Busca Binária em uma lista (só pode ser utilizado em lista ordenada) * esta é uma busca mais complexa
## Faz uma busca digidindo a lista ao meio e vai dividindo as sublistas ao meio até encontrar o valor

def BuscaBin(list, item):
    prim = 0 #variavel com primeiro elemento da lista iniciado em 0
    ult = len(list) - 1 #ultimo elemento da lista -1 
    found= False 

    while prim <= ult and not found:
        meio = (prim + ult) // 2
        if list[meio] == item:
            found = True
        else:
            if item < list[meio]:
                ult = meio - 1
            else:
                prim = meio + 1
    return found

lista = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(BuscaBin(lista, 3))
print(BuscaBin(lista, 13))


##### Não são recomendados para grandes estruturas
#### Bubble Sort: Percorrer o vetor várias vezes, a cada passagem fazer a troca para o topo o maior/menor elemento da sequencia
#### Selection Sort: Este Algoritmo seleciona em cada iteração um elemento para ser inserido na sequencia ordenada produzida
#### Insertion Sort: Ordena os elementos inserindo-os na posiçlão correta. Os elementos são divididos em duas regições, ordenados e ainda não ordenados
## Veja um exemplo com Bubble Sort implementado

def bubbleSort(list):
    n = len(lista)
    for j in range(n - 1):
        for i in range(n - 1):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                print(list)

lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(lista)
print(lista)



##### Recomendados para grandes estruturas
#### MergeSort: Utiliza a estratégia de divisão e conquista;
### - Divide recursivamente a sequencia ao meio;
### - Ao chegar a uma subsequencia unitaria, esta encontra-se ordenada
### - A partir desse ponto, intercale gradativamente subsequencias ordenadas, gerando subsequencias ordenada de maior tamanho;
### - Termine ao intercalar a sequencia original;
#### QuickSort: Utiliza a estratégia de divisão e conquista;
### - Escolha de um elemento: Pivô;
### - Rearranja a lista, aonde todos os elementos anteriores ao pivô sejam menores e os elementos posteriores ao pivô sejam maiores;
### - Recusrivamente ordena as sequencias esquerda e direita do pivô;
## Veja um exemplo com o QuickSort

def executar_quicksort(lista, inicio, fim):
    if inicio < fim:
        pivo = executar_particao(lista, inicio, fim)
        executar_quicksort(lista, inicio, pivo - 1)
        executar_quicksort(lista, pivo + 1, fim)
    return lista

def executar_particao(lista, inicio, fim):
    pivo = lista[fim]
    esquerda = inicio
    for direita in range(inicio, fim):
        if lista[direita] <= pivo:
            lista[direita], lista[esquerda] = lista[esquerda], lista[direita]
            esquerda += 1
    lista[esquerda], lista[fim] = lista[fim], lista[esquerta]
    return esquerda


#### EXERCÍCIO

aluno = dict()

aluno['nome'] = str(input('Nome:'))
aluno['media'] = float(input('Media:'))

if aluno['media'] >= 7:
    aluno['situacao'] = "aprovado"

else: 
    aluno['situacao'] = "reprovado"

for x, y in aluno.items():
    print(f'-{x} é igual a {y}')

print(aluno.keys())
print(aluno.values())