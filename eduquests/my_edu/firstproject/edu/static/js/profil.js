// Fungsi untuk menyimpan data profil ke localStorage
function saveProfileData() {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const gender = document.getElementById('gender').value;
    const phone = document.getElementById('phone').value;
    const parentPhone = document.getElementById('parent-phone').value;
    const profession = document.getElementById('profession').value;
    const nisn = document.getElementById('nisn').value;

    // Simpan data di localStorage
    localStorage.setItem('name', name);
    localStorage.setItem('email', email);
    localStorage.setItem('gender', gender);
    localStorage.setItem('phone', phone);
    localStorage.setItem('parentPhone', parentPhone);
    localStorage.setItem('profession', profession);
    localStorage.setItem('nisn', nisn);

    // Simpan foto profil di localStorage
    const profileImage = document.getElementById('profileImage').src;
    if (profileImage && profileImage !== "default-profile.jpg") {
        localStorage.setItem('profileImage', profileImage); // Simpan URL gambar profil
    }

    // Tampilkan pop-up notifikasi
    alert("Profil Anda telah berhasil disimpan!");

    // Redirect ke halaman detail profil setelah pop-up ditutup
    setTimeout(function() {
        window.location.href = "detail.html"; // Ubah dengan URL halaman detail profil yang sesuai
    }, 1000); // Delay 1 detik sebelum redirect
}

// Fungsi untuk mengisi ulang data dari localStorage saat halaman dimuat
window.onload = function () {
    // Mengisi ulang data profil dari localStorage
    if (localStorage.getItem('name')) {
        document.getElementById('name').value = localStorage.getItem('name');
    }
    if (localStorage.getItem('email')) {
        document.getElementById('email').value = localStorage.getItem('email');
    }
    if (localStorage.getItem('gender')) {
        document.getElementById('gender').value = localStorage.getItem('gender');
    }
    if (localStorage.getItem('phone')) {
        document.getElementById('phone').value = localStorage.getItem('phone');
    }
    if (localStorage.getItem('parentPhone')) {
        document.getElementById('parent-phone').value = localStorage.getItem('parentPhone');
    }
    if (localStorage.getItem('profession')) {
        document.getElementById('profession').value = localStorage.getItem('profession');
    }
    if (localStorage.getItem('nisn')) {
        document.getElementById('nisn').value = localStorage.getItem('nisn');
    }

    // Memuat foto profil dari localStorage jika ada
    const storedProfileImage = localStorage.getItem('profileImage');
    if (storedProfileImage && storedProfileImage !== "default-profile.jpg") {
        document.getElementById('profileImage').src = storedProfileImage;

        // Memuat gambar profil ke sidebar juga jika ada
        document.getElementById('sidebarProfileImage').src = storedProfileImage;
    }
};

// Fungsi untuk pratinjau gambar profil saat diunggah
document.querySelector('.profile-pic img').addEventListener('click', function () {
    const fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = 'image/*';

    fileInput.onchange = function (event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                // Menyimpan URL gambar ke elemen img untuk ditampilkan
                document.getElementById('profileImage').src = e.target.result;
                document.getElementById('sidebarProfileImage').src = e.target.result; // Set foto di sidebar juga

                // Menyimpan URL gambar ke localStorage
                localStorage.setItem('profileImage', e.target.result);
            };
            reader.readAsDataURL(file);
        }
    };

    fileInput.click();
});
