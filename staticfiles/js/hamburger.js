document.addEventListener("DOMContentLoaded", () => {
    const hamburger = document.getElementById("hamburger");
    const nav = document.getElementById("nav");

    if (!hamburger || !nav) return;

    hamburger.addEventListener("click", () => {
        nav.classList.toggle("active");
    });

    // メニュー内のリンクをクリックしたら閉じる
    nav.addEventListener("click", (e) => {
        if (e.target.tagName === "A") {
            nav.classList.remove("active");
        }
    });
});
