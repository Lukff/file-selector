import csv
import os

locations = input('Informe o nome do arquivo contendo as classificações: ')

with open(locations, 'r') as f:
    rows = csv.reader(f, delimiter=',')
    for row in rows:
        file_sel = row[0] # files names on first column
        folder_sel = row[1] # directory names on second column

        # create directory if it does not exist
        if (folder_sel not in list(os.walk('.'))[0][1]):
            os.mkdir(folder_sel)

        # if file does not exist go to the next one
        if (file_sel not in list(os.walk('.'))[0][2]):
            continue

        # move file
        new_file_path = os.path.join(folder_sel, file_sel)
        os.rename(file_sel, new_file_path)
