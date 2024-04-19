const CXO = ({ roles, setValues }) => {
  const handleCheckBox = (e) => {
    setValues((prev) => {
      if (prev.includes(e.target.name)) {
        let newArray = prev.filter((role) => role !== e.target.name);
        return newArray;
      } else {
        return [...prev, e.target.name];
      }
    });
  };
  let styles = {
    backgroundColor: roles.includes("CMO") ? "red" : "black",
  };

  return (
    <div className="px-72 pb-4 flex justify-start" style={{ backgroundColor: "#EBEBEB" }}>
      <div className="inline-block p-3 rounded-md" style={{ backgroundColor: "#FFCACE" }}>
        <p className="text-black font-bold">I want :</p>
        {/* Buttons style to be changed based on functionlity */}
        <button
          className={`m-2 text-white rounded-full ${
            roles.includes("CEO")
              ? "bg-red-700 text-white"
              : "bg-black text-white"
          }`}
          onClick={handleCheckBox}
          name="CEO"
        >
          CEO
        </button>
        <button
          className={`m-2 text-white rounded-full ${
            roles.includes("CTO")
              ? "bg-red-700 text-white"
              : "bg-black text-white"
          }`}
          onClick={handleCheckBox}
          name="CTO"
        >
          CTO
        </button>
        <button
          className={`m-2 text-white rounded-full ${
            roles.includes("CMO")
              ? "bg-red-700 text-white"
              : "bg-black text-white"
          }`}
          onClick={handleCheckBox}
          name="CMO"
        >
          CMO
        </button>
      </div>
    </div>
  );
};

export default CXO;
