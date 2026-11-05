import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";
import "../Styles/dashboard.css";
import { api, getParent, logout } from "../api";
import Icon from "../components/Icon";
import StudyGuideDownloader from "../components/StudyGuideDownloader";

export default function Dashboard() {
  const navigate = useNavigate();
  const [parent] = useState(() => getParent());
  const [children, setChildren] = useState([]);
  const [subjectCatalog, setSubjectCatalog] = useState([]);
  const [error, setError] = useState("");
  const [editingChild, setEditingChild] = useState(null);
  const [editForm, setEditForm] = useState({ name: "", age: "", grade: "" });
  const [isSavingChild, setIsSavingChild] = useState(false);
  const [deletingChildId, setDeletingChildId] = useState(null);
  useEffect(() => {
    if (!parent) {
      navigate("/login");
      return;
    }
    api("/children")
      .then(async (data) => {
        const withProgress = await Promise.all(
          data.children.map(async (child) => {
            try {
              return {
                ...child,
                learning: await api(`/learning/children/${child.id}/progress`),
              };
            } catch {
              return child;
            }
          }),
        );
        setChildren(withProgress);
      })
      .catch((err) => {
        if (err.status === 401) navigate("/login");
        else setError(err.message);
      });
  }, [navigate, parent]);
  useEffect(() => {
    if (!parent) return;
    api("/learning/subjects")
      .then((data) => setSubjectCatalog(data.subjects || []))
      .catch((err) => setError(err.message));
  }, [parent]);
  function exit() {
    logout(navigate);
  }
  function openEditChild(child) {
    setError("");
    setEditingChild(child);
    setEditForm({ name: child.name, age: String(child.age), grade: String(child.grade) });
  }
  function closeEditChild() {
    if (!isSavingChild) setEditingChild(null);
  }
  function updateEditField(event) {
    const { name, value } = event.target;
    setEditForm((current) => ({ ...current, [name]: value }));
  }
  async function saveChild(event) {
    event.preventDefault();
    if (isSavingChild || !editingChild) return;
    setIsSavingChild(true);
    setError("");
    try {
      const data = await api(`/children/${editingChild.id}`, {
        method: "PUT",
        body: JSON.stringify(editForm),
      });
      setChildren((current) => current.map((child) => (
        child.id === editingChild.id ? { ...child, ...data.child } : child
      )));
      setEditingChild(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsSavingChild(false);
    }
  }
  async function removeChild(child) {
    if (deletingChildId || !window.confirm(`¿Eliminar el perfil de ${child.name}? Esta acción también eliminará su progreso.`)) return;
    setDeletingChildId(child.id);
    setError("");
    try {
      await api(`/children/${child.id}`, { method: "DELETE" });
      setChildren((current) => current.filter((item) => item.id !== child.id));
    } catch (err) {
      setError(err.message);
    } finally {
      setDeletingChildId(null);
    }
  }
  const allPoints = children.reduce(
    (sum, child) => sum + (child.learning?.points || 0),
    0,
  );
  const totalSubjects = subjectCatalog.filter((item) => item.available).length;
  const totalActivities = subjectCatalog.reduce((sum, item) => sum + item.activity_count, 0);
  const totalLearning = subjectCatalog.reduce((sum, item) => sum + item.learning_count, 0);
  const totalGames = subjectCatalog.reduce((sum, item) => sum + item.game_count, 0);
  return (
    <div className="dashboard-page">
      <Navbar />
      <main className="dashboard-container">
        <header className="dashboard-header">
          <div>
            <span className="dashboard-label">PANEL DE FAMILIA</span>
            <h1>
              ¡Hola, {parent?.name?.split(" ")[0] || "familia"}!{" "}
              <Icon name="hand" size={34} className="title-icon" />
            </h1>
            <p>
              Administra los perfiles y acompaña el aprendizaje de tus niños.
            </p>
          </div>
          <div className="dashboard-header-actions">
            <Link to="/aprende" className="dashboard-learn-button">
              <Icon name="game" size={19} /> Ver actividades
            </Link>
            <button className="logout-button" onClick={exit}>
              Salir
            </button>
          </div>
        </header>
        {error && <div className="form-error">{error}</div>}
        <section className="dashboard-section">
          <div className="section-heading">
            <div>
              <h2>Mis hijos</h2>
              <p>Cada perfil tiene actividades adaptadas a su grado.</p>
            </div>
            <Link to="/register-child" className="outline-button">
              <span aria-hidden="true">+</span> Agregar niño/niña
            </Link>
          </div>
          {children.length ? (
            <div className="children-list">
              {children.map((child) => {
                const childProgress = child.learning?.progress || 0;
                return (
                  <article className="child-card" key={child.id}>
                    <div className="child-avatar">
                      <Icon name="star" size={29} />
                    </div>
                    <div className="child-info">
                      <span className="child-label">ESTUDIANTE</span>
                      <h3>{child.name}</h3>
                      <p>
                        {child.grade}.º grado · {child.age} años ·{" "}
                        {child.learning?.points || 0} puntos
                      </p>
                    </div>
                    <div className="child-progress">
                      <div className="progress-header">
                        <span>Progreso</span>
                        <strong>{childProgress}%</strong>
                      </div>
                      <div className="progress-bar">
                        <div
                          className="progress-value"
                          style={{ width: `${childProgress}%` }}
                        />
                      </div>
                    </div>
                    <div className="child-card-actions">
                      <Link
                        to={`/aprende?child=${child.id}`}
                        className="primary-action"
                      >
                        Aprender ahora
                      </Link>
                      <div className="child-actions">
                        <button type="button" className="secondary-action" onClick={() => openEditChild(child)}>
                          Editar
                        </button>
                        <button
                          type="button"
                          className="danger-action"
                          onClick={() => removeChild(child)}
                          disabled={deletingChildId === child.id}
                        >
                          {deletingChildId === child.id ? "Eliminando..." : "Eliminar"}
                        </button>
                      </div>
                    </div>
                    <div className="child-guides-wrapper">
                      <StudyGuideDownloader child={child} />
                    </div>
                  </article>
                );
              })}
            </div>
          ) : (
            <div className="empty-state">
              <Icon name="rainbow" size={50} />
              <h3>Aún no hay perfiles</h3>
              <p>Agrega a tu primer niñ@ para empezar la aventura.</p>
              <Link to="/register-child" className="primary-action">
                Crear primer perfil
              </Link>
            </div>
          )}
        </section>
        <section className="stats-grid">
          <article className="stat-card">
            <span>Materias</span>
            <strong>{totalSubjects || "—"}</strong>
            <p>{totalSubjects ? "Catálogo disponible" : "Cargando catálogo"}</p>
          </article>
            <article className="stat-card">
              <span>Actividades</span>
              <strong>{totalActivities || "—"}</strong>
              <p>{totalActivities ? `${totalLearning} aprendizajes y ${totalGames} juegos` : "Cargando catálogo"}</p>
            </article>
          <article className="stat-card">
            <span>Niños</span>
            <strong>{children.length}</strong>
            <p>Perfiles activos</p>
          </article>
          <article className="stat-card">
            <span>Puntos acumulados</span>
            <strong>{allPoints}</strong>
            <p>Mejor puntaje por actividad</p>
          </article>
        </section>
      </main>
      {editingChild && (
        <div className="modal-backdrop" role="presentation" onMouseDown={closeEditChild}>
          <section className="edit-child-modal" role="dialog" aria-modal="true" aria-labelledby="edit-child-title" onMouseDown={(event) => event.stopPropagation()}>
            <div className="modal-header">
              <div>
                <span className="dashboard-label">PERFIL DEL ESTUDIANTE</span>
                <h2 id="edit-child-title">Editar perfil</h2>
              </div>
              <button type="button" className="modal-close" onClick={closeEditChild} disabled={isSavingChild} aria-label="Cerrar">×</button>
            </div>
            <form onSubmit={saveChild}>
              <div className="form-group">
                <label htmlFor="edit-child-name">Nombre completo</label>
                <input id="edit-child-name" name="name" value={editForm.name} onChange={updateEditField} required />
              </div>
              <div className="form-row">
                <div className="form-group">
                  <label htmlFor="edit-child-age">Edad</label>
                  <input id="edit-child-age" name="age" type="number" min="3" max="12" value={editForm.age} onChange={updateEditField} required />
                </div>
                <div className="form-group">
                  <label htmlFor="edit-child-grade">Grado</label>
                  <select id="edit-child-grade" name="grade" value={editForm.grade} onChange={updateEditField} required>
                    <option value="1">1.º grado</option>
                    <option value="2">2.º grado</option>
                    <option value="3">3.º grado</option>
                    <option value="4">4.º grado</option>
                    <option value="5">5.º grado</option>
                  </select>
                </div>
              </div>
              <div className="modal-actions">
                <button type="button" className="secondary-action" onClick={closeEditChild} disabled={isSavingChild}>Cancelar</button>
                <button type="submit" className="primary-action" disabled={isSavingChild}>{isSavingChild ? "Guardando..." : "Guardar cambios"}</button>
              </div>
            </form>
          </section>
        </div>
      )}
    </div>
  );
}
