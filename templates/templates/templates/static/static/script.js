// ===== static/script.js =====
// Simple animations or interactions
document.addEventListener("DOMContentLoaded", function(){
    const tables = document.querySelectorAll("table");
    tables.forEach(table => {
        table.addEventListener("mouseover", () => {
            table.style.boxShadow = "0 0 15px rgba(0,0,0,0.3)";
        });
        table.addEventListener("mouseout", () => {
            table.style.boxShadow = "none";
        });
    });
});
