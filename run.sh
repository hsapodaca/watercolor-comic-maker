echo "Installing required modules"
pip install -r requirements.txt

echo "Setting up Flask"
export FLASK_ENV=development
export FLASK_APP=app.py

echo "Starting server on port 5000"
flask run