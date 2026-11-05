import { useEffect, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import { api, getParent, logout } from "../api";

const IDLE_MS = 30 * 60 * 1000;       // 30 minutos
const WARN_AT = 20 * 60 * 1000;      // aviso a los 20 minutos
const PING_EVERY = 5 * 60 * 1000;    // mantener la sesión viva en el backend

export default function SessionGuard({ children }) {
  const navigate = useNavigate();
  const [status, setStatus] = useState("none"); // none | warning | expired
  const statusRef = useRef("none");
  const warningTimer = useRef(null);
  const expireTimer = useRef(null);
  const lastPingRef = useRef(0);

  function updateStatus(next) {
    statusRef.current = next;
    setStatus(next);
  }

  function clearTimers() {
    if (warningTimer.current) clearTimeout(warningTimer.current);
    if (expireTimer.current) clearTimeout(expireTimer.current);
    warningTimer.current = null;
    expireTimer.current = null;
  }

  function pingBackend() {
    if (!getParent()?.token) return;
    const now = Date.now();
    if (now - lastPingRef.current < PING_EVERY) return;
    lastPingRef.current = now;
    api("/children").catch(() => {});
  }

  function schedule() {
    clearTimers();
    warningTimer.current = setTimeout(() => {
      if (statusRef.current !== "expired") updateStatus("warning");
    }, WARN_AT);
    expireTimer.current = setTimeout(() => {
      const parent = getParent();
      if (parent?.token) {
        api("/auth/logout", { method: "POST" }).catch(() => {});
      }
      logout(navigate);
      updateStatus("expired");
    }, IDLE_MS);
  }

  function reactivate() {
    if (statusRef.current === "expired") return;
    clearTimers();
    updateStatus("none");
    pingBackend();
    schedule();
  }

  useEffect(() => {
    if (!getParent()?.token) return;

    schedule();

    function onActivity() {
      if (!getParent()?.token) return;
      if (statusRef.current === "expired") return;
      if (statusRef.current === "warning") {
        reactivate();
      } else {
        clearTimers();
        pingBackend();
        schedule();
      }
    }

    const events = ["mousedown", "keydown", "scroll", "touchstart", "pointermove"];
    const throttled = (() => {
      let last = 0;
      return () => {
        const now = Date.now();
        if (now - last < 1000) return;
        last = now;
        onActivity();
      };
    })();

    events.forEach((e) => window.addEventListener(e, throttled, { passive: true }));

    return () => {
      events.forEach((e) => window.removeEventListener(e, throttled));
      clearTimers();
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const parent = getParent();

  if (status === "none" && !parent?.expired) {
    return children;
  }

  return (
    <>
      {children}
      <div
        style={{
          position: "fixed",
          inset: 0,
          background: "rgba(15, 23, 42, 0.65)",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          zIndex: 9999,
          padding: "1.5rem",
        }}
      >
        <div
          style={{
            background: "#ffffff",
            color: "#1e293b",
            borderRadius: "20px",
            padding: "2rem",
            maxWidth: "420px",
            width: "100%",
            textAlign: "center",
            boxShadow: "0 24px 60px rgba(0,0,0,0.35)",
            animation: "popIn 0.25s ease",
          }}
        >
          {status === "warning" ? (
            <>
              <div style={{ fontSize: "3rem", marginBottom: "0.5rem" }}>⏳</div>
              <h2 style={{ marginBottom: "0.5rem" }}>¿Sigues ahí?</h2>
              <p style={{ color: "#475569", lineHeight: 1.5, marginBottom: "1.25rem" }}>
                Tu sesión se cerrará en <strong>10 minutos</strong> por inactividad.
                Haz clic en “Seguir conectado” o mueve el mouse para mantenerla activa.
              </p>
              <button
                onClick={reactivate}
                style={{
                  background: "linear-gradient(135deg,#5b5ce2,#35b9dd)",
                  color: "#fff",
                  border: "none",
                  borderRadius: "12px",
                  padding: "0.85rem 1.5rem",
                  fontWeight: 800,
                  fontSize: "1rem",
                  cursor: "pointer",
                  width: "100%",
                }}
              >
                Seguir conectado
              </button>
            </>
          ) : (
            <>
              <div style={{ fontSize: "3rem", marginBottom: "0.5rem" }}>🔒</div>
              <h2 style={{ marginBottom: "0.5rem" }}>Sesión cerrada por inactividad</h2>
              <p style={{ color: "#475569", lineHeight: 1.5, marginBottom: "1.25rem" }}>
                Hemos cerrado tu sesión después de 30 minutos sin actividad. ¡No te
                preocupes, puedes volver a entrar cuando quieras!
              </p>
              <button
                onClick={() => {
                  updateStatus("none");
                  navigate("/login");
                }}
                style={{
                  background: "linear-gradient(135deg,#5b5ce2,#35b9dd)",
                  color: "#fff",
                  border: "none",
                  borderRadius: "12px",
                  padding: "0.85rem 1.5rem",
                  fontWeight: 800,
                  fontSize: "1rem",
                  cursor: "pointer",
                  width: "100%",
                }}
              >
                Iniciar sesión de nuevo
              </button>
            </>
          )}
        </div>
      </div>
    </>
  );
}
