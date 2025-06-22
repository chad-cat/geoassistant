import pandas as pd
from PIL import Image

def load_csv_summary(file_path):
    try:
        df = pd.read_csv(file_path)
        summary = df.describe(include='all').to_string()
        return f"CSV Summary:\n{summary}"
    except Exception as e:
        return f"Error reading CSV: {e}"

def load_image(file_path):
    try:
        return Image.open(file_path)
    except Exception as e:
        print("Error loading image:", e)
        return None
