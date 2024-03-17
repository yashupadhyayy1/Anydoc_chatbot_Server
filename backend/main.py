from dotenv import load_dotenv
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any
from Model import DocumentProcessor
from MongoServer import GeminiProDatabase

# Load environment variables from .env file (if any)
load_dotenv()


#Check File type:
def identify_file_type(file: UploadFile) -> str:
    """
    Identify the file type of an uploaded file.

    Args:
    file (UploadFile): The uploaded file to identify.

    Returns:
    str: The type of file ('pdf', 'doc', 'docx', 'text', 'csv' or 'unknown').
    """
    # Mapping of content types to file types
    content_type_mapping = {
        "application/pdf": "pdf",
        "application/msword": "doc",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "docx",
        "text/plain": "text",
        "text/csv": "csv"  
    }

    # Get the content type of the file
    content_type = file.content_type

    # Return the corresponding file type or 'unknown' if not found
    return content_type_mapping.get(content_type, "unknown")



class Response(BaseModel):
    result: str | None

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict", response_model=Response)
async def predict(question: str = Form(...), file: UploadFile = File(...)) -> Any:
    # Process the question and file here
    # For example, save the file and analyze the question
    file_type = identify_file_type(file)
    # file_content = await file.read()
    # print(file_type)
    # Placeholder for the result
    
    # Initialize DocumentProcessor
    document_processor = DocumentProcessor(question, file.file, file_type)

    # Process the document
    result = document_processor.process_document()
    
    # result = "Processed result based on the question and file"
    GeminiProDatabase('mongodb://localhost:27017/', 'gemini_pro_db').store_question_file_response(question, file.file, {'result': result})
    # data = db.show_dbid(document_id)
    # print(data)

    # Return the result
    return {"result": result}