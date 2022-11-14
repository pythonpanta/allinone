import React from 'react'
import { Link } from 'react-router-dom'
import '../css/footer.css'
const Footer = () => {
  return (
    <div className='footer'>
        <div className=" footerc">
          <p>Know More us</p>
         <Link  className='link' to='/about'>About</Link>
         <Link  className='link'  to='/'>FAQ</Link>
         <Link   className='link' to='/contact'>Blog</Link>
         <Link   className='link' to=''>Services</Link>
         <Link  className='link' to='/'>Hisroty</Link>

        </div>
        <div className=" footerc">
          <p>New Features</p>
        <Link   className='link'to='/'>Latest Course</Link>
        <Link  className='link' to='/'>New Course</Link>
        <Link   className='link'to='/'>Programming Course</Link>
        <Link   className='link'to='/'>Networking Course</Link>
        <Link  className='link' to='/'>Communacation Course</Link>
        </div>
        <div className="footer-right ">
        <p>News Letter</p>
          <input type="text" placeholder='Send us your Email' />
          <button>Send</button>
        </div>
    </div>
  )
}

export default Footer