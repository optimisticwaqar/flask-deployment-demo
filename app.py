"""Simple Flask Web Application for Deployment Demo"""

from flask import Flask, render_template_string, jsonify
import os
import datetime

app = Flask(__name__)

# HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Deployment Demo App</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f4f4f4; }
        .container { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .header { color: #333; text-align: center; }
        .info { background: #e8f4fd; padding: 15px; border-radius: 5px; margin: 20px 0; }
        .status { background: #d4edda; padding: 10px; border-radius: 5px; color: #155724; }
        .version { font-size: 0.9em; color: #666; }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="header">🚀 Deployment Demo Application</h1>
        <div class="info">
            <h3>Environment: {{ env }}</h3>
            <p><strong>Version:</strong> {{ version }}</p>
            <p><strong>Deployment Time:</strong> {{ deploy_time }}</p>
            <p><strong>Container ID:</strong> {{ container_id }}</p>
        </div>
        <div class="status">
            ✅ Application is running successfully!
        </div>
        <div class="version">
            <p>This application demonstrates automated Docker deployment with GitHub Actions.</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    """Home page with deployment information."""
    return render_template_string(HTML_TEMPLATE,
        env=os.getenv('ENVIRONMENT', 'development'),
        version=os.getenv('APP_VERSION', '1.0.0'),
        deploy_time=os.getenv('DEPLOY_TIME', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        container_id=os.getenv('HOSTNAME', 'local')[:12]
    )

@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'version': os.getenv('APP_VERSION', '1.0.0'),
        'timestamp': datetime.datetime.now().isoformat()
    })

@app.route('/version')
def version():
    """Version information endpoint."""
    return jsonify({
        'app_version': os.getenv('APP_VERSION', '1.0.0'),
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'build_number': os.getenv('BUILD_NUMBER', 'local'),
        'git_commit': os.getenv('GIT_COMMIT', 'unknown')
    })
# Add this broken code to test failure
def broken_function():
    return undefined_variable  # This will cause an error

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)