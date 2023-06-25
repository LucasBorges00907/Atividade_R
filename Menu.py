import random
def main():

    print ('''
    [1]  Gerar vetor N posições, ou com valor padrão
    [2]  Preencher vetor manualmente item a item
    [3]  Preencher vetor automaticamente
    [4]  Mostrar vetor
    [5]  Transformar vetor: elevar a potência N
    [6]  Contar: Positivos, Negativos e Zeros
    [7]  Somatório: De todos, Dos Negativos e dos Positivos
    [8]  Exibir Média e Mediana: De Todos, Dos Positivos e Dos Negativos
    [9]  Exibir Maior e Menor número
    [10] Sortear dois números: um positivo e um negativo
    [11] Gerar N grupos de T tamanhos. Não repetir valores
    [12] Pedir um novo vetor e verificar se está 100% presente nos números do sistema (e na mesma ordem)
    [13] Top N maiores números
    [14] Top N menores números
    [15] Listar valor médio, e listar números maiores que a Média e Menores que a Média
    [16] Somatório da Média dos Números Positivos múltiplos dois COM o Produto acumulado dos números negativos pares reduzidos à metade
    [17] Ordenar os números em ordem crescente: 
    [18] Ordenar em ordem decrescente
    [19] Eliminar números múltiplos de N e M (simultaneamente)
    [0]  Sair do programa ''' )
            
    opcao = int(input("Qual a sua opção? "))
    vetor_principal=[]

    while opcao!=0:
        if opcao == 1:
            print("Pressione 1 para gerar vetor com um valor padrão e 2 para um vetor com valor indefinido: ")
            escolha = int(input("Qual a sua escolha? "))
            if escolha == 1:
                posicoes = int(input("Quantidade de posições do vetor: "))
                valorpadraovetor = int(input("Valor padrão do vetor: "))
                vetor_principal = [valorpadraovetor]*posicoes
                print(vetor_principal)
                opcao = int(input("Qual a sua opção? "))
            elif escolha == 2:
                posicoes = int(input("Quantidade de posições do vetor: "))
                vetor_principal = [None]*posicoes
                print(vetor_principal)
                opcao = int(input("Qual a sua opção? "))     
        if opcao == 2:
            vetor_principal = preecher_vetor_manualmente(vetor_principal)
            print (vetor_principal)
            opcao = int(input("Qual a sua opção? "))
        if opcao == 3:
            vetor_principal = preencher_valor_automaticamente(vetor_principal)
            print (vetor_principal)
            opcao = int(input("Qual a sua opção? "))
        if opcao == 4:
            print(vetor_principal)
            opcao = int(input("Qual a sua opção? "))
        if opcao == 5:
            vetor_principal = elevar_a_potencia_n(vetor_principal) 
            print(vetor_principal)
            opcao = int(input("Qual a sua opção? "))
        if opcao == 6:
            contar_positivos_negativos_e_zeros(vetor_principal)
            opcao = int(input("Qual a sua opção? "))
        if opcao == 7:
            somar_positivos_negativos_e_zeros(vetor_principal)
            opcao = int(input("Qual a sua opção? "))
        if opcao == 8:
            positivos = dividir_positivos(vetor_principal)
            negativos = dividir_negativos(vetor_principal)
            media_vetorcompleto = calcular_media_do_vetor(vetor_principal)
            media_positivos = calcular_media_do_vetor(positivos)
            media_negativos = calcular_media_do_vetor(negativos)
            print(f"Média do vetor completo: {media_vetorcompleto:.2f}") 
            print(f"Média dos positivos: {media_positivos:.2f}")
            print(f"Média negativos: {media_negativos:.2f}")
            vetor_principal = ordenar_vetor(vetor_principal)
            print (f"Vetor principal ordenado: {vetor_principal}")
            mediana = definir_mediana(vetor_principal)
            print(f"A mediana do vetor principal é: {mediana}")

            positivos = ordenar_vetor(positivos)
            print(f"Vetor dos positivos ordenados: {positivos}") 
            mediana_positivos = definir_mediana(positivos)
            print(f"A mediana do Vetor dos positivos é: {mediana_positivos}")

            negativos = ordenar_vetor(negativos)
            print(f"Vetor dos negativos ordenados: {negativos}") 
            mediana_negativos = definir_mediana(negativos)
            print(f"A mediana do Vetor dos negativos é: {mediana_negativos}")
            opcao = int(input("Qual a sua opção? "))
        if opcao == 9:
            maior = maior_do_vetor(vetor_principal)
            menor  = menor_do_vetor(vetor_principal)
            print(f"Maior: {maior}")
            print(f"Menor: {menor}")
            opcao = int(input("Qual a sua opção? "))
        if opcao == 10:
            positivos = dividir_positivos(vetor_principal)
            negativos = dividir_negativos(vetor_principal)

            positivo_sorteado = sortear_positivo(positivos)
            print(f"Positivo sorteado: {positivo_sorteado}")
            
            negativo_sorteado = sortear_negativo(negativos)
            print(f"Negativo sorteado: {negativo_sorteado}")
            opcao = int(input("Qual a sua opção? "))
        if opcao == 11:
            numero_grupos = int(input("Digite o número de grupos: "))
            tamanho = int(input("Digite o tamanho dos grupos: "))
            gerar_n_grupos_de_t_tamanhos(vetor_principal,numero_grupos,tamanho)
            opcao = int(input("Qual a sua opção? "))
        if opcao == 12:
            vetor_em_string = input("Digite os elementos do vetor separados por vírgulas: ")
            vetor_novo = list(map(int,vetor_em_string.split(",")))
            if verificar_ordem_vetor(vetor_principal,vetor_novo):
                print("Sim, o vetor digitado está 100% presente nos números do sistema (e na mesma ordem)")
            else:
                print("Não, o vetor digitado não está 100% presente nos números do sistema (e na mesma ordem)")
            opcao = int(input("Qual a sua opção? "))
        if opcao == 13:
            n = int(input("Deseja ver quantos dos maiores números do vetor? "))
            top_n = top_n_maiores_numeros(vetor_principal,n)
            print(f"Top n maiores números do vetor: {top_n}")
            opcao = int(input("Qual a sua opção? "))
        if opcao == 14:
            n = int(input("Deseja ver quantos dos menores número do vetor? "))
            top_n_menores = top_n_menores_numeros(vetor_principal,n)
            print(f"Top n menores números do vetor: {top_n_menores}")
            opcao = int(input("Qual a sua opção? "))
        if opcao == 15:
            media = calcular_media_do_vetor(vetor_principal)
            acima = acima_da_media(vetor_principal,media)
            abaixo = abaixo_da_media(vetor_principal,media)

            print(f"Média dos itens do vetor: {media}")
            print(f"Itens acima da média: {acima}")
            print(f"Itens abaixo da média: {abaixo}")
            opcao = int(input("Qual a sua opção? "))
        if opcao == 16:
            positivos = dividir_positivos(vetor_principal)
            positivos_pares = item_eh_par(positivos)
            media = calcular_media_do_vetor(positivos_pares)
            negativos = dividir_negativos(vetor_principal)
            produto = produto_metade_negativos_pares(negativos)
            soma = media + produto 
            print (f"Media: {media}")
            print(f"Produto: {produto}")
            print(f"O resultado da soma é: {soma}")
            opcao = int(input("Qual a sua opção? "))
        if opcao == 17:
            vetor_principal = ordenar_vetor(vetor_principal)
            print(f"O vetor em ordem crescente é: {vetor_principal}")
            opcao = int(input("Qual a sua opção? "))
        if opcao == 18: 
            vetor_principal = vetor_em_ordem_decrescente(vetor_principal)
            print(f"O vetor em ordem decrescente é: {vetor_principal} ")
            opcao = int(input("Qual a sua opção? "))
        if opcao == 19:
            n = int(input("Digite n(para eliminar seus múltiplos do vetor): "))
            m = int(input("Digite m(para eliminar seus múltiplos do vetor): "))
            vetor_principal = eliminar_multiplos_de_n(vetor_principal,n)
            vetor_principal = eliminar_multiplos_de_m(vetor_principal,m)
            print (f"Tirando os múltiplos dos números digitados, seu vetor fica: {vetor_principal}")
            opcao = int(input("Qual a sua opção? "))
        if opcao == 0:
            print("Finalizando .... Atividade boa demais:D <3")

             



            
            

        

        
        







def preencher_valor_automaticamente(vetor_principal):
    tamanho = len(vetor_principal)
    vetor = []
    contador = 1
    minimo = int(input("Digite o valor mínimo do vetor: "))
    maximo = int(input("Digite o valor máximo do vetor: "))
    while contador<=tamanho:
        valor = random.randint(minimo, maximo)
        vetor.append(valor)
        contador = contador + 1
    vetor_principal = vetor
    return vetor_principal

def mostrar_vetor(vetor_principal):
    print(vetor_principal) 

def preecher_vetor_manualmente(vetor_principal):
    vetor = []
    tamanho = len(vetor_principal)
    contador = 1
    while contador<=tamanho:
        novo_item = int(input("Digite o próximo valor do vetor: "))
        vetor.append(novo_item)
        contador = contador+1
    vetor_principal = vetor
    return vetor_principal
    

def elevar_a_potencia_n(vetor_principal):
    n = int(input("Digite o expoente: "))
    vetor = []
    for i in vetor_principal:
        termo = i**n
        vetor.append(termo)
    vetor_principal = vetor
    return vetor_principal


def contar_positivos_negativos_e_zeros(vetor_principal):
    positivos = 0
    negativos = 0
    zeros = 0

    for i in vetor_principal:
        if i>0:
            positivos = positivos + 1
        elif i<0:
            negativos = negativos + 1
        else:
            zeros = zeros + 1

    print("Positivos:", positivos)
    print("Negativos:", negativos)
    print("Zeros:", zeros)

def somar_positivos_negativos_e_zeros(vetor_principal):
    positivos = 0
    negativos = 0
    zeros = 0

    for i in vetor_principal:
        if i>0:
            positivos = positivos + i
        elif i<0:
            negativos = negativos + i
        else:
            zeros = zeros + i

    print(f"Soma dos positivos: {positivos}")
    print(f"Soma dos negativos: {negativos}")
    print(f"Soma dos zeros: {zeros}")


def exibir_maior_e_menor_numero(vetor_principal):
    maior = vetor_principal[0]
    menor = vetor_principal[0]

    for i in vetor_principal:
        if i> maior:
            maior = i
        elif i<menor:
            menor = i

    print (f"O maior número do vetor é: {maior}")
    print (f"O menor número do vetor é: {menor}")


def ordenar_vetor(vetor_principal):
    n = len(vetor_principal)
    for i in range(n):
        for j in range(i+1, n):
            if vetor_principal[j] < vetor_principal[i]:
                vetor_principal[i], vetor_principal[j] = vetor_principal[j], vetor_principal[i]
    return vetor_principal


def dividir_positivos(vetor_principal):
    positivos = []
    for i in vetor_principal:
        if i > 0:
            positivos.append(i)
    return positivos


def calcular_media_do_vetor(vetor):
    soma = 0
    if vetor == []:
       media = 0
       return media
    else:
        for i in vetor:
            soma = soma + i
        media = soma/len(vetor)
        return media

def dividir_negativos(vetor_principal):
    negativos = []
    for i in vetor_principal:
        if i < 0:
            negativos.append(i)
    return negativos

def definir_mediana(vetor_principal):
    if vetor_principal == []:
        return "Vetor Vazio!"
    tamanho_vetor = len(vetor_principal)
    if tamanho_vetor%2 == 0:
        mediana = (vetor_principal[(tamanho_vetor//2)-1] + vetor_principal[tamanho_vetor//2])/2
    else:
        mediana = (vetor_principal[int((tamanho_vetor/2) - 0.5)])

    return mediana

def maior_do_vetor(vetor_principal):
    maior = vetor_principal[0]
    if vetor_principal == []:
        return "O seu vetor é vazio"
    else:
        for i in vetor_principal:
            if i > maior:
                maior = i
    return maior

def menor_do_vetor(vetor_principal):
    menor = vetor_principal[0]
    if vetor_principal == []:
        return "O seu vetor é vazio"
    else:
        for i in vetor_principal:
            if i < menor:
                menor = i
    return menor


def sortear_positivo(positivos):
    if positivos == []:
        return " Não há números positivos no seu vetor! "
    else:
        for i in positivos:
            indice_sorteado = random.randint(0,len(positivos)-1)
            numero_sorteado = positivos[indice_sorteado]
            return numero_sorteado
        
def sortear_negativo(negativos):
    if negativos == []:
        return " Não há número negativos no seu vetor! "
    else:
        for i in negativos:
            indice_sorteado = random.randint(0,len(negativos)-1)
            numero_sorteado = negativos[indice_sorteado]
    return numero_sorteado


def verificar_vetor(vetor_principal,vetor_novo):
    for item in vetor_novo:
        if item not in vetor_principal:
            return False
        return True


def verificar_ordem_vetor(vetor_principal,vetor_novo):
    if verificar_vetor:
        i = 0
        for j in range(len(vetor_principal)):
            if vetor_novo[i] == vetor_principal[j]:
             i = 1 + 1
            if i == len(vetor_novo):
                return True
    return False


def top_n_maiores_numeros(vetor_principal,n):
    if n > len(vetor_principal):
        return "O número digitado é maior que o número de posições do vetor!"
    else:
        top_n = []
        vetor_principal = ordenar_vetor(vetor_principal)
        primeiro_index = len(vetor_principal) - n
        for i in range(primeiro_index,len(vetor_principal)):
            top_n.append(vetor_principal[i])
        return top_n
    
def top_n_menores_numeros(vetor_principal,n):
    if n > len(vetor_principal):
        return "O número digitado é maior que o número de posições do vetor!"
    else:
        top_n_menores = []
        vetor_principal = ordenar_vetor(vetor_principal)
        for i in range(0,n):
            top_n_menores.append(vetor_principal[i])
        return top_n_menores
    
def calcular_media_do_vetor(vetor_principal):
    soma = 0
    for item in vetor_principal:
        soma = soma + item
    media = soma/len(vetor_principal)
    return media


def acima_da_media(vetor_principal,media):
    acima_da_media = []
    for item in vetor_principal:
        if item >= media:
            acima_da_media.append(item)
    return acima_da_media


def abaixo_da_media(vetor_principal,media):
    abaixo_da_media = []
    for item in vetor_principal:
        if item < media:
            abaixo_da_media.append(item)
    return abaixo_da_media


def item_eh_par(positivos):
    positivos_pares = []
    for item in positivos:
        if item%2 == 0:
            positivos_pares.append(item)
    return positivos_pares


def produto_metade_negativos_pares(negativos):
    produto = 1
    if negativos == []:
        return 0
    else:
        for item in negativos:
            if item%2 == 0:
                metade = item/2
                produto = produto*metade
                 

def calcular_media_do_vetor(positivos_pares):
     if len(positivos_pares) == 0:
        return 0
     else:
        soma = 0
        tamanho = len(positivos_pares)
        for item in positivos_pares:
            soma = soma+item
        media = soma/tamanho
        return media


def vetor_em_ordem_decrescente(vetor_principal):
    n = len(vetor_principal)
    for item in range(n):
        for j in range(item+1,n):
            if vetor_principal[j]>vetor_principal[item]:
                vetor_principal[item],vetor_principal[j] = vetor_principal[j],vetor_principal[item]
    return vetor_principal


def eliminar_multiplos_de_n(vetor_principal,n):
    vetor_sem_multiplos_de_n = []
    for item in vetor_principal:
         if item%n != 0:
            vetor_sem_multiplos_de_n.append(item)
    vetor_principal = vetor_sem_multiplos_de_n
    return vetor_principal

def eliminar_multiplos_de_m(vetor_principal,m):
    vetor_sem_multiplos_de_n = []
    for item in vetor_principal:
         if item%m != 0:
            vetor_sem_multiplos_de_n.append(item)
    vetor_principal = vetor_sem_multiplos_de_n
    return vetor_principal

main()