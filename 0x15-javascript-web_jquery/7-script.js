const URL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.getJSON(URL, (resp) => {
    $('#character').text(resp.name);
})
