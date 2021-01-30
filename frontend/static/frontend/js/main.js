const chk = document.getElementById("check");

let logos = document.querySelectorAll("img");

chk.addEventListener("change", () => {
  if (chk.checked) {
    document.getElementById("theme-style").href = static + "/secondary.css";
  } else {
    document.getElementById("theme-style").href = static + "/mains.css";
  }
});
