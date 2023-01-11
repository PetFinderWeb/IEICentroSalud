/**
 * Fetches a la API del backend, según la petición a realizar
 */

// Borra la base de datos
async function deleteCentros() {
  var requestOptions = {
    method: "GET",
    redirect: "follow",
  };
  const respuesta = await fetch(
    "http://172.23.182.233:8000/core/borrar_bdd/",
    requestOptions
  );
  return respuesta;
}

//Devuelve todos los centros
async function getAllCentros() {
  var requestOptions = {
    method: "GET",
    redirect: "follow",
  };
  const respuesta = await fetch(
    "http://172.23.182.233:8000/core/carga_parametrizada/?c=true&p=true&b=true",
    requestOptions
  );

  return respuesta;
}

//Devuelve los centros de la Comunidad valenciana
async function gettCVCentros() {
  var requestOptions = {
    method: "GET",
    redirect: "follow",
  };

  const respuesta = await fetch(
    "http://172.23.182.233:8000/core/carga_parametrizada/?c=true",
    requestOptions
  );

  return respuesta;
}

//Devuelve los centros de las Islas baleares
async function getIBCentros() {
  var requestOptions = {
    method: "GET",
    redirect: "follow",
  };
  const respuesta = await fetch(
    "http://172.23.182.233:8000/core/carga_parametrizada/?b=true",
    requestOptions
  );
  return respuesta;
}

//Devuelve los centros de Euskera
async function getECentros() {
  var requestOptions = {
    method: "GET",
    redirect: "follow",
  };
  const respuesta = await fetch(
    "http://172.23.182.233:8000/core/carga_parametrizada/?p=true",
    requestOptions
  );
  return respuesta;
}

//Devuelve los centros de la Comunidad Valenciana y Euskera
async function getCVECentros() {
  var requestOptions = {
    method: "GET",
    redirect: "follow",
  };

  const respuesta = await fetch(
    "http://172.23.182.233:8000/core/carga_parametrizada/?c=true&p=true",
    requestOptions
  );
  return respuesta;
}

//Devuelve los centros de Islas baleares y la Comunidad Valenciana
async function getIBCVCentros() {
  var requestOptions = {
    method: "GET",
    redirect: "follow",
  };
  const respuesta = await fetch(
    "http://172.23.182.233:8000/core/carga_parametrizada/?c=true&b=true",
    requestOptions
  );
  return respuesta;
}

//Devuelve los centros de Islas baleares y Euskera
async function getIBECentros() {
  var requestOptions = {
    method: "GET",
    redirect: "follow",
  };

  const respuesta = await fetch(
    "http://172.23.182.233:8000/core/carga_parametrizada/?p=true&b=true",
    requestOptions
  );

  return respuesta;
}

//Devuelve la lista de centros según la localidad, codigo postal, procincia y/o tipo
async function getCentrosByParams(datos) {
  var requestOptions = {
    method: "GET",
    redirect: "follow",
  };

  return await fetch(
    "http://172.23.182.233:8000/core/busqueda?localidad=" +
      datos.localidad +
      "&cod_postal=" +
      datos.cod_postal +
      "&provincia=" +
      datos.provincia +
      "&tipo=" +
      datos.tipo,
    requestOptions
  );
}

//Exporta los metodos para que puedan ser usados desde otros scripts
export {
  getCentrosByParams,
  deleteCentros,
  getAllCentros,
  getIBECentros,
  getIBCVCentros,
  getCVECentros,
  getECentros,
  getIBCentros,
  gettCVCentros,
};
