# run.py

import os
import uvicorn

if __name__ == "__main__":
    # Check if the app is running inside a container
    host = "0.0.0.0"  # Expose to all IP addresses (needed for Docker containers)
    port = 8000

    # Run FastAPI app using Uvicorn
    uvicorn.run("app.main:app", host=host, port=port, reload=True)
