
def start():
    while True:
        ui.menu_console()
        user_input = input()
        if user_input == '1':
            com.show("all")