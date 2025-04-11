from flask import Flask, request, render_template, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the Deepfake Detection Model
deepfake_detector = pipeline("image-classification", model="Wvolf/ViT_Deepfake_Detection")
print("✅ Model loaded successfully!")

@app.route('/')
def index():
    # Serve the HTML page
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    try:
        # Retrieve uploaded image
        image_file = request.files['image']
        image_path = "uploaded_image.jpg"  # Save the uploaded image locally
        image_file.save(image_path)

        # Perform deepfake detection
        result = deepfake_detector(image_path)
        prediction = max(result, key=lambda x: x['score'])  # Find label with highest confidence
        label = prediction['label']
        confidence = prediction['score'] * 100  # Convert confidence score to percentage

        # Return detection result as JSON
        return jsonify({"label": label, "confidence": confidence})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
