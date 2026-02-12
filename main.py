from time import sleep

def linha(txt):
    print("~"* len(txt))

def tempo():
    sleep(0.2)
    
def contador(inicio, fim, passo):
    print(f"Contagem de {inicio} até {fim}, de {passo} em {passo}.")
    tempo()
    if passo == 0:
        passo = 1

    if inicio > fim and passo > 0:
        passo = -passo
    
    for i in range(inicio, fim + (1 if passo > 0 else -1), passo):
        tempo()
        print(i, end=' ')
    print()

def contagem_personalizada():
  
    print("Contangem Personalizada...")
    while True:
      
        try:
            inicio = int(input("Início: "))
            fim = int(input("Fim: "))
            passo = int(input("Passo: "))
            contador(inicio, fim, passo)
            tempo()
            break
        except ValueError:
            print("Erro, Digite apenas número interiros.")
            
    
def deseja_sair():

    while True:

            print("""1. sim    2. Não""")
            perguta = input("Deseja continuar? ")

            if perguta == '1':
                return False
            elif perguta == '2':
                print("Programa se encerrando")
                return True
            else:
                print("Opção Invalida!!! Digite 1 ou 2")

def tela_principal():

    titulo = '    CONTAGEM DE NÚMEROS   '
    
    linha(titulo)
    print(titulo)
    linha(titulo)
    

    contador(1, 10, 1)
    linha(titulo)
    contador(10, 0, 2)
    linha(titulo)
    
        
    while True:
        contagem_personalizada()
        linha(titulo)
        if deseja_sair():
            break
        linha(titulo)




tela_principal()
