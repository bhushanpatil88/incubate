import React from "react";

const IdeaSelector = ({ idea, setIdea }) => {
  const ideas = [];
  const handleChange = (event) => {
    setIdea(event.target.value);
  };
  return (
    <>
      <div className="w-full rounded-md">
        <input
          id="idea-selector"
          name="idea"
          value={idea}
          onChange={handleChange}
          className="mt-1 block w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 bg-white text-black"
        />
      </div>
    </>
  );
};

const Idea = ({ idea, setIdea, setIsSelected, handleSubmit, roles }) => {
  return (
    <>
      <div
        style={{ backgroundColor: "#EBEBEB" }}
        className="container mx-auto p-8"
      >
        <div className="my-8 px-10 text-center">
          <h2
            style={{ color: "#FF8991" }}
            className="text-4xl font-bold mb-4 text-left"
          >
            <span style={{ color: "#FF8991" }}>Welcome,</span>
          </h2>
          <p className="text-black font-medium text-start">Enter Your Idea..</p>
          <IdeaSelector idea={idea} setIdea={setIdea} />
          <div className="flex justify-around mt-6 space-x-4">
            <div>
              <button
                style={{ backgroundColor: "#FF8991", color: "#FFFFFF" }}
                value="role"
                className="rounded-md py-2 px-4"
                onClick={() =>
                  setIsSelected((prev) => {
                    return { ...prev, role: true };
                  })
                }
              >
                Select Role
              </button>
            </div>
            <div>
              <button
                disabled={roles.length === 0}
                onClick={handleSubmit}
                value="incubate"
                style={{ backgroundColor: "#FF8991", color: "#FFFFFF" }}
                className="rounded-md py-2 px-4"
              >
                Incubate
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Idea;
