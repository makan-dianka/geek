import os, shutil

path_1 = os.getcwd()
path_2 =  f'{path_1}/text'
    
current_path = os.listdir(path_1)
for f in current_path:
    if f.endswith('.txt'):
        shutil.move(f'{path_1}/{f}', f'{path_2}/{f}')
        print(f'\n le fichier: {f}, a bien été déplacé')
    else:
        print("\n il n'y a aucun fichier dans le repertoire indiqué portant l'extantion '.txt' " )
        break
        