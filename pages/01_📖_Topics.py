import streamlit as st

st.title("SSL Certificate 🔒")
st.image("images/ssl1.jpg")
st.header("Definisi SSL Certificate")
st.markdown("""Sertifikat SSL adalah sertifikat digital yang mengotentikasi identitas situs web dan memungkinkan koneksi terenkripsi. SSL adalah singkatan dari Secure Sockets Layer, protokol keamanan yang membuat tautan terenkripsi antara server web dan browser web. Perusahaan dan organisasi perlu menambahkan sertifikat SSL ke situs web mereka untuk mengamankan transaksi online dan menjaga kerahasiaan dan keamanan informasi pelanggan.
Secara singkat, SSL menjaga koneksi internet tetap aman dan mencegah penjahat membaca atau mengubah informasi yang ditransfer antara dua sistem. Saat Anda melihat ikon gembok di sebelah URL di bilah alamat, itu berarti SSL melindungi situs web yang Anda kunjungi.""")

st.header("Cara Kerja SSL Certificate")
st.image("images/SSL.jpg")
st.markdown("SSL bekerja dengan memastikan bahwa setiap data yang ditransfer antara pengguna dan situs web, atau antara dua sistem, tetap tidak mungkin untuk dibaca. Ini menggunakan algoritme enkripsi untuk mengacak data dalam perjalanan, yang mencegah peretas membacanya saat dikirim melalui koneksi. Data ini mencakup informasi yang berpotensi sensitif seperti nama, alamat, nomor kartu kredit, atau detail keuangan lainnya.")
st.markdown("""Prosesnya bekerja seperti ini:
- Peramban atau server mencoba menyambung ke situs web (yaitu, server web) yang diamankan dengan SSL.
- Browser atau server meminta agar server web mengidentifikasi dirinya sendiri.
- Server web mengirimkan salinan sertifikat SSL-nya kepada browser atau server sebagai tanggapan.
- Browser atau server memeriksa untuk melihat apakah itu mempercayai sertifikat SSL. Jika ya, itu menandakan ini ke server web.
- Server web kemudian mengembalikan pengakuan yang ditandatangani secara digital untuk memulai sesi terenkripsi SSL.
- Data terenkripsi dibagi antara browser atau server dan server web.""")

st.markdown("""Ketika sebuah situs web diamankan dengan sertifikat SSL, akronim HTTPS (yang merupakan singkatan dari HyperText Transfer Protocol Secure) muncul di URL. Tanpa sertifikat SSL, hanya huruf HTTP – yaitu, tanpa S untuk Aman – yang akan muncul. Ikon gembok juga akan ditampilkan di bilah alamat URL. Ini menandakan kepercayaan dan memberikan kepastian kepada mereka yang mengunjungi situs web.

Untuk melihat detail sertifikat SSL, Anda dapat mengklik simbol gembok yang terletak di bilah browser. Detail yang biasanya disertakan dalam sertifikat SSL meliputi:

- Nama domain tempat sertifikat diterbitkan
- Orang, organisasi, atau perangkat mana yang dikeluarkannya
- Otoritas Sertifikat mana yang mengeluarkannya
- Tanda tangan digital Otoritas Sertifikat
- Subdomain terkait
- Tanggal penerbitan sertifikat
- Tanggal kedaluwarsa sertifikat
- Kunci publik (kunci pribadi tidak diungkapkan).""")

st.header("Kenapa SSL Certificate dibutuhkan?")
st.markdown("""Situs web memerlukan sertifikat SSL untuk menjaga keamanan data pengguna, memverifikasi kepemilikan situs web, mencegah penyerang membuat versi palsu situs, dan menyampaikan kepercayaan kepada pengguna.

Jika sebuah situs web meminta pengguna untuk masuk, memasukkan detail pribadi seperti nomor kartu kredit mereka, atau melihat informasi rahasia seperti manfaat kesehatan atau informasi keuangan, maka penting untuk menjaga kerahasiaan data. Sertifikat SSL membantu menjaga interaksi online tetap pribadi dan meyakinkan pengguna bahwa situs web itu asli dan aman untuk berbagi informasi pribadi.

Lebih relevan untuk bisnis adalah kenyataan bahwa sertifikat SSL diperlukan untuk alamat web HTTPS. HTTPS adalah bentuk aman dari HTTP, yang berarti bahwa situs web HTTPS memiliki lalu lintas yang dienkripsi oleh SSL. Sebagian besar browser menandai situs HTTP – yang tidak memiliki sertifikat SSL – sebagai "tidak aman". Ini mengirimkan sinyal yang jelas kepada pengguna bahwa situs tersebut mungkin tidak dapat dipercaya – mendorong bisnis yang belum melakukannya untuk bermigrasi ke HTTPS.

Sertifikat SSL membantu mengamankan informasi seperti:

- Kredensial masuk
- Transaksi kartu kredit atau informasi rekening bank
- Informasi identitas pribadi — seperti nama lengkap, alamat, tanggal lahir, atau nomor telepon
- Dokumen dan kontrak hukum
- Rekam medis
- Informasi eksklusif""")

st.header("Tipe - Tipe SSL Certificate")
st.image("images/tipe ssl.jpg")
st.markdown("""
- Extended Validation certificates (EV SSL), Ini adalah jenis sertifikat SSL dengan peringkat tertinggi dan termahal. Ini cenderung digunakan untuk situs web profil tinggi yang mengumpulkan data dan melibatkan pembayaran online. Saat dipasang, sertifikat SSL ini menampilkan gembok, HTTPS, nama bisnis, dan negara di bilah alamat browser. Menampilkan informasi pemilik situs web di bilah alamat membantu membedakan situs dari situs jahat. Untuk menyiapkan sertifikat SSL EV, pemilik situs web harus melalui proses verifikasi identitas standar untuk mengonfirmasi bahwa mereka berwenang secara hukum atas hak eksklusif domain.
- Organization Validated certificates (OV SSL), Versi sertifikat SSL ini memiliki tingkat jaminan yang serupa dengan sertifikat SSL EV sejak mendapatkannya; pemilik situs web harus menyelesaikan proses validasi yang substansial. Jenis sertifikat ini juga menampilkan informasi pemilik situs web di bilah alamat untuk membedakan dari situs jahat. Sertifikat SSL OV cenderung menjadi yang paling mahal kedua (setelah EV SSL), dan tujuan utamanya adalah untuk mengenkripsi informasi sensitif pengguna selama transaksi. Situs web komersial atau publik harus memasang sertifikat SSL OV untuk memastikan bahwa informasi pelanggan yang dibagikan tetap rahasia.
- Domain Validated certificates (DV SSL), Proses validasi untuk mendapatkan jenis sertifikat SSL ini minimal, dan akibatnya, sertifikat SSL Validasi Domain memberikan jaminan yang lebih rendah dan enkripsi yang minimal. Mereka cenderung digunakan untuk blog atau situs web informasi – yaitu, yang tidak melibatkan pengumpulan data atau pembayaran online. Jenis sertifikat SSL ini adalah salah satu yang paling murah dan tercepat untuk didapatkan. Proses validasi hanya mengharuskan pemilik situs untuk membuktikan kepemilikan domain dengan membalas email atau panggilan telepon. Bilah alamat browser hanya menampilkan HTTPS dan gembok tanpa nama bisnis yang ditampilkan.
- Wildcard SSL certificates, Sertifikat SSL Wildcard memungkinkan Anda untuk mengamankan domain dasar dan sub-domain tak terbatas pada satu sertifikat. Jika Anda memiliki beberapa sub-domain untuk diamankan, maka pembelian sertifikat SSL Wildcard jauh lebih murah daripada membeli sertifikat SSL individual untuk masing-masing subdomain. 
- Multi-Domain SSL Certificate (MDC), Sertifikat Multi-Domain dapat digunakan untuk mengamankan banyak domain dan/atau nama sub-domain. Ini termasuk kombinasi domain dan sub-domain yang benar-benar unik dengan TLD (Top-Level Domains) yang berbeda kecuali yang lokal/internal.
- Unified Communications Certificate (UCC), Sertifikat Komunikasi Terpadu (UCC) juga dianggap sebagai sertifikat SSL Multi-Domain. UCC awalnya dirancang untuk mengamankan server Microsoft Exchange dan Live Communications. Saat ini, setiap pemilik situs web dapat menggunakan sertifikat ini untuk memungkinkan beberapa nama domain diamankan pada satu sertifikat. Sertifikat UCC divalidasi secara organisasi dan menampilkan gembok di browser. UCC dapat digunakan sebagai sertifikat SSL EV untuk memberikan pengunjung situs web jaminan tertinggi melalui bilah alamat hijau. Sangat penting untuk mengetahui berbagai jenis sertifikat SSL untuk mendapatkan jenis sertifikat yang tepat untuk situs web Anda.
""")

st.title("Apa itu SSL Certificate?")
st.video("https://www.youtube.com/watch?v=SJJmoDZ3il8")

st.title("Bagaimana Cara Kerja SSL Cerificate?")
st.video("https://www.youtube.com/watch?v=T4Df5_cojAs")