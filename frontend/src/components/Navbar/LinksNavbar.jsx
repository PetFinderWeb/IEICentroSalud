import { NavLink } from "react-router-dom";

export default function LinksNavbar({ claseNav }) {
  return (
    <>
      <div className={"contenedor-links-principales " + claseNav}>
        <ul>
          <li>
            <NavLink to="/LoadForm" className="link-navbar">
              Carga
            </NavLink>
          </li>
          <li>
            <NavLink to="/FiltersForm" className="link-navbar">
              Búsqueda
            </NavLink>
          </li>
        </ul>
      </div>
    </>
  );
}
