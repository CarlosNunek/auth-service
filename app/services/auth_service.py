import redis
from config import REDIS_HOST, REDIS_PORT

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def publicar_usuario_registrado(cedula):
    mensaje = f"usuario registrado: {cedula}"
    redis_client.publish("usuarios", mensaje)
    print(f"📢 Evento enviado a Redis → {mensaje}")