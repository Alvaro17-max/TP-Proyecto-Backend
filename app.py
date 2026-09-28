from flask import Flask
from src.routes.socios import socios_bp
from src.routes.canchas import canchas_bp, deportes_bp
from src.routes.reservas import reservas_bp

app = Flask(__name__)

app.register_blueprint(socios_bp)
app.register_blueprint(canchas_bp)
app.register_blueprint(deportes_bp)
app.register_blueprint(reservas_bp)

if __name__ == "__main__":
    app.run(port=5000, debug=True)