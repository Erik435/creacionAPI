# Web Insight API

API REST en Python para analizar sitios web, transformar datos HTML en métricas y devolver resultados estructurados con scores claros.

## Objetivo

Recibir una o varias URLs, extraer información técnica y de contenido, procesarla y devolver:

- métricas de estructura y contenido,
- detección de problemas frecuentes,
- recomendaciones prácticas,
- scores interpretables (SEO, accesibilidad, calidad de contenido y score global),
- enriquecimiento opcional con IA.

## Tecnologías

- Python 3.12
- FastAPI
- httpx
- BeautifulSoup4
- Pydantic
- logging (librería estándar)
- Docker
- pytest

## Estructura del proyecto

```text
.
├── app
│   ├── main.py
│   ├── schemas
│   │   ├── __init__.py
│   │   └── analysis.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── ai_enrichment.py
│   │   ├── analyzer.py
│   │   ├── scoring.py
│   │   ├── text_processing.py
│   │   └── web_scraper.py
│   └── utils
│       ├── __init__.py
│       └── logger.py
├── tests
│   └── test_api.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows PowerShell
pip install -r requirements.txt
```

## Ejecución local

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Documentación automática:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Endpoints

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
curl -X GET "http://localhost:8000/health"
```

### Análisis de un sitio

```bash
curl -X POST "http://localhost:8000/analyze-site" \
  -H "Content-Type: application/json" \
  -d "{\"url\":\"https://example.com\"}"
```

### Comparación de sitios

```bash
curl -X POST "http://localhost:8000/compare-sites" \
  -H "Content-Type: application/json" \
  -d "{\"urls\":[\"https://example.com\",\"https://python.org\",\"https://fastapi.tiangolo.com\"]}"
```

## Uso con Docker

Construcción:

```bash
docker build -t web-insight-api .
```

Ejecución:

```bash
docker run --rm -p 8000:8000 web-insight-api
```

## Explicación breve de los scores

La API calcula cuatro scores entre 0 y 100:

- `seo_score`: valora título, meta descripción, presencia de H1 y estado HTTP.
- `accessibility_score`: penaliza imágenes sin `alt` y falta de encabezados de apoyo.
- `content_quality_score`: considera volumen de texto, enlaces internos y uso de HTTPS.
- `overall_score`: combinación ponderada:
  - 40% SEO
  - 25% Accesibilidad
  - 35% Calidad de contenido

Las reglas están implementadas en `app/services/scoring.py` de forma explícita para facilitar trazabilidad.

## Integración opcional con IA (Gemini)

La API funciona completamente sin IA. Si se desea enriquecer la salida de `analyze-site`, se pueden configurar:

- `GEMINI_API_KEY`
- `GEMINI_API_URL` (opcional)
- `GEMINI_MODEL` (opcional)

Cuando está configurado, se intenta completar:

- tipo de sitio,
- tema principal,
- resumen corto,
- recomendaciones semánticas.

Si la llamada a IA falla, la API continúa con el análisis base sin interrumpir el servicio.

## Pruebas

```bash
python -m pytest -q
```
