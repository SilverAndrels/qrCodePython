import qrcode
print("Olá, este é um gerador de qrCode!")
link = input("Cole aqui o link: ")
imagem = qrcode.make(link)
nome = input("Nome do qr e extenção: ")
imagem.save(nome)