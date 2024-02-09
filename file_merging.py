def merging_files(files_list):
    files_str_num = []
    for file in files_list:
        with open(file, encoding='utf-8') as f:
            files_str_num.append(len(f.read().split('\n')))
    while len(files_list) > 0:
        min_file_ind = files_str_num.index(min(files_str_num))
        min_file_name = files_list.pop(min_file_ind)
        min_file_len = str(files_str_num.pop(min_file_ind))
        with open(min_file_name, encoding='utf-8') as f1:
            min_file_text = f1.read()
        with open('merging.txt', 'a',  encoding='utf-8') as f2:
            f2.write(min_file_name + '\n')
            f2.write(min_file_len + '\n')
            f2.write(min_file_text + '\n')
merging_files(['1.txt', '2.txt', '3.txt'])