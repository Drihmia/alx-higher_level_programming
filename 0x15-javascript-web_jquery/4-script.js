$('DIV#toggle_header').on('click', function () {
  if (!$('header').hasClass('red') && !$('header').hasClass('green')) {
    $('header').addClass('red');
  } else {
    if ($('header').hasClass('green')) {
      $('header').attr('class', 'red');
    } else {
      $('header').attr('class', 'green');
    }
  }
});
