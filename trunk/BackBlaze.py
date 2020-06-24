import os
import re
from os import path

import PTN
from b2sdk.v1 import *


class BackBlaze:
    def __init__(self, settings):
        self.settings = settings
        self.b2 = None

    def get_valid_filename(self, s):
        s = str(s).strip().replace(' ', '_')
        return re.sub(r'(?u)[^-\w.]', '', s)

    def connect_b2(self):
        # Connect to B2
        info = InMemoryAccountInfo()
        self.b2 = B2Api(info)
        key_id = self.settings.get_keyID()
        application_key = self.settings.get_applicationID()
        self.b2.authorize_account("production", key_id, application_key)


    def download_folder_structure(self, bucket_name, start_path):
        bucket = self.b2.get_bucket_by_name(bucket_name)
        print("Downloading file list from bucket: " + bucket.name)
        for file_info, folder_name in bucket.ls(show_versions=False, recursive=True):
            # print("Original filename: " + file.file_name)
            file_parts = os.path.split(file_info.file_name)
            if file_parts[1] and int(file_info.size) > 0 or 'imdb' in file_parts[1]:
                full_path = os.path.join(start_path, bucket_name, file_parts[0], self.get_valid_filename(file_parts[1]))
                if path.exists(full_path):
                    file_size = os.stat(full_path).st_size/1024/1024
                else:
                    file_size = 0
                if file_size < 10:
                    print("Writing file: " + full_path)
                    os.makedirs(os.path.dirname(full_path), exist_ok=True)
                    with open(full_path, "w+") as f:
                        f.write("NOT AN EMPTY FILE")
                else:
                    print(f"Skipping file: {full_path} ({file_size:.2f}MB)")

    def remote_file_download(self, remote_file, bucket, start_path):
        print(f'Found remote file: {remote_file.file_name} ({remote_file.size/1024/1024:.2f}MB)')
        choice = input('Do you to download this file? (Y/N, default N): ')
        if choice == 'Y':
            try:
                file_parts = os.path.split(remote_file.file_name)
                full_path = os.path.join(start_path, bucket.name, file_parts[0], self.get_valid_filename(file_parts[1]))

                download_dest = DownloadDestLocalFile(full_path)
                progress_listener = TqdmProgressListener('Downloading remote file: ' + remote_file.file_name)
                self.b2.download_file_by_id(remote_file.id_, download_dest, progress_listener)

            except Exception as e:
                print('Error: ' + str(e))

    def parse_movie_name(self, movie_name):
        try:
            info = PTN.parse(movie_name)
            return info['title']
        except KeyError:
            return movie_name

    def download_movie(self, movie_name, bucket_name, start_path):
        bucket = self.b2.get_bucket_by_name(bucket_name)

        print('Searching for movie ' + movie_name + ' to download...')
        movie_found = False
        remote_file = None
        for file_info, folder_name in bucket.ls(show_versions=False, recursive=True):
            file_parts = os.path.split(file_info.file_name)
            remote_filename = self.parse_movie_name(file_parts[1])
            if movie_name in remote_filename:
                remote_file = file_info
                movie_found = True
                break

        if movie_found:
            self.remote_file_download(remote_file, bucket, start_path)
        else:
            print('No remote file found...')

    def match_tvshow_name(self, filename, tvshow_name, season, episode):
        try:
            info = PTN.parse(filename)
            int_season = int(info['season'])
            if isinstance(info['episode'], list):
                if tvshow_name.lower() in info['title'].lower() and season == int_season and episode in info['episode']:
                    return True
            else:
                int_episode = info['episode']
                if tvshow_name.lower() in info['title'].lower() and season == int_season and episode == int_episode:
                    return True

            return False
        except (KeyError, ValueError):
            return False

    def download_tvshow(self, tvshow_name, season, episode, bucket_name, start_path):
        bucket = self.b2.get_bucket_by_name(bucket_name)

        print('Searching for tvshow ' + tvshow_name + ' S' + str(season) + 'x' + str(episode) + ' to download...')
        tvshow_found = False
        remote_file = None
        for file_info, folder_name in bucket.ls(show_versions=False, recursive=True):
            file_parts = os.path.split(file_info.file_name)
            if self.match_tvshow_name(file_parts[1], tvshow_name, season, episode):
                remote_file = file_info
                tvshow_found = True
                break

        if tvshow_found:
            self.remote_file_download(remote_file, bucket, start_path)
        else:
            print('No remote file found...')