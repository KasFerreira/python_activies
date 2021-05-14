#Abrir todos arquivos, o f no modo leitura e os outros de escrita
todosips =open('myfile.txt')
ipinvalidos=open('inv.txt','w')
ipvalidos=open('val.txt','w')



#Função para avaliar se o ip é valido
def ip_ok(linha):
    linha = linha.split('.')  
    for x in linha:
        if int(x) > 255:
           return False
    return True

for linha in todosips.readlines():
    
    if ip_ok(linha):
        ipvalidos.write(linha)
             
    else:
        ipinvalidos.write(linha)
         
               
ipvalidos.close()               
ipinvalidos.close()
            
todosips.close()

    # if int(nLinha) > 255:
    #     #    inv.writelines('.'.join(nLinha))
    #     #    inv.writelines('\n')
    #        print(nLinha)
    #        continue
      