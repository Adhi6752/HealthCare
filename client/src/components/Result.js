import React from "react";
import { useEffect,useState } from "react";
const Result = () =>{
    const [info,setInfo] = useState([]);
    useEffect(() => {
        fetch('http://127.0.0.1:8000/students/')
          .then((res) => {
            return res.json();
          })
          .then((data) => {
            console.log(data);
            setInfo(data);
          });
      }, []);
      if(info.length==0){
        return(
            <h3>please wait....</h3>
        )
      }
    return(
        <>
            {info.map((inf) => (
                
                <h3 key={inf.id}>The predicted disease is <b style={{color:"red"}}>{inf.result}</b></h3>
            ))}
            
        </>
    );
};

export default Result;