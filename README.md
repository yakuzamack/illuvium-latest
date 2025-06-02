# Illuvium Latest

A Flask web application for the Illuvium game website that serves as a proxy and content handler.

## 🚨 Important Notice

**This is a Flask application that requires Python server execution. GitHub Pages only supports static websites and cannot run this application.**

## Project Structure

This is a Flask-based web application that serves as a proxy and content handler for Illuvium game assets and pages.

### Key Components

- **app.py**: Main Flask application with routing and configuration
- **modules/**: Python modules for various functionality
  - `static_files.py`: Handles static file serving and proxying
  - `security_headers.py`: Security headers and CORS configuration
  - `content_proxy.py`: Content proxying and modification
  - `image_handler.py`: Image processing and optimization
  - `ip_validation.py`: IP validation and filtering
- **templates/**: HTML templates
- **static/**: Static assets (CSS, JavaScript, etc.)
- **images/**: Image assets

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yakuzamack/illuvium-latest.git
   cd illuvium-latest
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

The application will be available at `http://localhost:8000`

## Deployment Options

### Recommended Hosting Platforms

Since this is a Flask application, you'll need a platform that supports Python:

#### 1. **Railway** (Recommended)
- Connect your GitHub repository
- Automatic deployment on push
- Free tier available

#### 2. **Render**
- Connect GitHub repository
- Set build command: `pip install -r requirements.txt`
- Set start command: `gunicorn wsgi:app`

#### 3. **Heroku**
```bash
# Install Heroku CLI
heroku create your-app-name
git push heroku main
```

#### 4. **Vercel** (with Python runtime)
- Connect GitHub repository
- Configure for Python runtime

#### 5. **PythonAnywhere**
- Upload files manually
- Configure WSGI application

### Environment Variables

For production deployment, set these environment variables:
- `FLASK_ENV=production`
- `PORT=8000` (or as required by platform)

## Features

- Content proxying from original Illuvium site
- Static file handling and optimization
- Image processing and caching
- Security headers and CORS handling
- Dynamic content modification
- Cross-origin resource sharing support

## Development

For local development:

```bash
# Enable debug mode
export FLASK_ENV=development
python app.py
```

## Production Configuration

For production deployment:

1. Set `debug=False` in app.py (or use environment variables)
2. Use a production WSGI server like Gunicorn:
   ```bash
   gunicorn wsgi:app --bind 0.0.0.0:$PORT
   ```
3. Configure proper security headers
4. Set up SSL/TLS certificates

## GitHub Pages Alternative

To deploy on GitHub Pages, you would need to completely rewrite the application as a static site:

1. Convert Flask templates to static HTML files
2. Remove all server-side Python logic
3. Use only client-side JavaScript for dynamic features
4. Serve assets directly without proxying

This would be a significant rewrite and would lose most of the current functionality.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

Please ensure you have proper rights to use Illuvium game assets and content.

## Support

For issues and questions:
- Create an issue in this repository
- Check the application logs for error messages
- Ensure all dependencies are properly installed