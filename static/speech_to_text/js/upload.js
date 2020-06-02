$(document).ready(function () {

  // function whichAnimationEvent(){
  //   let t;
  //   let el = document.createElement("fakeelement");

  //   var animations = {
  //     "animation"      : "animationend",
  //     "OAnimation"     : "oAnimationEnd",
  //     "MozAnimation"   : "animationend",
  //     "WebkitAnimation": "webkitAnimationEnd"
  //   }

  //   for (t in animations){
  //     if (el.style[t] !== undefined){
  //       return animations[t];
  //     }
  //   }
  // }

  // let animationEvent = whichAnimationEvent();

  // $(".button").click(function(){
  //   $(this).addClass("animate");
  //   $(this).one(animationEvent,
  //               function(event) {
  //     // Do something when the animation ends
  //   });
  // });

  $('#upload_form input[type="file"]').change(function () {
    if ( this.files.length > 0 ) {
      event.preventDefault(); //prevent default action 
      
      $('#upload_form > p').removeClass('text-danger');
      $('#upload_form > p').text('Selected File.');
      $('.loading-section').removeClass('hide');
      $('#upload_section').css('opacity', .5);

      // form submit
      var post_url = $('#upload_form').attr("action"); //get form action url
      var request_method = $('#upload_form').attr("method"); //get form GET/POST method
      var formData = new FormData();
      formData.append('csrfmiddlewaretoken', $('#upload_form input[name="csrfmiddlewaretoken"]').val());
      formData.append('file', $('#upload_form input[type="file"]')[0].files[0]);
      
      $.ajax({
        url: post_url,
        type: request_method,
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        success: function(response) {
          if (response == 'success') {
            location.href = '/speech-to-text/list/'
            event.preventDefault(); //prevent default action 
          } else if (response == 'wrong_type') {
            $('#upload_form > p').text('Unsupported File. Please Reselect File.');
          } else if (response == 'long_name') {
            $('#upload_form > p').text('The name of File is too long. Please Reselect File.');
          } else if (response == 'error') {
            $('#upload_form > p').text('Raised Some Error. Please Reselect File.');
          }

          $('#upload_form > p').addClass('text-danger');
          $('.loading-section').addClass('hide');
          $('#upload_section').css('opacity', 1);
        
          // $('#upload_form .loading-div .mainBar-animate').one(animationEvent, function(event) {
          //   $('#upload_form .loading-div .mainBar-animate').css('max-width', '100%');
          // });
        },
      });
    }
  });

  $('.navbar-toggler').click(function () {
    $('body').toggleClass('noscroll');
  });

});
