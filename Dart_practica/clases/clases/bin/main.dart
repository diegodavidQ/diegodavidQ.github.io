
//##################################//
//clases
class Persona{
  String nombre;
  int edad;

//set and get
String get getNombre{
  return this.nombre;
}
//String get getNombre => nombre;

 void set setNombre(String valor){
  this.nombre = valor;
}
//void set setNombre(String valor) => nombre = valor;


  //constructor
  Persona(this.nombre, this.edad);

  //name constructor
  Persona.nombre2(this.nombre){
    this.nombre = "David";
    this.edad = 25;
  }

//método
  void saludar(){
    print("Hola soy: $nombre");
  }




} //fin de clase



void main(List<String> arguments) {
  
//clase
var diego = new Persona("Diego", 28);
diego.saludar(); //usar método

var x = new Persona.nombre2("anything");
x.saludar();

diego.setNombre = "nuevo nombre"; //set
print(diego.getNombre); //get

}
