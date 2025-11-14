from fastapi import UploadFile
import fitz

def extract_pdf(file: UploadFile):
    #convert the pdf to string

    file_content = file.file.read()
    
    # Open the PDF from the in-memory bytes using PyMuPDF
    doc = fitz.open(stream=file_content, filetype="pdf")
    
    # Now you can process the document, e.g., extract text
    text = ""
    for page in doc:
        text += page.get_text()
        text += "\n\n Next page content: \n\n"
    
    # Close the document to free resources
    doc.close()
    
    return text
