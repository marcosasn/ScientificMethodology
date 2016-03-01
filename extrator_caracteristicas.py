import sys
arquivo_saida = sys.argv[3]
nome_arquivo = sys.argv[1]
caminho_pasta = sys.argv[2]
f = open(str(caminho_pasta)+"/"+ nome_arquivo)
email = f.read()
tem_link = "<a" in email
tamanho = len(email)
f.close()

#f = open("/home/lucasmlm/Downloads/CSDMC2010_SPAM/CSDMC2010_SPAM/SPAMTrain.label")
#label = int(filter(lambda x : nome_arquivo in x, f.read().split("\n"))[0].split(' ')[0])
#f.close()

f = open(arquivo_saida, "a")
f.write(str(tem_link) + "," + str(tamanho) + "\n")
f.close()
