from flask import Flask, request, render_template, jsonify
import requests
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/getSettings', methods=['POST'])
def get_settings():
    data = request.json
    id_instance = data.get('idInstance')
    api_token_instance = data.get('apiTokenInstance')
    base_url = f'https://7103.api.greenapi.com/waInstance{id_instance}/getSettings/{api_token_instance}'

    try:
        response = requests.get(base_url)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.RequestException as e:
        logging.error(f'Error response: {e.response.text if e.response else "No response"}')
        error_message = e.response.json().get('message', 'No response') if e.response else 'No response'
        return jsonify({'error': str(e), 'message': error_message}), 400

@app.route('/api/getStateInstance', methods=['POST'])
def get_state_instance():
    data = request.json
    id_instance = data.get('idInstance')
    api_token_instance = data.get('apiTokenInstance')
    base_url = f'https://7103.api.greenapi.com/waInstance{id_instance}/getStateInstance/{api_token_instance}'

    try:
        response = requests.get(base_url)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.RequestException as e:
        logging.error(f'Error response: {e.response.text if e.response else "No response"}')
        error_message = e.response.json().get('message', 'No response') if e.response else 'No response'
        return jsonify({'error': str(e), 'message': error_message}), 400

@app.route('/api/sendMessage', methods=['POST'])
def send_message():
    data = request.json
    id_instance = data.get('idInstance')
    api_token_instance = data.get('apiTokenInstance')
    base_url = f'https://7103.api.greenapi.com/waInstance{id_instance}/sendMessage/{api_token_instance}'

    params = {
        'chatId': data['params']['chatId'],
        'message': data['params']['message']
    }
    logging.debug(f'Sending message with params: {params}')
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(base_url, headers=headers, json=params)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.RequestException as e:
        logging.error(f'Error response: {e.response.text if e.response else "No response"}')
        error_message = e.response.json().get('message', 'No response') if e.response else 'No response'
        return jsonify({'error': str(e), 'message': error_message}), 400

@app.route('/api/sendFileByUrl', methods=['POST'])
def send_file_by_url():
    data = request.json
    id_instance = data.get('idInstance')
    api_token_instance = data.get('apiTokenInstance')
    base_url = f'https://7103.api.greenapi.com/waInstance{id_instance}/sendFileByUrl/{api_token_instance}'

    params = {
        'chatId': data['params']['chatId'],
        'urlFile': data['params']['urlFile'],
        'fileName': data['params']['fileName'],
        'caption': data['params'].get('caption', '')
    }
    logging.debug(f'Sending file with params: {params}')
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(base_url, headers=headers, json=params)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.RequestException as e:
        logging.error(f'Error response: {e.response.text if e.response else "No response"}')
        error_message = e.response.json().get('message', 'No response') if e.response else 'No response'
        return jsonify({'error': str(e), 'message': error_message}), 400

if __name__ == '__main__':
    app.run(debug=True)
