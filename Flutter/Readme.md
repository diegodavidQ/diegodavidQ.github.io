# Flutter

## Instalación

* En la web oficial de [Flutter](https://flutter.dev/docs/get-started/install) descargar el SDK de Flutter.

![SDK Flutter](images/SDK_Flutter.PNG)

* Descomprimir el fichero.zip dentro del directorio _C:\src\\_

![src Flutter](images/src_flutter.PNG)

* Crear la variable de entorno para Flutter, como sigue:

![variable Flutter](images/variables_entorno.png)

* Crear un nuevo _Path_ con la dirección de _C:\src\flutter\bin_

![path Flutter](images/flutter_bin.PNG)

* En la cmd ejecutar **flutter doctor** para verificar si se ha instalado correctamente.

![doctor Flutter](images/flutter_doctor.PNG)

# Instalar los _plugins_ de Flutter y Dart en Android Studio

1. Iniciar Android Studio.
2. Abrir _plugin preferences_ (Configure > Plugins).
3. Seleccionar el plugin de **Flutter** y click en **Install**.

![plugins Flutter](images/Plugin_Flutter.PNG)

4. Click en **Restart** cuando finalice.

# Crear un nuevo template

1. En Android Studio seleccionar _Start a new Flutter project_

![new Flutter project](images/proyecto1/new_Flutter_project.png)


2. Seleccionar Flutter application

![new Flutter application](images/proyecto1/Flutter_application.PNG)

3. Definir el nombre del proyecto, la ubicación del SDK de Flutter _C:\src\Flutter_ y la ubicación del proyecto.

![new Project name](images/proyecto1/Project_name.png)

4. Colocar el nombre del paquete y **Finalizar**.

5. Crear la clase principal **main()**. Además, las clases _MyApp_ y _State_

```dart
void main() {

}

class MyApp extends StatefulWidget{
  @override
  _State createState() => _State();
}

class _State extends State<MyApp>{
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
  }
}
```

6. Completar los métodos con _Scaffold_ los _Widget_ por ejemplo:
```dart

import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    home: MyApp(),
  ));
}

class MyApp extends StatefulWidget{
  @override
  _State createState() => _State();
}

class _State extends State<MyApp>{
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Scaffold(
      appBar: AppBar(
        title: Text('My App'),
      ),
      body: Container(
        child: Center(
          child: Text('Hola Mundo'),
        )
      )
    );
  }

}

```

7. Para crear un template con este código primero seleccionar todo el código y copiarlo. Luego ir a **File>Settings>Editor>Live Templates**

![new Flutter_live_templates](images/proyecto1/Flutter_live_templates.PNG)

8. Seleccionar _Flutter_ luego en el botón derecho superior de **+** y escoger _1. Live template_

9. Colocar el nombre del template, una descripción y dentro de _Template text_ pegar el código.

![template_title](images/proyecto1/template_title.PNG)

10. Definir para **dart** como se indica en la imágen. Finalmente, dar click en **Apply**

![template_dart](images/proyecto1/template_dart.PNG)

11. Para hacer uso del template creado, simplemente, se escribe el nombre del template y se selecciona en la opción del autocompletado como se observa a continuación.

![usar_template](images/proyecto1/usar_template.PNG)

## Ejecutar el projecto

1. Iniciar el _Android Virtual Device_ o conectar un dispositivo Android al computador.

2. Ejecutar la App en dispositivo conectado.

<img src="images/proyecto1/emulacion.jpg" height="50%" align="Center">

