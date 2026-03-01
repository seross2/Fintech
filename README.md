curl -X POST http://127.0.0.1:5000/api/evaluar-credito \
-H "Content-Type: application/json" \
-d '{"salario_smmlv": 3.0, "tiene_reportes": false, "anos_historial": 2}'


curl -X POST http://127.0.0.1:5000/api/evaluar-credito \
-H "Content-Type: application/json" \
-d '{"salario_smmlv": 5.0, "tiene_reportes": false, "anos_historial": 3}'


curl -X POST http://127.0.0.1:5000/api/evaluar-credito \
-H "Content-Type: application/json" \
-d '{"salario_smmlv": 1.5, "tiene_reportes": true, "anos_historial": 2}'