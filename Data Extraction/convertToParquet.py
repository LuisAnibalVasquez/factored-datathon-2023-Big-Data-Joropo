import os
import gzip
import json
import pandas as pd
import time

#Search all the folders in amazon_reviews_folder
allFolders = os.listdir('amazon_reviews_folder')
allFolders.remove('amazon_reviews')

#Empty list
listJsonObjects = []

#Counters
cont = 1
cont_parts = 1
start_time = time.time()
for folder in allFolders:
    #Search of all the folders fo the reviews
    files = os.listdir('amazon_reviews_folder/'+folder)
    for file in files:
        if ".gz" not in file:
            continue
        
        #Searching for the file that is needed
        currentWorkingDirectory = os.getcwd()
        folderPath = os.path.join(os.path.join(currentWorkingDirectory,'amazon_reviews_folder'),folder)
        filePath = os.path.join(folderPath,file)

        #Filling the list
        with gzip.open(filePath, 'rb') as fileMetadata:
            for row in fileMetadata:
                listJsonObjects.append(json.loads(row.decode().strip()))
        cont += 1

        #The conversion into parquet
        if cont%100==0:
            print('comienza la conversion')
            df=pd.json_normalize(listJsonObjects)
            df.to_parquet('reviews'+str(cont_parts)+'.parquet')
            print('Termina la conversion')
            listJsonObjects = []
            cont_parts += 1

end_time = time.time()
print(end_time-start_time)