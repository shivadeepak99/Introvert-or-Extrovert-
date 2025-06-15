from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("introvert.pkl")

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")  # Serve your frontend HTML file

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get data from request (handles both JSON and form data)
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form

        # Extract features in the correct order
        features = [
            int(data.get('aloneTime', 0)),      # Time spent alone
            int(data.get('stageFear', 0)),      # Stage fear (1=yes, 0=no)
            int(data.get('socialEvents', 0)),   # Social event attendance
            int(data.get('outsideFrequency', 0)),# Going outside frequency
            int(data.get('drained', 1)),        # Feeling drained (1=yes, 0=no)
            int(data.get('friendsCircle', 0)),  # Friends circle size
            int(data.get('socialMedia', 0))     # Social media post frequency
        ]

        # Convert to numpy array and reshape for prediction
        features_array = np.array(features).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features_array)[0]

        # Map numeric prediction to personality type
        personality = "Introvert" if prediction == 0 else "Extrovert"

        return jsonify({"personality": personality})

    except Exception as e:
        print(f"Prediction error: {str(e)}")
        return jsonify({"error": "Prediction failed", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)