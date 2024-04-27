import { useEffect, useState } from "react";
import "./App.css";
import Idea from "./components/Idea";
import Navbar from "./components/Navbar";
import CXO from "./components/CXO";
import Results from "./components/Results";
import Modal from "./components/Modal";

function App() {
  const [idea, setIdea] = useState("");
  const [roles, setRoles] = useState([]);
  const [isSelected, setIsSelected] = useState({
    role: false,
    result: false,
  });
  const [isLoading, setIsLoading] = useState(false);
  const [results, setResults] = useState();
  const handleSubmit = () => {
    setIsLoading(true);
    let address = "";
    if (roles.includes("CEO")) address += "1";
    else address += "0";
    if (roles.includes("CTO")) address += "1";
    else address += "0";
    if (roles.includes("CMO")) address += "1";
    else address += "0";
    console.log(address);
    fetch(`http://127.0.0.1:5000/${idea}/${address}`)
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        console.log(data);

        setResults(data);
        setIsLoading(false);
        setIsSelected((prev) => {
          return { ...prev, result: true };
        });
      });
  };
  // let res = { 
  //   "ceo": [ [ "Aravind Patel", 73.94 ], [ "Rajveer Jha", 71.57 ], [ "Nisha Bhatnagar", 69.55 ], [ "Sahil Chauhan", 69.2 ], [ "Tanya Sharma", 68.19 ] ] ,
  //   "Community_1_community": [ [ "Community_1", 60, [ "Aahan Puri", "Avani Shah", "Aviraag Mishra", "Chandrika Sharma", "Dhruv Trikha", "Eshana Kumar", "Gauri Patel", "Harshit Jain", "Ishaan Verma", "Kaavya Bhatnagar", "Mahi Malhotra", "Nihal Chauhan", "Paridhi Sharma", "Rohan Jha", "Sachin Kumar", "Sanskruti Thakkar", "Swara Bahl", "Tanya Bhatia", "Uday Sharma", "Vedant Chaturvedi" ] ] ], 
  //   "Community_2_community": [ [ "Community_2", 60, [ "Viraaj Mehta", "Yashvi Jain", "Zara Siddiqui", "Aditi Singh", "Aarav Bhatia", "Ahaana Kodur", "Anushka Sharma", "Ayushman Chauhan", "Divyansh Jain", "Eesha Mishra", "Gauri Singh", "Harshit Suri", "Iravati Patel", "Kaavya Rastogi", "Khushi Jha" ] ] ], 
  //   "Community_3_community": [ [ "Community_3", 60, [ "Niharika Singh", "Param Bajaj", "Priyanka Sharma", "Riya Mishra", "Saurabh Trivedi", "Shruti Sawant", "Swaroop Chauhan", "Tejas Rane", "Utsav Jha", "Vedanshi Sharma", "Vikram Sharma", "Yashaswini Raje", "Aadya Gupta", "Anushka Mehta", "Ayushi Sharma", "Chhavi Jain", "Drishti Kumar" ] ] ], 
  //   "cto": [ [ "Aravind Patel", 73.94 ], [ "Rajveer Jha", 71.57 ], [ "Nisha Bhatnagar", 69.55 ], [ "Sahil Chauhan", 69.2 ], [ "Tanya Sharma", 68.19 ] ] ,
  // }

  return (
    <>
      {isLoading && <Modal />}
      <Navbar />
      {!isSelected.result && (
        <>
          <Idea
            setIsSelected={setIsSelected}
            idea={idea}
            setIdea={setIdea}
            roles={roles}
            handleSubmit={handleSubmit}
          />
          {isSelected.role && <CXO roles={roles} setValues={setRoles} />}
        </>
      )}
      {isSelected.result && <Results results ={results} />}
    </>
  );
}

export default App;
