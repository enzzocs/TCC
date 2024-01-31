import os

# Diretório contendo as imagens e arquivos de anotação
input_dir = "C:/Users/csenz/Desktop/obj/"

# Percorre todos os arquivos no diretório
for file_name in os.listdir(input_dir):
    if file_name.endswith(".JPG"):  # Verifica se o arquivo é uma imagem .JPG (maiúsculas)
        image_file_path = os.path.join(input_dir, file_name)
        # Verifica se existe um arquivo de anotação correspondente (.txt)
        txt_file_name = file_name.replace(".JPG", ".txt")
        txt_file_path = os.path.join(input_dir, txt_file_name)
        if os.path.exists(txt_file_path):
            # Exclui o arquivo de imagem e o arquivo de anotação
            os.remove(image_file_path)
            os.remove(txt_file_path)