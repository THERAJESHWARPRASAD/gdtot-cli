# Copyright (c) 2022 [.shovon]
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
from pickle import load as pload, dump as pdump
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

def createService():
    with open("token.pickle", 'rb') as f:
        credentials = pload(f)
    return build('drive', 'v3', credentials=credentials, cache_discovery=False)

# url to id
def urltoid(url):
    res = url.split("?id=")
    return res[1]

# copy to desired folder
def gdCopy(gd_service, file_id, dest_id):
    body = {
    'parents': [dest_id]
    }
    return gd_service.files().copy(supportsAllDrives=True, fileId=file_id, body=body).execute()

# delete the original file
def gdDel(gd_service,file_id):
    gd_service.files().delete(fileId=file_id, supportsTeamDrives=True).execute()

# get file info
def gdMeta(gd_service, file_id):
    meta = gd_service.files().get(supportsAllDrives=True, fileId=file_id,fields="name,id,mimeType,size").execute()
    return meta