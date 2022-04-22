# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def deadlock_detector(instructions):

    #define variables
    # fill process matrix with ints
    process_matrix = []
    for i in instructions[3:]:
        row = [int(m) for m in i if m.isdigit()]
        process_matrix.append(row)

    num_processes = [int(m)for m in instructions[0] if m.isdigit()][0]

    num_resources = [int(m)for m in instructions[1] if m.isdigit()][0]

    resource_cap = [int(m)for m in instructions[2] if m.isdigit()]


    #find currently allocated blocks by process
    allocation_matrix = []
    for i in range(len(process_matrix[num_resources:])):
        allocation_matrix.append([row[i]for row in process_matrix[num_processes:]])

    #find requested resources by process
    request_matrix = []
    for i in process_matrix[:num_processes]:
        request_matrix.append(i[num_resources:])

    #find current availability
    # #initalize work and finish matrix
    total_alloc = [sum(x) for x in zip(*allocation_matrix)]
    work_matrix = [x-y for x, y in zip(resource_cap, total_alloc)]
    finish_matrix = [False for x in range(num_processes)]

    #iterate through matrix and find knots(Needs Work!)
    for i in range(len(request_matrix)):
        if request_matrix[i] <= work_matrix and finish_matrix[i] is False:
            work_matrix = [x+y for x, y in zip(allocation_matrix[i], work_matrix)]
            finish_matrix[i] = True

    print(finish_matrix)

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
    print(instructions)
    deadlock_detector(instructions)


    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_file()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
