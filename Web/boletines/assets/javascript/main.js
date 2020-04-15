
/*let container = document.querySelector(".container");
//console.log(container);
let celdas = document.querySelectorAll("td");
//console.log(celdas);
celdas.forEach(function(i){
    console.log(i);
});
*/

let links = document.querySelectorAll(".close");

links.forEach(function (link) {
    //agregar un evento click a cada uno de ellos
    link.addEventListener('click', function (ev) {
        ev.preventDefault();

        //Agregar clases para animar su salida fadeOutUp
        let content = document.querySelector(".content");

        //Quitarle las clases de animación que ya tiene
        content.classList.remove("bounceInDown");
        content.classList.remove("animated");

        //Agregar las clases para animar la salida fadeOutUp
        content.classList.add("fadeOutUp");
        content.classList.add("animated");

        setTimeout(function () {
            location.href = "/boletines";
        }, 600);

        return false;
    });
});


