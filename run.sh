echo "Installing required modules"
pip install -r requirements.txt

echo "Setting up Flask"
export FLASK_ENV=development
export FLASK_APP=app.py

echo "Starting server on port 8888"
 uvicorn main:app --host 0.0.0.0 --port 8888