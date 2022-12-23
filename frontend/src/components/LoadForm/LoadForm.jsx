import { useRef } from "react";
import "./LoadForm.css";

function LoadForm() {
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
    <div className="landing2">
      <div className="titulo2">
        <h1>Carga del almacén de datos</h1>
      </div>
      <div className="contenedor-principal2">
        <div className="contenedor-formulario2">
          <form ref={refForm} onSubmit={handleSubmint}>
            <label>Seleccione fuente</label>
            <input
              type="checkbox"
              name="showRatings"
              id="showRatings"
              value="1"
              checked
            />
            <label className="checkboxLabel2" for="showRatings">
              Show Ratings
            </label>
            <div className="contenedor-botones2">
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
          </form>{" "}
          <div>
            <text>Resultados de la carga</text>
          </div>
        </div>
      </div>
    </div>
  );
}

export default LoadForm;
