import React from 'react';
const Navbar = () => {
  return (
    <div className="bg-black">
  <div className="container mx-auto">
    <div className="flex items-center justify-between p-4">
      <h6 className="text-white text-2xl font-semibold">BRAIN CHAIN</h6>
      <div className="flex space-x-4">
        <button className="text-white">About us</button>
        <button className="text-white">Contact</button>
        <button className="text-white">More</button>
      </div>
    </div>
  </div>
</div>
  );
};

export default Navbar;