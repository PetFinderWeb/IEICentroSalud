// Componente padre que englobara otros elementos que nunca cambiaran de sitio y son comunes a todas las paginas.
//Por ejemplo, la Navbar
import "./Layout.css";
import Navbar from "../Navbar/Navbar";
import { Outlet } from "react-router-dom";

const Layout = () => {
  return (
    <>
      <Navbar></Navbar>
      <Outlet></Outlet>
    </>
  );
};

export default Layout;
