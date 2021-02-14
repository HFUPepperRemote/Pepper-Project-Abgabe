const responsive = {
    0: {
        items: 1
    },
    320: {
        items: 1
    },
    560: {
        items: 2
    },
    960: {
        items: 3
    }
}

$(document).ready(function () {

    $nav = $('.nav');
    $toggleCollapse = $('.nav-brand');

    /** click event on toggle menu */
    $toggleCollapse.click(function () {
        $nav.toggleClass('collapse');
    })

    // owl-crousel for blog
    $('.owl-carousel').owlCarousel({
        loop: true,
        autoplay: false,
        autoplayTimeout: 3000,
        dots: false,
        nav: true,
        navText: [$('.owl-navigation .owl-nav-prev'), $('.owl-navigation .owl-nav-next')],
        responsive: responsive
    });


    // click to scroll top
    $('.move-up span').click(function () {
        $('html, body').animate({
            scrollTop: 0
        }, 1000);
    })

    // AOS Instance
    AOS.init();

});

var session;
var session = new QiSession(); //das ist wichtig


// connecting to robot
try {
  QiSession( function (s) {
    console.log('connected!');
    session = s;
    // now that we are connected, we can use the buttons on the page
    $('button').prop('disabled', false);
  });
} catch (err) {
  console.log("Error when initializing QiSession: " + err.message);
  console.log("Make sure you load this page from the robots server.")
}



// event callback
$(function () {
  $('#say').click(sayHelloWorld);
});

document.querySelector('#indexButton').onsubmit = sayHelloWorld;
// example of calling a Naoqi API method
function sayHelloWorld() {
  session.service('ALTextToSpeech').then(function (tts) {
    tts.say('Hallo jetzt wirst du aber ziemlich frech. einfach wärend eines videos zu reden');
  }, function (error) {
    console.log(error);
  })
}

//animated speech
function sayAnimatedText(meinText, dauer) {
  setTimeout(defaultPosture, dauer);
  session.service('ALAnimatedSpeech').then(function (asr_service) {
    configuration = {"bodyLanguageMode":"contextual"}
    asr_service.say(meinText, configuration)
  }, function (error) {
    console.log(error);
  })
}

//preLoadImage
function preLoadImage() {
  session.service('ALTabletService').then(function (tabletService) {
    tabletService.preLoadImage("/apps/vasTest/html/Bilder/credits.png")
    //tabletService.showImage("https://198.18.0.1/apps/vasTest/html/Bilder/credits.png")
  }, function (error) {
    console.log(error);
  })
}
//showImage -> zeigt bild an
function showImage() {
  setTimeout(hideImage, 5000);
  session.service('ALTabletService').then(function (tabletService) {
    //tabletService.preLoadImage("/vasTest/html/Bilder/credits.png")
    tabletService.showImage("http://198.18.0.1/apps/vasTest/Bilder/wallpaper.jpg")
    tabletService.hideImage()
  }, function (error) {
    console.log(error);
  })
}

function hideImage() {
  session.service('ALTabletService').then(function (tabletService) {
    //tabletService.preLoadImage("/vasTest/html/Bilder/credits.png")
    tabletService.hideImage()
  }, function (error) {
    console.log(error);
  })
}


//hideWebview -> beendet die Anzeige der lokalen Webdateien
function hideWebview() {
  session.service('ALTabletService').then(function (tabletService) {
  tabletService.hideWebview()
  //showWebview('http://198.18.0.1/apps/vasTest/hygienekonzept.html')
  
  }, function (error) {
    console.log(error);
  })
}

//hier soll er einfach nur in seine Anfangsposition zurückkehren
function defaultPosture() {
  session.service('ALRobotPosture').then(function (goToPosture) {
    goToPosture.goToPosture("StandInit", 0.5)
  }, function (error) {
    console.log(error);
  })
}

//showWebview -> zeige eine Website aus dem www. an
function showWebview(adresse) {
  session.service('ALTabletService').then(function (tabletService) {
    //tabletService.enableWifi()
    //tabletService.loadUrl(url)
    tabletService.showWebview(adresse)
    setBrightness(0.9)
  }, function (error) {
    console.log(error);
  })
}





function showVideo(url, dauerS, dauerV) {
  setTimeout(defaultPosture, dauerS);
  setTimeout(hideVideo, dauerV);
  setTimeout(sayBild1, 14000);
  setTimeout(sayBild2, 24000);
  setTimeout(sayBild3, 34000);
  setTimeout(sayBild4, 44000);
  setTimeout(sayBild5, 54000);
  setTimeout(sayBild6, 74000);
  session.service('ALTabletService').then(function (tabletService) {
    //tabletService.preLoadImage("/vasTest/html/Bilder/credits.png")
    tabletService.playVideo(url)
    //tabletService.playVideo("http://198.18.0.1/apps/vasTest/videos/gandalf.mp4")
    tabletService.hideImage()
  }, function (error) {
    console.log(error);
  })
}

function hideVideo() {
  session.service('ALTabletService').then(function (tabletService) {
    //tabletService.preLoadImage("/vasTest/html/Bilder/credits.png")
    tabletService.stopVideo()
  }, function (error) {
    console.log(error);
  })
}

function setBrightness(zahl) {
  session.service('ALTabletService').then(function (tabletService) {
    tabletService.setBrightness(zahl)
  }, function (error) {
    console.log(error);
  })
}

function sayAnimatedExpl1() {
  session.service('ALAnimatedSpeech').then(function (asr_service) {
    configuration = {"bodyLanguageMode":"contextual"}
    asr_service.say('hier erkläre ich das eine')
  }, function (error) {
    console.log(error);
  })
}

function sayAnimatedExpl2() {
  session.service('ALAnimatedSpeech').then(function (asr_service) {
    configuration = {"bodyLanguageMode":"contextual"}
    asr_service.say('hier erkläre ich das andere')
  }, function (error) {
    console.log(error);
  })
}

function sayBild1() {
  session.service('ALTextToSpeech').then(function (tts) {
    tts.say('zu aller erst registriere dich über den q r code');
  }, function (error) {
    console.log(error);
  })
}

function sayBild2() {
  session.service('ALTextToSpeech').then(function (tts) {
    tts.say('in dem labor dürfen sich maximal 12 personen aufhalten. auf besprechungen sollte verzichtet werden');
  }, function (error) {
    console.log(error);
  })
}

function sayBild3() {
  session.service('ALTextToSpeech').then(function (tts) {
    tts.say('abstand halten schützt euch und andere');
  }, function (error) {
    console.log(error);
  })
}

function sayBild4() {
  session.service('ALTextToSpeech').then(function (tts) {
    tts.say('das selbe gilt auch für die maske');
  }, function (error) {
    console.log(error);
  })
}

function sayBild5() {
  session.service('ALTextToSpeech').then(function (tts) {
    tts.say('desinfiktionsmittel findes du auf dem fensterbrett');
  }, function (error) {
    console.log(error);
  })
}

function sayBild6() {
  session.service('ALTextToSpeech').then(function (tts) {
    tts.say('viel erfolg und produktives arbeiten');
  }, function (error) {
    console.log(error);
  })
}

function waithideWebview() {
  setTimeout(hideWebview, 5000)
}

function tanz() {
  session.service('ALMotion').then(function (motion_service) {
    names  = ['LWristYaw']
    stiffnessLists  = [0.25, 0.5, 1.0, 0.0]
    timeLists  = [1.0, 2.0, 3.0, 4.0]
    motion_service.stiffnessInterpolation(names, stiffnessLists, timeLists)
    //motion_service.stiffnessInterpolation(['LWristYaw'], [0.25, 0.5, 1.0, 0.0], [1.0, 2.0, 3.0, 4.0])

  }, function (error) {
    console.log(error);
  })
}






