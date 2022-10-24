def new_file ():
    file = 'data_base.csv'
    with open (file, 'w', encoding = 'utf-8') as f:
        f.write(f'Фамилия; Имя; \n')