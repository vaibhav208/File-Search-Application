from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static')  # Set 'static' as the folder for static files
CORS(app)  # Enable CORS for all routes

def find_file(file_name, search_path, stop_first_match=False):
    file_name = file_name.lower()  # For case-insensitive search
    result = []
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file.lower() == file_name:
                result.append(os.path.join(root, file))
                if stop_first_match:
                    return result  # Stop if we only need the first match
    return result

@app.route('/')
def serve_frontend():
    return send_from_directory('static', 'index.html')  # Serve the frontend HTML file

@app.route('/search-file', methods=['POST'])
def search_file():
    data = request.get_json()
    
    # Retrieve parameters from JSON request
    file_name = data.get("file_name")
    search_path = data.get("search_path", "C:\\")  # Default to C:\ if not provided
    stop_first_match = data.get("stop_first_match", False)
    
    if not file_name:
        return jsonify({"error": "File name is required"}), 400
    
    # Perform the file search
    matches = find_file(file_name, search_path, stop_first_match)
    
    # Return the results as JSON
    if matches:
        return jsonify({"status": "success", "matches": matches})
    else:
        return jsonify({"status": "not found", "matches": []})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)  # Run on all network interfaces, port 80
