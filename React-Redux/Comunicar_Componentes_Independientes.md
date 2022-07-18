# Comunicar Componentes React Independientes

React usa **props** para comunicarse entre componentes relacionados (padres-hijos).
Al no existir relación se debe crear "intermediarios de estados", estos se encargan de gestionar el estado para ser entregados a los componentes que lo consulten, permitiendo crear, modificar, borrar información.

Se puede crear, pero es recomendable utilizar alguna librería especializada en gestión de estados de aplicaciones, como **[Redux](https://es.redux.js.org/)**, o **[PubSub.js](https://www.npmjs.com/package/pubsub-js)**.


# Creando Event Bus

Para lograr la comunicación se debe establecer un sistema global de manejos de eventos para la aplicación (sistema PubSub), un *event bus* implementa el patron PubSub y permite escuchar y enviar eventos a componentes, permitiendo el intercambio de información.

**Event Bus, es un fichero <italic>'.js'</italic> que debe ser importado en los ficheros de los componentes que lo utilizarán**.

Tiene tres métodos **on**, **dispatch**, y **remove**.

```javascript
const eventBus = {
	on(event, callback) {
		//
	},
	dispatch(event, data) {
		//
	},
	remove(event, callback) {
		//
	},
};
```

## on()

Adjunta un event listener a un objeto **document**. Este método tiene dos argumentos: el evento y un callback.
El callback se llama cuando el evento es desencadenado.

```javascript
on(event, callback) {
	document.addEventListener(event, (e) => callback(e.detail));
},
```


## dispatch()

Desencadenará un evento usando API **CustomEvent**, junto con algo de información.

```javascript
dispatch(event, data) {
	document.dispatchEvent(new CustomEvent(event, { detail: data }));
},
```

## remove()

Elimina el evento asignado al objeto **document** para prevenir fuja de memoria en la app.

```javascript
remove(event, callback) {
	document.removeEventListener(event, callback);
},
```



# Usando un Event Bus

Una vez escrito el event bus, se debe utilizar en los componentes involucrados no relacionados.

El componente que desencadenará o creará este evento se debe utilizar en un método de dicho componente, utilizando **dispatch()**.

El componente que recibirá los datos compartidos, se debe declarar en **componentDidMount** utilizando **on()**, y eliminar este event bus en **componentWillUnmount** utilizando **remove()**.



## Al código

* EventBus.js
```javascript
const eventBus = {
  on(event, callback) {
    document.addEventListener(event, (e) => callback(e.detail));
  },
  dispatch(event, data) {
    document.dispatchEvent(new CustomEvent(event, { detail: data }));
  },
  remove(event, callback) {
    document.removeEventListener(event, callback);
  },
};


export default eventBus;
```


* Coupon.js
```javascript
import React, { Component } from "react";


import eventBus from "./EventBus";


class Coupon extends Component {
  constructor(props) {
    super(props);
    this.state = {
      couponCode: "",
    };
  }
  
  applyCoupon = () => {
    console.log("applying");
    eventBus.dispatch("couponApply", { message: "coupone applied" });
  };


  render() {
    return (
      <div>
        <input
          value={this.state.couponCode}
          onChange={(e) => this.setState({ couponCode: e.target.value })}
        />
        <button onClick={this.applyCoupon}>Apply Coupon</button>
      </div>
    );
  }

}


export default Coupon;
```


* Message.js
```
import React, { Component } from "react";

import eventBus from "./EventBus";


class Message extends Component {
  constructor(props) {
    super(props);
    this.state = {
      message: "",
    };
  }

  componentDidMount() {
    eventBus.on("couponApply", (data) =>
      this.setState({ message: data.message })
    );
  }

  componentWillUnmount() {
    eventBus.remove("couponApply");
  }

  render() {
    return <div>{this.state.message}</div>;
  }

}


export default Message;
```



[Fuente](https://www.pluralsight.com/guides/how-to-communicate-between-independent-components-in-reactjs) 
