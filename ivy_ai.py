# 🔹 Installa le librerie necessarie
from flask import Flask, request, jsonify
from transformers import pipeline

# 🔹 Crea l'app Flask
app = Flask(__name__)

# 🔹 Modello NLP per generare risposte
nlp_ai = pipeline("text-generation", model="distilgpt2")

@app.route("/ivy_ai", methods=["POST"])
def ivy_ai():
    data = request.json
    domanda = data.get("domanda", "")
    risposta = nlp_ai(domanda, max_length=50, do_sample=True)[0]["generated_text"]
    return jsonify({"risposta": risposta})

# 🔹 Avvia il server Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
