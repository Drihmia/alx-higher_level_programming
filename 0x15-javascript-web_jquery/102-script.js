document.addEventListener('DOMContentLoaded', function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';

  $('INPUT#btn_translate').on('click return', function () {
    const value = $('INPUT#language_code').val();
    $.get(url + value, function (data, status) {
      if (status === 'success') {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});
