import csv

counter = 0

# Modificar el archivo CSV en turno
with open('./listings.csv', 'w') as f:
    reader = csv.writer(f)
    
    for row in reader:
        if(counter == 0): # Cabecera
            # eliminar la columna neighbourhood_group
            # eliminar la columna last_review
            # crear la columna day_last_review
            # crear la columna month_last_review
            # crear la columna year_last_review
            print("Cabecera")
        else: # Datos
            # eliminar la columna neighbourhood_group
            # crear la columna day_last_review
            # crear la columna month_last_review
            # crear la columna year_last_review
            # eliminar la columna last_review


            print("id: {0}, name: {1}, host_id: {2}, host_name: {3}, neighbourhood_group:{4}, neighbourhood:{5}, latitude: {6}, longitude:{7}, room_type: {8}, price:{9}, minimum_nights:{10}, number_of_reviews: {11}, last_review: {12}, reviews_per_month: {13}, calculated_host_listings_count: {14}, availability_365:{15}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[4], row[15]))

        counter+=1

