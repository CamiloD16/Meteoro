let dataReload = document.getElementsByClassName("data-reload")
let language = {
  en: {
    welcome: "ingles"
  },
  es: {
    welcome: "texto en español"
  }
}
if (window.location.hash) {
  if (window.location.hash === "#en") {
    discover.textContent = language.en.welcome
  }
}
// for (i = 1; i <= dataReload.length; i++) {
  dataReload.onclick = function () {
    alert("#")
    // location.reload(true);
    // window.location.reload();
  // }
}