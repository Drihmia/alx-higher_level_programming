document.addEventListener('DOMContentLoaded', function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  $.get(url, function (data, status) {
    if (status === 'success') {
      $(data.results).each(function (index, item) {
        $('UL#list_movies').append('<li>' + item.title + '</li>');
      });
    }
  });
});
