import { useEffect } from "react";
import { Link } from "react-router-dom";
import Navbar from "../components/Navbar";
import Icon from "../components/Icon";
import "../Styles/terms.css";

export default function Terms() {
  // Update navbar auth state on mount
  useEffect(() => {
    window.dispatchEvent(new Event("edutopia-auth-change"));
  }, []);

  return (
    <div className="terms-page">
      <Navbar />
      <main className="terms-container">
        <header className="terms-header">
          <span className="eyebrow">INFORMACIÓN LEGAL</span>
          <h1>Términos y Condiciones</h1>
          <p className="terms-subtitle">
            Última actualización: {new Date().toLocaleDateString("es-ES", { year: "numeric", month: "long", day: "numeric" })}
          </p>
        </header>

        <div className="terms-content">
          <nav className="terms-toc" aria-label="Tabla de contenidos">
            <h3>Contenido</h3>
            <ul>
              <li><a href="#aceptacion">1. Aceptación de los términos</a></li>
              <li><a href="#servicio">2. Descripción del servicio</a></li>
              <li><a href="#cuentas">3. Cuentas y registro</a></li>
              <li><a href="#privacidad">4. Privacidad y datos personales</a></li>
              <li><a href="#uso">5. Uso responsable</a></li>
              <li><a href="#propiedad">6. Propiedad intelectual</a></li>
              <li><a href="#limitacion">7. Limitación de responsabilidad</a></li>
              <li><a href="#modificaciones">8. Modificaciones</a></li>
              <li><a href="#contacto">9. Contacto</a></li>
            </ul>
          </nav>

          <div className="terms-sections">
            <section id="aceptacion" className="terms-section">
              <h2>1. Aceptación de los términos</h2>
              <p>
                Al acceder y usar Edutopia, aceptas cumplir y estar legalmente obligado por estos Términos y Condiciones.
                Si no estás de acuerdo con alguna parte de estos términos, no debes usar nuestro servicio.
              </p>
              <p>
                Edutopia es una plataforma educativa diseñada para niños de primaria (grados 1.º a 5.º) que combina
                aprendizajes estructurados, juegos interactivos y gestión familiar para el seguimiento del progreso.
              </p>
            </section>

            <section id="servicio" className="terms-section">
              <h2>2. Descripción del servicio</h2>
              <p>Edutopia proporciona:</p>
              <ul>
                 <li>Actividades curriculares adaptadas por grado (Matemáticas, Lengua Castellana, Ciencias Naturales, Sociales, Inglés)</li>
                <li>Juegos educativos con retroalimentación inmediata</li>
                <li>Seguimiento de progreso por perfil infantil</li>
                <li>Panel familiar para gestión de perfiles y supervisión</li>
                <li>Guías de estudio descargables en PDF</li>
              </ul>
              <p>
                El contenido está alineado con estándares curriculares de primaria y se actualiza periódicamente.
                Nos reservamos el derecho de modificar, suspender o descontinuar cualquier parte del servicio.
              </p>
            </section>

            <section id="cuentas" className="terms-section">
              <h2>3. Cuentas y registro</h2>
              <h3>3.1 Registro de adultos</h3>
              <p>
                Solo los padres, madres o tutores legales pueden crear una cuenta. Debes proporcionar información
                veraz, precisa y completa. Eres responsable de mantener la confidencialidad de tus credenciales.
              </p>
              <h3>3.2 Perfiles infantiles</h3>
              <p>
                Los perfiles infantiles se crean bajo la supervisión del adulto. No se recopilan datos de contacto
                directo de los menores. El adulto gestiona el acceso y puede eliminar perfiles en cualquier momento.
              </p>
              <h3>3.3 Seguridad</h3>
              <p>
                Las sesiones usan tokens firmados con expiración de 30 minutos. El cierre de sesión revoca el token
                inmediatamente. Recomendamos no compartir credenciales y usar contraseñas seguras.
              </p>
            </section>

            <section id="privacidad" className="terms-section">
              <h2>4. Privacidad y tratamiento de datos personales</h2>
              <h3>4.1 Datos que recopilamos</h3>
              <ul>
                <li><strong>Adultos:</strong> Nombre, correo electrónico, hash de contraseña</li>
                <li><strong>Perfiles infantiles:</strong> Nombre, edad, grado, avatar, progreso de actividades</li>
                <li><strong>Datos de uso:</strong> Actividades completadas, puntuaciones, tiempo de uso</li>
              </ul>
              <h3>4.2 Finalidad del tratamiento</h3>
              <p>Los datos se usan exclusivamente para:</p>
              <ul>
                <li>Proveer el servicio educativo y personalizar la experiencia por grado</li>
                <li>Guardar progreso y generar reportes para el adulto</li>
                <li>Enviar comunicaciones relacionadas con el servicio (no marketing)</li>
                <li>Mejorar la plataforma mediante analíticas agregadas y anónimas</li>
              </ul>
              <h3>4.3 Base legal</h3>
              <p>
                El tratamiento se basa en el consentimiento del tutor legal (Art. 6.1.a RGPD) y en la ejecución
                del contrato de servicio (Art. 6.1.b RGPD).
              </p>
              <h3>4.4 Derechos del usuario</h3>
              <p>Como tutor legal, tienes derecho a:</p>
              <ul>
                <li>Acceder a los datos de tus perfiles infantiles</li>
                <li>Rectificar información inexacta o incompleta</li>
                <li>Solicitar la supresión de datos (derecho al olvido)</li>
                <li>Limitar u oponerte al tratamiento</li>
                <li>Portabilidad de los datos</li>
              </ul>
              <p>Para ejercer estos derechos, contacta a <a href="mailto:privacidad@edutopia.app">privacidad@edutopia.app</a>.</p>
              <h3>4.5 Conservación</h3>
              <p>
                Los datos se conservan mientras la cuenta esté activa. Tras la eliminación de la cuenta,
                los datos se anonimizan o eliminan en un plazo máximo de 30 días, salvo obligación legal.
              </p>
              <h3>4.6 Seguridad técnica</h3>
              <p>
                Implementamos medidas técnicas y organizativas apropiadas: cifrado en tránsito (HTTPS),
                hashing de contraseñas (bcrypt), tokens de sesión firmados y revocables, y acceso a base de datos
                restringido. No obstante, ninguna transmisión por Internet es 100% segura.
              </p>
            </section>

            <section id="uso" className="terms-section">
              <h2>5. Uso responsable</h2>
              <p>Te comprometes a:</p>
              <ul>
                <li>Usar la plataforma solo con fines educativos y personales</li>
                <li>No intentar acceder a cuentas ajenas ni vulnerar medidas de seguridad</li>
                <li>No distribuir, modificar ni crear obras derivadas del contenido sin autorización</li>
                <li>No usar bots, scripts o automatizaciones que sobrecarguen el servicio</li>
                <li>Reportar cualquier vulnerabilidad o uso indebido</li>
              </ul>
              <p>Nos reservamos el derecho de suspender o eliminar cuentas que incumplan estos términos.</p>
            </section>

            <section id="propiedad" className="terms-section">
              <h2>6. Propiedad intelectual</h2>
              <p>
                Edutopia, su marca, logotipo, código fuente, diseños, contenidos curriculares, ilustraciones
                y materiales descargables son propiedad de sus creadores o licenciados. Queda prohibida su
                reproducción, distribución o comunicación pública sin autorización expresa.
              </p>
              <p>
                Los iconos e ilustraciones SVG son creaciones originales o provienen de fuentes de dominio público
                / licencias abiertas compatibles.
              </p>
            </section>

            <section id="limitacion" className="terms-section">
              <h2>7. Limitación de responsabilidad</h2>
              <p>
                Edutopia se proporciona "tal cual" y "según disponibilidad". No garantizamos que el servicio
                sea ininterrumpido, libre de errores, o que los resultados educativos sean específicos.
              </p>
              <p>
                En la medida máxima permitida por ley, no seremos responsables por daños indirectos, incidentales,
                consecuentes o punitivos, incluyendo pérdida de datos, uso o beneficios.
              </p>
            </section>

            <section id="modificaciones" className="terms-section">
              <h2>8. Modificaciones</h2>
              <p>
                Podemos actualizar estos términos periódicamente. Los cambios sustanciales se notificarán
                mediante aviso en la plataforma o por correo electrónico. El uso continuado tras la notificación
                implica aceptación de los nuevos términos.
              </p>
            </section>

            <section id="contacto" className="terms-section">
              <h2>9. Contacto</h2>
              <p>Para consultas sobre estos términos, privacidad o el servicio:</p>
              <ul className="contact-list">
                <li><Icon name="mail" size={18} /> <a href="mailto:legal@edutopia.app">legal@edutopia.app</a></li>
                <li><Icon name="mail" size={18} /> <a href="mailto:privacidad@edutopia.app">privacidad@edutopia.app</a></li>
                <li><Icon name="mail" size={18} /> <a href="mailto:soporte@edutopia.app">soporte@edutopia.app</a></li>
              </ul>
              <p className="contact-note">
                Edutopia — Proyecto académico desarrollado por Samuel Calderón, Johan Castro, Manuel Pulido y Samuel Rendón.
              </p>
            </section>
          </div>
        </div>

        <div className="terms-footer">
          <Link to="/" className="terms-back-link">
            <Icon name="arrowRight" size={18} />
            Volver al inicio
          </Link>
        </div>
      </main>
    </div>
  );
}
