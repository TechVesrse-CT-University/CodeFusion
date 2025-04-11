# DeepBuzz: Deepfake Detection Tool

DeepBuzz is an AI-powered solution designed to detect deepfake images with precision and confidence. The tool uses cutting-edge machine learning models, along with web scraping integrations, to analyze whether an uploaded image is real or fake, providing a detailed confidence score. The solution prioritizes privacy, accessibility, and usability for users looking to safeguard their digital identities.

## Features
- **Deepfake Detection**:
  - Upload an image to determine whether it is real or a deepfake.
  - Powered by the `Wvolf/ViT_Deepfake_Detection` model from Hugging Face.
- **Confidence Score**:
  - The tool provides a confidence score to quantify its prediction.
- **Web Scraping**:
  - Utilizes SerpApi to search for images online based on keywords.
  - Integrates with ImgBB to securely upload and handle images.

## Technologies Used
- **Backend**: Flask for server-side logic and API endpoints.
- **Deepfake Detection Model**: `Wvolf/ViT_Deepfake_Detection` (Hugging Face Transformers).
- **Web Scraping Tools**:
  - **SerpApi**: Fetches image results from search engines.
  - **ImgBB**: Handles uploading and hosting of images.
- **Libraries**:
  - `transformers` and `torch` for model inference.
  - `Pillow` for image processing.
  - `requests` for API communication.

## Installation
### Prerequisites
- Python 3.8 or higher
- API keys for:
  - **SerpApi**: [Get your API key here](https://serpapi.com/).
  - **ImgBB**: [Get your API key here](https://api.imgbb.com/).

### Steps
1. Clone the repository:
   git clone https://github.com/TechVesrse-CT-University/CodeFusion
