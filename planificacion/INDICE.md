# Índice de Planificación - Edutopia

**Última actualización:** 2026-10-06  
**Proyecto:** Plataforma educativa primaria (React + Flask + MySQL)

---

## Estructura de Carpetas

```
planificacion/
├── INDICE.md                              ← Este archivo
├── analisis-proyecto/
│   └── analisis-completo.md               ← Análisis completo del código base
├── curriculo-pedagogico/
│   └── plan-curricular-completo.md        ← Plan 5 materias × 5 grados
├── generador-guias-pdf/
│   └── plan-generador-guias.md            ← Generador PDF guías de estudio
└── configuracion-agentes/
    └── referencia-agentes.md              ← Referencia configuración agentes
```

---

## Resumen por Categoría

### 1. Análisis del Proyecto (`analisis-proyecto/`)
**Archivo:** `analisis-completo.md`

- Propósito e intención de Edutopia
- Estructura completa del proyecto
- **34 hallazgos clasificados:**
  - 🔴 5 Críticos (seguridad/correctitud)
  - 🟠 7 Altos (arquitectura/mantenibilidad)
  - 🟡 10 Medios (calidad/UX)
  - 🟢 10 Bajos (sugerencias mejora)
- Fortalezas identificadas
- Plan de acción priorizado en 4 fases
- Próximos pasos inmediatos con checkboxes

---

### 2. Currículo Pedagógico (`curriculo-pedagogico/`)
**Archivo:** `plan-curricular-completo.md`

- 5 principios pedagógicos rectores
- Mapa curricular general (tabla 5×5)
- **Detalle por materia (5 materias × 5 grados):**
  - **Matemáticas**: 4 unidades + 2 juegos/grado (juegos existentes ✅)
  - **Lengua Castellana**: 4 unidades + 2 juegos/grado (muy completa ✅)
  - **Ciencias**: 4 unidades + 1 juego + 1 experiencia/grado (❌ todo por crear)
  - **Sociales**: 4 unidades + 1 juego + 1 proyecto/grado (❌ todo por crear)
  - **Inglés**: 4 unidades + 1 juego + 1 reto oral/grado (❌ todo por crear)
- Estado actual vs plan (tabla resumen)
- Plan de implementación en 4 fases (70h estimadas)
- Estructura técnica recomendada para catálogo modular (YAML + loaders)
- Métricas de cobertura pedagógica

---

### 3. Generador de Guías PDF (`generador-guias-pdf/`)
**Archivo:** `plan-generador-guias.md`

- Arquitectura frontend/backend para generación on-demand
- Estructura de la guía (portada, índice, 8 secciones, contraportada)
- **Backend:**
  - Dependencias: `weasyprint`, `qrcode`, `Pillow`
  - Estructura archivos: `study_guide/` (service, generator, routes, templates)
  - Datos curriculares en YAML por grado/materia (ejemplo grado 3 matemáticas)
  - 3 componentes clave: Service, PDFGenerator, Routes
  - Rutas API: `/pdf`, `/preview`, `/subjects`
- **Frontend:**
  - Componente `StudyGuideDownloader.jsx` con vista previa + descarga
  - Integración en Dashboard (por niño) y Aprende (toolbar)
- Plantillas Jinja2 (10 archivos) + CSS print (@page, variables por materia)
- Flujo UX completo con diagrama ASCII
- Checklist implementación: 6 fases, ~70h
- Próximos pasos inmediatos con checkboxes

---

### 4. Configuración de Agentes (`configuracion-agentes/`)
**Archivo:** `referencia-agentes.md`

- Referencia al `AGENTS.md` principal en raíz
- Configuración `opencode.json` sugerida
- Variables de entorno requeridas
- Comandos de verificación rápida
- Estructura de directorios clave
- Puntos de entrada principales (tabla backend/frontend)
- Convenciones de código (Python + React)
- Estado de testing actual
- Próximas configuraciones a agregar
- Notas importantes para agentes futuros

---

## Archivo Principal de Agentes

**`AGENTS.md`** (en raíz del proyecto: `C:\1-Universidad\6to\Desarrollo Sostenible\Edutopia\AGENTS.md`)

Instrucciones compactas para sesiones OpenCode:
- Quick start (backend + frontend + DB)
- Key commands table
- Architecture notes
- Critical implementation details
- Common gotchas (7 items)
- Testing + Environment variables
- File locations for key changes

---

## Estado General del Proyecto

| Área | Estado | Completitud |
|------|--------|-------------|
| **Backend Core** | Funcional | ~80% |
| **Frontend Core** | Funcional | ~75% |
| **Auth + Sesiones** | Funcional | ~90% |
| **Matemáticas** | Parcial | ~70% |
| **Lengua Castellana** | Parcial | ~85% |
| **Ciencias Naturales** | Implementado | 100% del catálogo textual |
| **Sociales** | Implementado | 100% del catálogo textual |
| **Inglés** | Implementado en texto | 100% del catálogo textual |
| **Tests** | Mínimos | ~15% |
| **Guías PDF** | Planificado | 0% |

---

## Próximas Acciones Prioritarias

1. **[ ] Fixes críticos seguridad** (CORS, validación grade, mutación activity, sesiones Redis)
2. **[ ] Unificar generadores preguntas** (los juegos nuevos ya usan el currículo común; queda consolidar Matemáticas)
3. **[ ] Migrar currículo a YAML** (estructura `curriculum_data/` + loader)
4. **[ ] Refactorizar Aprende.jsx** (dividir en hooks + componentes)
5. **[ ] Implementar Guías PDF** (fase 1: YAMLs muestra + pipeline WeasyPrint)
6. **[ ] Ampliar tests** (auth, routes, games, integration)

---

## Cómo Usar Esta Planificación

- **Para continuar desarrollo**: Revisar `analisis-proyecto/analisis-completo.md` → fase 1
- **Para contenido pedagógico**: Consultar `curriculo-pedagogico/plan-curricular-completo.md`
- **Para feature Guías PDF**: Seguir `generador-guias-pdf/plan-generador-guias.md`
- **Para onboarding agentes**: Leer `AGENTS.md` (raíz) + `configuracion-agentes/referencia-agentes.md`

---

## Convención de Actualización

- **Cada fase completada** → Marcar checkboxes en archivos correspondientes
- **Cambios de alcance** → Actualizar archivos afectados + `INDICE.md`
- **Nuevas planificaciones** → Crear archivo en carpeta correspondiente + actualizar índice
- **Decisiones técnicas** → Documentar en archivo relevante con fecha y razonamiento
