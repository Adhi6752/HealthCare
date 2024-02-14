import React ,{useState} from 'react'
import Result from './Result';

const Recorder = () => {
    const [file, setFile] = useState(null);
    const [status,setStatus] = useState(0);

    const handleFileChange = (event) => {
        const selectedFile = event.target.files[0];
        if(selectedFile.type=='audio/wav')
        setFile(selectedFile);
        else{
          setFile(null);
         
        }
      };

     const handleUpload = async () => {
    if (file) {
      const formData = new FormData();
      formData.append('Id',0);
      formData.append('Text','Hello');
      formData.append('File', file);
      setFile(null)
      try {
        const response = await fetch('http://127.0.0.1:8000/students/', {
          method: 'POST',
          body: formData,
        });

        if (response.ok) {
          console.log('File uploaded successfully!');
          // Handle success, if needed
        } else {
          console.error('Failed to upload file');
          // Handle failure, if needed
        }
      } catch (error) {
        console.error('Error uploading file:', error);
        // Handle errors, if needed
      }
      setStatus(1);
    } else {
      console.error('No file selected');
      // Handle no file selected, if needed
      alert("Please upload audio file...")
    }
    
  }; 
  if(status==0){
  return (
    <div>
      <h3>please Upload your Audio file</h3><br/>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
  }
  return(
    <>

    <Result />
    <button onClick={() => {setStatus(0)}}>Back</button>
    </>
  )
};

export default Recorder;
