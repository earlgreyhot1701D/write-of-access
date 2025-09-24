
import os
from pdf2image import convert_from_path
import cv2
from PIL import Image

# Define your actual input and output paths
INPUT_FOLDER = r"C:\Users\DXHubAWS\Documents\Handwriting OCR Integration\Input"
OUTPUT_PNG_FOLDER = r"C:\Users\DXHubAWS\Documents\Handwriting OCR Integration\Output\pngs"
OUTPUT_PROCESSED_FOLDER = r"C:\Users\DXHubAWS\Documents\Handwriting OCR Integration\Output\processed"

os.makedirs(OUTPUT_PNG_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_PROCESSED_FOLDER, exist_ok=True)

def convert_pdf_to_png(pdf_path, output_folder):
    images = convert_from_path(pdf_path, dpi=300)
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    for i, img in enumerate(images):
        filename = f"{base_name}_pg{i+1}.png"
        img_path = os.path.join(output_folder, filename)
        img.save(img_path, "PNG")
        print(f"Saved PNG: {img_path}")
        preprocess_image(img_path, base_name, i+1)

def preprocess_image(image_path, base_name, page_number):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    processed_filename = f"{base_name}_pg{page_number}_processed.png"
    processed_path = os.path.join(OUTPUT_PROCESSED_FOLDER, processed_filename)
    cv2.imwrite(processed_path, thresh)
    print(f"Saved Processed Image: {processed_path}")

def main():
    for filename in os.listdir(INPUT_FOLDER):
        if filename.lower().endswith(".pdf"):
            full_path = os.path.join(INPUT_FOLDER, filename)
            print(f"Processing PDF: {full_path}")
            convert_pdf_to_png(full_path, OUTPUT_PNG_FOLDER)
    print("All PDFs processed.")

if __name__ == "__main__":
    main()
