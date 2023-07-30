from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/healthz')
def healthz():
    return {
        'o': 'k'
    }
    
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)