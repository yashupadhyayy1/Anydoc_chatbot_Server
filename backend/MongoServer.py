from pymongo import MongoClient
from bson import ObjectId
import gridfs

class GeminiProDatabase:
    def __init__(self, db_uri, db_name):
        self.client = MongoClient(db_uri)
        self.db = self.client[db_name]
        self.fs = gridfs.GridFS(self.db)

    def store_question_file_response(self, question, file_content, response):
        # Store the file in GridFS
        file_id = self.fs.put(file_content)

        # Create a document for the question and response
        document = {
            "question": question,
            "file_id": file_id,
            "response": response
        }

        # Insert the document into the database
        return self.db.questions_responses.insert_one(document).inserted_id

    def show_dbid(self, document_id):
        # Retrieve the document from the database
        document = self.db.questions_responses.find_one({"_id": ObjectId(document_id)})

        if document:
            # Retrieve the file content from GridFS
            file_content = self.fs.get(document["file_id"]).read()
            return {
                "question": document["question"],
                "file_content": file_content,
                "response": document["response"]
            }
        else:
            return None

# Example usage:
# db = GeminiProDatabase('mongodb://localhost:27017/', 'gemini_pro_db')
# document_id = db.store_question_file_response('What is the meaning of life?', b'file content', {'answer': 42})
# data = db.show_dbid(document_id)
# print(data)
