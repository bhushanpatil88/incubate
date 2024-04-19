import React, { useState } from 'react';
import ReactDOM from 'react-dom';

// LoadingSpinner component
const LoadingSpinner = ({ text }) => {
  return (
    <div className="loading-spinner">
      <div className="spinner"></div>
      <div className="text">{text}</div>
    </div>
  );
};

// Modal component
const Modal = () => {
    console.log('Modal')
  return ReactDOM.createPortal(
    <div className="modal-overlay">
      <div className="modal">
      <LoadingSpinner text="Loading..." />
      </div>
    </div>,
    document.getElementById('modal')
  );
};

export default Modal;

