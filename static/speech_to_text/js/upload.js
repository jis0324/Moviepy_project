$(document).ready(function () {
  $('#upload_form input').change(function () {
    if ( this.files.length > 0 ) {
      $('#upload_form p').text(this.files.length + " file(s) selected");
      $('#upload_section').addClass('hide');
    }
  });

  $('.navbar-toggler').click(function () {
    $('body').toggleClass('noscroll');
  });

});