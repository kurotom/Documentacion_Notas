# Audio - element

Proporciona acceso a las propiedades de los elementos **[<audio>](https://developer.mozilla.org/es/docs/Web/HTML/Element/audio)**, así como métodos para manipularlos. Se deriva de la interfaz [HTMLAudioElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAudioElement); se implementa por medio de *nsIDOMHTMLMediaElement*.


```
new Audio()
new Audio(url)
```


* url:  un string opcional conteniendo la URL del fichero de audio para ser asociado con el nuevo elemento de audio.

Un nuevo objeto [HTMLAudioElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAudioElement), configurado para ser utilizado para reproducir el audio del archivo especificado por url.


# Métodos

* **.play()**
* **.pause()**

* **.duration**
```
audio.duration
```

* **.currentTime**
```
audio.currentTime
```

* **.src**:  valores string.
```
audio.src = 'url'
audio.src
```

* **.muted**:  valores true/false.
```
audio.muted
audio.muted = true
```

* **.volume**:  valores float entre [0-1]
```
audio.volume
audio.volume = 0.1
```


