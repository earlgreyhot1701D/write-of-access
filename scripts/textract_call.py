# textract_call.py# This script processes PNG files in a specified input directory using AWS Textract
# and saves the extracted text to .txt files in a specified output directory.

import boto3
import os

# Textract client
textract = boto3.client("textract", region_name="us-west-2")  # Adjust region if needed

# Input and output directories
input_folder = r"C:\Users\DXHubAWS\Documents\Handwriting OCR Integration\Output\processed"
output_folder = r"C:\Users\DXHubAWS\Documents\Handwriting OCR Integration\Output\textract_output\pages"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Get list of PNG files
image_files = [f for f in os.listdir(input_folder) if f.endswith(".png")]

print(f"Found {len(image_files)} file(s) to process...\n")

for index, image_file in enumerate(image_files, start=1):
    input_path = os.path.join(input_folder, image_file)

    try:
        with open(input_path, 'rb') as img_file:
            image_bytes = img_file.read()

        # Call Textract
        response = textract.detect_document_text(Document={'Bytes': image_bytes})

        # Extract detected text
        extracted_text = ''
        for item in response['Blocks']:
            if item['BlockType'] == 'LINE':
                extracted_text += item['Text'] + '\n'

        # Write to .txt file
        base_filename = os.path.splitext(image_file)[0]
        output_path = os.path.join(output_folder, base_filename + ".txt")

        with open(output_path, 'w', encoding='utf-8') as out_file:
            out_file.write(extracted_text)

        print(f"[{index}/{len(image_files)}] Processed: {image_file} → {base_filename}.txt")

    except Exception as e:
        print(f"Error processing {image_file}: {e}")

