import './App.css';
import React, { Component } from 'react';
import { useState } from 'react';
import axios from "axios";

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/server/index/connect'
})
function App() {
    const [port, setPort] = useState('');
    const [responseMessage, setResponseMessage] = useState('');
    const [isConnected, setIsConnected] = useState(false); // Add isConnected state

    const validatePort = (port) => {
        const portNumber = parseInt(port, 10);
        return !isNaN(portNumber) && portNumber >= 0 && portNumber <= 65535;
    };

    const toggleButton = () => {
        setIsConnected(!isConnected);
    };
    const handleConnect = async () => {
    // let res = await api.delete('');
    // console.log(res)

        if (validatePort(port)) {
            setResponseMessage('Loading');
            // this.setState({ responseMessage: 'Loading...' });
            try {
                let res = await api.post('', {port: port});
                console.log(res);
                if (res.status === 200) {
                    toggleButton()
                }
                setResponseMessage(res.data.message);
            } catch (e) {
                console.log(e);
                setResponseMessage(e.message);
            }
        } else {
            setResponseMessage('Invalid port. Please enter a number between 0 and 65535.')
        }
    };
    const handleDisconnect = async () => {
        try {
            let res = await api.delete('');
            console.log(res);
            toggleButton()
            setResponseMessage(res.data.message);
        } catch (e) {
            console.log(e);
            setResponseMessage(e.message);
        }
    }

  return (
        <div className="App">
          <input
            type="number"
            placeholder="Enter port (0-65535)"
            value={port}
            onChange={(e) => setPort(e.target.value)}
          />
          {isConnected ? (
            <button onClick={handleDisconnect}>Disconnect</button>
          ) : (
            <button onClick={handleConnect}>Connect</button>
          )}
          {responseMessage && <p>{responseMessage}</p>}
        </div>
    )
}

export default App;

// import React, { useState } from 'react';
// import './App.css';
// import axios from "axios";
//
// const api = axios.create({
//   baseURL: '"http://127.0.0.1:8000/api/server/index/connect'
// })
//
// class App() extends component {
//
//
//   const validatePort = (port) => {
//     const portNumber = parseInt(port, 10);
//     return !isNaN(portNumber) && portNumber >= 0 && portNumber <= 65535;
//   };
//
//   return (
//     <div className="App">
//       <input
//         type="number"
//         placeholder="Enter port (0-65535)"
//         value={port}
//         onChange={(e) => setPort(e.target.value)}
//       />
//       <button onClick={handleConnect}>Connect</button>
//       {responseMessage && <p>{responseMessage}</p>}
//     </div>
//   );
// }
//
// export default App;