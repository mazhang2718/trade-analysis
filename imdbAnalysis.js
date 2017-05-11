const imdb = require('imdb-api');

let movie;
 
imdb.getReq({ name: 'The Toxic Avenger' }, (err, things) => {
    movie = things;
});
 
// Promises! 
imdb.get('Jeff Tomsic').then(console.log);
//imdb.getById('tt0090190').then(console.log);
//imdb.getReq({ name: 'The Toxic Avenger' }).then(console.log);

//console.log(movie);