# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def deadlock_detector(instructions):
    # define variables
    # fill process matrix with ints
    process_matrix = []
    for i in instructions[3:]:
        row = [int(m) for m in i if m.isdigit()]
        process_matrix.append(row)
    # number of processes
    num_processes = [int(m) for m in instructions[0] if m.isdigit()][0]
    # number of resources
    num_resources = [int(m) for m in instructions[1] if m.isdigit()][0]
    # capacity of resources
    resource_cap = [int(m) for m in instructions[2] if m.isdigit()]

    # find currently allocated resources by process
    allocation_matrix = []
    for i in range(len(process_matrix[num_resources:])):
        allocation_matrix.append([row[i] for row in process_matrix[num_processes:]])

    # find requested resources by process
    request_matrix = []
    for i in process_matrix[:num_processes]:
        request_matrix.append(i[num_resources:])

    # find current availability
    # #initalize work and finish matrix
    total_alloc = [sum(x) for x in zip(*allocation_matrix)]
    # work matrix is the current availability of the resources
    work_matrix = [x - y for x, y in zip(resource_cap, total_alloc)]
    # set all values to false
    finish_matrix = [False for x in range(num_processes)]

    # number of times the loop has gone through without finding a valid value
    no_change = 0

    # iterate through matrix and find knots(Needs Work!)
    # its possible to get stuck in a loop here if holdings are disproportionate to availability
    while no_change != len(request_matrix):
        for i in range(len(request_matrix)):
            if request_matrix[i] <= work_matrix and finish_matrix[i] == False:
                work_matrix = [x + y for x, y in zip(allocation_matrix[i], work_matrix)]
                finish_matrix[i] = True
            else:
                no_change += 1
    # initialize dead lock as false

    is_deadlock = False
    # if a false value is found then a deadlock is present
    for i in finish_matrix:
        if not i:
            is_deadlock = True

    return is_deadlock


def read_file():
    # define list of instructions
    instructions = []

    s = input("enter a file name to be read : ")

    try:
        f = open("input.txt", "r")
        lines = f.readlines()

    # go through file and skip empty lines and comments
        for i in lines:
            if len(i.rstrip()) == 0:
                continue
            elif i[0] == '%':
                continue
            else:
                instructions.append(i.rstrip())
    except:

        print("the file", s, "could not be opened!")

    try:
        if deadlock_detector(instructions):
            print("this graph cannot be reduced therefore its in a deadlock state!")
        else:
            print("the graph is fully reducible and deadlock free!")
    except:
        print("file contents are invalid")
    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_file()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
