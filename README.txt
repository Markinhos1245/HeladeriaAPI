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
- Pytest

---

Instalación:

```bash
pip install -r requirements.txt