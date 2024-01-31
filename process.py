import os
import random

# Define o caminho das imagens e a proporção do conjunto de teste
path = 'data/obj'
test_ratio = 0.3  # 30% para teste, 70% para treinamento

# Obtém uma lista de todos os arquivos de imagem no caminho especificado
image_files = [f for f in os.listdir(path) if f.endswith('.jpg')]

# Embaralha a lista de arquivos aleatoriamente
random.shuffle(image_files)

# Calcula o número de imagens que devem ser incluídas no conjunto de teste e no conjunto de treinamento
num_images = len(image_files)
num_test_images = int(num_images * test_ratio)
num_train_images = num_images - num_test_images

# Separa as imagens em conjunto de teste e conjunto de treinamento
test_images = image_files[:num_test_images]
train_images = image_files[num_test_images:]

# Cria o arquivo de teste
with open('data/test.txt', 'w') as f:
    for img_file in test_images:
        f.write(os.path.join('data/obj', img_file) + '\n')

# Cria o arquivo de treinamento
with open('data/train.txt', 'w') as f:
    for img_file in train_images:
        f.write(os.path.join('data/obj', img_file) + '\n')
