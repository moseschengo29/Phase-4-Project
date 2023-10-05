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
import Appointment from "./pages/Appointment";
import Footer from "./ui/Footer";
import { useState, useEffect } from "react";

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch("/check_session").then((response) => {
      if (response.ok) {
        response.json().then((user) => setUser(user));
        console.log(user);
      }
    });
  }, []);

  function handleLogin(user) {
    setUser(user);
  }

  function handleSignup(user) {
    setUser(user);
  }

  function handleLogout() {
    setUser(null);
  }

  return (
    <>
      <Navbar user={user} onLogout={handleLogout} />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login onLogin={handleLogin} />} />
        <Route path="/signup" element={<Signup onSignup={handleSignup} />} />
        <Route path="/reviews" element={<Reviews />} />
        <Route path="/products" element={<Products />} />
        <Route path="/hair_studio" element={<HairStudio />} />
        <Route path="/make_up" element={<Makeup />} />
        <Route path="/nail_bar" element={<NailBar />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/book_appointment" element={<Appointment />} />
      </Routes>
      <Footer />
    </>
  );
}

export default App;
