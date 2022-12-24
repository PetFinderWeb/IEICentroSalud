import "./Navbar.css";
import { NavLink } from "react-router-dom";
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