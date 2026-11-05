# Plan de Implementación: 25 Guías de Estudio PDF

**Proyecto:** Edutopia  
**Alcance:** 5 materias × 5 grados = 25 guías curriculares  
**Estado:** Planificación aprobada; implementación pendiente

---

## 1. Objetivo

Crear una guía de estudio descargable para cada combinación de materia y grado:

- Matemáticas: grados 1.º a 5.º
- Lengua Castellana: grados 1.º a 5.º
- Ciencias Naturales/Biología: grados 1.º a 5.º
- Sociales: grados 1.º a 5.º
- Inglés: grados 1.º a 5.º

La plataforma tendrá **25 guías lógicas**, generadas por un sistema reutilizable y no por 25 implementaciones independientes.

---

## 2. Contenido de cada guía

Cada PDF debe incluir:

1. Portada personalizada con nombre del estudiante, materia y grado.
2. Objetivos de aprendizaje.
3. Cuatro unidades curriculares principales.
4. Actividades interactivas de Edutopia con códigos QR.
5. Ejemplos explicados.
6. Actividades para realizar en casa.
7. Proyecto o experiencia práctica.
8. Calendario sugerido de 36 semanas.
9. Autoevaluación por competencias.
10. Registro semanal de progreso.
11. Recursos recomendados.
12. Contraportada motivacional.

Las actividades adicionales del catálogo se mostrarán como refuerzo y consolidación.

---

## 3. Organización de los datos curriculares

Crear 25 archivos curriculares estructurados:

```text
Backend/app/curriculum_data/
├── matematicas/
│   ├── grade_1.yaml
│   ├── grade_2.yaml
│   └── ...
├── lengua/
├── ciencias/
├── sociales/
└── ingles/
```

Cada archivo debe contener:

- Objetivos del grado.
- Unidades y contenidos.
- Vocabulario fundamental.
- Actividades Edutopia relacionadas.
- Proyecto familiar.
- Rúbrica.
- Calendario.
- Recursos recomendados.

Como primera etapa se reutilizará el contenido actual de `learning_content.py` y `subject_units.py`, evitando duplicaciones innecesarias.

---

## 4. Arquitectura backend

Crear el módulo:

```text
Backend/app/study_guide/
├── routes.py
├── service.py
├── pdf_generator.py
├── curriculum_loader.py
├── templates/
└── static/
```

### Tecnología propuesta

- Jinja2 para plantillas HTML.
- WeasyPrint para convertir HTML/CSS en PDF.
- QRCode para enlaces a actividades.
- Fuente accesible como Nunito.

### Rutas API

```text
GET /api/study-guides/catalog
GET /api/study-guide/preview?subject=matematicas&grade=3
GET /api/study-guide/pdf?subject=matematicas&grade=3&child_id=5
```

El backend debe:

- Validar materia y grado.
- Verificar que el estudiante pertenece al padre autenticado.
- Personalizar el nombre del estudiante.
- Generar el PDF bajo demanda.
- Mantener cache por materia, grado y versión curricular.
- Generar códigos QR hacia las actividades.
- Entregar nombres como `Guia_Estudio_Matematicas_3_Juan.pdf`.

---

## 5. Generación y almacenamiento

Se utilizará generación bajo demanda con cache:

- Cache base por `materia + grado + versión curricular`.
- Personalización del nombre del estudiante durante la descarga.
- Regeneración automática cuando cambie la versión curricular.
- No se almacenarán PDFs personalizados indefinidamente sin necesidad.

---

## 6. Experiencia de usuario

En el Dashboard del padre se mostrará el bloque de guías del estudiante:

```text
Juan Pérez · 3.º grado

[Guía de Matemáticas]
[Guía de Lengua Castellana]
[Guía de Ciencias Naturales]
[Guía de Sociales]
[Guía de Inglés]
```

Cada tarjeta debe ofrecer:

- Vista previa.
- Descargar PDF.
- Materia y grado.
- Fecha de generación.

El niño verá las guías correspondientes a su grado. El padre podrá consultar las guías de todos los grados si se habilita esa opción.

---

## 7. Fases de implementación

### Fase 1: Modelo de datos

- Definir el esquema YAML.
- Crear cinco guías de muestra de 3.º.
- Validar coincidencia entre unidades y catálogo interactivo.

### Fase 2: Generador PDF

- Crear el servicio curricular.
- Crear plantilla base.
- Crear portada, índice, unidades y calendario.
- Generar el primer PDF completo.

### Fase 3: Integración backend

- Crear rutas API.
- Agregar autenticación y permisos.
- Implementar cache.
- Agregar códigos QR.

### Fase 4: Completar las 25 configuraciones

- Completar 5 materias × 5 grados.
- Revisar lenguaje y dificultad por edad.
- Incorporar proyectos y rúbricas.

### Fase 5: Integración frontend

- Crear `StudyGuideDownloader`.
- Integrar en Dashboard.
- Agregar vista previa.
- Agregar descarga automática.

### Fase 6: Pruebas

Validar las 25 combinaciones:

- PDF válido y legible.
- Materia y grado correctos.
- Nombre correcto del estudiante.
- Permisos de acceso.
- Códigos QR funcionales.
- Compatibilidad con padre y estudiante.

---

## 8. Decisiones recomendadas

1. Generación bajo demanda con cache.
2. El niño solo accede a la guía de su grado actual.
3. El padre puede acceder a todas las guías disponibles.
4. La guía infantil no incluye respuestas.
5. Se puede generar una versión opcional para padres con solucionario.
6. Cada guía tendrá una extensión aproximada de 25 a 45 páginas.
7. La primera validación se hará con las cinco guías de 3.º.

---

## 9. Criterios de aceptación

La funcionalidad se considerará completa cuando:

- Existan las 25 combinaciones materia/grado.
- Cada combinación produzca una vista previa.
- Cada combinación permita descargar un PDF.
- El contenido corresponda al grado seleccionado.
- El PDF pueda personalizarse con el nombre del estudiante.
- Los enlaces QR dirijan a actividades válidas.
- Se respeten los permisos entre padres y estudiantes.
- Existan pruebas automatizadas para las 25 guías.

---

## 10. Referencia relacionada

Esta planificación complementa el documento técnico:

`planificacion/generador-guias-pdf/plan-generador-guias.md`
