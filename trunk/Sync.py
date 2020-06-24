from Settings import Settings
from BackBlaze import BackBlaze
from Menu import Menu


def check_settings():
    settings.check_settings()


def set_exit():
    menu.set_should_exit(True)


def change_settings():
    menu.clear_screen()
    settings.print_settings()
    print('')
    choice = input('Do you want to change this settings? (Y/N, default N): ')
    if choice == 'Y':
        settings.ask_settings()


def sync_folder_structure():
    print('')
    print(' ***** SYNC FOLDER STRUCTURE *****')
    b2.connect_b2()
    b2.download_folder_structure(settings.get_bucket_name_tvshows(), settings.get_folder_tvshows())
    b2.download_folder_structure(settings.get_bucket_name_movies(), settings.get_folder_movies())


def download_movie():
    movie_name = input('What''s the movie?: ')
    b2.connect_b2()
    b2.download_movie(movie_name, settings.get_bucket_name_movies(), settings.get_folder_movies())


def download_show():
    tvshow_name = input('What''s the TvShow?: ')
    tvshow_season = input('What''s the season?: ')
    tvshow_episode = input('What''s the episode?: ')
    b2.connect_b2()
    b2.download_tvshow(tvshow_name, int(tvshow_season), int(tvshow_episode), settings.get_bucket_name_tvshows(), settings.get_folder_tvshows())


def show_menu():

    while not menu.get_should_exit():
        menu.show_menu()
        switcher = {
            0: set_exit,
            1: change_settings,
            2: sync_folder_structure,
            3: download_movie,
            4: download_show
        }
        func = menu.process_menu(switcher)
        func()


def main():
    check_settings()
    show_menu()


if __name__ == "__main__":
    # Init classes
    menu = Menu()
    settings = Settings()
    b2 = BackBlaze(settings)
    # Call Main
    main()

