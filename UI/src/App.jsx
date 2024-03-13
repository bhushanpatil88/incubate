import { useEffect, useState } from 'react'
import './App.css'
import Idea from './components/Idea'
import Navbar from './components/Navbar'
import CXO from './components/CXO';
import Results from './components/Results';
import Modal from './components/Modal';

function App() {
  const [idea, setIdea] = useState("");
  const [roles,setRoles] = useState([]);
  const [isSelected,setIsSelected] = useState({
    role:false,
    result:false,
  });
  const [isLoading,setIsLoading] = useState(false);
  const [results,setResults] = useState();



  const handleSubmit = ()=>{
    setIsLoading(true);
    let address = "";
    if(roles.includes('CEO'))address   += '1';
    else address += '0';
    if(roles.includes('CTO'))address += '1';
    else address += '0';
    if(roles.includes('CMO')) address += '1';
    else address += '0';
    console.log(address);
    fetch(`http://127.0.0.1:5000/${idea}/${address}`).then(res =>{
      return res.json();
    }).then(data => 
      {
        console.log(data)

        setResults(data);
        setIsLoading(false);
        setIsSelected(prev => {return  {...prev,result : true } })
      }
    
    )
    
  }

  return (
    <>
    {isLoading && <Modal />}
    <Navbar  />
    {!isSelected.result && 
    <>
      <Idea 
        setIsSelected={setIsSelected} 
        idea={idea} 
        setIdea = {setIdea} 
        roles={roles}
        handleSubmit={handleSubmit}
        />
      {isSelected.role && <CXO roles={roles} setValues={setRoles}/> }
    </>
    }
    {isSelected.result && <Results results ={results} />}
    </>
  )
}

export default App
