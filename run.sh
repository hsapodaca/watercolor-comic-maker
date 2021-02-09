echo "Installing required modules"
pip install -r requirements.txt

echo "Running tests"
python -m pytest hsapodaca/test

echo "Starting server on port 8888"
 uvicorn hsapodaca.src.main:app --host 0.0.0.0 --port 8888