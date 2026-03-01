from flask import Flask, request, jsonify
from models import calcular_riesgo_crediticio

app = Flask(__name__)
@app.route('/')
def inicio():
    return "funcionando"


@app.route('/api/evaluar-credito', methods=['POST'])
def evaluar_credito():
    data = request.get_json()
    
    # Validación básica (Capa de Controlador)
    if not data or 'salario_smmlv' not in data:
        return jsonify({"error": "Datos incompletos"}), 400
        
    try:
        salario = float(data['salario_smmlv'])
        reportes = bool(data['tiene_reportes'])
        historial = int(data['anos_historial'])
        
        # Llamada al Modelo
        resultado = calcular_riesgo_crediticio(salario, reportes, historial)
        
        return jsonify({"estado_credito": resultado}), 200
        
    except ValueError:
        return jsonify({"error": "Tipos de datos inválidos"}), 400

if __name__ == '__main__':
    app.run(debug=True)