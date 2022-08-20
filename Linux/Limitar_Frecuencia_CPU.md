# cpupower

cpupower es un conjunto de utilidades de espacio de usuario diseñadas para ayudar con el escalado de frecuencia de la CPU. No es necesario que el paquete utilice escalado, pero se recomienda encarecidamente porque proporciona utilidades útiles de línea de comandos y un servicio systemd para cambiar el gobernador en el arranque.

El archivo de configuración de cpupower se encuentra en `/etc/default/cpupower` (debian) o `/etc/sysconfig/cpupower` (Fedora). Este archivo de configuración es leído por un script bash en `/usr/lib/systemd/scripts/cpupower` que es activado por systemd con `cpupower.service`. Es posible que desee habilitar cpupower.service para que se inicie en el arranque.

```bash
$ sudo systemctl start cpupower.service
$ sudo systemctl enable cpupower.service
```

## Instalar paquete kernel-tools

Fedora 34, ejecutar el comando para instalarlo:

```bash
$ sudo dnf install kernel-tools
```


## Editar el fichero de configuracion

Los gobernadores son esquemas de energía para la CPU. Solo uno puede estar activo a la vez.

| Governor | Descripcion |
|-|-|
| performance | Frecuencia de cpu maximo. |
| powersave | Frecuencia baja de CPU. |
| userspace | Ejecuta la configuracion de usuario. |
| ondemand | Varia la frecuencia acorde el uso del CPU. |
| conservative | Escala la frecuencia dinámica acorde a la carga. Es más gradual que ondemand. |
| schedutil | Selección de frecuencia de CPU impulsada por un programador. |


Se puede activar mediante la línea de comando, pero es temporal, se restablece cada vez que se reinicia.

Para hacerlo permanente, editamos el fichero.

```bash
$ cat /etc/sysconfig/cpupower
    
    # See 'cpupower help' and cpupower(1) for more info
    CPUPOWER_START_OPTS="frequency-set -g performance frequency-set --max 3.0GHz"
    CPUPOWER_STOP_OPTS="frequency-set -g ondemand frequency-set --max 3.0GHz"
```

Donde se limitará hasta 3.0 GHZ todos los núcleos.

Habilitar, iniciar el servicio.

```bash
$ sudo systemctl enable cpupower.service
  
$ sudo systemctl start cpupower.service
  
$ sudo systemctl status cpupower.service
```



## Obtener información

Para obtener información de la frecuencia de CPU.

```bash
$ cpupower --cpu all frequency-info
```

Donde: ---cpu all : declara que se consulten todos los núcleos, usando 0-N para cada núcleo.

Ejemplo:

    [...]
    analyzing CPU 3:
      driver: intel_cpufreq
      CPUs which run at the same hardware frequency: 3
      CPUs which need to have their frequency coordinated by software: 3
      maximum transition latency: 20.0 us
      hardware limits: 800 MHz - 3.40 GHz
      available cpufreq governors: conservative ondemand userspace powersave performance schedutil
      current policy: frequency should be within 800 MHz and 3.00 GHz.
                      The governor "performance" may decide which speed to use
                      within this range.
      current CPU frequency: Unable to call hardware
      current CPU frequency: 2.69 GHz (asserted by call to kernel)
      boost state support:
        Supported: yes
        Active: yes
        25500 MHz max turbo 4 active cores
        25500 MHz max turbo 3 active cores
        25500 MHz max turbo 2 active cores
        25500 MHz max turbo 1 active cores


Visto lo anterior, se limitó a 3.0 GHZ, pero el cpu soporta hasta 3.40 GHZ, con ello se puede solucionar problemas de calor excesivo, por ejemplo. (Si es el problema, sería bueno que revisara la refrigeración).

:books: [Info dónde me apoyé](https://wiki.archlinux.org/title/CPU_frequency_scaling#Scaling_governors)

Consultar el manual de cpupower
