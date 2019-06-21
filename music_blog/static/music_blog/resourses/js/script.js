function active_login(){
  $("#cs_signin_form input").prop('disabled', false);
  $("#cs_signup_form input").prop('disabled', true);
}
function active_registration(){
  $("#cs_signin_form input").prop('disabled', true);
  $("#cs_signup_form input").prop('disabled', false);
}
$('#log').bind('click', function() {
    $('#sign').removeClass('active');
    $('#log').addClass('active');
    $('.login').show(500);
    $('.signup').hide(500);
    active_login()
});

$('#sign').bind('click', function() {
    $('#log').removeClass('active');
    $('#sign').addClass('active');
//    signupForm();
    $('.signup').show(500);
    $('.login').hide(500);
    active_registration()
});

$('.fade').bind('click', function() {
    $(".blur-screen").fadeOut(800);
});

$('#logi').bind('click', function() {
    $(".blur-screen").fadeIn(800);
    $('#sign').removeClass('active');
    $('#log').addClass('active');
    $('.login').show(500);
    $('.signup').hide(500);
    active_login()
});

$('#signu').bind('click', function() {
    $(".blur-screen").fadeIn(800);
    $('#log').removeClass('active');
    $('#sign').addClass('active');
    $('.signup').show(500);
    $('.login').hide(500);
    active_registration()
});

$('.js--section-songs').waypoint(function(direction) {
    if(direction == "down") {
        $('nav').addClass('sticky animated fadeInDown');
    } else {
        $('nav').removeClass('sticky animated fadeInDown');
    }
}, {
  offset: '25%'
});


$(".js--section-songs").waypoint(function(direction) {
    $('.hex-animate').addClass('animated bounceInUp');
}, {
  offset: '30%'
});


$(".section-album").waypoint(function(direction) {
    $('.album-animate').addClass('animated zoomIn');
}, {
  offset: '40%'
});

$(".section-videos").waypoint(function(direction) {
    $('.vid-animate').addClass('animated pulse');
}, {
  offset: '40%'
});

var i = 0;

$('.js--ico').click(function() {

    var nav = $('.js--main');
if (i == 0) {
        $('nav').addClass('sticky-s animated fadeInDown').slideDown(function() {
        nav.slideToggle();
        });
        $('#violin').css('top', '90px');
        //$('#violin').css('top', '14.1%');

        i = 1;
    } else {
        nav.slideToggle(function() {
            $('nav').removeClass('sticky-s animated fadeInDown');
            $('#violin').css('top', '0px');
        });
        i = 0;
    }
})

function listen() {

    $('.logo').after('<div class="circle" id="c1"></div>');
    $('#c1').animate({
        opacity: '0',
        height: '270px',
        width: '270px',
        margin: '0'
    }, 2500);

    $('.logo').after('<div class="circle" id="c2"></div>');
    $('#c2').delay(400).animate({
        opacity: '0',
        height: '270px',
        width: '270px',
        margin: '0'
    }, 2500);

    $('.logo').after('<div class="circle" id="c3"></div>');
    $('#c3').delay(1800).animate({
        opacity: '0',
        height: '270px',
        width: '270px',
        margin: '0'
    }, 2500);

    $('.logo').after('<div class="circle" id="c4"></div>');
    $('#c4').delay(2100).animate({
        opacity: '0',
        height: '270px',
        width: '270px',
        margin: '0'
    }, 2500);

    $('.logo').after('<div class="circle" id="c5"></div>');
    $('#c5').delay(2400).animate({
        opacity: '0',
        height: '270px',
        width: '270px',
        margin: '0'
    }, 2500);

}

var active = false;

// the listener to the close
$('.wrapper').click(function(){
    $('#song_card').hide();
});




$('.logo').click(function() {



    // var i = setInterval(listen, 4500);

    navigator.mediaDevices.getUserMedia({
            audio: true
        })
        .then(stream => {
            $('.quotes').addClass('animated fadeOutRight');
            $('.con').addClass('ani');
            listen();
            const mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.start();

            const audioChunks = [];
            mediaRecorder.addEventListener("dataavailable", event => {
                audioChunks.push(event.data);
            });
            var obj='';
            mediaRecorder.addEventListener("stop", () => {
                const audioBlob = new Blob(audioChunks);
                const audioUrl = URL.createObjectURL(audioBlob);
                const audio = new Audio(audioUrl);
                var xhr = new XMLHttpRequest();
                xhr.onload = function(e) {
                    if (this.readyState === 4) {
                      // alert("Data: " + e.target.responseText);
                      obj = JSON.parse(this.responseText);
                      document.getElementById("card_song_data").innerHTML = this.responseText;
                        console.log("Server returned: ", e.target.responseText);
                    }
                };
                var fd = new FormData();
                fd.append("song", audioBlob, 'filename.mp3');
                $("#api_field").val(fd);
                var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
                xhr.open("POST", "api", true);
                xhr.setRequestHeader('X-CSRFToken',$crf_token)
                xhr.send(fd);
                xhr.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                  // alert("Data: " + this.responseText);
                  // document.getElementById("card").innerHTML = this.responseText;
                }
              };
               // $.post("api",{'X-CSRFToken':$crf_token,fd},)
               audio.play();

                // player.src = audioUrl;

            });

            setTimeout(() => {

                $('.circle').remove();
                $('.quotes').removeClass('animated fadeOutRight');
                $('.quotes').addClass('animated fadeInRight');

                $('.con').removeClass('ani');
                $('.con').addClass('anir');
                $('.con').removeClass('anir');
                mediaRecorder.stop();


            }, 5900);
        });



    //listen();
    /*
    setTimeout(function () {

        //clearInterval(i);


        $('.circle').remove();
        $('.quotes').removeClass('animated fadeOutRight');
        $('.quotes').addClass('animated fadeInRight');

        $('.con').removeClass('ani');
        $('.con').addClass('anir');
        $('.con').removeClass('anir');


    }, 5900);
    */


});
document.querySelector('.signup').fakeScroll();
