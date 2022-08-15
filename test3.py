# You need to install : pip install googledrivedownloader

# How to run this script :
# python filename.py [gdrive_file_id] [filename_to_download.mp4]

import sys

from google_drive_downloader import GoogleDriveDownloader as gdd

gdd.download_file_from_google_drive(file_id=sys.argv[1],
                                    dest_path='./download/'+sys.argv[2],
                                    unzip=True)