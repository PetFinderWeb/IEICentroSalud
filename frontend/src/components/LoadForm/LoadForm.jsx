/**
 * Formulario encargado de seleccionar las fuentes de datos y su carga.
 * Muestra los errores encontrados en el proceso y la cantidad de centros cargados.
 */

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
  //Seguimiento de como cambian las variables (hooks)
  //Todos checkeados
  const [Tchecked, setTChecked] = useState(false);
  //Islas baleares check
  const [IBchecked, setIBChecked] = useState(false);
  //Comunidad valenciana check
  const [CVchecked, setCVChecked] = useState(false);
  //Euskera check
  const [Echecked, setEChecked] = useState(false);
  //Errores encontrados en los centros a cargar
  const [centros, setCentros] = useState([]);
  //Total de centros cargados
  const [totalCentros, setTotalCentros] = useState(0);
  //Permite volver a dar a cargar centros o reiniciar BDD cuando no se está llevando a cabo ninguna carga
  const [validate, setValidate] = useState(true);

  //Cambia los estados de los hooks (checkboxes)
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
    //Se está procesando una carga por lo que no se puede pedir otra
    setValidate(false);
    //Dependiendo de qué valores están checked, se pide la carga de ciertas fuentes
    //Si están todos
    if (Tchecked) {
      getAllCentros()
        .then(async (response) => {
          const data = await response.json();
          if (!response.ok) {
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
          }
          //Se cambian los errores encontrados
          setCentros(data.errores);
          //Actualiza el valor del total de centros cargados
          setTotalCentros(data.centrosSanitarios);
          //Al haber acabado la carga, permite hacer otra
          setValidate(true);
        })
        .catch((error) => {
          //Si ha ocurrido algun error se puede volver a pulsar cargar
          setValidate(true);
        });
      //Si están Islas baleares y la Comunidad Valenciana
    } else if (IBchecked && CVchecked) {
      getIBCVCentros()
        .then(async (response) => {
          const data = await response.json();
          if (!response.ok) {
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
          }
          //Se cambian los errores encontrados
          setCentros(data.errores);
          //Actualiza el valor del total de centros cargados
          setTotalCentros(data.centrosSanitarios);
          //Al haber acabado la carga, permite hacer otra
          setValidate(true);
        })
        .catch((error) => {
          //Si ha ocurrido algun error se puede volver a pulsar cargar
          setValidate(true);
        });
      //Si están Islas baleares y Euskera
    } else if (IBchecked && Echecked) {
      getIBECentros()
        .then(async (response) => {
          const data = await response.json();
          if (!response.ok) {
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
          }
          //Se cambian los errores encontrados
          setCentros(data.errores);
          //Actualiza el valor del total de centros cargados
          setTotalCentros(data.centrosSanitarios);
          //Al haber acabado la carga, permite hacer otra
          setValidate(true);
        })
        .catch((error) => {
          //Si ha ocurrido algun error se puede volver a pulsar cargar
          setValidate(true);
        });
      //Si están Euskera y Comunidad valenciana
    } else if (Echecked && CVchecked) {
      getCVECentros()
        .then(async (response) => {
          const data = await response.json();
          if (!response.ok) {
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
          }
          //Se cambian los errores encontrados
          setCentros(data.errores);
          //Actualiza el valor del total de centros cargados
          setTotalCentros(data.centrosSanitarios);
          //Al haber acabado la carga, permite hacer otra
          setValidate(true);
        })
        .catch((error) => {
          //Si ha ocurrido algun error se puede volver a pulsar cargar
          setValidate(true);
        });
      //Si está solo Islas baleares
    } else if (IBchecked) {
      getIBCentros()
        .then(async (response) => {
          const data = await response.json();
          if (!response.ok) {
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
          }
          //Se cambian los errores encontrados
          setCentros(data.errores);
          //Actualiza el valor del total de centros cargados
          setTotalCentros(data.centrosSanitarios);
          //Al haber acabado la carga, permite hacer otra
          setValidate(true);
        })
        .catch((error) => {
          //Si ha ocurrido algun error se puede volver a pulsar cargar
          setValidate(true);
        });
      //Si está solo Euskera
    } else if (Echecked) {
      getECentros()
        .then(async (response) => {
          const data = await response.json();
          if (!response.ok) {
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
          }
          //Se cambian los errores encontrados
          setCentros(data.errores);
          //Actualiza el valor del total de centros cargados
          setTotalCentros(data.centrosSanitarios);
          //Al haber acabado la carga, permite hacer otra
          setValidate(true);
        })
        .catch((error) => {
          //Si ha ocurrido algun error se puede volver a pulsar cargar
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
          //Se cambian los errores encontrados
          setCentros(data.errores);
          //Actualiza el valor del total de centros cargados
          setTotalCentros(data.centrosSanitarios);
          //Al haber acabado la carga, permite hacer otra
          setValidate(true);
        })
        .catch((error) => {
          //Si ha ocurrido algun error se puede volver a pulsar cargar
          setValidate(true);
        });
    }
  };

  //Reinicia la base de datos
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
          {/* Al pulsar el botón de submit (cargar), se lleva a la función handleSubmit */}
          <form ref={refForm} onSubmit={handleSubmint}>
            <label style={{ fontWeight: "bold" }}>Seleccione fuente</label>
            <div className="checkboxes">
              <label>
                <input type="checkbox" id="todas" onChange={handleCheck} />{" "}
                Seleccionar todas
              </label>
              <br />
              {/* Depende de qué elementos esten check, se podrán seleccionar los demás (checked y disabled)
                  Cuando alguno sea pulsado se lleva a la función handleCheck, que actualiza las checkboxes (handleCheck)
                */}
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
              {/* Botón de submit del form, también resetea las checkboxes seleccionadas */}
              <button type="submit">Cargar</button>
              <button
                type="button"
                onClick={() => {
                  refForm.current.reset();
                }}
              >
                Cancelar
              </button>
              {/* Al seleccionar esta opción se borra la BDD */}
              <button type="button" disabled={!validate} onClick={deleteDB}>
                {" "}
                Reiniciar almacén de datos
              </button>
            </div>
          </form>{" "}
          <div>
            {/* Muestra el total de centros cargados */}
            <label style={{ fontWeight: "bold" }}>
              {" "}
              Total de centros cargados: {totalCentros}
            </label>
            <br />
            {/* Muestra la lista de errores*/}
            <label style={{ fontWeight: "bold" }}> Errores:</label>
            <br />
            {centros.map((element) => {
              return (
                <label className="errorText">
                  {" "}
                  {element} <br />{" "}
                </label>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
}

export default LoadForm;
