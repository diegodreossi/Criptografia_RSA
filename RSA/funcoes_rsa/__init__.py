import random as rd

def leiaInt(msg):
    num = 0
    passar = False
    while True:
        n = input(f'{msg}')
        if n.isnumeric() == True:
          num = int (n)
          passar = True
        else:
          print('\033[0;31mErro! Digite um numero inteiro válido.\033[')  

        if passar:
           break  
    return num

def num_primo(msg):
  divisores = 0
  primo = False

  while primo == False:
     numero = leiaInt(f"{msg}")

     for i in range(1,numero + 1):
        if numero % i == 0:
            divisores += 1

     if divisores == 2:
     
        primo = True
        
      
     else:
        print('\033[0;31mErro! Numero Não primo.\033[')  
        primo = False
     divisores = 0   


       
  return numero




def mdc(num1,num2):
    while (num2 != 0):
       r = num1 % num2
       num1 = num2
       num2 = r
    return num1    

def chave_publica(n):   
    #Aleatorio
    while True:
      e = rd.randint(2,n) 
      if(mdc(n,e) == 1):
         return e
         #break

def chave_privada(z,e):
    d = 0
    while((d * e) % z != 1): 
      d += 1
    return d     

def criptografar(msg,n,e):
    msg_cript = "" #Mensagem criptografada  
    for letra in msg:
        if letra == " ":
           msg_cript += " "
        else:   
           cr = (ord(letra)**e ) % n  
           msg_cript += chr(cr) 

    return msg_cript 

def descriptografar(msg,n,d):
    msg_desc = "" #Mensagem descriptografada
    for letra in msg:
        dc = (ord(letra) ** d ) % n 
        msg_desc += chr(dc)  

    return msg_desc


def rsa_criptografador(acp,arq):
   """
   acp é o arquivo para onde vai a chave privada
   arq é para onde vai a mensagem criptografada
   """
   msg = "Programa"
   msg = input('Digite uma mensagem para criptografar: ')
   p = num_primo("(p) Digite um numero inteiro primo: ")
   q = num_primo("(q) Digite um numero inteiro primo: ")
   n = p * q
   z = (p - 1) * (q - 1)   
   e = chave_publica(z)

   print(f"Chave Publica: ({e},{n})")

   d = chave_privada(z,e)

   print(f"Chave Privada: ({d},{n})")
 
   
   arqacp = open(acp,"w") # w é o método que escreve por cima
   vc = [] #valores pra chave privada
   vc.append(str(d)+'\n')
   vc.append(str(n)+'\n')
   
   arqacp.writelines(vc)

   msg = criptografar(msg,n,e)
   print("Mensagem criptografada: " + msg)


   arquivo = open(arq,"w") # w é o método que escreve por cima
   arquivo.write(msg)

   msg = descriptografar(msg,n,d)
   print("Mensagem descriptografada: " + msg)

   

def rsa_descriptografador(arq,arq2):
   """
   arq para a mensagem codificada
   arq2 para mostrar a chave privada
   """
   arq = "/content/drive/MyDrive/Colab Notebooks/RSA/mensagem.txt"
   arquivo = open(arq,"rt") # w é o método que escreve por cima
   msm = ""
   for linha in arquivo:
       msm = linha
   print(f"Mensagem a decodificar: {msm}")

   arquivo2 = open(arq2,"rt")
 
   cp = []
   for linha in arquivo2:
        cp.append(int(linha.split('\n')[0]))
  
   d = cp[0]
   n = cp[1]

   print(f"Mensagem descriptografada: {descriptografar(msm,n,d)}")