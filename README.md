# 🦋 Introvert vs. Extrovert Predictor 🧌

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.2-lightgrey.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.2.2-orange.svg)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.0-38B2AC?logo=tailwind-css&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)

A modern, responsive, and beautifully designed AI-powered web application that predicts whether you are an **Introvert** or an **Extrovert** based on your behavioral habits. It uses a trained Machine Learning model (Logistic Regression) with an engaging Tailwind CSS frontend.

## ✨ Features

- **🧠 Machine Learning Integration**: Predictions are made using a Scikit-Learn Logistic Regression model (`introvert.pkl`) trained on behavioral data.
- **🎨 Beautiful UI/UX**: An elegant, dynamic interface built with vanilla HTML and Tailwind CSS, featuring floating shapes, micro-animations, and interactive sliders.
- **🌗 Dark Mode Support**: Seamless toggle between light and dark themes, saved to your local preferences.
- **🐳 Dockerized**: Fully containerized with a production-ready Docker setup using `gunicorn`.
- **⚡ Fast and Lightweight**: Built with Flask to serve the model quickly via a RESTful API.

## 🛠️ Tech Stack

- **Backend**: Python, Flask, Gunicorn
- **Machine Learning**: Scikit-Learn, Pandas, NumPy, Joblib
- **Frontend**: HTML5, Tailwind CSS (via CDN)
- **Deployment**: Docker

## 🚀 Getting Started

You can run this application directly using Python or seamlessly with Docker.

### 📋 Prerequisites

- Python 3.9+
- Docker (optional, but recommended)

### 💻 Local Setup

1. **Clone the repository** (or navigate to the project directory):
   ```bash
   cd Introvert-or-Extrovert-
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```
   The application will be available at `http://localhost:10000`.

### 🐳 Docker Setup

This project includes a `Dockerfile` for easy deployment.

1. **Build the Docker image**:
   ```bash
   docker build -t personality-predictor .
   ```

2. **Run the container**:
   ```bash
   docker run -p 10000:10000 personality-predictor
   ```
   The application will be accessible at `http://localhost:10000`.

## 📁 Project Structure

```text
.
├── Dockerfile              # Docker configuration for production deployment
├── app.py                  # Main Flask application and API routes
├── introvert.pkl           # Pre-trained Scikit-Learn Logistic Regression model
├── requirements.txt        # Python dependencies
├── skyfire.ipynb           # Jupyter Notebook detailing data exploration and model training
└── templates/
    └── home.html           # The beautiful frontend UI
```

## 🧠 About the Model

The prediction model was trained using the `extrovert-vs-introvert-behavior-data` dataset.
- **Algorithm**: Logistic Regression
- **Data processing**: The features are numerically encoded. The parameters consider:
  - Time spent alone
  - Stage fear presence
  - Social event attendance frequency
  - Outdoor frequency
  - "Drained after socializing" feeling
  - Friends circle size
  - Social media post frequency

You can view the exact exploratory data analysis (EDA) and the training pipeline inside the `skyfire.ipynb` Jupyter Notebook.
