import React from 'react'
import { useSelector } from 'react-redux';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faListCheck, faUserGear } from '@fortawesome/free-solid-svg-icons';


function index() {
  const fullname = useSelector((state) => state.user.fullname);
  return (
    <div className='w-screen  h-16 my-3 '>
      <div className="relative w-[80%] bg-white/30 border shadow-black/30 shadow-inner h-full mx-auto px-5 items-center flex flex-row justify-between rounded text-nowrap">
        <a href='/' className='text-black font-extrabold text-xl'>L O G O</a>
        {fullname && <a href='/settings' className='font-bold hover:text-black/70 flex flex-row gap-2 items-center justify-between md:relative sm:absolute sm:right-4 absolute right-4 '><span className='max-sm:invisible '>{fullname} </span><FontAwesomeIcon className='text-2xl' icon={faUserGear} /></a> }
        <h1 className='text-black font-bold flex flex-row items-center text-base justify-center px-5 invisible md:visible lg:visible'>Envanter Yönetim Sistemi <FontAwesomeIcon className="ml-2" icon={faListCheck} /></h1>
      </div>
    </div>
  )
}

export default index