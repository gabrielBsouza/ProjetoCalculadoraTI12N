import this
import soma
import subtracao
import multiplicacao
import divisao
import tabuada
import vetores
this.opcao = 0 #Crio variável global
num1 = 0
num2 = 0

def coletarNum1():
    print('Informe o primeiro número')
    this.num1 = float(input())

def coletarNum2():
    print('Informe o primeiro número')
    this.num2 = float(input())

def mostrarMenu():
    print('Escolha uma das opções abaixo\n' +
          '\n1. Soma'+
          '\n2. Subtração'+
          '\n3. Multiplicação'+
          '\n4. Divisão'+
          '\n5. Tabuada' +
          '\n6. Sair')
    this.opcao = int(input()) #Coletar a digitação do usuário

def operacao():
    #Mostrar o menu em tela
    while this.opcao != 5:
        mostrarMenu()
        #realizar operações
        if this.opcao == 1:
            #operacao para a soma
            coletarNum1()
            coletarNum2()
            soma.somar(this.num1, this.num2)
        elif this.opcao == 2:
            #operacao para a subtração
            coletarNum1()
            coletarNum2()
            subtracao.subtrair(this.num1, this.num2)
        elif this.opcao == 3:
            #operacao para a multiplicacao
            coletarNum1()
            coletarNum2()
            multiplicacao.multiplicar(this.num1, this.num2)
        elif this.opcao == 4:
            #operacao para a divisao
            coletarNum1()
            coletarNum2()
            divisao.dividir(this.num1, this.num2)
        elif this.opcao == 5:
            #operacao para a tabuada
            coletarNum1()
            coletarNum2()
            print(tabuada.calcularTabuada(int(this.num1), int(this.num2)))
        elif this.opcao == 6:
            #operação para vetores
            vetores.mostrarVetor()
        elif this.opcao == 7:
            print('Obrigado!')
        else:
            print('Opcao escolhida inválida! Tente novamente com as opções fornecidas.')