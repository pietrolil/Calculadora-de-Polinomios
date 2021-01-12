import math

def main():
    vezes = int(input("Numero de vezes que quer rodar o programa"))
    for i in range(vezes):
        escolha = int(input("1 . Calcular o valor do polinomio"
                        "\n2 . Somar dois polinomios"
                        "\n3 . Multiplicar dois polinomios"
                        "\n4 . Encerrar"))
    
        while escolha >= 5 or escolha <= 0:
            escolha = int(input("Digite um numero valido"))

    
        if escolha == 1:
            calcular()
        if escolha == 2:
            soma()
        if escolha == 3:
            multi()
        if escolha == 4:
            break



def calcular():
    grau = int(input("Digite o grau = "))
    while grau > 100 or grau < 0:
        grau = int(input("Digite um grau valido"))

    vetor = [0] * (grau+1)


    for i in range(0,grau+1):
                 
        vetor[i] = int(input("Coeficiente de menor para maior = "))

    string_polinomio = ''

    for j in range(grau+1,0,-1):
        if j < len(vetor)+1 and j > 0 :
            string_polinomio = string_polinomio + "+" + str(vetor[j-1]) + 'x^' + str(j-1) + ''
        else:
            string_polinomio = string_polinomio + "+" + str(vetor[j]) + 'x^' + str(j) + ''

    print("P(x) =",string_polinomio)

    
    x = int(input("Digite o valor da incognita do polinomio"))
    valor = 0
    for h in range(grau+1,0,-1):
        if h <= len(vetor)+1 and h >=0:
            valor = valor + (vetor[h-1])*pow(x,h-1)



 
    print(valor)    


def soma():
    print("Digite o maior grau primeiro")
    grau1 = int(input("Digite o grau do primeiro polinomio = "))
    while grau1 > 100 or grau1 < 0:
        grau1 = int(input("Digite um grau valido"))
    vetor1 = [0] * (grau1+1)
    for i in range(0,grau1+1):
        vetor1[i] = int(input("Coeficiente de menor para maior = "))
    string_polinomio1 = ''

    for j in range(grau1+1,0,-1):
        if j < len(vetor1)+1 and j > 0 :
            string_polinomio1 = string_polinomio1 + "+" + str(vetor1[j-1]) + 'x^' + str(j-1) + ''
        else:
            string_polinomio1 = string_polinomio1 + "+" + str(vetor1[j]) + 'x^' + str(j) + ''


    grau2 = int(input("Digite o grau do segundo polinomio = "))
    while grau2 > 100 or grau2 < 0:
        grau2 = int(input("Digite um grau valido"))
    if grau1 == grau2:
        vetor2 = [0] * (grau2+1)


        for i in range(0,grau2+1):
                 
            vetor2[i] = int(input("Coeficiente = "))

        string_polinomio2 = ''

        for j in range(grau2+1,0,-1):
            if j < len(vetor2)+1 and j > 0 :
                string_polinomio2 = string_polinomio2 + "+" + str(vetor2[j-1]) + 'x^' + str(j-1) + ''
            else:
                string_polinomio2 = string_polinomio2 + "+" + str(vetor2[j]) + 'x^' + str(j) + ''

    
        print("P(x) =",string_polinomio1)
        print("P(x) =",string_polinomio2)

    
        vetor3 = [0] * (grau1+1)
        for h in range(0,grau1+1):
            vetor3[h] = vetor1[h] + vetor2[h]

        string_polinomio3 = ''

        for d in range(grau1+1,0,-1):
            if d < len(vetor3)+1 and d > 0 :
                string_polinomio3 = string_polinomio3 + "+" + str(vetor3[d-1]) + 'x^' + str(d-1) + ''
            else:
                string_polinomio3 = string_polinomio3 + "+" + str(vetor3[d]) + 'x^' + str(d) + ''
        
        print("P(x) =",string_polinomio3)

    elif grau1 > grau2:
        dif = grau1-grau2
        vetor2 = [0] * ((grau2+1)+dif)


        for i in range(0,(grau2+1)+dif):
                 
            vetor2[i] = int(input("Coeficiente de menor para maior = "))

        string_polinomio2 = ''

        for j in range(grau2+1,0,-1):
            if j < len(vetor2)+1 and j > 0 :
                string_polinomio2 = string_polinomio2 + "+" + str(vetor2[j-1]) + 'x^' + str(j-1) + ''
            else:
                string_polinomio2 = string_polinomio2 + "+" + str(vetor2[j]) + 'x^' + str(j) + ''

    
        print("P(x) =",string_polinomio1)
        print("P(x) =",string_polinomio2)

    
        vetor3 = [0] * (grau1+1)
        for h in range(0,grau1+1):
            vetor3[h] = vetor1[h] + vetor2[h]

        string_polinomio3 = ''

        for d in range(grau1+1,0,-1):
            if d < len(vetor3)+1 and d > 0 :
                string_polinomio3 = string_polinomio3 + "+" + str(vetor3[d-1]) + 'x^' + str(d-1) + ''
            else:
                string_polinomio3 = string_polinomio3 + "+" + str(vetor3[d]) + 'x^' + str(d) + ''
        
        print("P(x) =",string_polinomio3)

def multi():
    print("Digite o maior grau primeiro")
    grau1 = int(input("Digite o grau do primeiro polinomio = "))
    while grau1 > 100 or grau1 < 0:
        grau1 = int(input("Digite um grau valido"))
    vetor1 = [0] * (grau1+1)
    for i in range(0,grau1+1):
        vetor1[i] = int(input("Coeficiente de menor para maior = "))
    string_polinomio1 = ''

    for j in range(grau1+1,0,-1):
        if j < len(vetor1)+1 and j > 0 :
            string_polinomio1 = string_polinomio1 + "+" + str(vetor1[j-1]) + 'x^' + str(j-1) + ''
        else:
            string_polinomio1 = string_polinomio1 + "+" + str(vetor1[j]) + 'x^' + str(j) + ''


    grau2 = int(input("Digite o grau do segundo polinomio = "))
    while grau2 > 100 or grau2 < 0:
        grau2 = int(input("Digite um grau valido"))
    if grau1 == grau2:
        vetor2 = [0] * (grau2+1)


        for i in range(0,grau2+1):
            
                 
            vetor2[i] = int(input("Coeficiente = "))

        string_polinomio2 = ''

        for j in range(grau2+1,0,-1):
            if j < len(vetor2)+1 and j > 0 :
                string_polinomio2 = string_polinomio2 + "+" + str(vetor2[j-1]) + 'x^' + str(j-1) + ''
            else:
                string_polinomio2 = string_polinomio2 + "+" + str(vetor2[j]) + 'x^' + str(j) + ''

    
        print("P(x) =",string_polinomio1)
        print("P(x) =",string_polinomio2)

    

    elif grau1 > grau2:
        dif = grau1-grau2
        vetor2 = [0] * ((grau2+1)+dif)


        for i in range(0,(grau2+1)+dif):
                 
            vetor2[i] = int(input("Coeficiente de menor para maior = "))

        string_polinomio2 = ''

        for j in range(grau2+1,0,-1):
            if j < len(vetor2)+1 and j > 0 :
                string_polinomio2 = string_polinomio2 + "+" + str(vetor2[j-1]) + 'x^' + str(j-1) + ''
            else:
                string_polinomio2 = string_polinomio2 + "+" + str(vetor2[j]) + 'x^' + str(j) + ''

    
        print("P(x) =",string_polinomio1)
        print("P(x) =",string_polinomio2)

    grau3 = (grau1+1) + (grau2)
    for i in range((grau3)+1,0,-1):
        vetor3 = [0] * (grau3)
        for j in range(grau3+1,0,-1):
            vetor3[j] = vetor1[j-i] * vetor2[j-i]


    print(vetor3)

main()