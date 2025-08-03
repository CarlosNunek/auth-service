# Imagen base
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos de requerimientos
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Exponer el puerto de Flask
EXPOSE 6000

# Comando por defecto
CMD ["python", "run.py"]
