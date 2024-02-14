def inverter_string(string):
    string_invertida = ""

    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]

    return string_invertida

while True:
    string_original = input("Digite uma string para inverter (ou digite 'sair' para encerrar): ")

    if string_original.lower() == 'sair':
        print("Encerrando o programa...")
        break

    string_invertida = inverter_string(string_original)

    print("String original:", string_original)
    print("String invertida:", string_invertida)