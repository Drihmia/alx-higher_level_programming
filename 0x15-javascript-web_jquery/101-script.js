document.addEventListener('DOMContentLoaded', function () {
  $('DIV#add_item').bind('click', function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').bind('click', function () {
    $('UL.my_list li').last().remove();
  });
  $('DIV#clear_list').bind('click', function () {
    $('UL.my_list').empty();
  });
});
