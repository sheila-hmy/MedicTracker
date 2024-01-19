from flask import Flask, send_from_directory, jsonify

app = Flask(__name__, static_folder='frontend/dist')

@app.route('/api/data')
def get_data():
    # Ici, vous pourrez interagir avec votre base de données ou vos services
    return jsonify({'message': 'Données récupérées avec succès'})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("frontend/dist/" + path):
        return send_from_directory('frontend/dist', path)
    else:
        return send_from_directory('frontend/dist', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
