# querySelector vs getElementById

Escribí un código que funcionaba bien en computador pero en no en móviles, tuve que cambiar querySelector por getElementById, eso fue raro.

A veces hay que saber usar uno por sobre el otro.

```
getElementById matches the id attributes to find DOM nodes, while querySelector searches by selectors.
So for an invalid selector e.g <div id="1"></div>, getElementById('1') would work while querySelector('#1') would fail, unless you tell it to match the id attribute (e.g querySelector('[id="1"]')
```

[stackoverflow](https://stackoverflow.com/q/26848289)


## document.querySelector()

Devuelve el primer elemento del documento que coincida con el grupo especificado de selectores.

```javascript
elemento = document.querySelector(selector);
```

### Compatibilidad

| Feature | Chrome |	Firefox (Gecko) | Internet Explorer |	Opera | Safari (WebKit) |
|-|-|-|-|-|-|
| Soporte Basico |  1  | 	3.5 (1.9.1) |	8  |  10 | 3.2 (525.3) |

| Feature  |	Android  |	Firefox Mobile (Gecko) | IE Phone |	Opera Mobile | 	Safari Mobile  |
|-|-|-|-|-|-|
| Soporte Basico | 	2.1  | 	Si  | 	9  |  10.0  |  3.2  |

[MDN - querySelector](https://developer.mozilla.org/es/docs/Web/API/Document/querySelector)

## document.getElementById()

Devuelve una referencia al elemento por su Id.

```javascript
elemento = document.getElementById(id);
```

### Compatibilidad

| Feature | Chrome |	Firefox (Gecko) | Internet Explorer |	Opera | Safari (WebKit) |
|-|-|-|-|-|-|
| Basic support  |	1.0  |	1.0 (1.7 o anterior)  |	5.5  |	7.0 | 	1.0

| Feature  |	Android  |	Firefox Mobile (Gecko) | IE Phone |	Opera Mobile | 	Safari Mobile |
|-|-|-|-|-|-|
| Basic support  |	1.0  |	1.0 (1.0)  |	6.0  |	6.0  |	1.0


[MDN - getElementById](https://developer.mozilla.org/es/docs/Web/API/Document/getElementById#compat-mobile)
