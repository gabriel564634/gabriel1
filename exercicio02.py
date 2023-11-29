idade= 18
status= False

if idade >= 18:
    print ("usuario e maior de ", idade)
    status= True
 
else:
  
    print ("usuario é menor de idade")
    status= False 
 
print (idade, status)

#elif faz a pergunta direta pro if para verificar   

idade= 18
status= False

if idade >= 18:
  
    print ("usuario e maior de ", idade)
elif idade <18:
    print ("usuario é menor de ", idade)

print (idade, status)