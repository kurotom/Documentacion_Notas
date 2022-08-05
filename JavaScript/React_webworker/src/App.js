import React from 'react';
import './App.css';
import script_worker from './worker.js'
import { marked } from 'marked';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {

    }

  }
  render() {

    const myworker = new Worker(script_worker);

    myworker.onmessage = (evento) => {
      console.log('ms from worker: ', evento.data, marked.parse(evento.data));
    }

    const d = '**mensaje**'
    myworker.postMessage(d);

    return (
      <div>

        app
      </div>
    )
  }
}


export default App;
