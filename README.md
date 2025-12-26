# AI Chatbot VNUK by GOAT AI
⚠️ Platform Limitation: This application currently only runs on Apple Silicon. Windows support is not yet available and will be added in a future release.
##
An AI-powered chatbot assistant for VNUK Institute, designed to help students and prospective students with information about academic programs, admissions, scholarships, and study abroad opportunities.

## Demo
Following this link: **https://drive.google.com/file/d/1enQHBHcWwBxt1Oz1E7KDDWKlwDDuv9KQ/view?usp=drive_link**
## 🎯 Overview

This chatbot provides an intelligent, conversational interface for answering questions about VNUK Institute. It uses a fine-tuned LLaMA 3 model optimized with Apple's MLX framework for efficient inference, enabling fast and responsive interactions.

## ✨ Features

- **Interactive Chat Interface**: Modern, user-friendly web interface with real-time streaming responses
- **Category-Based Navigation**: Quick access to information about:
  - Academic Programs
  - Scholarships & Tuition
- **Streaming Responses**: Real-time text generation for a smooth conversational experience
- **MLX-Optimized**: Uses Apple's MLX framework for efficient model inference on Apple Silicon
- **Responsive Design**: Clean, modern UI with smooth animations and transitions

## 🧠 Model Summary & Performance
The chatbot is powered by the Meta-Llama-3-8B-Instruct architecture, representing the cutting edge of open-source local LLMs.
### 🔬 Technical Specifications
- Base Model: Meta-Llama-3-8B-Instruct
- Architecture: Optimized Transformer with Grouped-Query Attention (GQA).
- Quantization: 6-bit (Q6_K) via MLX (balancing speed and reasoning depth).
- Context Length: 8,192 tokens.
- Training Foundation: 15 Trillion+ tokens.
### 📊 Baseline Model Performance (Reported by Meta)
The following metrics are baseline results of the original Meta-Llama-3-8B-Instruct model, as reported by Meta AI. These results are provided for reference only and serve as a comparison point for downstream fine-tuning.
| Benchmark              | Evaluation Setting | Score |
|------------------------|--------------------|-------|
| **MMLU**               | 5-shot             | ~68.4 |
| **ARC Challenge**      | Few-shot           | ~59.4 |
| **HellaSwag**          | Zero/Few-shot      | ~82.8 |
| **GSM8K**              | 8-shot             | ~77.4 |
| **TruthfulQA**         | 0-shot             | ~58.1 |
| **WinoGrande**         | Zero/Few-shot      | ~77.9 |

**Note:**  
These scores are reported by Meta AI for the **Meta-Llama-3-8B-Instruct** base model and are provided for reference only. Actual performance may vary after fine-tuning, quantization, and deployment using MLX on Apple Silicon.

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **ML Framework**: MLX (Apple's machine learning framework)
- **Model**: Fine-tuned LLaMA 3 (converted to MLX format with 6-bit quantization)
- **Frontend**: HTML, CSS, JavaScript
- **Dependencies**: 
  - `flask` - Web framework
  - `mlx-ml` - MLX machine learning library
  - `torch`, `transformers`, `accelerate`, `bitsandbytes` - Additional ML dependencies

## 📋 Prerequisites

Before setting up the project, ensure you have:
- **macOS with Apple Silicon** (M1/M2/M3) - MLX is optimized for Apple hardware
- **pip** package manager
- **MLX Model**: A converted MLX model file (see Model Setup section)

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/VinhPham131/AI-Chatbot-VNUK.git
cd AI-Chatbot-VNUK
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Model Setup
While using MLX, you need to convert a model from HuggingFace:

1. Edit `model/convert.py` to specify your HuggingFace repository and output path
2. Run the conversion script:

```bash
python model/convert.py
```

This will download and convert the model to MLX format with 6-bit quantization.

**Note**: The default model path in `app.py` is set to `/Users/vinhpham/Desktop/VNUK_Chatbot/model/mlx_model_q6`. Update this path to match your model location.
```python
repo = #Replace with your model path
upload_repo = #Replace with your desired output path
```

### 5. Update Model Path

Edit `app.py` and update the `MODEL_PATH` variable to point to your MLX model:

```python
MODEL_PATH = "/path/to/your/mlx_model"
```

## 🎮 Usage

### Running the Application

1. Start the Flask server:

```bash
python app.py
```

2. Open your web browser and navigate to:

```
http://localhost:3000
```

3. The chatbot interface will load with a welcome screen. Click "Start Conversation" or select a category to begin.

### Using the Chatbot

- **Select a Category**: Choose from the available categories to get started
- **Ask Questions**: Type your question in the input field and press Enter or click the send button
- **Streaming Responses**: Responses will appear in real-time as they are generated
- **Clear Chat**: Use the clear button in the header to reset the conversation

## 📁 Project Structure

```
AI-Chatbot-VNUK/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── model/
│   ├── convert.py         # Model conversion script
│   ├── inference.py       # Model inference functions
│   └── dataset/           # Training datasets
│       └── vnuk_dataset.jsonl
├── static/
│   ├── css/
│   │   └── style.css      # Stylesheet
│   └── images/
│       └── logo.png       # VNUK logo
└── templates/
    └── index.html         # Main HTML template
```

## ⚙️ Configuration

### Model Parameters

You can adjust generation parameters in the frontend JavaScript (in `templates/index.html`):

- `max_tokens`: Maximum number of tokens to generate (default: 512)

### Server Configuration

Edit `app.py` to change:
- **Host**: Default is `0.0.0.0` (accessible from all network interfaces)
- **Port**: Default is `3000`
- **Debug Mode**: Set to `True` for development (currently `False`)

## 🔧 Troubleshooting

### Model Not Found Error
- Ensure the `MODEL_PATH` in `app.py` points to a valid MLX model directory
- Verify the model was converted successfully

### Import Errors
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Verify you're using the correct Python version (3.8+)

### MLX Compatibility
- MLX is optimized for Apple Silicon. For other platforms, you may need to use alternative inference methods
- Ensure you're running on macOS with Apple Silicon (M1/M2/M3/M4)

### Port Already in Use
- Change the port number in `app.py` if port 3000 is already in use
- Or stop the process using that port

## 📝 Notes

- The model uses 6-bit quantization for efficient inference while maintaining good performance
- Streaming responses provide a better user experience by showing text as it's generated
- The chatbot is designed specifically for VNUK Institute information and may not perform well on unrelated topics

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 👥 Authors
### Product made by GOAT AI
- Phạm Quang Vinh
- Nguyễn Minh Nhân
- Phạm Nguyễn Huy Minh