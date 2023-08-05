import polars

#Cantidad de archivos a ver
cant_reviews = 52
df = polars.DataFrame()
books_ids = polars.read_parquet(source="books_list_top25k.parquet",columns=["asin"])
cont = 1

#Bucle que recorre todos los archivos
for i in range(1,cant_reviews+1):
    #Creacion de DF
    new_df = polars.read_parquet("reviews" + str(i) + ".parquet",columns=["asin","overall","reviewText","reviewerID","summary","verified","unixReviewTime"])

    #Formateo de unixtime
    new_df = new_df.with_columns(polars.col("unixReviewTime").str.replace(r"\"", ""))
    new_df = new_df.select(polars.all().exclude("unixReviewTime"),polars.col("unixReviewTime").cast(polars.Int32, strict=False))
    new_df = new_df.select(polars.all().exclude("unixReviewTime"),polars.from_epoch(polars.col("unixReviewTime"), time_unit="s"))
    df = polars.concat([df,new_df.filter(polars.col("asin").is_in(books_ids["asin"]))])
    
    #Creacion de parquet
    if i%4==0:
        print("Creando")
        df.write_parquet("processed_reviews_books_"+ str(cont)+".parquet")
        cont += 1
        df = polars.DataFrame()
        print(i)