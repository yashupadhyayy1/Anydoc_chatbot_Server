# Document Processor Chatbot

The Document Processor API is a FastAPI application that allows users to upload various types of documents (PDFs, DOCX, text files, etc.) and receive processed results based on user-provided questions. Whether you’re building a search engine, a chatbot, or any other application that requires document processing, this API can be a powerful tool.

## Features

- **File Type Identification:** The API identifies the type of uploaded files (PDF, DOC, DOCX, text, or CSV) and processes them accordingly.
  
- **Question-Driven Processing:** Users can submit a question along with the file, and the API generates a response based on the provided context and question.
  
- **Conversation Chain:** The API leverages a conversation chain to provide detailed answers, even if the answer is not directly in the provided context.

## Installation

### Clone the Repository:

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/document-processor.git
cd document-processor
```

## Installation

### Install Dependencies:

Install the required Python dependencies using pip:

```bash
pip install -r requirements.txt
```

# Environment Variables

- Create a `.env` file in the project root directory.
- Set any necessary environment variables (e.g., Google API key) in the `.env` file.

# Usage

## Run the FastAPI Server:

### Start the FastAPI server:

```bash
uvicorn main:app --reload
```

```markdown```
# Accessing the API

The API will be available at [http://localhost:8000](http://localhost:8000).

Use tools like `curl`, `httpie`, or a web browser to make POST requests to the `/predict` endpoint.


# Model.py: Document Processing and Text Analysis

The `Model.py` module is a critical component of the Document Processor API. Let's delve into its functionalities and how it interacts with the Google Gemini AI LLM model:

## Purpose and Responsibilities

1. **File Type Identification**:
    - The primary responsibility of `Model.py` is to identify the type of uploaded files (PDFs, DOCX, text files, etc.).
    - It ensures that the appropriate processing steps are applied based on the detected file type.

2. **Text Splitting**:
    - `Model.py` splits the raw text from files into smaller chunks.
    - This chunking process improves efficiency during subsequent analysis.

3. **Text Embeddings and Vector Store Creation**:
    - The module embeds these text chunks using Google Generative AI embeddings.
    - A vector store is then created for similarity search.

4. **Conversation Chain Integration**:
    - `Model.py` sets up a conversation chain to handle complex queries.
    - Even if the answer isn't directly present in the provided context, the conversation chain generates informative responses.
    - For instance, if a user asks a detailed question, the conversation chain combines context, question, and generated responses.

```markdown
# MongoServer.py: MongoDB Integration

The `MongoServer.py` module handles the integration with MongoDB, a popular NoSQL database. Here’s what it does:

## Purpose and Responsibilities

### Database Connection:
- `MongoServer.py` establishes a connection to a MongoDB server using the specified URI.
- It initializes the MongoDB client and provides access to the desired database.

### GridFS for File Storage:
- The module utilizes GridFS, a MongoDB feature, to store large files (such as uploaded documents) efficiently.
- GridFS splits files into smaller chunks and stores them as binary data in the database.

### Document Storage and Retrieval:
- The `GeminiProDatabase` class within `MongoServer.py` handles storing and retrieving question-file-response documents.
- It stores the user’s question, the uploaded file (e.g., research paper, legal document), and the generated response.

## Key Components

1. **Storing Question-File-Response Documents**:
    - The `store_question_file_response` method inserts documents into the MongoDB collection.
    - It stores the following information:
        - User’s question
        - File content (stored in GridFS)
        - Generated response

2. **Retrieving Documents by ID**:
    - The `show_dbid` method retrieves documents by their unique ID (ObjectID).
    - It fetches the stored question, file content, and response.

## Usage

### Database Configuration:
- Set up your MongoDB server and obtain the connection URI.
- Update the `.env` file with the appropriate MongoDB URI.

### Integration with FastAPI:
- In your FastAPI application (e.g., `main.py`), create an instance of `GeminiProDatabase`.
- Use the provided methods to store and retrieve documents.

## Customization

Feel free to extend or modify the functionalities of `MongoServer.py` based on your specific requirements. MongoDB offers additional features like indexing, aggregation, and geospatial queries that you can explore for advanced use cases.

Remember to handle security aspects such as authentication, authorization, and access control when deploying this API in production.

Feel free to customize this module further or add any additional details specific to your project. MongoDB is a versatile database, and integrating it effectively can enhance your application’s capabilities! 🌟📊
```  
