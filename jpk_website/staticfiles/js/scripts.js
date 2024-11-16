document.addEventListener("DOMContentLoaded", function() {
    const currentYear = new Date().getFullYear();
    document.getElementById("copyright").innerHTML = `Copyright &copy; Jeremy Kuehn ${currentYear}`;
});

// Ajax blog tag filter request
document.addEventListener("DOMContentLoaded", function () {
    const tagLinks = document.querySelectorAll(".tag-filter");
    const blogContainer = document.getElementById("blog-container");

    tagLinks.forEach(link => {
        link.addEventListener("click", function (e) {
            e.preventDefault(); // Prevent default link behavior
            const tag = this.getAttribute("data-tag");

            fetch(`/blogHome/?tag=${tag}`, {
                headers: {
                    "X-Requested-With": "XMLHttpRequest",
                },
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.json();
            })
            .then(data => {
                // Replace the content inside the blog container
                blogContainer.innerHTML = data.html;
            })
            .catch(error => console.error("Error fetching filtered blogs:", error));
        });
    });
});


