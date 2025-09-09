import os
import pyaes
import sys 

# Nome do arquivo a para descriptografar
file_name_encrypted = "teste.txt.ransomwaretroll"

key = b"testeransomwares"

## --- LÓGICA 

# 1. Verificar exitencia do arquivo
if not os.path.exists(file_name_encrypted):
    print(f"ERRO: O arquivo '{file_name_encrypted}' não foi encontrado no diretório atual.")
    sys.exit(1)

try:
    print(f"Lendo o arquivo criptografado: {file_name_encrypted}")
  
    with open(file_name_encrypted, "rb") as file:
        file_data = file.read()

    print("Descriptografando os dados...")
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)
  
    new_file_name = "teste.txt"

    # 5. Criar e escrever no novo arquivo no lugar do descriptografado
    print(f"Salvando o conteúdo descriptografado em: {new_file_name}")
    with open(new_file_name, "wb") as new_file:
        new_file.write(decrypt_data)

    # 6. Remover o arquivo criptografado APENAS se tudo deu certo até aqui
    os.remove(file_name_encrypted)

    print("\nSUCESSO! Arquivo descriptografado e o original removido.")

except Exception as e:
    # Captura erros
