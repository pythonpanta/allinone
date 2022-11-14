import React from 'react'
import { Routes,Route } from 'react-router-dom'
import Header from './component/Header';
import Footer from './component/Footer';
import About from './component/About';
import Home from './component/Home';
import Contact from './component/Contact';

const App = () => {
  return (
    <div className='App'>
      <Header/>
      <Routes>
        <Route exact path='/' element={<Home/>}/>
        <Route exact path='/about' element={<About/>}/>
        <Route exact path='/contact' element={<Contact/>}/>
      
      </Routes>
      <Footer/>
    </div>
  )
}

export default App
