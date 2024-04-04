document.addEventListener('DOMContentLoaded', function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  $.get(url, function (data, status) {
    if (status === 'success') {
      $('DIV#hello').text(data.hello);
    }
  });
});
