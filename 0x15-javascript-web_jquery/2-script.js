$(function () {
  $('div#red_header').html(function (index, oldText) {
    return "<a href='javascript:void(0):' onclick='changeColor();'>Red header</a>";
  });
});

function changeColor () {
  $('header').css('color', '#FF0000');
}
