# 🚀 Creación de API - Grupo 3
## 👥 Integrantes
- Erik Flores
- Cristian
- Klever
---
  ## 📌 Descripción del Proyecto
Esta API REST, desarrollada en Python, permite analizar sitios web mediante la extracción y procesamiento de contenido HTML. A partir de estos datos, el sistema genera métricas relevantes y devuelve resultados estructurados con indicadores de calidad (scores), facilitando la evaluación técnica y de contenido de páginas web.

## Funcionamiento de API localmente

<img width="723" height="126" alt="image" src="https://github.com/user-attachments/assets/897500bd-cbff-4657-902a-df1c1126a76c" />

<img width="990" height="250" alt="image" src="https://github.com/user-attachments/assets/56f0ec88-59c3-4af6-ad94-e0a4c02cec98" />

<img width="563" height="168" alt="image" src="https://github.com/user-attachments/assets/6c860499-8061-4ba5-860b-bb251ed2f66f" />

Las imágenes muestran la implementación, ejecución y verificación del endpoint /health dentro de la API desarrollada con FastAPI.

En la parte superior se observa el fragmento de código correspondiente al endpoint, donde se define una función que devuelve el estado de la API junto con un timestamp en la zona horaria UTC-5. Este endpoint responde con un mensaje personalizado indicando que la API se encuentra en funcionamiento.

En la sección central se visualiza la terminal de ejecución, donde se inicia el servidor utilizando Uvicorn en el puerto 8080. Los logs confirman que:

El servidor se ha iniciado correctamente
La aplicación está lista para recibir solicitudes
Se realizó una petición HTTP GET al endpoint /health
La respuesta fue exitosa con código 200 OK

 ## Funcionalidades de API-Endpoints

### `GET /health`

Valida que la API está activa.

### `POST /analyze-site`

Entrada:

```json
{
  "url": "https://example.com"
}
```

Salida (resumen):

- datos de respuesta HTTP,
- métricas de estructura HTML,
- análisis de texto limpio,
- scores,
- issues y recommendations,
- campo opcional `ai_insights` (solo si hay integración IA disponible).

### `POST /compare-sites`

Entrada:

```json
{
  "urls": ["https://example.com", "https://python.org"]
}
```

Salida:

- resultados por sitio,
- ranking por `overall_score`,
- observaciones comparativas agregadas.

## Ejemplos con curl

### Health

```bash
curl -X GET "http://localhost:8080/health"
```

### Análisis de un sitio

```bash
curl -X POST "http://localhost:8000/analyze-site" \
  -H "Content-Type: application/json" \
  -d "{\"url\":\"https://sitio.com\"}"
```

### Comparación de sitios

```bash
curl -X POST "http://localhost:8080/compare-sites" \
  -H "Content-Type: application/json" \
  -d "{\"urls\":[\"https://sitio1.com\",\"https://python.org\",\"https://fastapi.tiangolo.com\"]}"
```
## Construcción de imagen Docke

## Contenedor Ejecutandose

## Pruebas Curl exitosas
### Prueba 1 - curl -X GET "http://localhost:8080/health"
<img width="879" height="62" alt="image" src="https://github.com/user-attachments/assets/f964550d-c196-4d0b-889b-afcf6e969c38" />


## Uso de Branches
<img width="289" height="295" alt="image" src="https://github.com/user-attachments/assets/ec09dca5-b1c4-4f01-8e8a-d6475d7b5d6c" />

