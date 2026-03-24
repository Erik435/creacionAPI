<div align="center">

# 🌐 Construcción y Despliegue de API REST
**Trabajo Académico — Grupo 3**

*Integrantes: Erik Flores • Cristian González • Klever*

</div>

---

> **📌 Descripción del Proyecto:**  
> Esta API REST, desarrollada en Python con FastAPI, permite analizar sitios web mediante la extracción y procesamiento de contenido HTML. A partir de estos datos, el sistema genera métricas relevantes y devuelve resultados estructurados con indicadores de calidad (scores), facilitando la evaluación técnica y de contenido de páginas web.

### 🎯 Características principales
* **Análisis detallado**: Extracción de métricas de sitios web de manera individual.
* **Comparativas automatizadas**: Contraste de métricas entre múltiples sitios con generación de ranking.
* **Evaluación de calidad**: Cálculo de *scores* basados en la estructura HTML y el rendimiento del contenido.

---

## 🚀 Endpoints Disponibles

A continuación se detallan los servicios expuestos por la API y ejemplos de consumo utilizando `curl`.

<details>
<summary><b>1. 🟢 Verificación de Estado (<code>GET /health</code>)</b></summary>
<br>

Valida que el servicio se encuentra activo y operando correctamente. Retorna un timestamp del servidor.

```bash
curl -X GET "http://localhost:8080/health"
```
</details>

<details>
<summary><b>2. 📊 Análisis de Sitio (<code>POST /analyze-site</code>)</b></summary>
<br>

Ejecuta el análisis profundo de una URL específica.

```bash
curl -X POST "http://localhost:8080/analyze-site" \
  -H "Content-Type: application/json" \
  -d '{"url":"https://sitio.com"}'
```
</details>

<details>
<summary><b>3. ⚖️ Comparación Múltiple (<code>POST /compare-sites</code>)</b></summary>
<br>

Evalúa un conjunto de URLs simultáneamente, devolviendo el ranking de calidad.

```bash
curl -X POST "http://localhost:8080/compare-sites" \
  -H "Content-Type: application/json" \
  -d '{"urls":["https://sitio1.com","https://python.org"]}'
```
</details>

---

<div align="center">

## 📸 Parte 6 — Evidencia del Proyecto

</div>

A continuación, se presenta la validación visual y funcional de los despliegues cumpliendo estrictamente con los requerimientos académicos.

### 1️⃣ API funcionando localmente

Se evidencia el correcto funcionamiento del servidor local mediante el framework FastAPI y servidor Uvicorn. Los logs demuestran que el servidor levanta sin errores y el endpoint `/health` responde con un código de estado `HTTP 200 OK`.

<table>
<tr>
  <td align="center"><b>Código del endpoint <code>/health</code></b></td>
</tr>
<tr>
  <td><img src="https://github.com/user-attachments/assets/897500bd-cbff-4657-902a-df1c1126a76c" width="100%"></td>
</tr>
<tr>
  <td align="center"><b>Ejecución del servidor local (Puerto 8080)</b></td>
</tr>
<tr>
  <td><img src="https://github.com/user-attachments/assets/56f0ec88-59c3-4af6-ad94-e0a4c02cec98" width="100%"></td>
</tr>
<tr>
  <td align="center"><b>Respuesta exitosa del endpoint</b></td>
</tr>
<tr>
  <td><img src="https://github.com/user-attachments/assets/6c860499-8061-4ba5-860b-bb251ed2f66f" width="100%"></td>
</tr>
</table>

### 2️⃣ Construcción de imagen Docker

Proceso de construcción (`docker build`) donde se descarga la imagen base de Python, se instalan dependencias y se compila el entorno de ejecución asegurando la inmutabilidad de la aplicación.

<p align="center">
  <img src="https://github.com/user-attachments/assets/4be6b58f-7ce6-49c7-a355-bc2be2887550" width="100%" style="border-radius: 8px;">
</p>

### 3️⃣ Contenedor ejecutándose

La imagen generada fue subida exitosamente a Docker Hub (`docker push`) y posteriormente ejecutada (`docker run`), publicando el puerto 8080 para su consumo desde el host.

<table>
<tr>
  <td align="center"><b>Publicación en Docker Hub (Push)</b></td>
</tr>
<tr>
  <td><img src="https://github.com/user-attachments/assets/b15203ba-9c66-4b11-9a94-a14500bba650" width="100%"></td>
</tr>
<tr>
  <td align="center"><b>Instancia del contenedor activa (Run)</b></td>
</tr>
<tr>
  <td><img src="https://github.com/user-attachments/assets/f180aa1d-83b0-48b6-81bd-5a57932e60a4" width="100%"></td>
</tr>
</table>

### 4️⃣ Prueba curl exitosa

> [!NOTE]  
> **Aclaración sobre la prueba curl:** Para generar esta evidencia se utilizó `Invoke-RestMethod` de PowerShell como equivalente y alternativa directa a `curl`, logrando cumplir exactamente el mismo propósito de enviar peticiones HTTP y validar el tráfico de red.

Se obtuvieron respuestas coherentes y estructuradas en formato JSON para las funcionalidades de extracción y comparativa, demostrando que los endpoints funcionan según lo esperado.

<div align="center">
  <img src="https://github.com/user-attachments/assets/f964550d-c196-4d0b-889b-afcf6e969c38" width="100%">
  <img src="https://github.com/user-attachments/assets/3bcccf32-5265-4802-a1d2-f2a4772d3402" width="100%" style="margin-top: 10px;">
</div>

### Análisis de Sitio con Inteligencia Artificial

Se evidencia la capacidad de la API para integrar Inteligencia Artificial en el flujo de `POST /analyze-site`, retornando análisis cualitativos (`ai_insights`) sobre la estructura y contenido de los sitios evaluados, complementando el score y las métricas base calculadas.

<p align="center"><b>Salida de consola/Postman con atributo <code>ai_insights</code></b></p>
<p align="center">
<img width="933" height="583" alt="Captura de pantalla 2026-03-23 093152" src="https://github.com/user-attachments/assets/36f9064d-16b2-44eb-826c-a1f6fb4bf2cd" />
</p>

<details>
<summary><b>👀 Ver estructura JSON de la respuesta (Incluye <code>ai_insights</code>)</b></summary>
<br>

```json
{
    "url": "https://redskinsrs.com/",
    "status_code": 200,
    "response_time_ms": 3911.91,
    "has_https": true,
    "title": "Redskins",
    "meta_description": "Tienda de Ropa para hombre y mujer",
    "h1_count": 1,
    "h2_count": 3,
    "image_count": 68,
    "images_without_alt": 26,
    "internal_links": 174,
    "external_links": 12,
    "word_count": 1602,
    "main_text_excerpt": "Redskins Ecuador Navegación de palanca ☰ Inicio Hombre HOMBRE ACCESORIOS CALZADO CAMISAS CAMISETAS CHAQUETAS GAFAS PANTALONES SUDADERAS BUSOS ROPA INTERIOR BERMUDAS Mujer MUJER ACCESORIOS CAMISETAS PANTALONES SUDADERAS CALZADO GAFAS FALDAS CHAQUETAS BUSOS SHORTS ROPA INTERIOR VES...",
    "scores": {
        "seo_score": 85.0,
        "accessibility_score": 84.71,
        "content_quality_score": 100.0,
        "overall_score": 90.18
    },
    "issues": [
        "El título no está en un rango recomendado (15-70 caracteres).",
        "Hay imágenes sin atributo alt.",
        "La meta descripción no está en un rango recomendado."
    ],
    "recommendations": [
        "Ajusta la longitud del título para mejorar SEO.",
        "Ajusta la meta descripción entre 50 y 180 caracteres.",
        "Añade textos alternativos a las imágenes."
    ],
    "ai_insights": {
        "site_type": "E-commerce",
        "main_topic": "Venta de ropa y accesorios de moda",
        "short_summary": "Tienda oficial de la marca Redskins en Ecuador, especializada en la comercialización de prendas de vestir, calzado y accesorios para hombres y mujeres.",
        "semantic_recommendations": [
            "Optimizar descripciones de productos con atributos de material y corte",
            "Crear guías de tallas detalladas para reducir devoluciones",
            "Implementar una sección de 'Lookbook' para fomentar ventas cruzadas",
            "Fortalecer el SEO local mediante palabras clave específicas de Ecuador"
        ],
        "provider": "gemini"
    }
}
```
</details>

### 5️⃣  API desplegada en Cloud

> [!NOTE]  
> **Aclaración sobre plataforma:** El planteamiento inicial consideraba Google Cloud Platform (GCP). Por demoras en la activación del *billing* del servicio, se optó por **Render** como IaaS alernativo para asegurar el cumplimiento del objetivo técnico (acceso público).

<table>
<tr>
  <td align="center"><b>Creación del servicio asociado al Repositorio en Render</b></td>
</tr>
<tr>
  <td><img src="https://github.com/user-attachments/assets/83853233-1a05-45d4-adfa-904d8fca51d5" width="100%"></td>
</tr>
<tr>
  <td align="center"><b>Logs de Build e instalación de dependencias nativas en Render</b></td>
</tr>
<tr>
  <td><img src="https://github.com/user-attachments/assets/4270f744-eda6-45f0-81d5-3b17dd0c5605" width="100%"></td>
</tr>
<tr>
  <td align="center"><b>Despliegue finalizado y servicio inicializando online</b></td>
</tr>
<tr>
  <td><img src="https://github.com/user-attachments/assets/acb736f6-c3d3-423b-9e4e-34b7e3da7eba" width="100%"></td>
</tr>
</table>

### 6️⃣ Endpoint accesible públicamente

Pruebas concluyentes desde la red pública (fuera del *localhost*). El dominio generado por Render responde a las peticiones demostrando el éxito del despliegue en la red.

**URL Base del proyecto:**
`https://creacionapi.onrender.com`

<p align="center"><b>Acceso directo vía Navegador (GET /health)</b></p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/543801c6-a1c1-406a-94f7-bddd45ddc3bc" width="100%">
</p>

<p align="center"><b>Petición a través de cliente Postman</b></p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/e5de8d0c-4843-49d0-a61f-ed25d9f521b0" width="100%">
</p>


---

## 🌿 Gestión de Versiones (Branches)

Flujo de trabajo colaborativo evidenciado mediante las ramas del repositorio GIT.

<p align="center">
  <img src="https://github.com/user-attachments/assets/ec09dca5-b1c4-4f01-8e8a-d6475d7b5d6c" width="40%">
</p>
