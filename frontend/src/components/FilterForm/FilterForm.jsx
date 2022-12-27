import { useRef } from "react";
import "./FilterForm.css";
import { getCentrosByParams } from "../../services/fetches";
import {
  MapContainer,
  TileLayer,
  Marker,
  Popup,
} from "react-leaflet";

import "leaflet/dist/leaflet.css";
import L from "leaflet"
import { useState } from "react";

function FilterForm() {
  const refForm = useRef();
  const [datos, setDatos] = useState({
    localidad: "",
    cod_postal: "",
    provincia: "",
    tipo: "T",
  });
  const [centros, setCentros] = useState([])


  const handleSubmint = (e) => {
    e.preventDefault();
    getCentrosByParams(datos).then(async (response) => {
      const data = await response.json();
      if (!response.ok) {
        const error = response.statusText;
        return Promise.reject(error);
      }
      setCentros(data);
      console.log(data);
    })
    console.log(datos);
  };
  const IconoMapa = L.icon({
    iconUrl: require("../../recursos/icon.png"),
    iconSize: 100
  });


  const position = [51.505, -0.09]

  return (
    <div className="landing">
      <div className="titulo">
        <h1>Buscador de centros de salud</h1>
      </div>
      <div className="contenedor-principal">
        <div className="contenedor-formulario">
          <form ref={refForm} onSubmit={handleSubmint}>
            <label>Localidad</label>
            <input type="text" placeholder="Localidad" onChange={(e) => {
              let datosAux = datos;
              datosAux.localidad = e.target.value;
              setDatos(datosAux)
            }}></input>
            <label>Codigo postal</label>
            <input type="text" placeholder="Codigo postal" onChange={(e) => {
              let datosAux = datos;
              datosAux.cod_postal = e.target.value;
              setDatos(datosAux)
            }}></input>
            <label>Provincia</label>
            <input type="text" placeholder="Provincia" onChange={(e) => {
              let datosAux = datos;
              datosAux.provincia = e.target.value;
              setDatos(datosAux)
            }}></input>
            <label>Tipo de centro</label>
            <select
              onChange={(e) => {
                let datosAux = datos;
                datosAux.tipo = e.target.value;
                setDatos(datosAux)
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
            center={[39.466, -0.37]}
            zoom={12}
            scrollWheelZoom={false}
          >
            <TileLayer
              attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
             {centros.map((centro, index) => (
              <Marker
                key={index}
                position={[centro.fields.latitud, centro.fields.longitud]}
                icon={IconoMapa}
              >
                <Popup className="popup">
                  <div>
                    <h1>HOLAAAAA</h1>
                  </div>
                </Popup>
              </Marker>
            ))}
          </MapContainer>

        </div>
      </div>
    </div>
  );
}

export default FilterForm;
