const mongoose = require('mongoose');

const dbName = 'places_diegod_api';

module.exports = {
  connect: ()=> mongoose.connect('mongodb://localhost/'+dbName),
  dbName,
  connection: ()=>{
    if(mongose.connection)
      return mongoose.connection;
    return this.connect();
  }
}
