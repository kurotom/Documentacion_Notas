# Generar SECRET_KEY

Django ofrece una herramienta para generar esta llave.

```python
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```


