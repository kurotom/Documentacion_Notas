# Contenido

# Testing
1. [Testing](#Testing)
    1. [Ejemplo](#Ejemplo)
    2. [Consideraciones](#Consideraciones)
    3. [CLI](#CLI)
    4. [Test Discovery](#Test-Discovery)
    5. [Test Suite](#Test-Suite)
    6. [Skip Tests](#Skip-Tests)
    7. [Iterator subtests](#Iterator-subtests)
2. [TestCase](#TestCase)
    1. [Atributos](#Atributos)
    2. [Métodos](#Métodos)
    3. [Assert Methods](#Assert-Methods)
3. [IsolatedAsyncioTestCase](#IsolatedAsyncioTestCase)




# Testing

> Source code: `Lib/unittest/__init__.py`
> [`unittest` documentación](https://docs.python.org/3/library/unittest.html)


`unittest` es un framework de testeo inspirado en JUnit y es muy parecidos a otros framework de testing en otros lenguajes.

Soporta automatización de pruebas, setup compartido, código de apagado de pruebas, agregación de pruebas en colecciones e independencia de las pruebas del marco de informes.

Soporta conceptos OOP:

* test fixture : representa una preparación de lo que se hará en una o más pruebas y se asocia las operaciones de limpieza, por ejemplo, creaciones temporales de proxys, databases, directorios, iniciar procesos de servidor.
* test case : unidad de prueba individual. `unittest.TestCase` puede ser usado para cear nuevas clases pruebas.
* test suite : colección de pruebas, test suites, o ambos. Es usado para agregar pruebas que deben ser ejecutadas juntas.
* test runner : componente que orquesta la ejecución de pruebas.

## Ejemplo

```python
import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main
    unittest.main()
```

```python
import unittest

class WidgetTestCase(unittest.TestCase):

    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(
                self.widget.size(),
                (50,50),
                'incorrect default size'
        )

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(
            self.widget.size(),
            (100,150),
            'wrong size after resize'
        )
```

```python
import unittest

class WidgetTestCase(unittest.TestCase):

    def setUp(self):
        self.widget = Widget('The widget')
    def tearDown(self):
        self.widget.dispose()
```

## Consideraciones

* Los métodos de las clases deben empezar con `test_`.
* Los métodos de prueba deben usar algún tipo de `assert` de `unittest`.
* Método `setUp()` es para definir las instrucciónes que necesita el elemento a probar, ejemplo, inicializar una clase, establecer ruta de ficheros, etc.
* Método `tearDown()` es para definir las instrucciónes que se realizarán después de ejecutar las pruebas, sirve para realizar, por ejemplo, proceso de limpiado o borrado de elementos temporales.


## CLI

```bash
python -m unittest -h    # help

python -m unittest       # Test Discovery is started

python -m unittest test_module1 test_module2

python -m unittest test_module.TestClass

python -m unittest test_module.TestClass.test_method

python -m unittest tests/test_something.py

python -m unittest -v test_module
```


## Test Discovery

`unittest` soporta un simple descubridor de pruebas, los ficheros test deben ser módulos o paquetes importables desde el directorio principal del proyecto, ejemplo, `myproject.subpackage.test` será importado y su ubicación en el sistema de fichero será usado como directorio de inicio.

```bash
cd project_directory
python -m unittest discover
```

Equivalente a 

```bash
python -m unittest
```

## Test Suite

Crear un *suite* personalizado de pruebas.

```python
import unittest

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
```


## Skip Tests

`unittest` soporta saltado de pruebas o clases de pruebas completas, como *"expected faiure"* que en condiciones normales romplerán el flujo de testeo. Estas no se contarán en el reporte final `TestResult`.

El decorador `skip()` o sus variantes para clases `TestCase`. `skipTest()` dentro de `setUp()` o métodos de prueba o elevar directamente `SkipTest`.

| Decorator | Description |
|-|-|
| `@unittest.skip(reason)` | Unconditionally skip the decorated test. reason should describe why the test is being skipped. |
| `@unittest.skipIf(condition, reason)` | Skip the decorated test if condition is true. |
| `@unittest.skipUnless(condition, reason)` | Skip the decorated test unless condition is true. |
| `@unittest.expectedFailure` | Mark the test as an expected failure or error. If the test fails or errors in the test function itself (rather than in one of the test fixture methods) then it will be considered a success. If the test passes, it will be considered a failure. |
| `exception unittest.SkipTest(reason)` | This exception is raised to skip a test. Usually you can use TestCase.skipTest() or one of the skipping decorators instead of raising this directly. |


```python
class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(
            mylib.__version__ < (1, 3),
            "not supported in this library version"
    )
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("external resource not available")
        # test code that depends on the external resource
        pass
```

```python
@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass
```

```python
class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")
```


## Iterator subtests

Aplicable para probar parámetros, `SubTest()` permite distinguir el conjunto de datos de las pruebas individuales.

```python
class NumbersTest(unittest.TestCase):
    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
```

# TestCase

> `unittest.TestCase`

Representa las pruebas dl universo `unittest`, es usado como clase base.

Implementa interface necesaria para ejecutar las pruebas y métodos que debe ejecutar, reportando los errores generados.

| Métodos | Descripción |
|-|-|
| `setUp()` | prepara los elementos necesario para la clase y pruebas. |
| `tearDown()` | solo es llamado si `setUp()` es exitoso, ejecuta instrucciones de limpieza y cierre de elementos. |
| `setUpClass()` | llamado antes de ejecutar las pruebas en una clase en particular, si usa `@classmethod` es llamado como argumento de la clase. |
| `tearDownClass()` | llamado después de las pruebas en una clase en particular, si usa `@classmethod` es llamado como argumento de la clase. |
| `run(result=None)` | ejecuta la prueba, `TestResult` junta los resultados. Si `result=None` se crea `TestResult` temporalmente y se usa. |
| `skipTest(reason)` | llamado durante `setUp()` para saltar pruebas. |
| `subTest(msg=None, **params)` | retorna manejador de contexto que se ejecuta en un bloque de sub-prueba, `msg` y `params` son opcionales, permiten identificar las fallas. |
| `debug()` | ejecuta pruebas sin recolectar los resultados. Esto permite que las excepciones generadas por la prueba se propaguen a la persona que llama y se puede usar para admitir la ejecución de pruebas bajo un depurador. |

## Atributos

| Atributos | Descripción |
|-|-|
| `fail(msg=None)` | señales si falla una prueba. |
| `failureException` | atributo que da una excepción elevado por el método. |
| `longMessage` | determina que ocurre cuando un mensaje personalizado de falla se pasa como argumento `msg` a un assert que falle. |
| `maxDiff` | controla máximo de largo de diferencia de salida del reporte de métodos assert, default es `80*8`. |

## Métodos

| Métodos | Descripción |
|-|-|
| `countTestCases()` | retorna el número de prueba que representa por su objeto de prueba. |
| `defaultTestResult()` | retorna una instancia de result class. |
| `id()` | retorna string que identifica el testcase. |
| `shortDescription()` | retorna descripción de la prueba. None no retorna. |
| `addCleanup(function, /, *args, **kwargs)` | agrega funciones a `tearDown()`. |
| `enterContext(cm)` | ingresa al `context manager` dado. Agrega métodos `__exit__()` (limpieza) y `__enter__()` (retorna resultado). |
| `doCleanups()` | es llamado incondicionalmente después de `tearDown()` o después de `setUp()` si eleva una excepción. |
| `classmethod addClassCleanup(function, /, *args, **kwargs)` | agrega funciones después de `tearDownClass()` para liberar recursos durante las pruebas de clase. |
| `classmethod enterClassContext(cm)` | ingresa al `context manager` dado. |
| `classmethod doClassCleanups()` | llamado incondicionalmente después `tearDownClass()` o `setUpClass()` si eleva una excepción. |


## Assert Methods

| Método | Comprueba | Version |
|-|-|-|
| `assertEqual(a, b)` | a == b | |
| `assertNotEqual(a, b)` | a != b | |
| `assertTrue(x)` | bool(x) is True | |
| `assertFalse(x)` | bool(x) is False | |
| `assertIs(a, b)` | a is b | 3.1 |
| `assertIsNone(x)` | x is None | 3.1 |
| `assertIsNotNone(x)` | x is not None | 3.1 |
| `assertIn(a, b)` | a in b | 3.1 |
| `assertNotIn(a, b)` | a not in b | 3.1 |
| `assertIsInstance(a, b)` | isinstance(a, b) | 3.2 |
| `assertNotIsInstance(a, b)` | not isinstance(a, b) | 3.2 |
| `assertAlmostEqual(a, b)` | round(a - b, 7) == 0 | |
| `assertNotAlmostEqual(a, b)` | round(a-b, 7) != 0 | |
| `assertGreater(a, b)` | a > b | 3.1 |
| `assertGreaterEqual(a, b)` | a >= b | 3.1 |
| `assertLess(a, b)` | a < b | 3.1 |
| `assertLessEqual(a, b)` | a <= b | 3.1 |
| `assertRegex(s, r)` | r.search(s) | 3.1 |
| `assertNotRegex(s, r)` | not r.search(s) | 3.2 |
| `assertCountEqual(a, b)` | mismos cantidad elementos en a y b | 3.2 |
| `assertMultiLineEqual(a, b)` | compara strings | 3.1 |
| `assassertSequenceEqual(a, b)` | compara secuencias | 3.1 |
| `assassertListEqual(a, b)` | compara listas | 3.1 |
| `assassertTupleEqual(a, b)` | compara tuplas | 3.1 |
| `assassertSetEqual(a, b)` | compara sets o fronzensets | 3.1 |
| `assassertDictEqual(a, b)` | compara diccionarios | 3. 1 |
| `assertRaises(exc, fun, *args, **kwds)` | usando `with` comprueba si eleva `exc` | |
| `assertRaisesRegex(exc, r, fun, *args, **kwds)` | usando `with` eleva `exc` y el mensaje coincide con `r` regex. | 3.1 |
| `assertWarns(warn, fun, *args, **kwds)` | usando `with` eleva `warn`. | 3.2 |
| `assertWarnsRegex(warn, r, fun, *args, **kwds)` | usando `with` eleva `warn` y eleva regex `r` si coincide. | 3.2 |
| `assertLogs(logger, level)` | usando `with`, registra un *logger* con un nivel mínimo. | 3.4 |
| `assertNoLogs(logger, level)` | usando `with` no registra *logger* con nivel mínimo. | 3.10 |


```python
with self.assertRaises(SomeException):
    do_something()

with self.assertRaises(SomeException) as cm:
    do_something()
the_exception = cm.exception
self.assertEqual(the_exception.error_code, 3)

######
self.assertRaisesRegex(ValueError, "invalid literal for.*XYZ'$",
int, 'XYZ')
# or:
with self.assertRaisesRegex(ValueError, 'literal'):
    int('XYZ')


######
with self.assertWarns(SomeWarning):
    do_something()


with self.assertWarns(SomeWarning) as cm:
    do_something()

self.assertIn('myfile.py', cm.filename)
self.assertEqual(320, cm.lineno)


#####
self.assertWarnsRegex(
    DeprecationWarning,
    r'legacy_function\(\) is deprecated',
    legacy_function, 'XYZ'
)
# or:
with self.assertWarnsRegex(RuntimeWarning, 'unsafe frobnicating'):
    frobnicate('/etc/passwd')


#####
with self.assertLogs('foo', level='INFO') as cm:
    logging.getLogger('foo').info('first message')
    logging.getLogger('foo.bar').error('second message')

self.assertEqual(
    cm.output,
    ['INFO:foo:first message',
    'ERROR:foo.bar:second message']
)


#####

```


# IsolatedAsyncioTestCase

> `unittest.IsolatedAsyncioTestCase(methodName=’runTest’)`

Esta clase proporciona una API similar a `TestCase` y también acepta corrutinas como funciones de prueba.

| Método | Descripción |
|-|-|
| `coroutine asyncSetUp()` | método llamado para preparar las pruebas. |
| `coroutine asyncTearDown()` | método llamado inmediatamente después de los métodos de prueba. Llamado antes de `tearDown()`. |
| `addAsyncCleanup(function, /, *args, **kwargs)` | métodos que acepta una corutina que puede ser usado como una función de limpieza. |
| `coroutine enterAsyncContext(cm)` | ingresar al `asynchronous context manager`. Agrega `__aexit__()` (limpieza) y `__aenter__()` (retorna resultado). |
| `run(result=None)` | construye un nuevo evento para ejecutar las pruebas, `TestResult` es pasado como resultado. |

```python
from unittest import IsolatedAsyncioTestCase

events = []

class Test(IsolatedAsyncioTestCase):

    def setUp(self):
        events.append("setUp")

    async def asyncSetUp(self):
        self._async_connection = await AsyncConnection()
        events.append("asyncSetUp")

    async def test_response(self):
        events.append("test_response")
        response = await self._async_connection.get("https://example.com")
        self.assertEqual(response.status_code, 200)
        self.addAsyncCleanup(self.on_cleanup)

    def tearDown(self):
        events.append("tearDown")

    async def asyncTearDown(self):
        await self._async_connection.close()
        events.append("asyncTearDown")

    async def on_cleanup(self):
        events.append("cleanup")

if __name__ == "__main__":
    unittest.main()
```

Luego de ejecutar las pruebas, `events` contendrá `["setUp", "asyncSetUp", "test_response", "asyncTearDown", "tearDown", "cleanup"]`.




