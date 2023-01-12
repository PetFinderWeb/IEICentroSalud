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

//Componente del formulario filtrado
function FilterForm() {
  const refForm = useRef();
  //Datos del filtro aplicado por el usuario
  const [datos, setDatos] = useState({
    localidad: "",
    cod_postal: "",
    provincia: "",
    tipo: "T",
  });
  //Estado de los centros
  const [centros, setCentros] = useState([])

//Metodo que se llama cuando se envia el formulario
  const handleSubmint = (e) => {
    //Evita el reseteo de datos del formulario
    e.preventDefault();
    //Realiza la llamada al backend y recibe un json
    getCentrosByParams(datos).then(async (response) => {
      const data = await response.json();
      if (!response.ok) {
        const error = response.statusText;
        return Promise.reject(error);
      }
      //Define los dentros con los datos recibidos
      setCentros(data);
    })
  };
  //Añade una imagen para que sea el icono que aparece en el mapa
  const IconoMapa = L.icon({
    iconUrl: require("../../recursos/icon.png"),
    iconSize: 100
  });

  //Define la posicion inicial del mapa
  const position = [51.505, -0.09]

  return (
    //Div contenedor del formulario completo y del mapa
    <div className="landing">
      <div className="titulo">
        <h1>Buscador de centros de salud</h1>
      </div>
      {/* Contenedor del formulario y botones para el envio */}
      <div className="contenedor-principal">
        {/* Contenedor del formulario */}
        <div className="contenedor-formulario">
          {/* El formulario ejecuta el metodo handleSubmit cuando el usuario lo envia */}
          {/* Contiene los distintos inputs con sus respectivas labels para una mejor experiencia de usuario */}
          <form ref={refForm} onSubmit={handleSubmint}>
            <label>Localidad</label>
            {/* Cuando cambia el contenido del input text, se añade a los datos del estado Datos */}
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
        {/* Div contenedor del maña */}
        <div className="contenedor-mapa">
          {/* Contenedor del mapa, con los datos necesarios para la inicializacion. Tenemos las coordenadas del centro del mapa, el zoom aplicado
          y la opcion del usuario de hacer zoom con la ruleta del ratón */}
          <MapContainer
            center={[39.466, -0.37]}
            zoom={12}
            scrollWheelZoom={false}
          >
            {/* Componente necesario para que funcione el mapa de Leaflet. 
            Contiene datos de copyright y la url fuente del mapa */}
            <TileLayer
              attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            {/* Un bucle para crear un marcador por cada centro, indicando su posicion, el icono personalizado y una key necesaria para react. */}
             {centros.map((centro, index) => (
              <Marker
                key={index}
                position={[centro.fields.latitud, centro.fields.longitud]}
                icon={IconoMapa}
              >
              </Marker>
            ))}
          </MapContainer>

        </div>
      </div>
      <div className="contenedor-datos">
            {centros.map((centro, index) => (
              <div key={index} className="datos">
                <p>{centro.fields.nombre}</p>
                <p>{centro.fields.telefono}</p>
                <p>{centro.fields.direccion}</p>
                <p>{centro.fields.codigo_postal}</p>
              </div>
            ))}
      </div>
    </div>
  );
}

export default FilterForm;
