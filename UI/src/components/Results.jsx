import profile from '../assets/profile.png'
const Results = ({
    results,
}) =>{
    console.log(results)
    return (
        <div>
            <h1>Search Results</h1>
            <div>
                <img src={profile} alt='Profile' />
            </div>
            <div>

            </div>
        </div>
    );  
}

export default Results;