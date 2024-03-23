from flask import Flask, request, jsonify
from flask_cors import CORS
from object_detection import detect_objects
import base64

app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5000"}})  # Allow requests from localhost:3000 for routes starting with /api/

# Route for image upload and object detection
@app.route('/upload', methods=['POST'])
def upload():
    try:
        # Get the uploaded image from the request
        image_data = request.json['image']
        
        # Decode base64 image data
        image_data = base64.b64decode(image_data.split(',')[1])
        
        # Perform object detection
        predictions, vehicle_count = detect_objects(image_data)
        
        # Return the predictions and vehicle count as JSON response
        return jsonify({'predictions': predictions, 'vehicle_count': vehicle_count})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
