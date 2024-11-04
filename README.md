# File Search Application

This application allows users to search for files on their local system via a web-based interface. Built with Flask on the backend and HTML, CSS, and JavaScript on the frontend, this app provides a straightforward way to locate files by name and optionally by directory path. Designed for ease of use, it’s ideal for quick file lookups from a web interface.

## Features

- **Case-Insensitive Search**: Locate files regardless of uppercase or lowercase in the file name.
- **Custom Search Path**: Specify any directory as the starting point for searches (defaults to `C:\`).
- **Stop at First Match**: Option to stop the search as soon as the first match is found, making it quicker for specific file lookups.
- **Cross-Origin Resource Sharing (CORS)**: CORS is enabled, allowing frontend and backend to interact seamlessly in local development environments.

## Getting Started

1. **File Name**: Enter the file name you want to search for.
2. **Search Path**: Optionally, specify a path to narrow down the search (e.g., `D:\Documents`). Default path is `C:\`.
3. **Stop at First Match**: Check this box if you only need the first match.
4. **Search**: Click "Search" to begin the search. Results appear below if the file is found.

## Project Structure

├── app.py                # Flask backend
├── index.html            # Frontend with HTML, CSS, and JavaScript
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation


### Contributing

Feel free to open issues or submit pull requests to improve the project!
