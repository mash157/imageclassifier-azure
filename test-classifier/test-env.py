from dotenv import load_dotenv
import os

load_dotenv()
print(f'Endpoint: {os.getenv("PredictionEndpoint")}')
print(f'Key: {os.getenv("PredictionKey")[:10]}...')
print(f'ProjectID: {os.getenv("ProjectID")}')
print(f'ModelName: {os.getenv("ModelName")}')
