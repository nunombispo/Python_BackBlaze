import json


class Settings:
    def __init__(self):
        self.settingsFileName = "settings.json"
        self.settingsData = None

    def get_keyID(self):
        try:
            with open(self.settingsFileName) as json_file:
                self.settingsData = json.load(json_file)
            return self.settingsData["keyID"]
        except FileNotFoundError:
            return None

    def get_applicationID(self):
        try:
            with open(self.settingsFileName) as json_file:
                self.settingsData = json.load(json_file)
            return self.settingsData["applicationID"]
        except FileNotFoundError:
            return None

    def get_folder_tvshows(self):
        try:
            with open(self.settingsFileName) as json_file:
                self.settingsData = json.load(json_file)
            return self.settingsData["folderTvShows"]
        except FileNotFoundError:
            return None

    def get_folder_movies(self):
        try:
            with open(self.settingsFileName) as json_file:
                self.settingsData = json.load(json_file)
            return self.settingsData["folderMovies"]
        except FileNotFoundError:
            return None

    def get_bucket_name_tvshows(self):
        try:
            with open(self.settingsFileName) as json_file:
                self.settingsData = json.load(json_file)
            return self.settingsData["bucketNameTvShows"]
        except FileNotFoundError:
            return None

    def get_bucket_name_movies(self):
        try:
            with open(self.settingsFileName) as json_file:
                self.settingsData = json.load(json_file)
            return self.settingsData["bucketNameMovies"]
        except FileNotFoundError:
            return None

    def write_settings(self):
        try:
            with open(self.settingsFileName, 'w') as outfile:
                json.dump(self.settingsData, outfile, indent=4)
        except FileNotFoundError:
            print("Error saving Settings file")

    def create_settings(self):
        self.settingsData = {
            "keyID": "",
            "applicationID": "",
            "folderTvShows": "",
            "folderMovies": "",
            "bucketNameTvShows": "",
            "bucketNameMovies": ""
        }

    def print_settings(self):
        print('')
        print(" ***** CURRENT SETTINGS *****")
        try:
            with open(self.settingsFileName) as json_file:
                self.settingsData = json.load(json_file)
                print(json.dumps(self.settingsData, indent=2))
        except FileNotFoundError:
            pass

    def ask_settings(self):
        self.create_settings()
        print(" ***** NEW SETTINGS *****")
        self.settingsData["keyID"] = input(" - What's the keyID: ")
        self.settingsData["applicationID"] = input(" - What's the applicationID: ")
        self.settingsData["folderTvShows"] = input(" - What's the root folder path for Tv Shows: ")
        self.settingsData["folderMovies"] = input(" - What's the root folder path for Movies: ")
        self.settingsData["bucketNameTvShows"] = input(" - What's the bucketname for TvShows: ")
        self.settingsData["bucketNameMovies"] = input(" - What's the bucketname for Movies: ")
        self.write_settings()

    def check_settings(self):
        try:
            with open(self.settingsFileName) as json_file:
                self.settingsData = json.load(json_file)
        except FileNotFoundError:
            pass
        if not self.settingsData:
            self.ask_settings()
