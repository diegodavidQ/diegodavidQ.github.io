abstract class Figura{
  //abstract => métodos sin comportamiento
  void calcularArea();
  void calcularPerimetro();

}

abstract class MiInterface{
  void operacion(){
    print("operacion");
  }
}

//extends => class abstract
//implements => interface
class Triangulo extends Figura{
  @override
  void calcularArea() {
    // TODO: implement calcularArea
  }

  @override
  void calcularPerimetro() {
    // TODO: implement calcularPerimetro
  }

}






void main(List<String> arguments) {

  
}