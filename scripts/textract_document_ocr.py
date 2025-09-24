import boto3
import json
from pathlib import Path

# AWS Textract client
textract = boto3.client('textract')

# Input and output paths
input_dir = Path(r"C:/Users/DXHubAWS/Documents/Handwriting OCR Integration/Output/processed")
output_dir = Path(r"C:/Users/DXHubAWS/Documents/Handwriting OCR Integration/Output/textract_output/pages")
output_dir.mkdir(parents=True, exist_ok=True)

# Page files to process for one document
page_files = [
    input_dir / "sample_form_1_pg1_processed.png",
    input_dir / "sample_form_1_pg2_processed.png"
]

combined_lines = []
document_name = "sample_form_1"

# Process each page with Textract
for i, page_path in enumerate(page_files, 1):
    with open(page_path, 'rb') as document:
        image_bytes = document.read()
        response = textract.detect_document_text(Document={'Bytes': image_bytes})

    # Save raw Textract response for each page
    raw_outfile = output_dir / f"{document_name}_page{i}.json"
    with open(raw_outfile, "w") as f:
        json.dump(response, f, indent=2)

    # Extract LINE-level text from response
    lines = [block for block in response['Blocks'] if block['BlockType'] == 'LINE']
    combined_lines.extend(lines)

# Save combined output to a readable JSON
combined_output = {
    "document": document_name,
    "pages": len(page_files),
    "lines": combined_lines
}

combined_output_path = Path(r"C:/Users/DXHubAWS/Documents/Handwriting OCR Integration/Output/textract_output") / f"{document_name}_combined.json"
with open(combined_output_path, "w") as f:
    json.dump(combined_output, f, indent=2)

print(f"✅ Combined output saved to: {combined_output_path}")