import shelve


def add_item():
    db = shelve.open("items.db")
    print("Please, enter following information:\n")
    pid = input("Product ID: ")
    name = input("Name: ")
    price = int(input("Price: "))
    pay_price = int(input("Pay Price: "))
    count = int(input("Count: "))
    item = {
        "name": name,
        "price": price,
        "pay_price": pay_price,
        "count": count
    }
    db[pid] = item
    print("The Product add successful. ")

    db.close()

    return db


def find_item():
    check_elem = input("Please, enter item name (or part of it): ")
    db = shelve.open('items.db')
    count_find_elem = []
    for key, val in db.items():
        if check_elem in val['name']:
            count_find_elem.append(check_elem)
            print(' |', '' * 5, 'Prod_ID', '' * 4, '|', '' * 4, 'Name', '' * 4, '|',
                  '' * 4, 'Price', '' * 4, '|', 'Pay Price', '' * 4, '|', '' * 4, 'Count', ' ' * 4, '|\n',
                  "___________________________________________________________________\n",
                  "|", '' * 3, key, ' ' * (3 - len(str(key))), '|',
                  '' * 3, val['name'], ' ' * (4 - len(val['name'])), '|',
                  '' * 3, val['price'], ' ' * (5 - len(str((val['price'])))), '|',
                  '' * 3, val['pay_price'], ' ' * (9 - len(str((val['pay_price'])))), '|',
                  '' * 3, val['count'], ' ' * (13 - len(str((val['count'])))), '|\n',
                  "___________________________________________________________________")

    print("Found ", len(count_find_elem), "items.")

    # return check_elem


def sells_item():
    item_pid = int(input("Prod id:  "))
    count_item = int(input("Count: "))
    db = shelve.open('items.db', writeback=True)
    for key, val in db.items():
        if count_item <= val['count']:
            val['count'] -= count_item
            print("Your sale is registered successfully.")
            print("|__", key, "|__|", val['count'], "|__|",
                   val["pay_price"], "__|")
        else:
            print("There's not enough of this item in store!")

    return db


# {'name ': 'asd', 'price ': 7, 'count ': 6}
def exit_app():
    print("exit")
    exit()


def show_menu():
    print("a -> Add or update an item\n"
          "f -> Search for an item\n"
          "s -> Register a sale\n"
          "e -> Exit\n")


def prompt_command():
    cmd = input("Pleas chose your command: -> ")
    while True:
        if cmd.isdigit():
            show_menu()
            cmd = input("Pleas chose your command: -> ")
        else:
            break
    return cmd


def invoke_command(cmd: str):
    comand_runer = {
        'a': add_item,
        'f': find_item,
        's': sells_item,
        'e': exit_app}
    return comand_runer[cmd]()


while True:
    show_menu()
    cmd = prompt_command()
    invoke_command(cmd)
