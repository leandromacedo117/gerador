import random
num = "1234567890"
sim = ["!@#$&?"]
letras = "abcdefghijklmnopqrstuvwxyz"


senhaLetras = input("deseja criar senha com letras ? ")
senhaNum = input("deseja criar senha com números ? ")
senhaSim = input("deseha criar senha com símbolos ? ")
quantidade = int(input("quantidade de caracteres"))

senha = [num, sim, letras]
senhaList = random.choice(senha)
password = "".join(random.sample(senha ,quantidade))
print(password)
def gerarSenha():
    

    if "não" and "sim" and "sim" :
        senha.pop(0)
       
    elif "sim" and "não" and "sim":
        senha.pop(1)
    elif "sim" and "sim" and "não":
        senha.pop(2)
    elif "não" and "não" and "sim":
        senha.pop(0,1)
    elif "não" and "sim" and "não":
        senha.pop(0,2)
    elif "sim" and "não" and "não":
        senha.pop(1,2)
    elif "sim" and "sim" and "sim":
        senha.pop()
    
  

    
    
gerarSenha()
     


 



