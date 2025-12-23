from flask import Flask, jsonify, render_template, request, stream_with_context, Response
from model.inference import generate_response, stream_generate_response
from mlx_lm import load


app = Flask(__name__)

MODEL_PATH = "/Users/vinhpham/Desktop/VNUK_Chatbot/model/mlx_model_q6"
model, tokenizer = load(MODEL_PATH)
print(f"Model {MODEL_PATH} đã được tải thành công trên MLX.")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    return Response(
        stream_with_context(
            stream_generate_response(data, model, tokenizer)
        ),
        mimetype="text/plain"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=False)
