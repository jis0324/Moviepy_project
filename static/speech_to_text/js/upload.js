$(document).ready(function () {

  function whichAnimationEvent(){
    let t;
    let el = document.createElement("fakeelement");

    var animations = {
      "animation"      : "animationend",
      "OAnimation"     : "oAnimationEnd",
      "MozAnimation"   : "animationend",
      "WebkitAnimation": "webkitAnimationEnd"
    }

    for (t in animations){
      if (el.style[t] !== undefined){
        return animations[t];
      }
    }
  }

  let animationEvent = whichAnimationEvent();

  // $(".button").click(function(){
  //   $(this).addClass("animate");
  //   $(this).one(animationEvent,
  //               function(event) {
  //     // Do something when the animation ends
  //   });
  // });

  $('#upload_form input').change(function () {
    if ( this.files.length > 0 ) {
      event.preventDefault(); //prevent default action 
      
      $('#upload_form > input').addClass('hide');
      $('#upload_form > p').addClass('hide');
      $('#upload_form .loading-div').removeClass('hide');
      $('#upload_form .loading-div .mainBar').addClass('mainBar-animate');

      // form submit
      var post_url = $('#upload_form').attr("action"); //get form action url
      var request_method = $('#upload_form').attr("method"); //get form GET/POST method
      var form_data = $('#upload_form').serialize(); //Encode form elements for submission
      console.log($('#upload_form input[type="file"]').val());
      
      $.ajax({
        url : post_url,
        type: request_method,
        data : form_data,
      }).done(function(response){ //
        alert('end forom submit!')
      });

      $('#upload_form .loading-div .mainBar-animate').one(animationEvent,
              function(event) {
                // Do something when the transition ends
                // alert('animation end!');
                $('#upload_form .loading-div .mainBar-animate').css('max-width', '100%');
              });
    }
  });

  $('.navbar-toggler').click(function () {
    $('body').toggleClass('noscroll');
  });

});
