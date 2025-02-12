from flask import Flask, request, render_template, jsonify, session
import openai
import os

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "supersecretkey")

# Carrega a chave da API do OpenAI a partir das variáveis de ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")

# Função para melhorar a comunicação escrita
def improve_communication(text):
    if not text:
        return "O texto não pode estar vazio."
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": (
            "Você é um assistente especializado em melhorar a comunicação escrita, tornando-a clara, objetiva e profissional. "
            "Procure sempre ser humilde e empático."
            "utilize emojis para reforçar a mensagem." 
            "Mantenha o significado original da mensagem e evite qualquer alteração que possa mudar sua intenção. "
            "Se houver termos técnicos em inglês, preserve-os. "
            )},
            {"role": "user", "content": f"Reformule a seguinte frase para torná-la mais clara e eficaz: {text}"}
        ],
        temperature=0.3,
        max_tokens=500
    )
    return response["choices"][0]["message"]["content"].strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'greeted' not in session:
        session['greeted'] = []
    
    if request.method == 'POST':
        input_text = request.form.get('text', '').strip()
        if not input_text:
            return jsonify({"error": "O texto não pode estar vazio."}), 400

        improved_text = improve_communication(input_text)
        return jsonify({"corrected_text": improved_text})
    
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    user = request.form.get('user', '').strip()
    if user and user not in session['greeted']:
        session['greeted'].append(user)
        return jsonify({"greeting": f"Oi, {user}!"})
    return jsonify({"greeting": ""})

if __name__ == '__main__':
    app.run(debug=True)

