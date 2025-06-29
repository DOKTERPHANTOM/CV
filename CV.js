<script src="CV.js"></script>

document.addEventListener("DOMContentLoaded", function () {
  const hero = document.getElementById("hero");
  if (hero) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
        }
      });
    }, { threshold: 0.5 });

    observer.observe(hero);
  }
  console.log("JS loaded and working!");
});

