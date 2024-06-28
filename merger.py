import json
import os

current_directory = os.getcwd()
print('Current Directory:', current_directory)

# List all the files here to be merged. Do not include the file extension (.ipynb)
files = ['section1','section2'] 

# Enter the name of the final merged file
file_merged_name = 'merged' 


with open('{}/{}.ipynb'.format(current_directory,files[0])) as base_file:
    
    data = json.load(base_file)

del files[0]

for arquivo in files:
    
    with open('{}/{}.ipynb'.format(current_directory,arquivo)) as arquivo_nb:
        
        data_append = json.load(arquivo_nb)
        data['cells'] += data_append['cells']

with open('{}/{}.ipynb'.format(current_directory,file_merged_name),'w') as merged_file:
    json.dump(data,merged_file,ensure_ascii=False)