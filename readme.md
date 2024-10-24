# API Test with Python
A web application to play around with API's in Python (and also to try integrating React)

## Usage Steps
Since we are running a React frontend with a python API (in this case FastAPI), we need to start both and have them running at the same time.
**you need to have 2 terminals for this to work**
### Starting python API
1. Type "uvicorn app:app --host localhost --port 5000 --reload" in terminal

### Starting React frontend
1. cd react
2. npm run dev