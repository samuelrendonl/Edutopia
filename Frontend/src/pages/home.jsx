import { Link } from "react-router-dom";
import Navbar from "../components/Navbar";
import "../Styles/home.css";
import Icon from "../components/Icon";

export default function Home() {
  return (
    <div className="home">
      <Navbar />
      <main className="hero">
        <div className="hero-content">
          <span className="hero-tag">
            <Icon name="rainbow" size={18} /> UN ESPACIO PARA CRECER
          </span>
          <h1 style={{ size: "35px" }}>Aprender puede ser una gran aventura</h1>
          <p>
            Edutopia acompaña a niños de primaria con actividades, juegos y
            retos pensados para despertar su curiosidad.
          </p>
          <div className="hero-actions">
            <Link to="/register" className="primary-button">
              Soy papá o mamá
            </Link>
          </div>
          <div className="hero-trust">
            <span>
              <Icon name="check" size={16} /> Sin registro para explorar
            </span>
            <span>
              <Icon name="target" size={16} /> Grados 1.º a 5.º
            </span>
            <span>
              <Icon name="star" size={16} /> Hecho para niños
            </span>
          </div>
        </div>
        <div className="hero-illustration">
          <div className="sun">
            <Icon name="sun" size={42} />
          </div>
          <div className="cloud cloud-one">
            <Icon name="cloud" size={46} />
          </div>
          <div className="cloud cloud-two">
            <Icon name="cloud" size={42} />
          </div>
          <div className="planet">
            <Icon name="planet" size={82} />
          </div>
          <div className="character">
            <Icon name="star" size={132} />
          </div>
          <div className="book">
            <Icon name="book" size={68} />
          </div>
        </div>
      </main>
      <section id="about" className="about">
        <span className="eyebrow">ASÍ APRENDEMOS</span>
        <h2>Pequeños pasos, grandes descubrimientos</h2>
        <p>
          Los niños exploran a su ritmo y los adultos pueden acompañar su
          progreso desde un espacio seguro y sencillo.
        </p>
        <div className="features">
          <article>
            <span>
              <Icon name="game" size={34} />
            </span>
            <h3>Juega y descubre</h3>
            <p>
              Retos cortos que convierten cada materia en una misión divertida.
            </p>
          </article>
          <article>
            <span>
              <Icon name="family" size={34} />
            </span>
            <h3>Familias al mando</h3>
            <p>
              El adulto crea la cuenta y agrega uno o varios perfiles
              infantiles.
            </p>
          </article>
          <article>
            <span>
              <Icon name="book" size={34} />
            </span>
            <h3>Todo organizado</h3>
            <p>Actividades separadas por materias y grados de primaria.</p>
          </article>
        </div>
      </section>

      <footer className="site-footer" role="contentinfo">
        <div className="footer-main">
          <div className="footer-brand">
            <div className="footer-logo">
              <Icon name="sparkles" size={36} />
            </div>
            <p className="footer-tagline">
              Un espacio donde aprender se vuelve una aventura.
            </p>
          </div>

          <div className="footer-credits">
            <h4>Equipo de desarrollo</h4>
            <ul className="credits-list">
              <li>
                <Icon name="users" size={16} />
                <span>Samuel Calderón</span>
              </li>
              <li>
                <Icon name="users" size={16} />
                <span>Johan Castro</span>
              </li>
              <li>
                <Icon name="users" size={16} />
                <span>Manuel Pulido</span>
              </li>
              <li>
                <Icon name="users" size={16} />
                <span>Samuel Rendón</span>
              </li>
            </ul>
            <p className="credits-note">
              Proyecto académico · Desarrollo Sostenible · 2026
            </p>
          </div>

          <div className="footer-links">
            <h4>Enlaces rápidos</h4>
            <nav aria-label="Navegación principal">
              <Link to="/aprende" className="footer-link">
                <Icon name="book" size={16} /> Aprender
              </Link>
              <Link to="/register" className="footer-link">
                <Icon name="sparkles" size={16} /> Regístrate
              </Link>
              <Link to="/login" className="footer-link">
                <Icon name="hand" size={16} /> Iniciar sesión
              </Link>
              <Link to="/terminos-y-condiciones" className="footer-link">
                <Icon name="shield" size={16} /> Información Legal
              </Link>
            </nav>
          </div>
        </div>

        <div className="footer-bottom">
          <p className="copyright">
            &copy; {new Date().getFullYear()} Edutopia. Todos los derechos
            reservados.
          </p>
          <p className="made-with">
            Hecho con <Icon name="heart" size={14} /> para la educación infantil
          </p>
        </div>
      </footer>
    </div>
  );
}
