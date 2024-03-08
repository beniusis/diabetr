import helpers


def main():
    main_menu = helpers.init_main_menu()
    main_menu_exit = False

    while not main_menu_exit:
        selection = main_menu.show()
        helpers.clear_terminal()
        if selection == 0:
            helpers.init_carbs_calculation()
        elif selection == 1:
            helpers.init_show_doses()
        elif selection == 2:
            helpers.init_change_insulin_dose("short")
        elif selection == 3:
            helpers.init_change_insulin_dose("long")
        elif selection == 4:
            helpers.init_todays_injections()
        elif selection == 5:
            helpers.init_add_injection()
        elif selection == 6 or selection == None:
            main_menu_exit = True


if __name__ == "__main__":
    main()
