import React, { useState, useEffect, useRef } from 'react';

const AudioRecorder = () => {
  const [mediaRecorder, setMediaRecorder] = useState(null);
  const [audioChunks, setAudioChunks] = useState([]);
  const [isRecording, setIsRecording] = useState(false);
  const [recordingTime, setRecordingTime] = useState(0);
  const [startTime, setStartTime] = useState(0);
  const [isPaused, setIsPaused] = useState(false);
  const mediaStreamRef = useRef(null);

  useEffect(() => {
    let timer;
    if (isRecording && !isPaused) {
      timer = setInterval(() => {
        setRecordingTime(Math.floor((Date.now() - startTime) / 1000));
      }, 1000);
    } else {
      clearInterval(timer);
    }

    return () => clearInterval(timer);
  }, [isRecording, isPaused, startTime]);

  const startRecording = () => {
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then((stream) => {
        mediaStreamRef.current = stream;
        const recorder = new MediaRecorder(stream);
        recorder.ondataavailable = (e) => {
          setAudioChunks([...audioChunks, e.data]);
        };
        recorder.start();
        setIsRecording(true);
        setStartTime(Date.now());
        setMediaRecorder(recorder);
      })
      .catch((err) => {
        console.error('Error accessing microphone:', err);
      });
  };

  const pauseRecording = () => {
    if (mediaRecorder && isRecording) {
      mediaRecorder.pause();
      setIsPaused(true);
    }
  };

  const resumeRecording = () => {
    if (mediaRecorder && isRecording && isPaused) {
      mediaRecorder.resume();
      setIsPaused(false);
      setStartTime(Date.now() - recordingTime * 1000);
    }
  };

  const stopRecording = () => {
    if (mediaRecorder && isRecording) {
      mediaRecorder.stop();
      setIsRecording(false);
      mediaStreamRef.current.getTracks().forEach((track) => track.stop());
    }
  };

  const rewindRecording = () => {
    setRecordingTime(0);
    setIsPaused(false);
    setAudioChunks([]);
  };

  const handleUpload = async () => {
    // ... (Same as previous code)

    // Rest of the code remains the same
  };

  const formatTime = (seconds) => {
    const mins = Math.floor(seconds / 60).toString().padStart(2, '0');
    const secs = (seconds % 60).toString().padStart(2, '0');
    return `${mins}:${secs}`;
  };

  return (
    <div>
      <p>Recording Time: {formatTime(recordingTime)}</p>
      {isRecording ? (
        <div>
          {isPaused ? (
            <button onClick={resumeRecording}>Resume</button>
          ) : (
            <button onClick={pauseRecording}>Pause</button>
          )}
          <button onClick={stopRecording}>Stop</button>
        </div>
      ) : (
        <button onClick={startRecording}>Start Recording</button>
      )}
      <button onClick={rewindRecording}>Rewind</button>
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
};

export default AudioRecorder;
