import dropbox
import os 
from dropbox.files import WriteMode
class TransferData:
    def __init__(self,accessToken):
        self.accessToken=accessToken
    def uploadFile(self,fileFrom,fileTo):
        dbx=dropbox.Dropbox(self.accessToken)
        for root,dirs,files in os.walk(fileFrom):
            for fileName in files:
                localPath=os.path.join(root,fileName)
                relativePath=os.path.relpath(localPath,fileFrom)
                dropboxpath=os.path.join(fileTo,relativePath)
                with open(localPath,'rb')as f:
                    dbx.files_upload(f.read(),dropboxpath,mode=WriteMode('overwrite'))
def main():
    accessToken='sl.A_822uAQggGYIXv75lsZqp8vVMAkV4pgYeK1er8XvYCxJoEvNUyHRVPxdgwTbNtiHSlhZoMSUNfQT4gf6HBrUUB4wMBH_vtbUCWp5Pb-i8vrSvaSc_mzM8MwxIVjz_6Hib0ZZ3o'
    transferData=TransferData(accessToken)
    fileFrom=input("Enter the folder name that you want to send: ")
    fileTo=input("Enter teh dropbox folder path: ")
    transferData.uploadFile(fileFrom,fileTo)
    print("Folder moved")
main()

    