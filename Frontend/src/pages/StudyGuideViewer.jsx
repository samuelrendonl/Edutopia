import { useEffect, useState } from "react";
import { useNavigate, useSearchParams } from "react-router-dom";
import { fetchStudyGuidePdf, getParent } from "../api";
import "../Styles/study-guide-viewer.css";

const SUBJECT_LABELS = {
  matematicas: "Matemáticas",
  "lengua-castellana": "Lengua Castellana",
  "ciencias-naturales": "Ciencias Naturales",
  sociales: "Sociales",
  ingles: "Inglés",
};

export default function StudyGuideViewer() {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const subject = searchParams.get("subject") || "";
  const grade = Number(searchParams.get("grade"));
  const childId = searchParams.get("child_id") || "";
  const [pdfUrl, setPdfUrl] = useState("");
  const [error, setError] = useState("");

  useEffect(() => {
    if (!getParent()) {
      navigate("/login", { replace: true });
      return undefined;
    }
    let objectUrl = "";
    fetchStudyGuidePdf(subject, grade, childId, { download: false })
      .then((blob) => {
        objectUrl = URL.createObjectURL(blob);
        setPdfUrl(objectUrl);
      })
      .catch((requestError) => setError(requestError.message))
    return () => {
      if (objectUrl) URL.revokeObjectURL(objectUrl);
    };
  }, [childId, grade, navigate, subject]);

  const label = SUBJECT_LABELS[subject] || "Guía de estudio";

  return (
    <div className="study-guide-viewer">
      <header className="study-guide-viewer-header">
        <div>
          <strong>Edutopia</strong>
          <span>{label} · {grade}.º grado</span>
        </div>
        <button type="button" onClick={() => window.close()}>
          Cerrar guía
        </button>
      </header>
      <main className="study-guide-viewer-main">
        {error ? (
          <div className="study-guide-viewer-error">
            <h1>No se pudo abrir la guía</h1>
            <p>{error}</p>
            <button type="button" onClick={() => navigate("/dashboard")}>Volver al panel</button>
          </div>
        ) : pdfUrl ? (
          <iframe title={`${label} ${grade}.º grado`} src={pdfUrl} />
        ) : (
          <div className="study-guide-viewer-loading">Abriendo la guía guardada…</div>
        )}
      </main>
    </div>
  );
}
