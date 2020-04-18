# Servidor Node.js

* Conexión con el proyecto [SimplePageReact](https://github.com/diegodavidQ/diegodavidq.github.io/tree/master/SimplePageReact)
* Conexión con Cloudinary para subir imágenes
* Uso de mongodb como base de datos.

## Ejecución

Dentro de la carpeta del proyecto nodeServerPageReact. Este proyecto se ejecuta en el puerto 8080. 

1. `npm install`
2. cambiar el número del puerto en el archivo **www** dentro de la carpeta _bin_:
```
var port = normalizePort(process.env.PORT || '8080');
```
3. Instalar mongoose `npm install mongoose`
4. `mpm start`

Se debe instalar mongodb. Luego de instalar mongodb, en una terminal o cmd ejecutar mongodb:

```
mongod
```

**Nota**
* Se debe instalar nodemon `npm install -g nodemon`
* Crear una cuenta en Cloudinary y con estos datos cambiar las variables _api_key_, _cloud_name_, _api_secret_ del archivo **secrets.js** dentro de la carperta _config_