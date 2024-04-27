import profile from "../assets/profile.png";

const Results = ({ results }) => {
  return (
    <div className="p-4" style={{ backgroundColor: "#EBEBEB" }}>
  <h1 className="text-3xl font-bold mb-4" style={{ color: "#FF8991" }}>
    Search Results
  </h1>
  <div className="border border-slate-200 rounded p-4 m-2 shadow">
    <div className="border flex flex-col grid grid-cols-1 border-slate-200 shadow rounded p-4 m-2">
      {Object.keys(results).map((key, index) => (
        (!key.includes('community') &&
        <div key={index} className="flex flex-col justify-center mt-2">
          <h2 className="text-lg text-black font-semibold">{key.toUpperCase()}</h2>
          <div
              key={key}
              className="border grid grid-cols-5 border-slate-200 shadow rounded p-4"
            >
            {results[key].map((prf,index) => (
              <div key={index} className="flex flex-col items-center text-center">
                <img
                src={profile}
                className="w-14 h-14 m-2 rounded-full border-2 border-black"
                alt="Profile"
              />
              <p className="mt-2 font-bold text-black">
                <span className="font-bold text-black">Name:</span> {prf[0]}
              </p>
              <p className="mt-2 font-bold text-black">
                <span className="font-bold text-black">Score:</span> {prf[1]}%
              </p>
              </div>
            ))}
            </div>
        </div>
      )))}
    </div>
  </div>
  {Object.keys(results).map((key, i) =>
    key.includes("Community") ? (
      <div key={i} className="border flex flex-col border-slate-200 shadow rounded p-4 m-2">
        <h2 className="text-lg text-black font-semibold">
          {key.replace("_", " ").toUpperCase()}
        </h2>
        {results[key].map((com, index) => (
          <div key={index} className="flex flex-col justify-center mt-2">
            <div className="mt-2 font-bold text-black">
              <span className="font-bold text-black">{com[0]}</span>
              <br></br>
              <span className="font-bold text-black">Score:</span> {com[1]}%
            </div>
            <div
              key={key}
              className="border grid grid-cols-3 border-slate-200 shadow rounded p-4"
            >
              {com[2].map((person, index) => (
                <div key={index} className="flex flex-col items-center text-center">
                  <img
                    src={profile}
                    className="w-10 h-10  rounded-full border-2 border-black"
                    alt="Profile"
                  />
                  <p className="mt-2 font-bold text-black">
                    <span className="font-bold text-black">Name:</span> {person}
                  </p>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    ) : null
  )}
</div>
  );
};

export default Results;
