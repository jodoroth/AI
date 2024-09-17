$(document).ready(function () {
    // Display Speak Message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {
  
        $(".wave-msg2 li:first").text(message);
      //  $('.wave-msg1').textillate('start');
  
    }
   // Display hood
   /*eel.expose(ShowHood)
   function ShowHood() {
       $("#Feature").attr("hidden", false);
       $("#wave").attr("hidden", true);
   }*/
    
  
  });