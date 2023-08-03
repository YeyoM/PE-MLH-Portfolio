window.onload = () => {
  document.body.onkeyup = async function(e) {
    if (e.key == "Escape" || e.code == "Escape" || e.key == " ") {
      transitionOut() 
    }
  }
  setTimeout(() => {
    window.location.href = '/welcome'
  }, 25000)
}

function transitionOut() {
  // transition the whole page out
  $('div').css('opacity', 0.60)

  // redirect the user to the next page
  setTimeout(() => {
    window.location.href = '/welcome'
  }, 1500)
}