import { marked } from 'marked';

const workerCode = () => {
  onmessage = function(evento) {
    const info = evento.data;
    console.log('----- message from worker', info)
    console.log(typeof(info))
    const h = marked.parse('# 1')
    console.log(h)
    postMessage(info)
  }
};

let code = workerCode.toString();
let a = code.substring(code.indexOf('{') + 1, code.lastIndexOf('}'));

const blob = new Blob([a], {type: "application/javascript"});
const script_worker = URL.createObjectURL(blob);

// module.exports = script_worker;
export default script_worker;
