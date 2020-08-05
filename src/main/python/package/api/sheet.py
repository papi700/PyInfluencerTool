import gspread

try:
    from package.api.constants import SCOPE, CRED, CLIENT, SHEET
except:
    pass


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


def get_cell_name(value) :
    cols_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                  'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                  'V', 'W', 'X', 'Y', 'Z']

    try :
        cell = SHEET.find(value)
        for i in range(1, 26) :
            if i == cell.col :
                cell_name = cols_names[i - 1] + str(cell.row)
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
    values = SHEET.col_values(col)
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
