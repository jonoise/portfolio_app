const chk = document.getElementById("check");

let logos = document.querySelectorAll("img");

let theme = localStorage.getItem("blog_theme");

if (theme == "secondary") {
  document.getElementById("theme-style").href = static + "/secondary.css";
  chk.click();
}

chk.addEventListener("change", () => {
  if (chk.checked) {
    document.getElementById("theme-style").href = static + "/secondary.css";
    localStorage.setItem("blog_theme", "secondary");
  } else {
    document.getElementById("theme-style").href = "";
    localStorage.setItem("blog_theme", "main");
  }
});
