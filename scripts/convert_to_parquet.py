import os
import gzip
import json
import pandas as pd
import time

allFolders = os.listdir('amazon_reviews_folder')
allFolders.remove('amazon_reviews')

listJsonObjects = []
cont = 1
cont_parts = 1
# df1 = pl.DataFrame()
start_time = time.time()
for folder in allFolders:

    files = os.listdir('amazon_reviews_folder/'+folder)
    for file in files:
        if ".gz" not in file:
            continue

        currentWorkingDirectory = os.getcwd()
        folderPath = os.path.join(os.path.join(currentWorkingDirectory,'amazon_reviews_folder'),folder)
        filePath = os.path.join(folderPath,file)
        with gzip.open(filePath, 'rb') as fileMetadata:
            for row in fileMetadata:
                listJsonObjects.append(json.loads(row.decode().strip()))
                # df2 = pl.from_dict(json.loads(row.decode().strip()))
                # df1 = pl.concat([df1, df2], rechunk=True)
        cont += 1
        if cont%100==0:
            print('comienza la conversion')
            df=pd.json_normalize(listJsonObjects)
            df.to_parquet('reviews'+str(cont_parts)+'.parquet')
            print('Termina la conversion')
            listJsonObjects = []
            cont_parts += 1
        print(cont)

end_time = time.time()
print(end_time-start_time)
print("Funciono")