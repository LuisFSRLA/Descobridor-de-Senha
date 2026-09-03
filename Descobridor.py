
Senha= input("Informe a senha: ")
alfabeto_junto = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
Numero=['123456789']
caracteres=['!@#$%^&*()_+-=[]{}|;:",./<>?']
Senhafatiada=[]

for elements in Senha:
     if elements == str:
           elements.lower()
     Senhafatiada.append(elements)
Tentativa=0
TentativaDeSenha=[]
for elements in Senha:
    if elements in alfabeto_junto:    
        for x in range(len(alfabeto_junto)):
            if elements not in alfabeto_junto:
                    break
            elif elements==alfabeto_junto[x]:
                TentativaDeSenha.append(alfabeto_junto[x])
                print(TentativaDeSenha)
            Tentativa +=1
    elif elements in caracteres:    
            for z in range(len(caracteres)):
                if elements not in caracteres:
                        break
                elif elements==caracteres[z]:
                    TentativaDeSenha.append(caracteres[z])
                    print(TentativaDeSenha)
                Tentativa +=1
    elif elements in Numero:
        for y in range(len(Numero)):
            if elements not in Numero:
                 break
            elif elements==Numero[y]:
                        TentativaDeSenha.append(Numero[y])
                        print(TentativaDeSenha)
            Tentativa +=1
    
        

    
print(f"Demorou {Tentativa} Tentativas")
print(f"Senha fatiada: {Senhafatiada} ")
print(f"Senha Achada: {TentativaDeSenha} ")