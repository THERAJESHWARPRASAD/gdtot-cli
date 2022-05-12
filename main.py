# Copyright (c) 2022 [.shovon]
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
import configparser
import gdtot
import drive_tools

#config
config = configparser.RawConfigParser()
config.read('config.ini')
crypt = config['gdtot']['crypt']
dest_id = config['drive']['folder_id']
worker_url = config['worker']['worker_url']

# download from gdtot
gdtot_url = input("Enter gdtot url: ")
gdtot_info = gdtot.gdtot_dl(gdtot_url, crypt)
file_url = gdtot_info['gdrive_link']

# if want to upload to a specific folder
if(dest_id):
    gd_service =  drive_tools.createService()
    file_id = drive_tools.urltoid(file_url)
    file_meta = drive_tools.gdMeta(gd_service, file_id)
    file_name = file_meta['name']
    new_file = drive_tools.gdCopy(gd_service, file_id, dest_id)
    file_url = 'https://drive.google.com/open?id=' + new_file['id']
    drive_tools.gdDel(gd_service, file_id)

print("Google drive link:", file_url)
# genrate Cloudflare worker url
if(worker_url):
    import urllib
    def path2url(path):
        return urllib.request.pathname2url(path)
    worker_uri = path2url(file_name)
    worker_file_url = worker_url + worker_uri
    print("Cloudflare worker direct link:",worker_file_url)

