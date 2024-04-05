import React, { useState } from 'react';
import axios from 'axios';


const PythonCodeForm = () => {
    const [pythonCode, setPythonCode] = useState('');

    const generateFlowchart = () => {
        axios.post('http://localhost:5000/generate-flowchart', {
            code: pythonCode
        }, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (response.status === 200) {
                console.log('SVG data:', response.data);
                document.getElementById('flowchart-container').innerHTML = response.data;
            } else {
                console.error('Request was not successful, status:', response.status);
            }
        })
        .catch(error => {
            console.error('There was a problem with the request:', error);
        });
    };

    return (
        <div>
            <textarea
                value={pythonCode}
                onChange={(e) => setPythonCode(e.target.value)}
                placeholder="Enter Python code here"
                className="form-control"
                rows="10"
                cols="50"
            />
            <button onClick={generateFlowchart} className="btn btn-primary mt-3">Generate Flowchart</button>
            <div id="flowchart-container" className="mt-4"></div>
        </div>
    );
};

export default PythonCodeForm;
