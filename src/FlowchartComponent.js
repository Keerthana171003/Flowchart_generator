

import React, { useEffect } from 'react';
import flowchart from 'flowchart.js';

const FlowchartComponent = ({ code }) => {
  useEffect(() => {
    if (code) {
      const diagram = flowchart.parse(code);
      diagram.drawSVG('diagram', {
        
      });
    }
  }, [code]);

  return <div id="diagram"></div>;
};

export default FlowchartComponent;
