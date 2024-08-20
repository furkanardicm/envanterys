import React, { useEffect } from 'react';

const NotificationBar = ({ message, duration, isVisible, onClose }) => {
  useEffect(() => {
    if (isVisible) {
      const timer = setTimeout(() => {
        onClose();
      }, duration);

      return () => clearTimeout(timer);
    }
  }, [isVisible, duration, onClose]);

  return (
    <div
      className={`inset-x-0 bg-green-600 text-white p-4 flex items-center justify-between shadow-lg w-autotransition-transform transform ${isVisible ? 'translate-y-0' : '-translate-y-full'}`}
      style={{ transition: 'transform 0.5s ease-in-out' }}
    >
      <span className='text-nowrap'>{message}</span>
      <button onClick={onClose} className="ml-4">
        <svg className="h-5 w-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12"></path>
        </svg>
      </button>
    </div>
  );
};

export default NotificationBar;
