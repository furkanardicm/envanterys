import React from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faLinkedin, faInstagram } from '@fortawesome/free-brands-svg-icons';

function index() {
  return (
    <div className='max-sm:flex-col max-sm:relative relative w-[80%] bg-white/30 border shadow-inner shadow-black/30 h-16 mx-auto mt-2 flex flex-row text-center items-center justify-center rounded'>
      <span className='text-black max-sm:mx-auto font-semibold max-sm:relative  '>Logo - Tüm Hakları Saklıdır.  </span>
      <div className="flex flex-row gap-4 items-center max-sm:relative absolute right-4 text-xl justify-center max-sm:mx-auto">
        <a className='hover:text-black/70' href="https://www.linkedin.com/in/furkanardicm/"><FontAwesomeIcon icon={faLinkedin} /></a>
        <a className='hover:text-black/70' href="https://www.instagram.com/furkanardicm/"><FontAwesomeIcon icon={faInstagram} /></a>
      </div>
    </div>
  )
}

export default index