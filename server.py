from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/start-chatbot', methods=['POST'])
def start_chatbot():
    try:
        # Run the Streamlit app
        subprocess.Popen(["streamlit", "run", "app.py"])
        return jsonify({"status": "success", "message": "Chatbot started"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
