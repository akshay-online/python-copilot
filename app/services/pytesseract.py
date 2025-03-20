import os
import pytesseract
from PIL import Image
import PyPDF2
import whisper
import spacy
from spacy.lang.en import English

# Initialize spaCy model
nlp = spacy.load("en_core_web_sm")

# Define claim categories
CLAIM_CATEGORIES = {
    'car accident': 'Car Accident',
    'health': 'Health Claim',
    'theft': 'Theft Claim',
    'fire': 'Fire Claim'
}

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return None

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            text = ''
            for page_num in range(reader.numPages):
                page = reader.getPage(page_num)
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Error processing PDF {pdf_path}: {e}")
        return None

def transcribe_text_from_video(video_path):
    try:
        model = whisper.load_model("base")
        result = model.transcribe(video_path)
        return result['text']
    except Exception as e:
        print(f"Error processing video {video_path}: {e}")
        return None

def categorize_text(text):
    doc = nlp(text.lower())
    for token in doc:
        if token.lemma_ in CLAIM_CATEGORIES:
            return CLAIM_CATEGORIES[token.lemma_]
    return 'Unknown'

def process_files(file_paths):
    results = []
    for file_path in file_paths:
        if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            text = extract_text_from_image(file_path)
        elif file_path.lower().endswith('.pdf'):
            text = extract_text_from_pdf(file_path)
        elif file_path.lower().endswith(('.mp4', '.avi', '.mov')):
            text = transcribe_text_from_video(file_path)
        else:
            print(f"Unsupported file type: {file_path}")
            continue

        if text:
            category = categorize_text(text)
            results.append((file_path, category, text))
    return results

def main():
    # Example file paths
    file_paths = [
        'path/to/image1.jpg',
        'path/to/document1.pdf',
        'path/to/video1.mp4'
    ]
    
    results = process_files(file_paths)
    for file_path, category, text in results:
        print(f"File: {file_path}\nCategory: {category}\nExtracted Text: {text[:100]}...\n")

if __name__ == "__main__":
    main()

