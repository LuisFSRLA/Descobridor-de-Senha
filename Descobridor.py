
senha = input("Informe a senha: ")
alfabeto = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
caracteres_especiais = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '[', ']', '{', '}', '|', ';', ':', '', '"', ',', '.', '/', '<', '>', '?']
senha_fatiada = []

for elemento in senha:
     if elemento == str:
           elemento.lower()
     senha_fatiada.append(elemento)
tentativas = 0
tentativa_de_senha = []
for elemento in senha:
    if elemento in alfabeto:
        for indice in range(len(alfabeto)):
            if elemento not in alfabeto:
                    break
            elif elemento == alfabeto[indice]:
                tentativa_de_senha.append(alfabeto[indice])
                print(tentativa_de_senha)
            tentativas += 1
    elif elemento in caracteres_especiais:
            for indice in range(len(caracteres_especiais)):
                if elemento not in caracteres_especiais:
                        break
                elif elemento == caracteres_especiais[indice]:
                    tentativa_de_senha.append(caracteres_especiais[indice])
                    print(tentativa_de_senha)
                tentativas += 1
    elif elemento in numeros:
        for indice in range(len(numeros)):
            if elemento not in numeros:
                 break
            elif elemento == numeros[indice]:
                        tentativa_de_senha.append(numeros[indice])
                        print(tentativa_de_senha)
            tentativas += 1
    
        

    
print(f"Demorou {tentativas} Tentativas")
print(f"Senha fatiada: {senha_fatiada} ")
print(f"Senha Achada: {tentativa_de_senha} ")