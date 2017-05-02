def data_read(file_name):
    datatable_list = []
    with open(file_name, "r") as data_table:
        for line in data_table:
            cut_line = line.replace("\n", "")
            line_list = cut_line.split(',')
            datatable_list.append(line_list)
    return datatable_list


def data_write(file_name, datatable_list):
    with open(file_name, "w") as data_table_add:
        for item in datatable_list:
            line_to_csv = ','.join(item)
            data_table_add.write(line_to_csv + "\n")


def generate_id(datatable_list):

    new_id = len(datatable_list) + 1
    for row in datatable_list:

        if new_id == row[0]:
            new_id += 1

    return str(new_id)

