# Renombrar campos

Al usar un modelo, los campos deben tener el mismo nombre en los *serializers*, pero se pueden renombrar, una especie de alias, usando el parámetro `source`


* Modelo

```python
class Airplane(models.Model):
    airplane_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'airplane'
```

* Serializer

```python
class AirplaneSerializer(serializers.ModelSerializer):
    airplaneId = serializers.IntegerField(read_only=True, source='airplane_id')
    name = serializers.CharField()

    class Meta:
        model = Airplane
        fields = [
            'airplaneId',
            'name'
        ]
```


En este caso el campo `airplane_id` del modelo, se renombró en el serializer a `airplaneId`, este último se usará en los datos obtenidos mediante `.data` del serializer.

