import React from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faLinkedin, faInstagram } from '@fortawesome/free-brands-svg-icons';

function index() {
  return (
    <div className='relative w-[80%] bg-white/30 border shadow-inner shadow-black/30 h-16 mx-auto mt-2 flex flex-row text-center items-center justify-center rounded'>
      <span className='text-black font-semibold absolute left-4 md:relatie lg:relative xl:relative'>Logo - Tüm Hakları Saklıdır.  </span>
      <div className="flex flex-row gap-4 items-center absolute right-4 text-xl">
        <a className='hover:text-black/70' href="https://www.linkedin.com/in/furkanardicm/"><FontAwesomeIcon icon={faLinkedin} /></a>
        <a className='hover:text-black/70' href="https://www.instagram.com/furkanardicm/"><FontAwesomeIcon icon={faInstagram} /></a>
      </div>
      
    </div>
  )
}

export default index