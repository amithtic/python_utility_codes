import json

file_name = r"input file path .ipynb file"
output_file = r"output file path .py file"
with open(output_file, 'w') as file_object:
    file_object.write('# start of the code.\n')
        
    with open(file_name, 'r') as file:
        data = json.load(file)
        data = data["cells"]
        for i in range(len(data)):
            content = data[i]["source"]
            
            for j in range(len(content)):
                content_out = content[j].replace("'\n'", '')
                file_object.write(content_out)
            file_object.write('\n\n')
    print("done")
