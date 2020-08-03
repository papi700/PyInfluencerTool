import gspread

from package.api.constants import SCOPE, CRED, CLIENT, SHEET


def get_col_values(string) :
    cell_of_string = SHEET.find(string)
    return SHEET.col_values(cell_of_string.col)


def get_row_values(string) :
    cell_of_string = SHEET.find(string)
    return SHEET.row_values(cell_of_string.row)


def get_row(string) :
    cell_of_string = SHEET.find(string)
    return cell_of_string.row


def get_last_row() :
    return len(SHEET.get_all_values())


def getCellRange(start, end='') :
    cols_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                  'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                  'V', 'W', 'X', 'Y', 'Z']

    start_cell_name = ''
    end_cell_name = ''
    start_cell = SHEET.find(start)
    if end != '' :
        end_cell = SHEET.find(end)
    for i in range(1, 26) :
        if i == start_cell.col :
            start_cell_name = cols_names[i - 1] + str(start_cell.row)
        if end != '' and i == end_cell.col :
            end_cell_name = cols_names[i - 1] + str(start_cell.row)
    if end == '' :
        return start_cell_name
    else :
        cell_range = start_cell_name + ':' + end_cell_name
        return cell_range


def add_to_sheet(row, data) :
    if len(data) == 1 :
        SHEET.update_cell(row, data[0][1], data[0][0])
        cell = getCellRange(data[0][0])
        SHEET.format(cell, {'wrapStrategy' : "WRAP"})
    else :
        for i in range(len(data)) :
            SHEET.update_cell(row, data[i][1], data[i][0])
        cell_range = getCellRange(data[0][0], data[len(data) - 1][0])
        SHEET.format(cell_range, {'wrapStrategy' : "WRAP"})


def is_in_col(string, col) :
    values = SHEET.col_values(1)
    for i in range(len(values)) :
        if values[i] == string :
            return True
            break
        elif i == len(values) - 1 and values[i] != string :
            return False
            break


def add_the_zeros(string, decimal_part_lenght) :
    K = which_char_in_string(["k", "K"], string)
    M = which_char_in_string(["m", "M"], string)
    zeros = ""
    if K is not None :
        number_of_zero_to_add = 3 - decimal_part_lenght
        letter = K
    elif M is not None :
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
    row = current_index + 1
    value = SHEET.cell(row, col).value
    return value


