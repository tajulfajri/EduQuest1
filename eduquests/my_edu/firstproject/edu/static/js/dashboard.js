document.addEventListener("DOMContentLoaded", function () {
    // Mengambil kredensial dari local storage
    var storedUsername = localStorage.getItem("username");
    var storedPassword = localStorage.getItem("password");

    // Jika kredensial tidak ada, redirect ke halaman login
    if (!storedUsername || !storedPassword) {
        alert("Anda harus login terlebih dahulu!");
        window.location.href = "login.html"; // Ganti dengan URL halaman login Anda
    } else {
        // Tampilkan username di navbar
        document.getElementById("usernameDisplay").textContent = storedUsername;
    }
});

// Script untuk menangani logout
function logout() {
    localStorage.removeItem("username");
    localStorage.removeItem("password");
    window.location.href = "login.html"; // Redirect ke halaman login setelah logout
}
