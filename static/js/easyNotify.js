

(function($) {

  $.fn.easyNotify = function(options) {
    
    alert("Asda")  
    
    var settings = $.extend({
      title: "Notification",
      options: {
        body: "",
        icon: "",
        lang: 'pt-BR',
        onClose: "",
        onClick: "",
        onError: ""
      }
    }, options);

    this.init = function() {
        var notify = this;
      if (!("Notification" in window)) {
        alert("This browser does not support desktop notification");
      } else if (Notification.permission === "granted") {

        var notification = new Notification(settings.title, settings.options);
        
        notification.onclose = function() {
          alert("onclose")
            if (typeof settings.options.onClose == 'function') { 
                settings.options.onClose();
            }
        };

        notification.onclick = function(){
          alert("onclick")
            if (typeof settings.options.onClick == 'function') { 
                settings.options.onClick();
            }
        };

        notification.onerror  = function(){
          alert("onerror")
            if (typeof settings.options.onError  == 'function') { 
                settings.options.onError();
            }
        };

      } else if (Notification.permission !== 'denied') {
        Notification.requestPermission(function(permission) {
          if (permission === "granted") {
            notify.init();
          }

        });
      }

    };

    this.init();
    return this;
  };

}(jQuery));