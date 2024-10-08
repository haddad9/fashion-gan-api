from data_upload import upload_to_gcs

def ingest_data():
    ecommerce_data = "ecommerce_sales.csv"
    social_media_data = "social_trends.json"
    bucket_name = "fashion-data-lake"
    
    upload_to_gcs(bucket_name, ecommerce_data, ecommerce_data) 
    upload_to_gcs(bucket_name, social_media_data, social_media_data)

if __name__ == "__main__":
    ingest_data()