# %%
import json
import os

# %%
path_to_json = input("Write path to json files: ")
if (os.path.exists(path_to_json)):
    clases_file = open('classes.txt','r')
    clases = clases_file.read().split('\n')

    cajas_yolo = ""
    for json_file in os.listdir(path_to_json):
        if json_file.endswith('.json'):
            
            file = open(f'{path_to_json}/{json_file}')
            print(file.name)
            boxes = json.load(file)
            for box in boxes['shapes']:
                n_class = clases.index(box['label'])
                x_center = ((box['points'][1][0] + box['points'][0][0]) / 2) / boxes['imageWidth']
                y_center = ((box['points'][1][1] + box['points'][0][1]) / 2) / boxes['imageHeight']
                width = (box['points'][1][0] - box['points'][0][0]) / boxes['imageWidth']
                height = (box['points'][1][1] - box['points'][0][1]) / boxes['imageHeight']
                cajas_yolo += f"{n_class} {round(x_center, 6)} {round(y_center,6)} {round(width,6)} {round(height,6)}\n"
                
            nueva_ruta = file.name.split("/")[-1].split(".")[0]
            yolo_txt = open(f'{nueva_ruta}.txt', 'w')
            yolo_txt.write(cajas_yolo)
            yolo_txt.close()
            
    clases_file.close()
else:
    print("Directory does not exist")


