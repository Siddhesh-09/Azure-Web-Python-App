from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

@app.route('/')
def home():
    """Home page"""
    return render_template('index.html')

@app.route('/api/hello', methods=['GET'])
def hello():
    """API endpoint that returns a greeting"""
    name = request.args.get('name', 'World')
    return jsonify({'message': f'Hello, {name}!'})

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)
