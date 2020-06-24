

class Menu:
    def __init__(self):
        self.raw_choice = None
        self.should_exit = False

    def set_should_exit(self, value):
        self.should_exit = value

    def get_should_exit(self):
        return self.should_exit

    def clear_screen(self):
        print('')
        print('')

    def show_menu(self):
        self.clear_screen()
        print('********** Welcome to BackBlaze Sync **********')
        print('')
        print(' 1 - Settings')
        print(' 2 - Sync folder structure')
        print(' 3 - Download Movie')
        print(' 4 - Download TvShow')
        print('')

    def process_menu(self, switcher):
        self.raw_choice = input('Please choose an option (0 to exit): ')
        if self.raw_choice is None or self.raw_choice == '':
            self.raw_choice = 0
        choice = int(self.raw_choice)
        # Get the function from switcher dictionary
        func = switcher.get(choice, lambda: 'nothing')
        return func



