import { Routes, Route } from "react-router-dom";
import Navbar from "./ui/Navbar";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import Reviews from "./pages/Reviews";
import HairStudio from "./pages/HairStudio";
import Makeup from "./pages/Makeup";
import Contact from "./pages/Contact";
import Products from "./pages/Products";
import NailBar from "./pages/NailBar";

function App() {
  return (
    <>
      <Navbar />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/reviews" element={<Reviews />} />
        <Route path="/products" element={<Products />} />
        <Route path="/hair_studio" element={<HairStudio />} />
        <Route path="/make_up" element={<Makeup />} />
        <Route path="/nail_bar" element={<NailBar />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </>
  );
}

export default App;
