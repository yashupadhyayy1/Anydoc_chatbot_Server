import { useState } from "react";
import "./App.css";
// The Use og Toastify to get pop up in system

//please remind to install "npm install react-toastify"

import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
// import "./App.css";

export default function App() {
  const [result, setResult] = useState();
  const [question, setQuestion] = useState();
  const [file, setFile] = useState();

  const handleQuestionChange = (event: any) => {
    setQuestion(event.target.value);
  };

// As per instruction: which may occur while running the app.
//cases when the user has uploaded a very large file (>100mb) or a unsupported file type like video/mp3.
  const handleFileChange = (event: any) => {
    if (event.target.files && event.target.files.length > 0) {
      const selectedFile = event.target.files[0];
      const fileType = selectedFile.type;
      const fileSize = selectedFile.size;
  
      // Check if the file is a video or audio file
      const isVideo = fileType.includes('video');
      const isAudio = fileType.includes('audio') || fileType.includes('mp3');
  
      // Check if the file size is greater than 100MB
      const maxSize = 100 * 1024 * 1024; // 100MB in bytes
      const isTooLarge = fileSize > maxSize;
  
      if (isVideo || isAudio || isTooLarge) {
        // Alert the user and don't set the file
        alert('Invalid file type or size. Please select a different file.');
      } else {
        // File is valid, set the file
        setFile(selectedFile);
        // Notify that the file has been uploaded properly
        toast.success('File uploaded successfully!');
      }
    }
  };

  const handleSubmit = (event: any) => {
    event.preventDefault();

    const formData = new FormData();

    if (file) {
      formData.append("file", file);
    }
    if (question) {
      formData.append("question", question);
    }

    fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        setResult(data.result);
      })
      .catch((error) => {
        console.error("Error", error);
      });
  };

  return (
    <div className="appBlock">
      <form onSubmit={handleSubmit} className="form">
        <label className="questionLabel" htmlFor="question">
          Question:
        </label>
        <input
          className="questionInput"
          id="question"
          type="text"
          value={question}
          onChange={handleQuestionChange}
          placeholder="Ask your question here"
        />

        <br></br>
        <label className="fileLabel" htmlFor="file">
          Upload File file:
        </label>

        <input
          type="file"
          id="file"
          name="file"
          accept=".pdf,.doc,.csv,.txt"
          onChange={handleFileChange}
          className="fileInput"
        />
        {/* Pop up */}
        <ToastContainer />
        <br></br>
        <button
          className="submitBtn"
          type="submit"
          disabled={!file || !question}
        >
          Submit
        </button>
      </form>
      <p className="resultOutput">Result: {result}</p>
    </div>
  );
}
