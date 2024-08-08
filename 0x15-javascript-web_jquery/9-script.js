const URL = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

(() => {
  $.getJSON(URL, (resp) => {
    $('#hello').text(resp.hello);
  });
})();
