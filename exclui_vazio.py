import os

# Diretório contendo as imagens e arquivos de texto
input_dir = "C:/Users/csenz/Desktop/image/"

# Percorre todos os arquivos no diretório
for file_name in os.listdir(input_dir):
    if file_name.endswith(".txt"):
        # Verifica se o arquivo de texto está vazio
        if os.path.getsize(os.path.join(input_dir, file_name)) == 0:
            # Remove o arquivo de texto vazio
            os.remove(os.path.join(input_dir, file_name))
            # Remove a imagem correspondente, se existir
            image_file_name = file_name.replace(".txt", ".jpg")
            image_file_path = os.path.join(input_dir, image_file_name)
            if os.path.exists(image_file_path):
                os.remove(image_file_path)
