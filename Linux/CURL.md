# Curl

Herramienta para transferir información desde o hacia un servidor.

Protocolos soportados: DICT, FILE, FTP,  FTPS,  GOPHER,  GOPHERS,
HTTP,  HTTPS,  IMAP, IMAPS, LDAP, LDAPS, MQTT, POP3, POP3S, RTMP,
RTMPS, RTSP, SCP, SFTP, SMB, SMBS, SMTP, SMTPS, TELNET  or  TFTP.



## Ejemplo de uso de curl


Hacia una api Login.
```
$ curl -X POST --header "Content-Type:application/json" --data '{"username":"emailUser","email":"emailUser@user.com","password":"unapass"}' http://127.0.0.1:8000/api/login/
```

```
$ curl -X POST http://127.0.0.1:8000/login/ -F 'username=emailUser' -F 'password=unapass' -F 'email=emailUser@user.com'
```


Hacia una api Logout usando Token.
```
$ curl -X POST http://127.0.0.1:8000/logout/ -H 'Authorization: Token 3c00ff02e27940748b5f7f2efb44832713608c02'
```

