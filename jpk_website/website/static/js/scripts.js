document.addEventListener("DOMContentLoaded", function() {
    const currentYear = new Date().getFullYear();
    document.getElementById("copyright").innerHTML = `Copyright &copy; Jeremy Kuehn ${currentYear}`;
});

