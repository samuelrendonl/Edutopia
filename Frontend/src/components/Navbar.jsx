import Logo from "./logo";
import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { getParent } from "../api";
import "./../Styles/navbar.css";
import Icon from "./Icon";

const THEME_KEY = "edutopia-theme";

function applyTheme(theme) {
  const root = document.documentElement;
  root.dataset.theme = theme;
  root.style.colorScheme = theme;
}

function Navbar() {
  const navigate = useNavigate();
  const [parent, setParent] = useState(() => getParent());
  const [theme, setTheme] = useState(() =>
    localStorage.getItem(THEME_KEY) === "dark" ? "dark" : "light",
  );
  useEffect(() => {
    applyTheme(theme);
    localStorage.setItem(THEME_KEY, theme);
  }, [theme]);
  useEffect(() => {
    const refreshSession = () => setParent(getParent());
    window.addEventListener("edutopia-auth-change", refreshSession);
    window.addEventListener("storage", refreshSession);
    return () => {
      window.removeEventListener("edutopia-auth-change", refreshSession);
      window.removeEventListener("storage", refreshSession);
    };
  }, []);

  const handleLogoClick = () => {
    if (parent) {
      navigate("/Dashboard");
    } else {
      navigate("/");
    }
  };

  return (
    <nav className="navbar">
      <button
        type="button"
        className="navbar-logo"
        onClick={handleLogoClick}
        aria-label={parent ? "Ir al panel familiar" : "Ir al inicio"}
      >
        <Logo variant="navbar" />
      </button>

      <div className="navbar-actions">
        {parent ? (
          parent.role === "admin" ? (
            <Link to="/admin" className="nav-learn">Administración</Link>
          ) : (
            <Link to="/Dashboard" className="nav-learn">Mi familia</Link>
          )
        ) : (
          <Link to="/login" className="nav-learn">
            Iniciar sesión
          </Link>
        )}

        <button
          type="button"
          className="theme-toggle"
          aria-label={`Tema actual: ${theme === "dark" ? "oscuro" : "claro"}. Cambiar tema`}
          title={`Tema: ${theme === "dark" ? "oscuro" : "claro"}`}
          onClick={() =>
            setTheme((current) => (current === "dark" ? "light" : "dark"))
          }
        >
          <Icon name={theme === "dark" ? "sun" : "cloud"} size={18} />
          <span>{theme === "dark" ? "Oscuro" : "Claro"}</span>
        </button>
      </div>
    </nav>
  );
}

export default Navbar;
