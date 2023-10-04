import Logo from "./Logo";
import { NavLink, Link } from "react-router-dom";
import { HiShoppingCart } from "react-icons/hi";
import { useState } from "react";

function Navbar() {
  const [user, setUser] = useState(false);

  return (
    <div className="header">
      <Logo />
      <ul className="navbar">
        <li>
          <NavLink to="/">Home</NavLink>
        </li>
        <li>
          <NavLink to="/hair_studio">Hair Studio</NavLink>
        </li>
        <li>
          <NavLink to="/nail_bar">Nail Bar</NavLink>
        </li>
        <li>
          <NavLink to="/make_up">Make Up</NavLink>
        </li>
        <li>
          <NavLink to="/reviews">Reviews</NavLink>
        </li>
        <li>
          <NavLink to="/contact">Contact</NavLink>
        </li>
        <li>
          <NavLink to="/products">Products</NavLink>
        </li>
        <li className="nav_btn login_btn">
          <Link to="/login">Login</Link>
        </li>
        <li className="nav_btn signup_btn">
          <Link to="/signup">Sign Up</Link>
        </li>
      </ul>
    </div>
  );
}

export default Navbar;
