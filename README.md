# Azure Web Python App

A Flask-based Python web application designed to run on Azure.

## Prerequisites

- Python 3.14+
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Azure-Web-Python-App
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Set environment variables (optional):
   ```bash
   set FLASK_ENV=development  # Windows
   export FLASK_ENV=development  # macOS/Linux
   ```

2. Run the Flask application:
   ```bash
   python app.py
   ```

3. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## API Endpoints

- `GET /` - Home page
- `GET /api/hello?name=YourName` - Returns a greeting
- `GET /api/health` - Health check endpoint

## Project Structure

```
Azure-Web-Python-App/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/            # Jinja2 HTML templates
│   └── index.html        # Home page template
└── static/               # Static files (CSS, JS, images)
    ├── css/
    └── js/
```

## Development

For local development, make sure to:
1. Use a virtual environment
2. Set `FLASK_ENV=development` for auto-reloading
3. Install dependencies from `requirements.txt`

## Deployment to Azure

This application can be deployed to Azure App Service:
1. Create an Azure App Service
2. Connect your repository
3. Configure Python 3.14 runtime
4. Deploy using Azure DevOps or GitHub Actions

## License

MIT License
