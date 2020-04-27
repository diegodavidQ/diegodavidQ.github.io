
//##################################//
//clases
class Persona{
  String nombre;
  int edad;

  Persona(this.nombre, this.edad);
} //fin de clase

class Hombre extends Persona{
  String genero = "masculino"; 

  Hombre(String nombre, int edad): super(nombre, edad); //definir el constructor, super hace referencia a la clases padre
}

class Mujer extends Persona{
  String genero = "femenino"; 

  Mujer(String nombre, int edad): super(nombre, edad);
}


void main(List<String> arguments) {
  
  var diego = new Hombre("Diego", 28);
  print(diego.nombre);

}