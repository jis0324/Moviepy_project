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

function openLoginModal(){
  $('#loginModal').modal('show');    
}

function loginAjax(){
  /*   Remove this comments when moving to server
  $.post( "/login", function( data ) {
          if(data == 1){
              window.location.replace("/home");            
          } else {
               shakeModal(); 
          }
      });
  */

/*   Simulate error message from the server   */
   shakeModal();
}

function shakeModal(){
  $('#loginModal .modal-dialog').addClass('shake');
           $('.error').addClass('alert alert-danger').html("Invalid email/password combination");
           $('input[type="password"]').val('');
           setTimeout( function(){ 
              $('#loginModal .modal-dialog').removeClass('shake'); 
  }, 1000 ); 
}