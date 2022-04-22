# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def deadlock_detector(instructions):
    #define variables
    num_processes = [int(m)for m in instructions[0] if m.isdigit()][0]

    num_resources = [int(m)for m in instructions[1] if m.isdigit()][0]

    resource_cap = [int(m)for m in instructions[2] if m.isdigit()]

    process_matrix =[]

    #fill matrix
    for i in instructions[3:]:
        row = [int(m)for m in i if m.isdigit()]
        process_matrix.append(row)
    matrix_length = len(process_matrix)-1




    print(process_matrix)

def read_file():
    #define list of instructions
    instructions = []


    #s = input("enter a file name: ")
    f = open("input.txt", "r")
    lines = f.readlines()

    #go through file and skip empty lines and comments
    for i in lines:
        if len(i.rstrip()) == 0:
            continue
        elif(i[0]=='%'):
            continue
        else:
           instructions.append(i.rstrip())

    deadlock_detector(instructions)


    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_file()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
