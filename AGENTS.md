# Edutopia - Agent Instructions

## Project Overview
Educational platform for primary school children (grades 1-5) with React + Vite frontend and Flask + MySQL backend. Parents create accounts and child profiles; children complete learning activities and games with progress tracking.

## Quick Start

### Prerequisites
- XAMPP (Apache + MySQL) or standalone MySQL
- Python 3.11+ with pip
- Node.js 18+ with npm

### Backend Setup
```bash
cd Backend
pip install -r requirements.txt
# Create .env with MySQL config (see README_XAMPP.md)
python app.py
```
API runs on `http://localhost:5000/api`

### Frontend Setup
```bash
cd Frontend
npm install
npm run dev
```
Vite dev server runs on `http://localhost:5173` (or next available port)

### Database Initialization
1. Start MySQL (via XAMPP)
2. Import `Backend/schema.sql` via phpMyAdmin or CLI
3. For updates: import `Backend/migrations/001_child_activity_progress.sql`

## Key Commands

| Task | Command |
|------|---------|
| Run backend | `cd Backend && python app.py` |
| Run frontend | `cd Frontend && npm run dev` |
| Build frontend | `cd Frontend && npm run build` |
| Lint frontend | `cd Frontend && npm run lint` |
| Run backend tests | `cd Backend && python -m pytest tests/` or `python -m unittest tests.test_learning_content` |

## Architecture Notes

### Backend Structure
```
Backend/
├── app.py                 # Flask entrypoint, auth, children CRUD
├── requirements.txt       # Python deps
├── schema.sql             # Initial DB schema
├── migrations/            # SQL migrations
├── app/
│   ├── __init__.py
│   ├── learning_content.py    # Curriculum catalog + question generators
│   ├── learning_routes.py     # /api/learning/* endpoints
│   ├── auth_sessions.py       # Signed tokens + SQLite revocation store
│   └── extra_content.py       # 6 curriculum units per grade
└── juegos/backend/
    ├── catalog.py         # Game definitions + question generators
    └── routes.py          # /api/games/check (immediate feedback)
```

### Frontend Structure
```
Frontend/
├── src/
│   ├── api.js             # API client + localStorage cache
│   ├── App.jsx            # Routes
│   ├── main.jsx           # Entry + logout on pagehide
│   ├── pages/             # Home, Login, Register, Aprende, Dashboard, RegisterChild
│   ├── components/        # Navbar, Icon, Logo
│   └── Styles/            # CSS modules (global.css has design system)
├── package.json
└── vite.config.js
```

### Critical Implementation Details

**Auth System**
- Tokens: `itsdangerous.URLSafeTimedSerializer` (30 min expiry)
- Revocation: Local SQLite (`sessions.sqlite3` at project root)
- Header: `X-Auth-Token` on all authenticated requests
- Frontend stores `{parent, token}` in `localStorage.edutopia_parent`
- Logout on pagehide via `navigator.sendBeacon` to `/api/auth/logout`

**Database**
- MySQL with `mysql-connector-python` (no ORM)
- Connection per request via Flask `g` object
- Tables: `parents`, `children`, `activities`, `child_activity_progress`

**Activity System**
- 7 base activities in `learning_content.py` (5 aprendizajes, 2 juegos)
- 6 extra curriculum units in `extra_content.py` (3 math, 3 language)
- 4 games in `juegos/backend/catalog.py`
- Questions generated per-grade at runtime (`activity_for_grade`, `game_questions`)
- Public catalog (`/api/learning/activities`) strips answer keys

**CORS**: Currently open (`origins: "*"`) - restrict for production

## Common Gotchas

1. **Circular import**: `learning_content.py` imports from `extra_content.py` and `juegos.backend.catalog`, but `catalog.py` imports from `extra_content.py`
2. **Global cache** `_catalog_cache` in `learning_routes.py` has no TTL/invalidation
3. **SQL injection risk**: Raw SQL in `query()` - all params use `%s` placeholders correctly
4. **Bool passes as int**: `isinstance(True, int) == True` - grade validation in `guest/submit` must exclude bool
5. **Session SQLite** not suitable for multi-worker production (race conditions)
6. **Frontend**: `Aprende.jsx` is a 270-line god component - consider splitting
7. **Hardcoded counts** in Dashboard (15 activities, 11 aprendizajes, 4 juegos)

## Testing
```bash
# Backend only
cd Backend
python -m unittest tests.test_learning_content -v
```
No frontend tests configured. No integration tests.

## Environment Variables
| Variable | Default | Required |
|----------|---------|----------|
| `MYSQL_HOST` | `127.0.0.1` | No |
| `MYSQL_PORT` | `3306` | No |
| `MYSQL_USER` | `root` | Yes |
| `MYSQL_PASSWORD` | `` | Yes (empty for XAMPP default) |
| `MYSQL_DATABASE` | `edutopia` | Yes |
| `SECRET_KEY` | Auto-generated in `.secret_key` | No |
| `PORT` | `5000` | No |

## File Locations for Key Changes

| Change | File(s) |
|--------|---------|
| Add curriculum content | `Backend/app/learning_content.py`, `Backend/app/extra_content.py` |
| Add game | `Backend/juegos/backend/catalog.py`, `Backend/juegos/backend/routes.py` |
| Modify auth flow | `Backend/app/auth_sessions.py`, `Backend/app.py` |
| Add API endpoint | `Backend/app/learning_routes.py` or new blueprint |
| Frontend page | `Frontend/src/pages/*.jsx` |
| Styling | `Frontend/src/Styles/*.css` |
| API client | `Frontend/src/api.js` |