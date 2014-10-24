from time import time
from datetime import datetime
import glob


def pizza():
    has_changed = False
    last_command = None
    current_order = {}
    filename_dict = {}
    command = input("Enter command > ")
    while True:
        args = command.split(' ')
        # args[0] is the command and the others are arguments

        #-----------------------------------------------
        if len(args) == 3 and args[0] == "take":
            name = args[1]
            price = float(args[2])
            if name not in current_order.keys():
                current_order[name] = price
            else:
                current_order[name] += price
            print("taking order from %s for %.2f" % (name, price))
            has_changed = True
            last_command = "take"

        #-----------------------------------------------
        elif len(args) == 1 and args[0] == "status":
            for name in current_order.keys():
                print("%s - %.2f" % (name, current_order[name]))
            last_command = "status"

        #-----------------------------------------------
        elif len(args) == 1 and args[0] == "save":
            ts = time()
            stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
            filename = "orders_"+stamp
            with open(filename, 'w') as file:
                for name in current_order.keys():
                    file.write("%s - %.2f\n" % (name, current_order[name]))
            print("saved the current order to %s" % (filename))
            has_changed = False
            last_command = "save"
        #-----------------------------------------------
        elif len(args) == 1 and args[0] == "list":
            filenames = glob.glob("orders_*")
            for index, filename in enumerate(filenames):
                filename_dict[index + 1] = filename

            for key in filename_dict.keys():
                print("[%d] - %s" % (key, filename_dict[key]))
            last_command = "list"

        #-----------------------------------------------
        elif len(args) == 2 and args[0] == "load":
            if last_command != "list" and last_command != "load":
                print("Use list command before loading")
            elif has_changed and last_command != "load":
                print("You have not saved the current order.\n"
                      "If you wish to discard it, type load <number> again.")
            else:
                with open(filename_dict[int(args[1])], 'r') as file:
                    current_order = {}
                    lines = file.read().split("\n")
                    for i in range(len(lines)):
                        lines[i] = lines[i].split(" ")
                    lines.pop()  # remove empty string
                    for line in lines:
                        current_order[line[0]] = float(line[2])
            last_command = "load"
            has_changed = False

        #-----------------------------------------------
        elif len(args) == 1 and args[0] == "finish":
            if has_changed and last_command != "finish":
                print("You have not saved your order.\n"
                      "If you wish to continue, type finish again.\n"
                      "If you want to save your order, type save")
            else:
                break
            last_command = "finish"

        #-----------------------------------------------
        else:
            print("Try one of the following:\n"
                  "take <name> <price>\n"
                  "status\n"
                  "save\n"
                  "list\n"
                  "load <number>\n"
                  "finish")

        command = input("Enter command > ")


def main():
    pizza()

if __name__ == '__main__':
    main()
