function showPopup() {
    var popup = document.getElementById("showPopup");
    popup.style.display="visible";
  }

function closePopup() {
    var popup = document.getElementById("student");
    if(popup.value == 1){
        window.location.href = studentLogin.html;
    }
    else{
        window.location.href = mentorLogin.html;
    }
  }