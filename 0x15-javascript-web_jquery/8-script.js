const URL = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.getJSON(URL, (resp) => {
  $.map(resp.results, (item) => {
    $('#list_movies').append('li', item.title);
  });
});
