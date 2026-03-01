import multiprocessing

# 1. Conexión: Escuchar en el puerto interno 8000
bind = "127.0.0.1:8000"

# 2. Desempeño: Cálculo automático de Workers (Hilos de trabajo)
workers = multiprocessing.cpu_count() * 2 + 1

# 3. Tipo de trabajador
threads = 2
worker_class = 'gthread'

# 4. Seguridad y Estabilidad (Timeout para evitar bloqueos)
timeout = 120

# 5. Registro de eventos (Logs)
loglevel = "info"
accesslog = "-"  
errorlog = "-"