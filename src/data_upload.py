from google.cloud import storage

def upload_to_gcs(bucket_name, file_name, data):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
    blob.upload_from_string(data)
    print(f"File {file_name} uploaded to {bucket_name}")