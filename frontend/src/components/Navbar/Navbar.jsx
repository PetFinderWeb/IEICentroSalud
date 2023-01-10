/**
 * Componente que crea la barra de navegación, desde donde se seleccionan dos los formularios
 */
import "./Navbar.css";
import { useState } from "react";
import LinksNavbar from "./LinksNavbar";
const Navbar = () => {
  const [activo, setActivo] = useState("false");

  const handleToggle = () => {
    setActivo(!activo);
  };

  return (
    <>
      <div className="navbar">
        <div className="logo"></div>
        <LinksNavbar claseNav={activo ? "" : "navbar-movil"} />
        <div className="contenedor-botones-sesion">
          <button className="navbar-toggler" onClick={handleToggle}></button>
        </div>
      </div>
    </>
  );
};

export default Navbar;
