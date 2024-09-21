# BUild server image
docker build -f ./Server_Dockerfile -t sonhm232901/flask_server .

# Build client image
docker build -f ./Client_Dockerfile -t sonhm232901/streamlit_client .

# Run server container
docker run -d -p 8000:8000 --name flask_server sonhm232901/flask_server -v ./server:/app

# Run Client container
docker run -d -p 8501:8501 --name streamlit_client sonhm2329201/streamlit_client