import { useRef, useState } from "react";
import {
  deleteCentros,
  getAllCentros,
  getIBECentros,
  getIBCVCentros,
  getCVECentros,
  getECentros,
  getIBCentros,
  gettCVCentros,
} from "../../services/fetches";
import "./LoadForm.css";

function LoadForm() {
  const refForm = useRef();
  const [Tchecked, setTChecked] = useState(false);
  const [IBchecked, setIBChecked] = useState(false);
  const [CVchecked, setCVChecked] = useState(false);
  const [Echecked, setEChecked] = useState(false);
  const [centros, setCentros] = useState([]);
  const [validate, setValidate] = useState(true);

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
  };

  const handleSubmint = (e) => {
    e.preventDefault();
    setValidate(false);
    console.log(Tchecked, IBchecked, CVchecked, Echecked);
    if (Tchecked) {
      getAllCentros()
        .then(async (response) => {
          const data = await response.json();
          if (!response.ok) {
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
          }
          setCentros(data.errores);
          setValidate(true);
          console.log(centros);
        })
        .catch((error) => {
          console.error("Hay un error", error);
          setValidate(true);
        });
    } else if (IBchecked && CVchecked) {
      getIBCVCentros()
        .then(async (response) => {
          const data = await response.json();
          if (!response.ok) {
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
          }
          setCentros(data.errores);
          setValidate(true);
        })
        .catch((error) => {
          console.error("Hay un error", error);
          setValidate(true);
        });
    } else if (IBchecked && Echecked) {
      getIBECentros()
        .then(async (response) => {
          const data = await response.json();
          if (!response.ok) {
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
          }
          setCentros(data.errores);
          setValidate(true);
        })
        .catch((error) => {
          console.error("Hay un error", error);
          setValidate(true);
        });
    } else if (Echecked && CVchecked) {
      getCVECentros()
        .then(async (response) => {
          const data = await response.json();
          if (!response.ok) {
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
          }
          setCentros(data.errores);
          setValidate(true);
        })
        .catch((error) => {
          console.error("Hay un error", error);
          setValidate(true);
        });
    } else if (IBchecked) {
      getIBCentros()
        .then(async (response) => {
          const data = await response.json();
          if (!response.ok) {
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
          }
          setCentros(data.errores);
          setValidate(true);
        })
        .catch((error) => {
          console.error("Hay un error", error);
          setValidate(true);
        });
    } else if (Echecked) {
      getECentros()
        .then(async (response) => {
          const data = await response.json();
          if (!response.ok) {
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
          }
          setCentros(data.errores);
          setValidate(true);
        })
        .catch((error) => {
          console.error("Hay un error", error);
          setValidate(true);
        });
    } else if (CVchecked) {
      gettCVCentros()
        .then(async (response) => {
          const data = await response.json();
          if (!response.ok) {
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
          }
          setCentros(data.errores);
          setValidate(true);
        })
        .catch((error) => {
          console.error("Hay un error", error);
          setValidate(true);
        });
    }
  };

  const deleteDB = (e) => {
    deleteCentros();
    setCentros([]);
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
            <div className="checkboxes">
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
              <button type="button" disabled={!validate} onClick={deleteDB}>
                {" "}
                Reiniciar almacén de datos
              </button>
            </div>
          </form>{" "}
          <label>Resultados de la carga</label>
          <div>
            <label> &nbsp;</label>
            {centros.map((element) => {
              return (
                <label className="errorText">
                  {" "}
                  {element} <br />{" "}
                </label>
              );
              console.log(centros);
            })}
          </div>
        </div>
      </div>
    </div>
  );
}

export default LoadForm;
