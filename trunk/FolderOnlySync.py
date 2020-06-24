from Settings import Settings
from BackBlaze import BackBlaze


def sync_folder_structure():
    print('')
    print(' ***** SYNC FOLDER STRUCTURE *****')
    b2.connect_b2()
    b2.download_folder_structure(settings.get_bucket_name_tvshows())
    b2.download_folder_structure(settings.get_bucket_name_movies())


if __name__ == "__main__":
    settings = Settings()
    b2 = BackBlaze(settings)
    sync_folder_structure()