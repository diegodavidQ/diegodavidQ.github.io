import { func } from "prop-types";

/* acceder a los datos*/ 
function getPlaces(){
  return fetch("http://localhost:8080/places").then(data =>{
    return data.json(); //retornar el json
  }).catch(console.log)
}

function getPlace(slug){// informacion individual
  return fetch("http://localhost:8080/places/"+slug).then(data =>{
    return data.json(); //retornar el json
  }).catch(console.log)
}


export{getPlaces, getPlace};

export default {
  places: [
    {
      imageUrl: '/images/place-3.jpg',
      title: 'Desayunos el rey',
      description: 'Starbucks Corporation is an American coffee company and coffeehouse chain.',
      address:'Av Principal #20'
    },
    {
      imageUrl: '/images/place-1.jpg',
      title: 'Starbucks Norte',
      description: 'Starbucks Corporation is an American coffee company and coffeehouse chain.',
      address:'Av Principal #20'
    },
    {
      imageUrl: '/images/place-2.jpg',
      title: 'Pizza de amor',
      description: 'Starbucks Corporation is an American coffee company and coffeehouse chain.',
      address:'Av Principal #20'
    }
  ]
}
