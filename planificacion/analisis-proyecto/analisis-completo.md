# Análisis Completo del Proyecto Edutopia

**Fecha:** 2026-10-06  
**Estado:** ✅ Completado - Análisis inicial realizado

---

## 1. Propósito e Intención del Proyecto

**Edutopia** es una plataforma educativa web para niños de primaria (grados 1.º a 5.º) que combina:
- Aprendizajes estructurados (lecciones + prácticas guiadas)
- Juegos interactivos con retroalimentación inmediata
- Gestión familiar: adultos crean cuentas y perfiles infantiles para guardar progreso

**Arquitectura:** Full-stack con React + Vite (frontend) y Flask + MySQL (backend).

**Público objetivo:** Familias con niños en edad escolar primaria; también permite modo "invitado" sin registro.

---

## 2. Estructura del Proyecto

```
Edutopia/
├── Backend/                 # Flask API
│   ├── app.py              # Punto de entrada, auth, children CRUD
│   ├── requirements.txt    # Dependencias Python
│   ├── schema.sql          # Esquema MySQL (parents, children, activities, progress)
│   ├── migrations/         # Migraciones SQL
│   ├── app/
│   │   ├── learning_content.py   # Catálogo curricular (5 aprendizajes base + 6 unidades extra)
│   │   ├── learning_routes.py    # API /api/learning/*
│   │   ├── auth_sessions.py      # Tokens firmados + SQLite para revocación
│   │   └── extra_content.py      # 6 unidades curriculares por grado
│   ├── juegos/backend/
│   │   ├── catalog.py      # 4 juegos + generadores de preguntas por grado
│   │   └── routes.py       # API /api/games/check (feedback inmediato)
│   └── tests/              # Tests unitarios (learning_content)
├── Frontend/               # React + Vite
│   ├── src/
│   │   ├── pages/          # Home, Login, Register, Aprende, Dashboard, RegisterChild
│   │   ├── components/     # Navbar, Icon, Logo
│   │   ├── api.js          # Cliente API + cache localStorage
│   │   └── Styles/         # CSS modular (global, learning, dashboard, etc.)
│   └── package.json
└── run.py                  # (vacío)
```

---

## 3. Hallazgos: Errores, Fallas y Malas Prácticas

### 🔴 CRÍTICOS (Seguridad / Correctitud)

| # | Problema | Ubicación | Impacto |
|---|----------|-----------|---------|
| 1 | CORS abierto a todos los orígenes (`origins: "*"`) | `Backend/app.py:50` | Cualquier sitio puede hacer peticiones autenticadas |
| 2 | Sesiones en SQLite local sin bloqueo para producción multi-proceso | `Backend/app/auth_sessions.py:16-20` | Race conditions, corrupción de BD en Gunicorn/uWSGI |
| 3 | Token de logout por `sendBeacon` con body JSON pero endpoint espera `application/json` | `Frontend/src/main.jsx:9-14` vs `Backend/app.py:117-121` | Logout silencioso al cerrar pestaña puede fallar |
| 4 | Validación de `grade` en `guest/submit` permite `bool` | `Backend/app/learning_routes.py:118` | `grade=true` pasa validación y causa errores |
| 5 | `activity["questions"]` puede mutarse inadvertidamente en `public_activity` | `Backend/app/learning_content.py:193-206` | `activity_for_grade` modifica el objeto original |

### 🟠 ALTOS (Arquitectura / Mantenibilidad)

| # | Problema | Ubicación |
|---|----------|-----------|
| 6 | Import circular: `learning_content.py` ↔ `extra_content.py` ↔ `juegos.backend.catalog` | Múltiples archivos |
| 7 | Cache global `_catalog_cache` sin invalidación ni límite de tamaño | `Backend/app/learning_routes.py:11, 44-45` |
| 8 | SQL crudo en todas partes sin ORM / query builder | `Backend/app.py`, `learning_routes.py` |
| 9 | `query()` cierra cursor pero no maneja transacciones correctamente | `Backend/app.py:75-80` |
| 10 | `Aprende.jsx` tiene 274 líneas en un solo componente (God component) | `Frontend/src/pages/Aprende.jsx` |
| 11 | Duplicación de lógica de preguntas: `game_questions` vs `questions_for_grade` | `catalog.py` vs `learning_content.py` |
| 12 | Hardcoded activity counts en Dashboard | `Frontend/src/pages/Dashboard.jsx:139-141` |

### 🟡 MEDIOS (Calidad de Código / UX)

| # | Problema | Ubicación |
|---|----------|-----------|
| 13 | `run.py` existe pero está vacío | Raíz del proyecto |
| 14 | Tests solo cubren `learning_content` | `Backend/tests/test_learning_content.py` |
| 15 | `availableSubjects` hardcodeado en frontend | `Frontend/src/pages/Aprende.jsx:9` |
| 16 | Inconsistencia naming: `activity.key` vs `activity_key` | Frontend vs Backend |
| 17 | No hay rate limiting / throttling en endpoints públicos | `app.py`, `learning_routes.py` |
| 18 | Password minimum 6 chars sin requisitos de complejidad | `app.py:103` |
| 19 | `localStorage` para tokens sin `httpOnly` cookie alternative | `Frontend/src/api.js:19-32` |
| 20 | Dark mode aplica `!important` masivamente en CSS | `global.css:158-171` |
| 21 | `learning_content.py` mezcla datos y lógica | `Backend/app/learning_content.py` |
| 22 | `public_activity` filtra campos manualmente (frágil) | `learning_content.py:196` |

### 🟢 BAJOS / SUGERENCIAS MEJORA

- Extraer catálogo a JSON/YAML + loader
- Usar Pydantic/marshmallow para validación
- Migrar sesiones a Redis o flask-session
- Dividir `Aprende.jsx` en componentes + hooks
- Agregar OpenAPI/Swagger
- Migrar a TypeScript
- Agregar CSP headers
- Consolidar `schema.sql` y migración

---

## 4. Fortalezas Identificadas

- Diseño curricular con progresión pedagógica real
- Separación guest/auth funcional
- Tokens firmados + revocación (buena arquitectura JWT-like)
- Cache localStorage en frontend (6h TTL)
- Dark mode completo con CSS variables
- Tests unitarios existentes (base para ampliar)
- Migraciones SQL versionadas
- Accesibilidad básica (aria-label, role, aria-live)
- Responsive design con breakpoints

---

## 5. Plan de Acción Recomendado (Priorizado)

### Fase 1: Seguridad y Corrección (Inmediato)
1. Restringir CORS a dominio del frontend
2. Fix validación `grade` en `guest/submit`: excluir bool
3. Clonar `activity` en `activity_for_grade` antes de mutar
4. Migrar sesiones a Redis o flask-session

### Fase 2: Arquitectura Backend (1-2 semanas)
5. Introducir SQLAlchemy o Tortoise ORM
6. Eliminar import circular: mover generadores a `question_generators.py`
7. Reemplazar `_catalog_cache` con `functools.lru_cache` + TTL o Redis
8. Unificar generadores de preguntas en un solo módulo

### Fase 3: Frontend Modularización (1-2 semanas)
9. Dividir `Aprende.jsx` en componentes + hooks (`useLearningCatalog`, `useChildProgress`, `useGameSession`)
10. Mover `subjectModules` y `availableSubjects` a API (`/api/learning/subjects`)
11. Migrar a TypeScript

### Fase 4: Calidad y Observabilidad (Continuo)
12. Ampliar tests: auth, games, edge cases, integration
13. Agregar rate limiting (`flask-limiter`)
14. Configurar CSP, HSTS, Secure headers (`flask-talisman`)
15. Documentar API con `flask-smorest` / OpenAPI
16. Eliminar `run.py` vacío o convertirlo en entry point unificado

---

## Próximos Pasos Inmediatos

- [ ] Implementar fixes críticos de seguridad (Fase 1)
- [ ] Crear estructura modular para currículo (JSON/YAML)
- [ ] Refactorizar `Aprende.jsx` en componentes reutilizables