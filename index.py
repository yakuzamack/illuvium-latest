from app import app

# This is the entry point for Vercel
# Vercel will look for a variable named 'app' to serve
if __name__ == "__main__":
    app.run(debug=False)