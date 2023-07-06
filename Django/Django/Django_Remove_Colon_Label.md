# Eliminar dos puntos en labels Django

> [Label suffix - doc](https://docs.djangoproject.com/es/4.0/ref/forms/api/#django.forms.Form.label_suffix)

En Django los labels de los formularios agregan por defecto dos puntos, para poder eliminarlos simplemente se debe utilizar `label_suffix`, por ejemplo:

```python
nombre = forms.CharField(
                                    label="Nombre",
                                    label_suffix="",
                                    widget=forms.TextInput(
                                                    attrs={'placeholder': '64 characters maximum'}
                                                )
                                )
```

Por otro lado, si se quiere usar otro carácter se debe señalar dentro de las comillas.

```python
nombre = forms.CharField(
                                    label="Nombre",
                                    label_suffix="-",
                                    widget=forms.TextInput(
                                                    attrs={'placeholder': '64 characters maximum'}
                                    )
                            )
```
