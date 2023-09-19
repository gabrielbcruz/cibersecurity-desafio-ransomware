import os
import pyaes

def main():
    # Abrir o arquivo criptografado
    file_name = "teste.txt.ransomwaretroll"
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

    # Descriptografar os dados
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)

    # Salvar o arquivo descriptografado
    new_file_name = input("Nome do arquivo descriptografado: ")
    new_file = open(f'{new_file_name}', "wb")
    new_file.write(decrypt_data)
    new_file.close()

if __name__ == "__main__":
    main()
