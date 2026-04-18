#!/bin/bash
# Render Deployment Script for University Policy Assistant Backend

echo "🚀 Starting Render deployment process..."

# Check if required environment variables are set
if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ Error: OPENAI_API_KEY environment variable is not set"
    echo "Please set it in your Render dashboard under Environment"
    exit 1
fi

echo "✅ Environment variables configured"

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Run any database migrations or setup (if needed)
echo "🗄️ Setting up data directories..."
mkdir -p data/vectorstore/faiss_index
mkdir -p data/logs
mkdir -p data/processed

echo "🎉 Backend deployment setup complete!"
echo "The application will start with: uvicorn app.api.main:app --host 0.0.0.0 --port \$PORT"