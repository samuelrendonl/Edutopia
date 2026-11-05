# Plan: Generador de Guías de Estudio en PDF

**Fecha:** 2026-10-06  
**Estado:** ✅ Completado - Diseño técnico definido

---

## Objetivo

Generar PDFs "bien cheveres" (atractivos, pedagógicos, completos) que el padre/hijo pueda descargar con la planificación completa del curso por grado y materia, incluyendo:
- Objetivos de aprendizaje
- Calendario 36 semanas
- Actividades Edutopia mapeadas
- Proyectos para casa con rúbricas
- Autoevaluación trimestral
- Recursos recomendados

---

## Arquitectura General

```
┌─────────────────────────────────────────────────────────────────┐
│                        FRONTEND (React)                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐  │
│  │ Selector    │  │ Vista Previa│  │ Botón Descargar         │  │
│  │ Grado/Materia│──▶│ (HTML/iframe)│──▶│ /api/study-guide/pdf   │  │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                        BACKEND (Flask)                          │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────┐  │
│  │ /api/study-guide │  │ StudyGuideService│  │ PDF Generator│  │
│  │ /pdf?grade=3&    │──▶│ (compone contenido)│──▶│ (WeasyPrint│  │
│  │ subject=math     │  │ + plantilla HTML) │  │ / ReportLab) │  │
│  └──────────────────┘  └──────────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Estructura de la Guía de Estudio (Contenido Pedagógico)

### Plantilla Maestra por Grado/Materia

```json
{
  "portada": {
    "titulo": "Guía de Estudio - {{ subject }} - {{ grade }}.º Grado",
    "subtitulo": "Edutopia · {{ year }} · {{ child_name }}",
    "ilustracion": "assets/grade_{{ grade }}_{{ subject }}.svg",
    "qr_codigo": "url_actividades_interactivas"
  },
  "indice": [
    "1. Objetivos de Aprendizaje",
    "2. Contenidos por Unidad",
    "3. Actividades Interactivas en Edutopia",
    "4. Proyectos y Experiencias en Casa",
    "5. Rúbrica de Autoevaluación",
    "6. Recursos Adicionales (libros, videos, webs)",
    "7. Calendario Sugerido (36 semanas)",
    "8. Registro de Progreso Semanal"
  ],
  "cuerpo": {
    "objetivos": [...],
    "unidades": [
      {
        "numero": 1,
        "titulo": "Unidad 1: ...",
        "duracion_semanas": 6,
        "objetivos_especificos": [...],
        "contenidos_clave": [...],
        "vocabulario_fundamental": [...],
        "actividades_edutopia": ["math-laboratory", "math-balloons"],
        "proyecto_casa": {...},
        "evaluacion": {...}
      }
    ],
    "proyectos_transversales": [...],
    "rubro_autoevaluacion": {...},
    "recursos": {...},
    "calendario": [...],
    "registro_progreso": [...]
  },
  "contraportada": {
    "motivacion": "¡Cada paso cuenta! ...",
    "contacto": "padres@edutopia.app",
    "logo": "Edutopia"
  }
}
```

---

## Backend: Implementación Técnica

### Dependencias Nuevas (`Backend/requirements.txt`)

```txt
# PDF Generation
weasyprint==62.0          # HTML+CSS → PDF (mejor calidad tipográfica)
# OPCIÓN B: reportlab==4.2.5  # Más control programático, más código
# OPCIÓN C: fpdf2==2.7.4      # Ligero, puro Python

# Plantillas
jinja2==3.1.6             # Ya está en Flask deps

# Utilidades
qrcode==7.4.2             # QR codes para enlaces a actividades
Pillow==10.4.0            # Manipulación imágenes
```

### Estructura de Archivos Nueva

```
Backend/
├── app/
│   ├── study_guide/
│   │   ├── __init__.py
│   │   ├── routes.py              # Blueprint /api/study-guide
│   │   ├── service.py             # Lógica de composición de contenido
│   │   ├── pdf_generator.py       # HTML → PDF (WeasyPrint)
│   │   ├── curriculum_map.py      # Mapeo grado/materia → unidades
│   │   └── templates/
│   │       ├── base.html          # Layout principal
│   │       ├── cover.html         # Portada
│   │       ├── toc.html           # Índice
│   │       ├── unit.html          # Detalle unidad
│   │       ├── project.html       # Proyecto casa
│   │       ├── rubric.html        # Rúbrica
│   │       ├── calendar.html      # Calendario 36 semanas
│   │       ├── tracker.html       # Registro progreso
│   │       └── back_cover.html    # Contraportada
│   │   └── static/
│   │       ├── css/
│   │       │   └── study_guide.css    # Estilos PDF (print media)
│   │       ├── fonts/
│   │       │   ├── Nunito-Regular.ttf
│   │       │   ├── Nunito-Bold.ttf
│   │       │   └── icons.svg
│   │       └── images/
│   │           ├── grade_1_math.svg
│   │           ├── grade_2_language.svg
│   │           └── ...
│   └── curriculum_data/           # Datos estructurados (JSON/YAML)
│       ├── math/
│       │   ├── grade_1.yaml
│       │   ├── grade_2.yaml
│       │   └── ...
│       ├── language/
│       ├── science/
│       ├── social/
│       └── english/
```

### Esquema de Datos Curriculares (YAML por Grado/Materia)

```yaml
# Backend/app/curriculum_data/math/grade_3.yaml
grade: 3
subject: "Matemáticas"
subject_icon: "calculator"
subject_color: "#5b5ce2"
year_objectives:
  - "Resolver problemas de multiplicación y división hasta 100"
  - "Entender fracciones unitarias (1/2, 1/3, 1/4) como partes de un todo"
  - "Calcular perímetro de polígonos y distinguir área/perímetro"
  - "Leer e interpretar gráficas de barras con escala >1"
  - "Identificar y clasificar ángulos (recto, agudo, obtuso)"

units:
  - number: 1
    title: "Números hasta 1.000 y Valor Posicional"
    weeks: 5
    objectives:
      - "Leer, escribir y ordenar números de 3 cifras"
      - "Descomponer en centenas, decenas y unidades"
      - "Redondear al diez y ciento más cercano"
    key_contents:
      - "Valor posicional (C, D, U)"
      - "Recta numérica hasta 1.000"
      - "Comparación con >, <, ="
      - "Patrones de conteo (de 10 en 10, de 100 en 100)"
    vocabulary: ["centena", "decena", "unidad", "redondear", "ordenar", "recta numérica"]
    edutopia_activities:
      - key: "math-laboratory"
        grade_adaptations: ["patterns"]
      - key: "math-balloons"
        rounds: 10
    home_project:
      title: "Mi Ciudad de Números"
      description: "Construye edificios con bloques base-10 (centenas=edificios, decenas=pisos, unidades=ladrillos). Escribe el número de cada edificio."
      materials: ["Bloques base-10 o recortables PDF", "Cartulina", "Marcadores"]
      evidence: "Foto de la ciudad + tabla de números"
      rubric:
        - criterion: "Representación correcta del valor posicional"
          weight: 40
        - criterion: "Creatividad y presentación"
          weight: 30
        - criterion: "Explicación oral del niño"
          weight: 30

  - number: 2
    title: "Multiplicación y División: Conceptos y Tablas"
    weeks: 7
    # ... resto similar

transversal_projects:
  - title: "Feria de Matemáticas Familiar"
    description: "Diseña 3 juegos de matemáticas para jugar en familia. Incluye instrucciones, materiales y tabla de puntuación."
    suggested_week: 30

rubric_self_assessment:
  dimensions:
    - name: "Comprensión Conceptual"
      indicators:
        - "Explico con mis palabras qué significa multiplicar"
        - "Uso dibujos o materiales para mostrar fracciones"
        - "Relaciono la división con el reparto justo"
    - name: "Resolución de Problemas"
      indicators:
        - "Identifico los datos y la pregunta del problema"
        - "Elijo la operación correcta y la justifico"
        - "Compruebo si mi respuesta tiene sentido"
    # ...

### Guía priorizada: Matemáticas de 1.º

La primera guía debe seguir la misma secuencia que el catálogo interactivo para
que la práctica en casa no adelante conceptos. Se recomienda una ficha breve por
paso, con dibujos, objetos manipulables y una evidencia sencilla:

1. **Contamos y representamos hasta 20:** contar colecciones, ordenar tarjetas y
   representar cantidades con tapas o bloques.
2. **Juntamos y quitamos:** resolver historias de suma y resta dibujando antes de
   usar los signos `+` y `−`.
3. **Formas, cuerpos y posiciones:** clasificar objetos, describir posiciones y
   construir figuras con palitos o plastilina.
4. **Patrones y pictogramas:** continuar secuencias AB/ABB y registrar datos de
   colores, animales u objetos de la casa.
5. **La tienda de las cantidades:** simular compras, juntar y quitar objetos, y
   explicar oralmente la operación elegida.
6. **Medimos nuestro mundo:** comparar largo, corto, pesado, liviano y duración;
   medir objetos con una regla y ordenarlos.
7. **Juegos de consolidación:** jugar Globos matemáticos para conteo y Misión
   cohete para sumas hasta 10.

Cada ficha debe incluir: objetivo en lenguaje infantil, ejemplo resuelto, tres
actividades guiadas, una actividad familiar y una autoevaluación con pictogramas.

resources:
  books:
    - "Matemáticas 3º Primaria (Santillana/SM/Anaya) - libro de texto escolar"
    - "El Diablo de los Números - Hans Magnus Enzensberger"
  videos:
    - title: "Multiplicación en la recta numérica"
      url: "https://www.youtube.com/watch?v=..."
      channel: "Math2Me / Khan Academy Español"
  websites:
    - "https://www.khanacademy.org/math/cc-third-grade-math"
    - "https://nrich.maths.org/primary"

calendar:  # 36 semanas auto-generadas desde units[].weeks
  - week: 1
    unit: 1
    focus: "Valor posicional: centenas, decenas, unidades"
    edutopia_activity: "math-laboratory (patterns, grade 3)"
    home_task: "Completa la ficha 'Descompongo números' (PDF adjunto)"
  - week: 2
    unit: 1
    focus: "Recta numérica hasta 1.000 y redondeo"
    edutopia_activity: "math-balloons (grade 3)"
    home_task: "Juego 'Adivina el número' en familia"
  # ... se genera automáticamente
```

### Componentes Clave del Backend

#### 1. `StudyGuideService` (`service.py`)
- Carga YAML por grado/materia
- Compone contenido dinámico
- Genera calendario automático (36 semanas)
- Genera QR codes base64 para embed en HTML

#### 2. `PDFGenerator` (`pdf_generator.py`)
- Usa WeasyPrint: HTML + CSS print → PDF
- Jinja2 para renderizar plantillas
- CSS @page para márgenes, headers/footers, numeración
- Fuentes Nunito embebidas
- Variables CSS por materia (colores)

#### 3. Rutas API (`routes.py`)
```python
GET /api/study-guide/pdf?grade=3&subject=math&child_id=5
  → Descarga PDF personalizado (con nombre niño, QR deep-links)

GET /api/study-guide/preview?grade=3&subject=math
  → HTML para vista previa en iframe (frontend)

GET /api/study-guide/subjects
  → Lista materias disponibles con iconos/colores
```

---

## Frontend: Componente de Descarga

### `StudyGuideDownloader.jsx`
- Selector materia + grado (pre-selecciona si hay childId)
- Botón "Vista Previa" → abre modal con iframe
- Botón "Descargar PDF" → fetch blob → download automático
- Personalizado con nombre del niño si autenticado
- Estilos CSS con variable `--subject-color` dinámica

### Integración
- **Dashboard**: Un botón por tarjeta de niño
- **Aprende**: En toolbar o sidebar
- **Perfil**: Posible futura página "Mis Guías"

---

## Plantillas HTML (Jinja2) - Clave para PDF "Bien Chévere"

### Características Visuales
- **Portada**: Full-color, icono grande, badge grado, QR principal
- **Índice**: Navegable (bookmarks en PDF)
- **Unidades**: Cards con header colorido, vocabulario 2 columnas, badges actividades con QR
- **Proyectos**: Caja destacada naranja, meta-grid (materiales, tiempo, rúbrica)
- **Rúbrica**: Tabla 4 dimensiones × 3 indicadores = 12 filas para autoevaluación trimestral
- **Calendario**: Tabla compacta 36 filas (3-4 páginas)
- **Registro**: Tabla vacía semanal para rellenar a mano (4 páginas)
- **Recursos**: 2 columnas: libros, videos (QR), webs
- **Contraportada**: Motivacional + contacto

### CSS Print (@media print)
- `@page` con márgenes, headers/footers dinámicos
- `page-break-inside: avoid` en unidades/proyectos
- `page-break-before: always` en secciones mayores
- Fuentes Nunito embebidas (@font-face)
- Variables CSS `--subject-color` por materia

---

## Flujo de Usuario (UX)

```
PADRE EN DASHBOARD
  └─ Tarjeta hijo: "Juan Pérez · 3º Grado" [Aprender ahora] [📄 Guía de Estudio]
        │
        ▼
  Componente StudyGuideDownloader
    Materia: [Matemáticas ▼]  Grado: [3º ▼]  ✨ Personalizado para Juan
    [Vista Previa] [⬇ Descargar PDF]
        │
        ├─▶ Vista Previa → Modal iframe con HTML renderizado (scrollable)
        │
        └─▶ Descargar → PDF generado on-demand → Save As "Guia_Estudio_Matemáticas_3º_Juan.pdf"
```

---

## Checklist de Implementación

| Fase | Tarea | Archivos | Esfuerzo |
|------|-------|----------|----------|
| **1. Datos** | Crear YAMLs currícula 5 materias × 5 grados (25 archivos) | `curriculum_data/*/grade_*.yaml` | ~20h |
| **2. Backend Core** | Service, PDF Generator, Routes | `study_guide/*.py` | ~12h |
| **3. Plantillas** | 10 plantillas Jinja2 + CSS print | `study_guide/templates/*.html` | ~16h |
| **4. Assets** | Icons SVG por grado/materia, fuentes Nunito | `study_guide/static/` | ~6h |
| **5. Frontend** | Componente Downloader + integración | `StudyGuideDownloader.jsx`, CSS | ~8h |
| **6. Testing** | Generar 25 PDFs, validar render, links QR | Manual + Cypress | ~8h |
| **TOTAL** | | | **~70h** |

---

## Próximos Pasos Inmediatos

- [ ] Crear estructura de carpetas `Backend/app/study_guide/` y `Backend/app/curriculum_data/`
- [ ] Instalar dependencias: `weasyprint`, `qrcode`, `Pillow`
- [ ] Crear 5 YAMLs de muestra (1 por materia, grado 3) para validar pipeline
- [ ] Implementar `service.py` + `pdf_generator.py` + `routes.py`
- [ ] Crear plantillas base: `base.html`, `cover.html`, `unit.html`, `calendar.html`
- [ ] CSS print base con variables por materia
- [ ] Componente React `StudyGuideDownloader.jsx`
- [ ] Integrar en Dashboard y Aprende

---

## Nombre de Archivo Generado (Ejemplo)

```
Guia_Estudio_Matemáticas_3º_Juan.pdf
Guia_Estudio_Lengua_Castellana_5º_María.pdf
Guia_Estudio_Ciencias_2º_General.pdf  (sin child_id)
```

---

## Consideraciones Técnicas

1. **Performance**: Cachear HTML renderizado por (grade, subject) con TTL 1h
2. **Deep-links**: QR apuntan a `/aprende?grade=3&activity=math-laboratory`
3. **Internacionalización**: Estructura lista para `language: "en"` futuro
4. **Accesibilidad**: PDF tagged, alt text en imágenes, contraste AA
5. **Tamaño**: Objetivo < 2MB por PDF (fuentes embebidas ~500KB)
