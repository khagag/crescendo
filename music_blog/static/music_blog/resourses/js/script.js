function showCoords(event) {

    setTimeout(function() {
        var x = event.clientX;
        var y = event.clientY;
        var mar = $('#violin').css('marginLeft');

        var xp = $("#violin").position();
        //console.log(xp.left);
        //console.log(mar);
        var sum = parseFloat(xp.left) +parseFloat(mar);
        console.log(sum);
        var xm = (287.5 + 160 + sum) - x;
        var ym = (380 + xp.top - $(window).scrollTop()) - y;
        var deg = (Math.atan2(ym, xm) * 180 / Math.PI) - 90;
        if (deg < 0) {
            deg += 360;
            document.getElementById("pow").style.transition = '0s';
        } else if (deg > 360) {
            deg -= 360;
            document.getElementById("pow").style.transition = '0s';
        } /*else if (deg == 0 || (deg > 0 && deg < 10)) {
            document.getElementById("pow").style.transition = '0s';
        } else {
            document.getElementById("pow").style.transition = '.4s';
        }*/
        document.getElementById("pow").style.transform = 'rotate(' + deg + 'deg)';
    }, 200)
}

/*
$('#log').bind('click', function() {
    $('#sign').removeClass('active');
    $('#log').addClass('active');
    $('.login').css("display", "block");
    $('.signup').css("display", "none");
});

$('#sign').bind('click', function() {
    $('#log').removeClass('active');
    $('#sign').addClass('active');
    $('.signup').css("display", "block");
    $('.login').css("display", "none");
});
*/

$('#log').bind('click', function() {
    $('#sign').removeClass('active');
    $('#log').addClass('active');
    $('.login').show(500);
    $('.signup').hide(500);
});

$('#sign').bind('click', function() {
    $('#log').removeClass('active');
    $('#sign').addClass('active');
    $('.signup').show(500);
    $('.login').hide(500);
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
});

$('#signu').bind('click', function() {
    $(".blur-screen").fadeIn(800);
    $('#log').removeClass('active');
    $('#sign').addClass('active');
    $('.signup').show(500);
    $('.login').hide(500);
});



/*var waypoints = $('#handler-first').waypoint(function(direction) {
  notify(this.element.id + ' hit 25% from top of window')
}, {
  offset: '25%'
})*/


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

/*
var i = 0;

$('.js--ico').click(function() {

    var nav = $('.js--main');

    if($('nav').hasClass('sticky')) {
            if (i == 1){
                nav.slideToggle(function() {
                $('nav').removeClass('sticky-s animated fadeInDown');
                $('#violin').css('top', '0px');
            });
            i = 0;
        } else
            nav.slideToggle();
    } else if (i == 0) {
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
*/
