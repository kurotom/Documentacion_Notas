# SSL - TLS

Transport Layer Secure (TLS) y el antecesor Secure Socket Layer (SSL)  son protocolos criptográficos que proporcionan comunicaciones seguras por la red.

Se usan certificados X.509, criptografía asimétrica y para autenticar usa una llave simétrica.

Ultima version TLS es 1.3 - agosto 2018.
Utilizar TLS por sobre SSL.

Pasos

El cliente y servidor negocian que algoritmo utilizar:

Para criptogradía llave pública.
* RSA
* Diffie-Hellman
* DSA (Digital Signature Algorithm)
* Fortezza

Para cifrado simétrico.
* RC2
* RC4
* IDEA (International Data Encryption Algorithm)
* DES (Data Encryption Standar)
* Triple DES
* AES (Advanced Encryption Standar)

Con funciones hash.
* MD5 - insegura, solo para test o cosas menores.
* SHA - 256, 512


## Versiones del protocolo

| Protocolo | Publicación |
|-|-|
| SSL 1.0 | No publicado |
| SSL 2.0 | 1995 |
| SSL 3.0 | 1996 |
| TLS 1.0 | 1999 |
| TLS 1.1 | 2006 |
| TLS 1.2 | 2008 |
| TLS 1.3 | 2018 |



# Heroku SSL

Soporta protocolos:
* TLS 1.2
* TLS 1.3

## Tipo de ficheros SSL soportados

* `.csr`: fichero [Certificate Signing Request](https://en.wikipedia.org/wiki/Certificate_signing_request), es un certificado para firmar peticiones, es un mensaje enviado desde una aplicacińo a una authoridad certificada de infraestructura de llave pública para aplicar por un certificado de indentidad digital.

* `.key`: fichero que contiene la llave privada.

* `.pem` y `.crt`: extenciones basadas en codificación base64 ASCII. Ficheros `.pem` contiene el certificado y la llave, por otra parte, `.crt` contiene solamente el certificado.



## Certificados con LetsEncrypt

Instalar `certbot`

```
$ sudo dnf install certbot
```


