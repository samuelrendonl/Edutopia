# Referencia de Configuración de Agentes - Edutopia

**Fecha:** 2026-10-06  
**Estado:** ✅ Completado - AGENTS.md creado en raíz

---

## Archivo Principal

**`AGENTS.md`** (en raíz del proyecto: `C:\1-Universidad\6to\Desarrollo Sostenible\Edutopia\AGENTS.md`)

Contiene instrucciones compactas para futuras sesiones de OpenCode:
- Comandos exactos de desarrollo
- Arquitectura y estructura de directorios
- Detalles críticos de implementación (auth, DB, activities)
- Gotchas comunes documentados
- Variables de entorno
- Mapa de archivos para cambios frecuentes

---

## Configuración de OpenCode (si aplica)

### `opencode.json` (proyecto)
```json
{
  "instructions": [
    "AGENTS.md"
  ]
}
```

### Variables de Entorno Requeridas

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| `MYSQL_HOST` | Host MySQL | `127.0.0.1` |
| `MYSQL_PORT` | Puerto MySQL | `3306` |
| `MYSQL_USER` | Usuario MySQL | `root` |
| `MYSQL_PASSWORD` | Password MySQL | `` (vacío para XAMPP) |
| `MYSQL_DATABASE` | Base de datos | `edutopia` |
| `SECRET_KEY` | Clave firmado tokens | `auto-generada en .secret_key` |
| `PORT` | Puerto Flask | `5000` |

---

## Comandos de Verificación Rápida

```bash
# Verificar backend
cd Backend && python -c "from app import app; print('OK')"

# Verificar tests
cd Backend && python -m unittest tests.test_learning_content -v

# Verificar frontend build
cd Frontend && npm run build

# Verificar lint
cd Frontend && npm run lint
```

---

## Estructura de Directorios Clave

```
Edutopia/
├── AGENTS.md                    ← Instrucciones principales para agentes
├── Backend/
│   ├── app.py                   ← Entry point Flask
│   ├── requirements.txt         ← Python deps
│   ├── schema.sql               ← Schema inicial MySQL
│   ├── migrations/              ← Migraciones SQL
│   ├── app/                     ← App modules
│   │   ├── learning_content.py  ← Catálogo + generadores
│   │   ├── learning_routes.py   ← API /api/learning/*
│   │   ├── auth_sessions.py     ← Tokens + revocación SQLite
│   │   └── extra_content.py     ← 6 unidades curriculares
│   └── juegos/backend/          ← Juegos
│       ├── catalog.py           ← Definiciones + generadores
│       └── routes.py            ← /api/games/check
├── Frontend/
│   ├── src/
│   │   ├── api.js               ← Cliente API + cache
│   │   ├── App.jsx              ← Rutas
│   │   ├── main.jsx             ← Entry + logout pagehide
│   │   ├── pages/               ← Páginas
│   │   ├── components/          ← Componentes
│   │   └── Styles/              ← CSS
│   ├── package.json
│   └── vite.config.js
└── planificacion/               ← Documentación de planificación
    ├── analisis-proyecto/
    ├── curriculo-pedagogico/
    ├── generador-guias-pdf/
    └── configuracion-agentes/
```

---

## Puntos de Entrada Principales

| Funcionalidad | Backend | Frontend |
|---------------|---------|----------|
| Auth (register/login/logout) | `app.py:99-121` | `pages/login.jsx`, `pages/Register.jsx` |
| Children CRUD | `app.py:123-135` | `pages/Dashboard.jsx`, `pages/RegisterChild.jsx` |
| Catálogo actividades | `learning_routes.py:39-46` | `pages/Aprende.jsx` (línea 58-66) |
| Progreso niño | `learning_routes.py:49-66` | `pages/Aprende.jsx` (línea 68-73) |
| Submit actividad | `learning_routes.py:69-107` | `pages/Aprende.jsx` (línea 153-182) |
| Guest submit | `learning_routes.py:110-135` | `pages/Aprende.jsx` (línea 168-171) |
| Game feedback | `juegos/backend/routes.py` | `pages/Aprende.jsx` (línea 137-151) |

---

## Convenciones de Código

### Backend (Python)
- **Imports**: Absolute desde `app.` o `juegos.backend.`
- **SQL**: `%s` placeholders (mysql-connector-python)
- **Error handling**: `jsonify({"error": "msg"}), status_code`
- **Auth decorator**: `@auth_parent` para endpoints protegidos
- **Child access**: `_child_access` decorator en learning_routes

### Frontend (React)
- **API client**: `api.js` - usa `fetch` + `localStorage` token
- **Auth state**: `localStorage.edutopia_parent` + event `edutopia-auth-change`
- **Routing**: `react-router-dom` v7, rutas en `App.jsx`
- **Styles**: CSS modules en `Styles/*.css`, variables en `global.css`
- **Icons**: Componente `Icon.jsx` con SVG inline

---

## Testing

```bash
# Solo backend tests existentes
cd Backend
python -m unittest tests.test_learning_content -v

# Cobertura actual: learning_content.py únicamente
# FALTAN: auth, routes, games, integration tests
```

---

## Próximas Configuraciones a Agregar

Cuando se implementen:

1. **Study Guide Generator** → Agregar `weasyprint`, `qrcode` a requirements.txt
2. **TypeScript migration** → `tsconfig.json`, `@types/react`
3. **CI/CD** → GitHub Actions workflow
4. **Docker** → `Dockerfile`, `docker-compose.yml`
5. **Redis sessions** → `flask-session`, `redis` config

---

## Notas para Agentes Futuros

1. **Leer AGENTS.md primero** - contiene lo esencial
2. **No modificar `run.py`** - está vacío, sin uso confirmado
3. **Cuidado con imports circulares** - `learning_content.py` ↔ `extra_content.py` ↔ `catalog.py`
4. **CORS abierto** - solo para desarrollo, restringir en prod
5. **SQLite sessions** - no usar en producción multi-worker
6. **Aprende.jsx** - componente grande, dividir si se toca
7. **Datos curriculares** - hardcodeados en `.py`, migrar a YAML/JSON
8. **Tests mínimos** - ampliar antes de refactors grandes