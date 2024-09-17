$(document).ready(function() {
    /*	$('.text').textillate({
            loop: true,
            sync: true,
            in: {
                effect: "fadeInLeft",
            },
            out: {
                effect: "fadeOutRight",
            },
    
        });*/
    
    
            $('.wave-msg1').textillate({
            loop: true,
            sync: true,
            in: {
                effect: "fadeInUp",
                sync: true
            },
            out: {
                effect: "fadeOutUp",
                sync: true
            },
    
        });
    
        $('#micoption').click(function(){
          // eel.playsoundformicoption();
           $('#Feature').attr("hidden",true);
           $('#wave').attr("hidden",false);
           eel.playClickSound();
           //eel.recognize_from_microphone()();
           eel.allcommands()();
        });
    });