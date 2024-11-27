import os
import json
import csv
import pickle

def get_dir_size(path):
    total_size = 0
    for root1, dirs1, files1 in os.walk(path):
        for f in files1:
            file_path = os.path.join(root1, f)
            total_size += os.path.getsize(file_path)
    return total_size

def traverse_directory(directory):
    result = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            size = os.path.getsize(path)
            result.append({'Path': path, 'Type': 'File', 'Size': size})

        for folder in dirs:
            path = os.path.join(root, folder)
            size = get_dir_size(path)
            result.append({'Path': path, 'Type': 'Directory', 'Size': size})
    return result
            

def save_results_to_json(res):
    with open('json.json', 'w', encoding='utf-8') as f:
        json.dump(res, f)

def save_results_to_csv(res):
    with open('csv.csv', 'w', encoding='utf-8') as f:
        csv_writer = csv.DictWriter(f, fieldnames = ['Path', 'Type', 'Size'])
        csv_writer.writeheader()
        csv_writer.writerows(res)

def save_results_to_pickle(res):
    with open('pickle.txt', 'wb') as f:
        pickle.dump(res, f)

my_list = traverse_directory('test_folder')
save_results_to_json(my_list)
save_results_to_csv(my_list)
save_results_to_pickle(my_list)