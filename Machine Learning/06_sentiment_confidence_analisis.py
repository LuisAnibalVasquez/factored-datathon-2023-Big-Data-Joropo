import polars
from pattern.en import sentiment

count = 0

#Funcion que realiza el analisis de sentimiento y confianza
def a_sentiment(review):
    global count
    a_sent = sentiment(review)
    count += 1
    if count%50000 == 0:
        print("Sigue iterando",count)
    return a_sent
    
#Cantidad de parquets
cant = 13
#Tratado de data
for i in range(1,cant+1):
    df = polars.read_parquet("processed_reviews_books_"+str(i)+".parquet")
    print(df.shape[0]*2)
    #Se anexa el análisis de sentimiento y de confianza
    df.with_columns(polars.col("reviewText").apply(lambda x: a_sentiment(x)[0]).alias("sentiment"))
    df.with_columns(polars.col("reviewText").apply(lambda x: a_sentiment(x)[1]).alias("confidence"))

    #Se crea el parquet
    df.write_parquet("processed_reviews_books_new_"+str(i)+".parquet")