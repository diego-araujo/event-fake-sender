import json
import os
import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template

load_dotenv()

app = Flask(__name__)

# Caminho para a pasta de arquivos JSON, agora relativo ao arquivo app.py
JSON_FILES_DIR = os.path.join(os.path.dirname(__file__), 'json_files')
BACKEND_URL = os.getenv('BACKEND_URL')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/send/<notification_type>', methods=['POST'])
def send_notification(notification_type):
    """
    Endpoint para enviar notificações
    notification_type pode ser: transito, video, acidente
    """
    file_path = os.path.join(JSON_FILES_DIR, f"{notification_type}.json")

    if not os.path.exists( file_path):
        return jsonify({'error': f'Arquivo {notification_type}.json não encontrado'}), 404
    

    try:
        # Ler o arquivo JSON
        with open(file_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)

        # Enviar dados para o backend se a URL estiver configurada
        if not BACKEND_URL:
            return jsonify({'error': 'URL do backend não configurada'}), 500

        try:
            response = requests.post(BACKEND_URL, json=json_data, timeout=10)
            response.raise_for_status()

            backend_response = {}
            if response.text and response.headers.get('Content-Type') == 'application/json':
                backend_response = response.json()

            return jsonify({
                'success': True,
                'message': f'Notificação {notification_type} enviada com sucesso para o backend',
                'backend_status': response.status_code,
                'backend_response': backend_response
            }), 200

        except requests.exceptions.RequestException as e:
            return jsonify({'error': f'Erro ao enviar para o backend: {str(e)}'}), 500
        
    except json.JSONDecodeError as e:
        return jsonify({'error': f'Erro ao ler JSON: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Erro ao processar: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

