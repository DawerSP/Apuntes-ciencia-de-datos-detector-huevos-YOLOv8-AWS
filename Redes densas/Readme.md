Detector de Huevos en Tiempo Real (Sano vs. Roto)


Sistema de Visión Artificial e Inteligencia Artificial Desplegado en AWS EC2Este proyecto implementa un sistema completo de Visión por Computador y Deep Learning capaz de detectar y clasificar huevos en tiempo real como SANO, ROTO o en REVISIÓN, utilizando la cámara de un dispositivo móvil o computadora.


 Demostración y Arquitectura del SistemaEl flujo de trabajo abarca desde la captura del frame hasta la inferencia en la nube:[ Dispositivo Móvil / Laptop ]
            │ (Video Stream / Frames en JPEG)
            ▼
[ Cliente Web (HTML5 Canvas + JS Fetch) ]
            │ (POST /predict)
            ▼
[ Servidor AWS EC2 (Ubuntu 24.04 LTS) ]
    ├── FastAPI App (ASGI Server - Uvicorn)
    ├── Modelo YOLOv8 (Ultralytics - Deep Learning)
    └── Visión por Computador (OpenCV & NumPy)
            │ (Coordenadas Bounding Boxes + Diagnóstico)
            ▼
[ Overlay Dibujado en Tiempo Real ]


 Tecnologías UtilizadasLenguaje: Python 3.12+Deep Learning Framework: Ultralytics YOLOv8 (PyTorch)Visión por Computador: OpenCV, NumPyBackend API: FastAPI, UvicornCloud Platform: Amazon Web Services (AWS EC2 - AWS Academy)Sistema Operativo Servidor: Ubuntu 24.04 LTSFrontend: HTML5, CSS3, JavaScript (Fetch API, WebRTC MediaDevices)
 
 
  Puntos Claves Realizados en la Práctica (AWS EC2)Configuración de la Instancia EC2 en AWS:Creación y aprovisionamiento de una instancia Ubuntu Server en la nube.Configuración del Grupo de Seguridad (Security Group) para permitir tráfico SSH (Puerto 22) e Inbound HTTP en el puerto 8000.Conexión remota segura vía SSH utilizando llaves de autenticación privada (.pem).Despliegue del Modelo e Inferencia backend:Carga y optimización del modelo preentrenado best.pt con YOLOv8.Desarrollo de un servicio backend de alto rendimiento con FastAPI para procesar multi-part form requests con cuadros de imagen decodificados al vuelo con OpenCV (cv2.imdecode).
  
  
  Lógica de Visión por Computador & Calibración Anti-Sesgo:Implementación de análisis espacial de Bounding Boxes e Intersección sobre Unión (IoU).Eliminación del sesgo de color (evitando la confusión entre cáscaras marrones/blancas y roturas físicas).Lógica condicional de estados por nivel de confianza ($Confidence Thresholds$):SANO: Huevo detectado sin evidencia de discontinuidad en la superficie.ROTO: Detección de fisura/grieta con $Confianza \ge 50\%$.REVISIÓN: Indicios leves de imperfección con $30\% \le Confianza < 50\%$.Automatización como Servicio del Sistema (Systemd):Configuración de un Demonio/Servicio systemd (egg-detector.service) en Linux para garantizar ejecución 24/7 en segundo plano y reinicio automático ante fallos de la instancia.
 
  Estructura del Proyecto.
├── main.py              # Código fuente principal (FastAPI + YOLOv8 + Dashboard Web)
├── best.pt              # Pesos del modelo entrenado YOLOv8
├── requirements.txt     # Dependencias del proyecto Python
├── .gitignore           # Archivos ignorados por Git (entornos virtuales, keys, etc.)
└── README.md            # Documentación del proyecto
🔧 Instalación y Ejecución LocalClonar el repositorio:git clone https://github.com/DawerSPMain/Apuntes-Ciencia-de-Datos-nuevo.git
cd Apuntes-Ciencia-de-Datos-nuevo
Crear y activar entorno virtual:python -m venv .venv
# En Windows:
.venv\Scripts\activate
# En Linux/Mac:
source .venv/bin/activate
Instalar dependencias:pip install -r requirements.txt
Ejecutar servidor de desarrollo:uvicorn main:app --host 0.0.0.0 --port 8000 --reload
Abrir el navegador en http://localhost:8000.🌐 Comandos de Administración en AWS EC2Para conectarse al servidor y verificar el estado del servicio en tiempo real:Conexión por SSH:ssh -i ruta/de/tu-clave.pem ubuntu@52.54.184.190
Reiniciar el servicio en la nube:sudo systemctl restart egg-detector
Ver los logs de ejecución:sudo journalctl -u egg-detector -f


 AutorProyecto desarrollado para la materia de Ciencia de Datos / Inteligencia Artificial