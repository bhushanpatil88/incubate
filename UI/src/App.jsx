import { useState } from 'react'
import './App.css'
import Idea from './components/Idea'
import Navbar from './components/Navbar'
import CXO from './components/CXO';
import Results from './components/Results';

function App() {
  const [idea, setIdea] = useState("");
  const [roles,setRoles] = useState([]);
  const [isSelected,setIsSelected] = useState({
    role:false,
    result:false,
  });

  console.log(isSelected.role);
  console.log(isSelected.result)
  return (
    <>
    <Navbar  />
    {!isSelected.result && 
    <>
      <Idea setIsSelected={setIsSelected} idea={idea} setIdea = {setIdea} />
      {isSelected.role && <CXO roles={roles} setValues={setRoles}/> }
    </>
    }
    {isSelected.result && <Results />}
    </>
  )
}

export default App
