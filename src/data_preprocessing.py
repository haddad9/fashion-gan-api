from google.cloud import bigquery

def preprocess_data():
    client = bigquery.Client()
    query = """
        SELECT 
            product_id, 
            sales, 
            IFNULL(social_trends_score, 0) as trend_score, 
            (sales - MIN(sales) OVER()) / (MAX(sales) OVER() - MIN(sales) OVER()) as normalized_sales
        FROM 
            `project.dataset.sales_data` 
        WHERE 
            sales IS NOT NULL
    """
    job = client.query(query)
    result = job.result()  # Waits for query to finish
    return result