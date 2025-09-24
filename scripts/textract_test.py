import boto3

def test_textract_client():
    try:
        # Initialize Textract client
        textract_client = boto3.client('textract')
        print("✅ Textract client initialized successfully.")
    except Exception as e:
        print("❌ Error initializing Textract client:", e)

if __name__ == "__main__":
    test_textract_client()