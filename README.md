# Document Processor Chatbot

The Document Processor Chatbot is a FastAPI application that allows users to upload various types of documents (PDFs, DOCX, text files, etc.) and receive processed results based on user-provided questions. Whether you’re building a search engine, a chatbot, or any other application that requires document processing, this API can be a powerful tool as well as contain a databases to manage and save the documents in server.

## Features

- **File Type Identification:** The API identifies the type of uploaded files (PDF, DOC, DOCX, text, or CSV) and processes them accordingly.
  
- **Question-Driven Processing:** Users can submit a question along with the file, and the API generates a response based on the provided context and question.
  
- **Conversation Chain:** The API leverages a conversation chain to provide detailed answers, even if the answer is not directly in the provided context.

##Beneficial Fields:
Implementing the **Document Processor Chatbot** project would be highly beneficial in several fields where document management, information retrieval, and automated response generation are crucial. Here are some of the best fields to implement this project:

### 1. **Legal Industry**
- **Use Case**: Automating the review and analysis of legal documents, contracts, and case files.
- **Benefit**: Lawyers and paralegals can quickly upload documents and receive summaries, answers to specific legal questions, and insights, saving time on manual review.

### 2. **Healthcare**
- **Use Case**: Managing patient records, medical research papers, and clinical trial documents.
- **Benefit**: Healthcare professionals can get quick insights from patient records or research documents, aiding in diagnosis and treatment plans.

### 3. **Education**
- **Use Case**: Processing academic papers, dissertations, and educational resources.
- **Benefit**: Students and educators can upload academic documents and get summarized information, making research and study more efficient.

### 4. **Human Resources**
- **Use Case**: Handling resumes, employee records, and policy documents.
- **Benefit**: HR professionals can streamline the recruitment process by quickly analyzing resumes and retrieving relevant information from policy documents.

### 5. **Finance**
- **Use Case**: Managing financial reports, investment documents, and market research.
- **Benefit**: Financial analysts and advisors can upload documents to get quick summaries and insights, facilitating better investment decisions and financial planning.

### 6. **Customer Support**
- **Use Case**: Processing support tickets, FAQs, and product manuals.
- **Benefit**: Customer support teams can provide faster and more accurate responses to customer inquiries by retrieving information from uploaded documents.

### 7. **Research and Development**
- **Use Case**: Handling research papers, technical documents, and patents.
- **Benefit**: Researchers can quickly gather information from extensive documents, facilitating innovation and development.

### 8. **Real Estate**
- **Use Case**: Managing property documents, lease agreements, and market analysis reports.
- **Benefit**: Real estate agents and managers can efficiently handle and analyze property documents, improving transaction processes and client interactions.

### 9. **Government and Public Sector**
- **Use Case**: Processing legislative documents, policy papers, and public records.
- **Benefit**: Government officials can quickly access and analyze large volumes of documents, aiding in policy-making and public administration.

### 10. **Publishing and Media**
- **Use Case**: Handling manuscripts, articles, and content archives.
- **Benefit**: Editors and journalists can streamline content review processes and retrieve information from archives efficiently.

### Key Factors for Implementation
- **Data Security and Privacy**: Ensure compliance with data protection regulations (e.g., GDPR, HIPAA) to handle sensitive information securely.
- **Scalability**: Design the system to handle varying volumes of documents and user queries, enabling growth and adaptability.
- **User-Friendly Interface**: Provide an intuitive interface for users to easily upload documents and interact with the chatbot.
- **Integration Capabilities**: Ensure the system can integrate with existing tools and platforms used in the specific field, enhancing usability and functionality.

By targeting these fields, the Document Processor Chatbot can significantly improve efficiency, accuracy, and accessibility of information, providing valuable support to professionals in various industries.

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

