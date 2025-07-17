import os
import openai
from dotenv import load_dotenv

from file_reader import extract_text_from_pdf, extract_text_from_docx




# Load environment variables from .env
load_dotenv()

# Configure Azure OpenAI credentials
openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION")
openai.api_key = os.getenv("AZURE_OPENAI_KEY")

deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")



def summarize_text(input_text):
    response = openai.ChatCompletion.create(
        deployment_id=deployment_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes documents."},
            {"role": "user", "content": f"Summarize this document:\n{input_text}"}
        ]
    )
    summary = response.choices[0].message.content.strip()
    return summary




if __name__ == "__main__":
    file_path = input("Enter path to PDF or DOCX file: ")
    
    if file_path.endswith(".pdf"):
        input_text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        input_text = extract_text_from_docx(file_path)
    else:
        print("Unsupported file format. Use PDF or DOCX.")
        exit()

    print("\nExtracted text length:", len(input_text), "characters")
    summary = summarize_text(input_text)
    print("\n--- Summary ---\n", summary)

