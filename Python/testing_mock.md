# Mock

> [`unittest.mock` documentacion](https://docs.python.org/3/library/unittest.mock.html)

`unittest.mock` es una librería para testing en Python, permite reemplazar partes del sistema para pruebas con objetos `mock` y crear assertions sobre cómo deben ser usados.

`unittest.mock` provee una clase `Mock` para eliminar la necesidad de crear un host de cosas para la test suite.

Después de realizar una acción, puede hacer afirmaciones sobre qué métodos/atributos se utilizaron y los argumentos con los que se llamaron. También puede especificar valores de retorno y establecer los atributos necesarios de la forma habitual.

Mock provee decorador `patch()` para manejar módulos de parcheo y atributos de nivel de clase dentro de un alcance de prueba, junto con `sentinel` para crear objetos únicos.

Objetos `Mock` y `MagicMock` crea todos los atributos y métodos en el orden que son ingresados y almacenan detalles cómo ellos tienen que ser usados, configurarlos, especificar los valores de retorno o limitar que atributos están disponibles, y crear las assertiones sobre cómo debe ser usado.


```python
>>> mock = Mock(side_effect=KeyError('foo'))
>>> mock()
Traceback (most recent call last):
...
KeyError: 'foo'
```

```python
>>> values = {'a': 1, 'b': 2, 'c': 3}
>>> def side_effect(arg):
...
return values[arg]
...
>>> mock.side_effect = side_effect
>>> mock('a'), mock('b'), mock('c')
(1, 2, 3)
>>> mock.side_effect = [5, 4, 3, 2, 1]
>>> mock(), mock(), mock()
(5, 4, 3)
```

Decorador/context manager `patch()` hace fácil imitar clases u objetos en un módulo de prueba. El objeto que se especifica será reemplazado por un mock u otro objeto durante la prueba y se restaura cuando termina la prueba.


```python
>>> from unittest.mock import patch
>>> @patch('module.ClassName2')
... @patch('module.ClassName1')
... def test(MockClass1, MockClass2):
...     module.ClassName1()
...     module.ClassName2()
...     assert MockClass1 is module.ClassName1
...     assert MockClass2 is module.ClassName2
...     assert MockClass1.called
...     assert MockClass2.called
...
>>> test()
```


# Mock API

```python
# mocking a external api in python 
import requests 
import json 
import unittest 
from unittest.mock import patch, Mock 
  
# get_data() is a function that makes a request to an  
# external api and returns the data in json format 
  
  
def get_data(): 
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1') 
    data = json.loads(response.text) 
    return data 
  
  
# TestGetData is a class that contains a test_get_data()  
# method that tests the get_data() function using the mock library 
  
  
class TestGetData(unittest.TestCase): 
    @patch('main.get_data') 
    def test_get_data(self, mock_get_data): 
        """ 
        Test that get_data() returns the correct data demonstrating the  
        use of the mock library 
        """
  
        mock_data = {'userId': 1, 'id': 1, 
                     'title': 'delectus aut autem', 'completed': False} 
  
        mock_get_data.return_value = Mock() 
  
        mock_get_data.return_value.json.return_value = mock_data 
        mock_get_data.return_value.status_code = 200
  
        result = get_data() 
  
        self.assertEqual(result, mock_data) 
  
  
if __name__ == '__main__': 
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
```

