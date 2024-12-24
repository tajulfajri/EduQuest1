function checkPasswordMatch(event) {
    event.preventDefault(); // Mencegah pengiriman form secara langsung

    // Mengambil nilai dari input
    var username = $('#username').val(); // Pastikan input username ada di form
    var password = $('#password').val();
    var confirmPassword = $('#confirmPassword').val();
    var passwordError = $('#passwordError');

    // Validasi kekuatan password
    var strongPasswordPattern = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
    if (!strongPasswordPattern.test(password)) {
        passwordError.text("Password harus minimal 8 karakter dan mengandung huruf dan angka.").show();
        return false;
    }

    // Cek kesesuaian password
    if (password !== confirmPassword) {
        passwordError.text("Kata sandi tidak cocok!").show(); // Tampilkan pesan error
        return false;
    } else {
        passwordError.hide(); // Sembunyikan pesan error
        
        // Simpan kredensial di local storage
        localStorage.setItem("username", username);
        localStorage.setItem("password", password);
        
        alert("Selamat, registrasi berhasil!");

        // Redirect ke halaman login setelah 1 detik
        setTimeout(function() {
            window.location.href = "login.html";
        }, 1000);

        return true; // Form akan diproses
    }
}