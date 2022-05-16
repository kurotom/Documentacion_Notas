# Eliminar dos puntos en labels Django

En Django los labels de los formularios agregan por defecto dos puntos, para poder eliminarlos simplemente se debe utilizar `label_suffix`, por ejemplo:

```
	nombre = forms.CharField(label="Nombre", label_suffix="", widget=forms.TextInput(attrs={'placeholder': '64 characters maximum'}))
```

Por otro lado, si se quiere usar otro caracter se debe señalar dentro de las comillas.

```
	nombre = forms.CharField(label="Nombre", label_suffix="-", widget=forms.TextInput(attrs={'placeholder': '64 characters maximum'}))
```


[Label - Django Documentación](https://docs.djangoproject.com/es/4.0/ref/forms/api/#django.forms.Form.label_suffix)
