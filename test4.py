import gdown
import sys

# How to use : 
# 1. first you should run script : pip install gdown
# 2. make folder to save all file to be download
# 3. run this command to download file : python test4.py [gdrive_file_id] [yourfilename.ext]
# e.g : python test4.py 1CpRTsoz-Qey9f8wNcXpNh_aQXY6HWZgF video_coding.mp4


url = "https://drive.google.com/uc?id="+sys.argv[1]
output = 'download/'+sys.argv[2];
gdown.download(url, output, quiet=False)
print('file has been downloaded')