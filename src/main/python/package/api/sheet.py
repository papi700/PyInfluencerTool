import gspread
import json

try :
    from package.api.constants import SCOPE, CRED, CLIENT, SHEET
except :
    pass

data_list = SHEET.get_all_records()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
cols_name = ["USERNAME", "FOLLOWERS", "E.R", "COUNTRY", "NAME", "MAIL", "CONTACTED BY", "1", "2", "3", "4", "5", "6"]

cols_index = []

for i in range(len(cols_name)) :
    cols_index.append(i + 1)


def get_col_values(string) :
    values = []
    string_key = ""
    if string in cols_name:
        for dictionnary in data_list:
            values.append(dictionnary.get(string))
    else:
        for dictionnary in data_list :
            for key, value in dictionnary.items() :
                print(value)
                if value == string :
                    string_key = key
            for key, value in dictionnary.items() :
                if key == string_key :
                    values.append(value)
    return values


def get_row_values(string) :
    values = []
    for i in range(len(data_list)) :
        for value in data_list[i].values() :
            if value == string :
                for v in data_list[i].values() :
                    values.append(v)
    return values


def get_row(string) :
    for i in range(len(data_list)) :
        for value in data_list[i].values() :
            if value == string :
                row = i + 1
    return row


def get_last_row() :
    return len(data_list)


def get_cell_name(data) :
    try :
        for i in range(len(data_list)) :
            for key, value in data_list[i].items() :
                if value == data :
                    row = i + 1
                for i2 in range(len(cols_name)) :
                    if key == cols_name[i2] :
                        col = alphabet[i2]
        cell_name = col + str(row)
        return cell_name
    except :
        pass


def add_to_sheet(row, data) :
    if len(data) == 1 :
        SHEET.update_cell(row, data[0][0], data[0][1])
        cell_name = get_cell_name(data[0][0])
        try :
            SHEET.format(cell_name, {'wrapStrategy' : "WRAP"})
        except :
            pass
    else :
        for i in range(len(data)) :
            SHEET.update_cell(row, data[i][0], data[i][1])
            cell_name = get_cell_name(data[i][0])
            try :
                SHEET.format(cell_name, {'wrapStrategy' : "WRAP"})
            except :
                pass


def is_in_col(string, col) :
    is_in = None
    for i in range(len(cols_index)) :
        if cols_index[i] == col :
            col = cols_name[i]
    for diction in data_list :
        for key, value in diction.items() :
            if k == col and v == string :
                is_in = True
                break
            else :
                is_in = False
    return is_in


def add_the_zeros(string, decimal_part_lenght) :
    K = which_char_in_string(["k", "K"], string)
    M = which_char_in_string(["m", "M"], string)
    zeros = ""
    number_of_zero_to_add = 0
    if K :
        number_of_zero_to_add = 3 - decimal_part_lenght
        letter = K
    elif M :
        number_of_zero_to_add = 6 - decimal_part_lenght
        letter = M
    for _ in range(number_of_zero_to_add) :
        zeros = zeros + "0"
    string = string.replace(letter, zeros)
    return string


def which_char_in_string(chars, string) :
    for i in range(len(chars)) :
        if chars[i] in string :
            return chars[i]
            break
        elif chars[i] == chars[len(chars) - 1] and chars[i] not in string :
            return None
            break


def in_int(string) :
    if "." in string :
        s = string.split(".")
        string = string.replace(".", "")
        decimal_part_lenght = len(s[1]) - 1
    else :
        decimal_part_lenght = 0
    return int(add_the_zeros(string, decimal_part_lenght))


def get_cell_value_from_index(current_index, col) :
    diction = data_list[current_index]
    for i in range(len(cols_name)):
        if col == cols_index[i]:
            value = diction.get(cols_name[i])
    return value

