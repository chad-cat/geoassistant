from llm_handler import ask_text_query, ask_image_query
from utils import load_csv_summary, load_image

def ask_question():
    q = input(" Enter your question: ")
    print("\n Answer:\n", ask_text_query(q))

def analyze_csv():
    file_path = input(" Enter CSV file path (e.g., samples/delay_data.csv): ")
    summary = load_csv_summary(file_path)
    print("\n CSV Analysis:\n", ask_text_query(f"Analyze this dataset:\n{summary}"))

def analyze_image():
    image_path = input(" Enter image file path (e.g., samples/rock.jpg): ")
    img = load_image(image_path)
    if img:
        print("\n Image Analysis:\n", ask_image_query("Describe this geology image in detail", img))
        

def menu():
    while True:
        print("\n Universal LLM Assistant Menu")
        print("1. Ask any question")
        print("2. Analyze a CSV dataset")
        print("3. Analyze an image (Gemini only)")
        print("4. Exit")
        ch = input("Choose option (1-4): ")

        if ch == "1":
            ask_question()
        elif ch == "2":
            analyze_csv()
        elif ch == "3":
            analyze_image()
        elif ch == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
