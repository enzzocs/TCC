#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import xml.etree.ElementTree as ET

# mapeamento de classes
class_dict = {
    'car': 0,
    'person': 1,
    'motorcycle': 2,
    'Speed_limit_30km': 3,
    'Speed_limit_40km': 4,
    'Speed_limit_50km': 5,
    'Speed_limit_60km': 6,
    'Speed_limit_70km': 7,
    'Speed_limit_80km': 8,
    'Speed_limit_90km': 9,
    'Speed_limit_100km': 10,
    'Speed_limit_110km': 11,
    'Speed_limit_120km': 12,
    'Traffic_light_green': 13,
    'Traffic_light_red': 14,
    'Bend_to_right': 15,
    'Bend_to_left': 16,
    'Double_bend_right': 17,
    'Double_bend_left': 18,
    'No_right_turn': 19,
    'No_left_turn': 20,
    'No_u_turn': 21,
    'No_entry': 22,
    'Narrow_road': 23,
    'Fork_road': 24
}

# diretórios de entrada e saída
input_dir = 'C:/Users/csenz/Desktop/dataset/label/'
output_dir = 'C:/Users/csenz/Desktop/dataset/image/'

# loop pelos arquivos XML na pasta de entrada
for filename in os.listdir(input_dir):
    if filename.endswith('.xml'):
        # abrindo o arquivo XML
        tree = ET.parse(os.path.join(input_dir, filename))
        root = tree.getroot()

        # obtendo informações de tamanho da imagem
        size = root.find('size')
        width = int(size.find('width').text)
        height = int(size.find('height').text)

        # criando arquivo TXT de saída
        output_file = open(os.path.join(output_dir, filename[:-4] + '.txt'), 'w')

        # loop pelas informações dos objetos
        for obj in root.findall('object'):
            # obtendo informações do objeto
            obj_name = obj.find('name').text
            obj_class = class_dict[obj_name]
            obj_bbox = obj.find('bndbox')
            x_min = int(obj_bbox.find('xmin').text)
            y_min = int(obj_bbox.find('ymin').text)
            x_max = int(obj_bbox.find('xmax').text)
            y_max = int(obj_bbox.find('ymax').text)

            # convertendo para formato YOLO
            x_center = (x_min + x_max) / (2.0 * width)
            y_center = (y_min + y_max) / (2.0 * height)
            bbox_width = (x_max - x_min) / float(width)
            bbox_height = (y_max - y_min) / float(height)

            # escrevendo informações no arquivo de saída
            output_file.write(f"{obj_class} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}\n")

        output_file.close()

print('Conversão concluída.')

