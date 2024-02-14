import React from "react";
import  ReactDOM  from "react-dom/client";
import Recorder from "./src/components/Recorder";
import AudioRecorder from "./src/components/AudioRecorder";

const App = () => {
    return(
        <>
        <h1>LUNG DISEASE PREDICTION</h1>
        <Recorder />
        </>
    )
}

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(<App />);