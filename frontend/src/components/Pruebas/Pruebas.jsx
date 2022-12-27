import "./Pruebas.css"
import { MapContainer } from "react-leaflet"
import { TileLayer } from "react-leaflet"
import { Marker } from "react-leaflet"
import { Popup } from "react-leaflet"
import "leaflet/dist/leaflet.css";
import L from "leaflet"

export default function Pruebas() {
    const position = [51.505, -0.09]
    const IconoMapa = L.icon({
        iconUrl: require("../../recursos/icon.png"),
        iconSize: 100
      });
    return (<div className="contenedor-pruebas">
        <MapContainer center={position} zoom={13} scrollWheelZoom={false}>
            <TileLayer
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            <Marker position={position} icon={IconoMapa}>
                <Popup>
                    A pretty CSS3 popup. <br /> Easily customizable.
                </Popup>
            </Marker>
        </MapContainer>
    </div>)
}