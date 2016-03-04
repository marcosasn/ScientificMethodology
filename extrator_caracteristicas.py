import sys

nome_arquivo = sys.argv[1]
caminho_pasta = sys.argv[2]
arquivo_saida = sys.argv[3]

f = open(str(caminho_pasta)+"/"+ nome_arquivo)
email = f.read()
tem_link = "<a" in email
tamanho = len(email)
f.close()

f = open("labels.label")
label = int(filter(lambda x : nome_arquivo in x, f.read().split("\n"))[0].split(' ')[0])
f.close()
f = open(arquivo_saida, "a")
if (tem_link):
    link = "1"
else:
    link = "0"
f.write(str(label) + " " + "1:"+ link + " " + "2:"+str(tamanho) + "\n")
f.close()
