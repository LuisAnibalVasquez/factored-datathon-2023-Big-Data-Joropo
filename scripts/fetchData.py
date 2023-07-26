from urllib.parse import urlparse
from azure.storage.blob import ContainerClient
import os

#We define the list of objects where our script is going to save the data
objects = ['amazon_metadata','amazon_reviews']

#We iterate in all the objects
for object in objects:

    #We create our sasUrl which we will use to authenticate in Azure
    sasUrl = "https://safactoreddatathon.blob.core.windows.net/source-files/"+ object + "?sp=rle&st=2023-07-25T18:12:36Z&se=2023-08-13T02:12:36Z&sv=2022-11-02&sr=c&sig=l2TCTwPWN8LSM922lR%2Fw78mZWQK2ErEOQDUaCJosIaw%3D"
    
    #Some parsing/processment of the url
    sasUrlParts = urlparse(sasUrl)
    accountEndpoint = sasUrlParts.scheme + '://' + sasUrlParts.netloc
    sasToken = sasUrlParts.query
    pathParts = sasUrlParts.path.split('/')
    containerName = pathParts[1]
    folderName = pathParts[2]

    #Create a client container with all the blobs/data we need
    containerClient = ContainerClient(accountEndpoint, containerName, sasToken)

    #A list of all the blobs/files inside our container
    blobs = containerClient.list_blobs(folderName)

    #We iterate for each blob
    for blob in blobs:

        #We get th blob
        blobClient = containerClient.get_blob_client(blob)

        #Some path/dir manipulation to create and save dir/files if needed
        filePath = blobClient.get_blob_properties().name
        currentWorkingDirectory = os.getcwd()
        outputFolderPath = os.path.join(currentWorkingDirectory, object+'_folder')
        listFileName = filePath.split("/")
        folderName = listFileName[len(listFileName)-2]
        FileName = listFileName[-1]
        outputFilePath = os.path.join(outputFolderPath,folderName)
        if not os.path.isdir(outputFilePath):
            os.mkdir(outputFilePath)

        #Saving the files on local
        download = blobClient.download_blob()
        with open(os.path.join(outputFilePath,FileName), "wb") as my_file:
            download.readinto(my_file)