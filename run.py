from main import app

if __name__ == "__main__":
    from main.main import controller
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)