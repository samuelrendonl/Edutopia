import { useEffect, useRef, useState } from "react";
import { fetchStudyGuidePdf } from "../api";

const SUBJECTS = [
  { slug: "matematicas", label: "Matemáticas", color: "#5b5ce2" },
  { slug: "lengua-castellana", label: "Lengua Castellana", color: "#f28c28" },
  { slug: "ciencias-naturales", label: "Ciencias Naturales", color: "#21a889" },
  { slug: "sociales", label: "Sociales", color: "#e66a9b" },
  { slug: "ingles", label: "Inglés", color: "#3ba9dd" },
];

function saveBlob(blob, subject, child) {
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = `Guia_Estudio_${subject.slug}_${child.grade}.pdf`;
  document.body.appendChild(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(url);
}

export default function StudyGuideDownloader({ child }) {
  const [active, setActive] = useState("");
  const [error, setError] = useState("");
  const [notice, setNotice] = useState("");
  const [preview, setPreview] = useState(null);
  const previewUrlRef = useRef("");
  const grade = Number(child.grade);

  useEffect(() => () => {
    if (previewUrlRef.current) URL.revokeObjectURL(previewUrlRef.current);
  }, []);

  function closePreview() {
    if (previewUrlRef.current) URL.revokeObjectURL(previewUrlRef.current);
    previewUrlRef.current = "";
    setPreview(null);
  }

  async function handleGuide(subject, mode) {
    if (mode === "preview") {
      setActive(`${subject.slug}-${mode}`);
      setError("");
      setNotice(`Preparando la guía de ${subject.label} de ${grade}.º grado…`);
      try {
        const blob = await fetchStudyGuidePdf(subject.slug, grade, child.id, { download: false });
        if (previewUrlRef.current) URL.revokeObjectURL(previewUrlRef.current);
        previewUrlRef.current = URL.createObjectURL(blob);
        setPreview({ subject: subject.label, url: previewUrlRef.current });
      } catch (requestError) {
        setError(requestError.message);
      } finally {
        setActive("");
        setNotice("");
      }
      return;
    }
    setActive(`${subject.slug}-${mode}`);
    setError("");
    setNotice(`Descargando la guía guardada de ${subject.label} de ${grade}.º grado…`);
    try {
      const blob = await fetchStudyGuidePdf(subject.slug, grade, child.id);
      saveBlob(blob, subject, child);
    } catch (requestError) {
      setError(requestError.message);
    } finally {
      setActive("");
      setNotice("");
    }
  }

  return (
    <section className="study-guide-panel" aria-label={`Guías de ${child.name}`}>
      <div className="study-guide-heading">
        <div>
          <span className="child-label">GUÍAS DE ESTUDIO</span>
          <h4>Practica en casa</h4>
        </div>
        <span className="study-guide-grade">{grade}.º grado · 5 materias</span>
      </div>
      <div className="study-guide-grid">
        {SUBJECTS.map((subject) => (
          <div className="study-guide-card" key={subject.slug} style={{ "--guide-color": subject.color }}>
            <strong>{subject.label} · {grade}.º</strong>
            <div className="study-guide-actions">
              <button
                type="button"
                className="study-guide-button secondary"
                onClick={() => handleGuide(subject, "preview")}
                disabled={Boolean(active)}
              >
                {active === `${subject.slug}-preview` ? "Abriendo…" : "Vista previa"}
              </button>
              <button
                type="button"
                className="study-guide-button primary"
                onClick={() => handleGuide(subject, "download")}
                disabled={Boolean(active)}
              >
                {active === `${subject.slug}-download` ? "Preparando…" : "Descargar PDF"}
              </button>
            </div>
          </div>
        ))}
      </div>
      {error && <p className="study-guide-error">{error}</p>}
      {notice && <p className="study-guide-notice" role="status">{notice}</p>}
      {preview && (
        <div className="study-guide-preview-backdrop" role="presentation" onMouseDown={closePreview}>
          <section className="study-guide-preview-modal" role="dialog" aria-modal="true" aria-label={`Vista previa de ${preview.subject}`} onMouseDown={(event) => event.stopPropagation()}>
            <div className="study-guide-preview-header">
              <div>
                <span className="child-label">VISTA PREVIA</span>
                <h3>{preview.subject} · {grade}.º grado</h3>
              </div>
              <button type="button" onClick={closePreview}>Cerrar</button>
            </div>
            <iframe title={`Vista previa de ${preview.subject}`} src={preview.url} />
          </section>
        </div>
      )}
    </section>
  );
}
