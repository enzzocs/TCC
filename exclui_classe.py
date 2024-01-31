import os

# Lista de classes a serem excluídas
classes_to_exclude = list(range(1, 3))

# Diretório contendo as imagens e arquivos de anotação
input_dir = "C:/Users/csenz/Desktop/obj/"

# Percorre todos os arquivos no diretório
for file_name in os.listdir(input_dir):
    try:
        if file_name.endswith(".txt"):
            txt_file_path = os.path.join(input_dir, file_name)
            with open(txt_file_path, "r") as f:
                lines = f.readlines()
            with open(txt_file_path, "w") as f:
                for line in lines:
                    # Verifica se a linha começa com um número inteiro
                    try:
                        class_num = int(line.split()[0])
                    except ValueError:
                        continue
                    # Verifica se a classe deve ser excluída
                    if class_num in classes_to_exclude:
                        continue
                    f.write(line)
        elif file_name.endswith(".jpg"):
            # Obtém o nome do arquivo de anotação correspondente
            txt_file_name = file_name.replace(".jpg", ".txt")
            txt_file_path = os.path.join(input_dir, txt_file_name)
            with open(txt_file_path, "r") as f:
                lines = f.readlines()
            with open(txt_file_path, "w") as f:
                for line in lines:
                    # Verifica se a linha começa com um número inteiro
                    try:
                        class_num = int(line.split()[0])
                    except ValueError:
                        continue
                    # Verifica se a classe deve ser excluída
                    if class_num in classes_to_exclude:
                        continue
                    f.write(line)
            # Exclui a imagem se todas as anotações da classe forem excluídas
            with open(txt_file_path, "r") as f:
                lines = f.readlines()
            if not any(class_num not in classes_to_exclude for class_num in [int(line.split()[0]) for line in lines if line.startswith(str(tuple(classes_to_exclude))) == False]):
                os.remove(txt_file_path)
                image_file_path = os.path.join(input_dir, file_name)
                os.remove(image_file_path)
    except Exception as e:
        print(f"Erro ao processar o arquivo {file_name}: {e}")
