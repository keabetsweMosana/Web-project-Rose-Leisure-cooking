document.querySelectorAll(".fade-img").forEach((img) => {
    img.addEventListener("click", () => {
        img.classList.toggle("hidden");  // fade out / fade in
    });
});
