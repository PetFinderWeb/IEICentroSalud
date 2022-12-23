import { useRef } from "react";
import "./FilterForm.css";

import {
  MapContainer,
  TileLayer,
  useMapEvents,
  Marker,
  Popup,
} from "react-leaflet";

import "leaflet/dist/leaflet.css";
import L, { LatLng, marker } from "leaflet";

function FilterForm() {
  const refForm = useRef();

  const datos = {
    localidad: "",
    cod_postal: "",
    provincia: "",
    tipo: "",
  };
  const handleSubmint = (e) => {
    e.preventDefault();
    console.log(datos);
  };

  return (
    <div className="landing">
      <div className="titulo">
        <h1>Buscador de centros de salud</h1>
      </div>
      <div className="contenedor-principal">
        <div className="contenedor-formulario">
          <form ref={refForm} onSubmit={handleSubmint}>
            <label>Localidad</label>
            <input type="text" placeholder="Localidad"></input>
            <label>Codigo postal</label>
            <input type="text" placeholder="Codigo postal"></input>
            <label>Provincia</label>
            <input type="text" placeholder="Provincia"></input>
            <label>Tipo de centro</label>
            <select
              onChange={(e) => {
                datos.tipo = e.value;
              }}
            >
              <option value="T">Todos</option>
              <option value="C">Centro de salud</option>
              <option value="H">Hospital</option>
              <option value="O">Otros</option>
            </select>
            <div className="contenedor-botones">
              <button type="submit">Cargar</button>
              <button
                type="button"
                onClick={() => {
                  refForm.current.reset();
                }}
              >
                Cancelar
              </button>
            </div>
          </form>
        </div>
        <div className="contenedor-mapa">
          <MapContainer
            center={[51.505, -0.09]}
            zoom={13}
            scrollWheelZoom={false}
          >
            <TileLayer
              attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            <Marker position={[51.505, -0.09]}>
              <Popup>
                A pretty CSS3 popup. <br /> Easily customizable.
              </Popup>
            </Marker>
          </MapContainer>
        </div>
      </div>
    </div>
  );
}

export default FilterForm;
