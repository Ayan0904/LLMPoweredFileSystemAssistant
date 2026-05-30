import os
import glob
from datetime import datetime
from pathlib import Path
from pypdf import PdfReader
from docx import Document

def list_files(directory: str, extension: str = None) -> list:
    """List all files in a directory, optionally filtered by extension."""
    try:
        path = Path(directory)
        if not path.exists() or not path.is_dir():
            return [{"error": f"Directory '{directory}' does not exist."}]
        
        # Determine search pattern
        pattern = f"*.{extension.lstrip('.')}" if extension else "*"
        files = path.glob(pattern)
        
        results = []
        for f in files:
            if f.is_file():
                stat = f.stat()
                results.append({
                    "name": f.name,
                    "path": str(f.resolve()),
                    "size_bytes": stat.st_size,
                    "modified_date": datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                })
        return results
    except Exception as e:
        return [{"error": f"Failed to list files: {str(e)}"}]

def read_file(filepath: str) -> dict:
    """Read TXT, PDF, or DOCX files and return content with metadata."""
    try:
        path = Path(filepath)
        if not path.exists():
            return {"error": f"File '{filepath}' not found."}
        
        ext = path.suffix.lower()
        content = ""
        
        if ext == ".txt":
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        elif ext == ".pdf":
            reader = PdfReader(path)
            content = "".join([page.extract_text() or "" for page in reader.pages])
        elif ext == ".docx":
            doc = Document(path)
            content = "\n".join([para.text for para in doc.paragraphs])
        else:
            return {"error": f"Unsupported file extension: {ext}"}
            
        return {
            "filename": path.name,
            "content": content.strip(),
            "char_count": len(content)
        }
    except Exception as e:
        return {"error": f"Failed to read file: {str(e)}"}

def write_file(filepath: str, content: str) -> dict:
    """Write content to a file, creating directories if they don't exist."""
    try:
        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
            
        return {"status": "success", "message": f"Successfully wrote to {filepath}"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

def search_in_file(filepath: str, keyword: str) -> dict:
    """Search for a keyword in a file and return matching lines for context."""
    try:
        # Re-use our robust read_file tool to get text
        file_data = read_file(filepath)
        if "error" in file_data:
            return file_data
            
        content = file_data["content"]
        lines = content.split('\n')
        matches = []
        
        for i, line in enumerate(lines):
            if keyword.lower() in line.lower():
                # Provide a bit of context (line number and the text)
                matches.append({"line_number": i + 1, "text": line.strip()})
                
        return {
            "filename": Path(filepath).name,
            "keyword": keyword,
            "match_count": len(matches),
            "matches": matches
        }
    except Exception as e:
        return {"error": f"Search failed: {str(e)}"}