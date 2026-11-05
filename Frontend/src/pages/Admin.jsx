import { useEffect, useMemo, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";
import Icon from "../components/Icon";
import { api, getParent } from "../api";
import "../Styles/admin.css";

const roleLabels = {
  parent: "Familia",
  teacher: "Docente",
  editor: "Editor de contenidos",
  admin: "Administrador",
};

export default function Admin() {
  const navigate = useNavigate();
  const [parent] = useState(() => getParent());
  const [grade, setGrade] = useState("all");
  const [catalog, setCatalog] = useState([]);
  const [users, setUsers] = useState([]);
  const [roles, setRoles] = useState([]);
  const [overview, setOverview] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!parent) {
      navigate("/login", { replace: true });
      return;
    }
    if (parent.role !== "admin") {
      navigate("/Dashboard", { replace: true });
      return;
    }

    Promise.all([
      api("/admin/catalog"),
      api("/admin/users"),
      api("/admin/roles"),
      api("/admin/overview"),
    ])
      .then(([catalogData, usersData, rolesData, overviewData]) => {
        setCatalog(catalogData.activities || []);
        setUsers(usersData.users || []);
        setRoles(rolesData.roles || []);
        setOverview(overviewData);
      })
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, [navigate, parent]);

  const visibleCatalog = useMemo(
    () =>
      grade === "all"
        ? catalog
        : catalog.filter((item) => item.grade === Number(grade)),
    [catalog, grade],
  );

  async function changeRole(userId, role) {
    setError("");
    try {
      await api(`/admin/users/${userId}/role`, {
        method: "PATCH",
        body: JSON.stringify({ role }),
      });
      setUsers((current) =>
        current.map((user) => (user.id === userId ? { ...user, role } : user)),
      );
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <div className="admin-page">
      <Navbar />
      <main className="admin-container">
        <header className="admin-header">
          <div>
            <span className="eyebrow">CONTROL DE EDUTOPIA</span>
            <h1>
              Panel administrativo <Icon name="shield" size={32} />
            </h1>
            <p>Consulta el currículo completo y administra los permisos de la plataforma.</p>
          </div>
          <Link to="/Dashboard" className="admin-back-link">Volver al panel</Link>
        </header>

        {error && <div className="form-error" role="alert">{error}</div>}
        {loading ? (
          <div className="admin-empty">Cargando información administrativa…</div>
        ) : (
          <>
            <section className="admin-stats" aria-label="Resumen administrativo">
              <article><span>Aprendizajes</span><strong>{overview?.learning_activities || 0}</strong><small>Catálogo completo</small></article>
              <article><span>Usuarios</span><strong>{overview?.users || 0}</strong><small>Cuentas registradas</small></article>
              <article><span>Perfiles infantiles</span><strong>{overview?.children || 0}</strong><small>En toda la plataforma</small></article>
              <article><span>Roles</span><strong>{roles.length}</strong><small>Con permisos diferenciados</small></article>
            </section>

            <section className="admin-section">
              <div className="admin-section-heading">
                <div>
                  <span className="eyebrow">CATÁLOGO CURRICULAR</span>
                  <h2>Todos los aprendizajes</h2>
                  <p>Explora las unidades por grado. Las respuestas correctas permanecen protegidas.</p>
                </div>
                <label className="admin-filter">Grado
                  <select value={grade} onChange={(event) => setGrade(event.target.value)}>
                    <option value="all">Todos</option>
                    {[1, 2, 3, 4, 5].map((item) => <option key={item} value={item}>{item}.º grado</option>)}
                  </select>
                </label>
              </div>
              <div className="admin-catalog-grid">
                {visibleCatalog.map((activity) => (
                  <details className="admin-activity" key={`${activity.key}-${activity.grade}`}>
                    <summary>
                      <span className="admin-activity-icon" style={{ background: activity.color }}><Icon name={activity.icon} size={25} /></span>
                      <span><small>{activity.subject} · {activity.grade}.º grado</small><strong>{activity.title}</strong></span>
                    </summary>
                    <p>{activity.description}</p>
                    {activity.objective && <p className="admin-objective"><strong>Objetivo:</strong> {activity.objective}</p>}
                    <ul>{(activity.lesson || []).map((line) => <li key={line}>{line}</li>)}</ul>
                    <span className="admin-question-count">{activity.questions?.length || 0} preguntas de práctica</span>
                  </details>
                ))}
              </div>
            </section>

            <section className="admin-section">
              <div className="admin-section-heading">
                <div><span className="eyebrow">ACCESOS</span><h2>Usuarios y roles</h2><p>Asigna el nivel de acceso según la responsabilidad de cada cuenta.</p></div>
              </div>
              <div className="admin-table-wrap">
                <table className="admin-table">
                  <thead><tr><th>Usuario</th><th>Correo</th><th>Rol</th><th>Acceso</th></tr></thead>
                  <tbody>{users.map((user) => (
                    <tr key={user.id}>
                      <td><strong>{user.name}</strong></td>
                      <td>{user.email}</td>
                      <td>
                        <select value={user.role || "parent"} onChange={(event) => changeRole(user.id, event.target.value)}>
                          {Object.keys(roleLabels).map((role) => <option key={role} value={role}>{roleLabels[role]}</option>)}
                        </select>
                      </td>
                      <td><span className="admin-role-badge">{roleLabels[user.role] || "Familia"}</span></td>
                    </tr>
                  ))}</tbody>
                </table>
              </div>
            </section>

            <section className="admin-section">
              <div className="admin-section-heading"><div><span className="eyebrow">PERMISOS CONFIGURADOS</span><h2>Qué puede hacer cada rol</h2></div></div>
              <div className="admin-roles-grid">{roles.map((role) => (
                <article className="admin-role-card" key={role.name}>
                  <h3>{role.display_name}</h3><p>{role.description}</p>
                  <ul>{role.permissions.map((permission) => <li key={permission}>{permission}</li>)}</ul>
                </article>
              ))}</div>
            </section>
          </>
        )}
      </main>
    </div>
  );
}
