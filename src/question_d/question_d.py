def test_config():
    return True

def create_multiplication_table(rows, cols):
    list = []
    
    for r in range(0, rows):
        multiplication_row_list = []

        for c in range(0, cols):
            multiplication_row_list.append((r + 1) * (c + 1))

        list.append(multiplication_row_list)

    return list

def display_multiplication_table(list):

    for row_list in list:
        for item in row_list:
            print(str(item).rjust(3, " "), end = " ")

        print (" ")
