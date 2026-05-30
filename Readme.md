# LLM File Assistant Project

An AI-powered agent capable of executing local file system operations (listing, reading, writing, searching) using Tool Calling.

📁 Final Project Directory Structure

llm-file-assistant/
│
├── resumes/
│   ├── resume_john_doe.txt
│   ├── resume_jane_smith.txt
│   ├── resume_alex_martinez.docx
│   ├── resume_sarah_jenkins.pdf
│   └── resume_david_kim.txt
│
├── fs_tools.py
├── llm_file_assistant.py
├── requirements.txt
└── README.md

## 🚀 Quick Start & Setup

### 1. Prerequisites
Ensure you have Python 3.10+ installed on your system.

### 2. Install Dependencies
Navigate to the root directory of the project and install the required modules:
```bash
pip install -r requirements.txt


### 3. Configure Your Gemini API Key
The application requires a Gemini API Key to authenticate with Google AI Studio. Set it as an environment variable in your terminal:

macOS / Linux:

Bash
export GEMINI_API_KEY="your_actual_api_key_here"

3. Set your OpenAI API Key:
    export OPENAI_API_KEY="your-api-key-here"  # Mac/Linux
    set OPENAI_API_KEY="your-api-key-here"     # Windows CMD
4. Run the program:

    python llm_file_assistant.py