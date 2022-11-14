import React from "react";
import { Link } from "react-router-dom";
import '../css/Header.css'
const Header = () => {
  return (
    <div className="header">
      <div className="header-logo">
        <Link to="/">
          <img src="../collection/logo.png" alt="" />
        </Link>
      </div>
      <div className="header-nav">
        <Link className="header-link" to='/'>Home</Link>
        <Link  className="header-link" to='/about'>About</Link>
        <Link  className="header-link" to='/contact'>Contact</Link>
        <Link  className="header-link" to='/about'>Sign in</Link>
        <Link  className="header-link" to='/contact'>Login</Link>
        
      </div>
    </div>
  );
};

export default Header;
