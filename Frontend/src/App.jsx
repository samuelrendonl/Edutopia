import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useEffect } from "react";

import Home from "./pages/home";
import Login from "./pages/login";
import Register from "./pages/Register";
import Aprende from "./pages/Aprende";
import Dashboard from "./pages/Dashboard";
import RegisterChild from "./pages/RegisterChild";
import Terms from "./pages/Terms";
import SessionGuard from "./components/SessionGuard";
import Admin from "./pages/Admin";
import StudyGuideViewer from "./pages/StudyGuideViewer";

const THEME_KEY = "edutopia-theme";

function ThemeInitializer() {
  useEffect(() => {
    const theme = localStorage.getItem(THEME_KEY) === "dark" ? "dark" : "light";
    document.documentElement.dataset.theme = theme;
    document.documentElement.style.colorScheme = theme;
  }, []);

  return null;
}

function App() {
  return (
    <BrowserRouter>
      <ThemeInitializer />
      <SessionGuard>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/aprende" element={<Aprende />} />
          <Route path="/study-guide" element={<StudyGuideViewer />} />
          {/* Compatibilidad con despliegues que redirigen a index.html. */}
          <Route path="/index.html" element={<StudyGuideViewer />} />
          <Route path="/dashboard/*" element={<Dashboard />} />
          <Route path="/Dashboard/*" element={<Dashboard />} />
          <Route path="/admin" element={<Admin />} />
          <Route path="/register-child" element={<RegisterChild />} />
          <Route path="/terminos" element={<Terms />} />
          <Route path="/terminos-y-condiciones" element={<Terms />} />
        </Routes>
      </SessionGuard>
    </BrowserRouter>
  );
}

export default App;
