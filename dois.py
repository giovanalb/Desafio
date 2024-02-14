def verifica_fibonacci(numero):
    fibonacci = [0, 1]
    while fibonacci[-1] < numero:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if numero in fibonacci:
        return True
    else:
        return False

while True:
    numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci (ou digite 0 para sair): "))
    if numero == 0:
        print("Encerrando o programa...")
        break
    if verifica_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")