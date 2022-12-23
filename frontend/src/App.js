import { Route, Routes } from "react-router-dom";
import Layout from "./components/Layout/Layout";
import LoadForm from "./components/LoadForm/LoadForm";
import FilterForm from "./components/FilterForm/FilterForm";
function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Layout></Layout>}>
          <Route index element={<LoadForm></LoadForm>}></Route>
          <Route path="/LoadForm" element={<LoadForm></LoadForm>}></Route>
          <Route
            path="/FiltersForm"
            element={<FilterForm></FilterForm>}
          ></Route>
        </Route>
      </Routes>
    </>
  );
}

export default App;
