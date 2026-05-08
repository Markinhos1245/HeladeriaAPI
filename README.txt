API Heladeria 

Este proyecto es una API REST desarrollada con Flask con el objetivo de simular una heladeria

Pautas del trabajo:

Desarrollar una aplicación web Single Page Application (SPA) inspirada en la aplicación Coffee Cart, en dos etapas progresivas:

### Etapa 1: Backend con APIs

Implementar un servidor backend que exponga una serie de APIs RESTful para gestionar un carrito de compras de una heladería.

### Requerimientos mínimos:

- Endpoints para:
  - Listar productos disponibles
  - Agregar productos al carrito
  - Eliminar productos del carrito
  - Calcular el total de la compra
- Persistencia inicial en memoria (sin base de datos)
- Documentación de las APIs (Swagger/OpenAPI)
- Tests unitarios de los endpoints principales

---

Tecnologías utilizadas:

- Python
- Flask
- Flasgger (Swagger/OpenAPI)

---

Instalación:


pip install -r requirements.txt

---

Uso:

Ejecutar terminal y cargar la carpeta del proyecto

Crear entorno virtual con python -m venv venv

Ejecutar scripts del entorno virtual con venv\Scripts\activate

Instalar los requirements con pip install -r requirements.txt

Ejecutar el servidor con python aplicacion.py

Abrir el navegador y pegar la direccion brindada

Para swagger usar http://127.0.0.1:5000/apidocs
