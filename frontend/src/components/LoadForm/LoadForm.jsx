import { useRef, useState } from "react";
import { getAllCentros } from "../../services/fetches";
import "./LoadForm.css";

function LoadForm() {
  const refForm = useRef();
  const [Tchecked, setTChecked] = useState(false);
  const [IBchecked, setIBChecked] = useState(false);
  const [CVchecked, setCVChecked] = useState(false);
  const [Echecked, setEChecked] = useState(false);
  const [centros, setCentros] = useState([]);
  const [arr, setArr] = useState([]);

  const handleCheck = (e) => {
    if (e.target.id === "todas") {
      setTChecked((current) => !current);
    }
    if (e.target.id === "ib") {
      setIBChecked((current) => !current);
    }
    if (e.target.id === "cv") {
      setCVChecked((current) => !current);
    }
    if (e.target.id === "e") {
      setEChecked((current) => !current);
    }
    setArr([Tchecked, IBchecked, CVchecked, Echecked]);
  };

  const handleSubmint = (e) => {
    e.preventDefault();
    console.log(arr);
    getAllCentros()
      .then(async (response) => {
        const data = await response.json();
        if (!response.ok) {
          const error = (data && data.message) || response.statusText;
          return Promise.reject(error);
        }
        console.log(data);
        setCentros(data);
      })
      .catch((error) => {
        console.error("Hay un error", error);
      });
    console.log(centros);
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
            <div class="checkboxes">
              <label>
                <input type="checkbox" id="todas" onChange={handleCheck} />{" "}
                Seleccionar todas
              </label>
              <br />

              <label>
                <input
                  type="checkbox"
                  id="ib"
                  disabled={Tchecked ? true : false}
                  checked={Tchecked ? false : IBchecked}
                  onChange={handleCheck}
                />
                Illes Balears
              </label>
              <br />
              <label>
                <input
                  type="checkbox"
                  id="cv"
                  disabled={Tchecked ? true : false}
                  checked={Tchecked ? false : CVchecked}
                  onChange={handleCheck}
                />
                Comunitat Valenciana
              </label>
              <br />
              <label>
                <input
                  type="checkbox"
                  id="e"
                  disabled={Tchecked ? true : false}
                  checked={Tchecked ? false : Echecked}
                  onChange={handleCheck}
                />
                Euskadi
              </label>
            </div>
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