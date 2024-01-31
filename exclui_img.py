import os

# Diretório contendo as imagens
input_dir = "C:/Users/csenz/Desktop/image/"

# Percorre todos os arquivos no diretório
for file_name in os.listdir(input_dir):
    if file_name.endswith(".jpg"):
        # Verifica se o arquivo de texto correspondente existe
        txt_file_name = file_name.replace(".jpg", ".txt")
        txt_file_path = os.path.join(input_dir, txt_file_name)
        if not os.path.exists(txt_file_path):
            # Remove a imagem se o arquivo de texto correspondente não existe
            image_file_path = os.path.join(input_dir, file_name)
            os.remove(image_file_path)
