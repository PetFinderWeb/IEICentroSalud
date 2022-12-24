async function deleteCentros() {
  var requestOptions = {
    method: "GET",
    redirect: "follow",
  };

  const respuesta = await fetch(
    "http://localhost:8000/core/borrar_bdd/",
    requestOptions
  );

  return respuesta;
}

async function getAllCentros() {
  var requestOptions = {
    method: "GET",
    redirect: "follow",
  };

  const respuesta = await fetch(
    "http://localhost:8000/core/carga_parametrizada/?c=true&p=true&b=true",
    requestOptions
  );

  return respuesta;
}

async function gettCVCentros() {
  var requestOptions = {
    method: "GET",
    redirect: "follow",
  };

  const respuesta = await fetch(
    "http://localhost:8000/core/carga_parametrizada/?c=true",
    requestOptions
  );

  return respuesta;
}

async function getIBCentros() {
  var requestOptions = {
    method: "GET",
    redirect: "follow",
  };

  const respuesta = await fetch(
    "http://localhost:8000/core/carga_parametrizada/?b=true",
    requestOptions
  );

  return respuesta;
}

async function getECentros() {
  var requestOptions = {
    method: "GET",
    redirect: "follow",
  };

  const respuesta = await fetch(
    "http://localhost:8000/core/carga_parametrizada/?p=true",
    requestOptions
  );

  return respuesta;
}
async function getCVECentros() {
  var requestOptions = {
    method: "GET",
    redirect: "follow",
  };

  const respuesta = await fetch(
    "http://localhost:8000/core/carga_parametrizada/?c=true&p=true",
    requestOptions
  );

  return respuesta;
}

async function getIBCVCentros() {
  var requestOptions = {
    method: "GET",
    redirect: "follow",
  };

  const respuesta = await fetch(
    "http://localhost:8000/core/carga_parametrizada/?c=true&b=true",
    requestOptions
  );

  return respuesta;
}

async function getIBECentros() {
  var requestOptions = {
    method: "GET",
    redirect: "follow",
  };

  const respuesta = await fetch(
    "http://localhost:8000/core/carga_parametrizada/?p=true&b=true",
    requestOptions
  );

  return respuesta;
}

export {
  deleteCentros,
  getAllCentros,
  getIBECentros,
  getIBCVCentros,
  getCVECentros,
  getECentros,
  getIBCentros,
  gettCVCentros,
};
