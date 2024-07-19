from flask import Flask, render_template, request, jsonify
from src.summarizer import summarize_paper
from config import Config
from pypdf import PdfReader
import os

app = Flask(__name__)
app.config.from_object(Config)


def read_file_content(file_path):
    # Read the file content as bytes
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    save_path = os.path.join("research", "data", "sample_papers", file.filename)
    file.save(save_path)
    model_choice = request.form.get("model", "bart")

    if file:
        try:
            # Read the file content using our new function
            content = read_file_content(save_path)
            # Generate summary
            summary = summarize_paper(content, model_choice)

            return jsonify({"summary": summary})
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            app.logger.error(f"An error occurred: {str(e)}")
            return jsonify(
                {"error": "An unexpected error occurred. Please try again."}
            ), 500


if __name__ == "__main__":
    app.run(debug=True)
