# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image ruang_tamu_arman = "images/1.png"
image dapur_arman = "images/2.png"
image ruang_tamu_uztad = "images/3.png"
image ruang_kelas = "images/4.png"
image kampus = "images/5.png"
image masjid = "images/6.png"
image atap_markas = "images/7.png"
image ruang_rapat_rahasia = "images/8.png"
image aula_utama_markas_teroris = "images/9.png"
image lorong_markas_teroris = "images/10.png"
image hutan = "images/11.png"
image sungai_dalam_hutan = "images/12.png"
image meja_diskusi_markas_teroris = "images/13.png"
image garasi_markas_teroris = "images/14.png"
image dalam_mobil = "images/15.png"
image dermaga = "images/16.png"
image ruang_pengadilan = "images/17.png"
image dalam_penjara = "images/18.png"
image ruang_interogasi = "images/19.png"
image cafe_hancur = "images/21.png"
image kantor_hotel = "images/22.png"
image kantin_siang_ramai = "images/25.png"

define ar = Character("Arman")
define ay = Character("Ayah")
define ib = Character("Ibu")
define na = Character("Naomi")
define po = Character("Polisi")
define vi = Character("Victor")
define bu = Character("Budi")
define ri = Character("Rizal")
define ni = Character("Ibu-ibu")
define nb = Character("Bapak-bapak")
define ra = Character("Raksa")
define ja = Character("Jarwo")


# The game starts here.
label start:
    #Scene 1: Markas Teroris
    scene meja_diskusi_markas_teroris with fade
    play music "bm-s1.mp3"
    play sound "lampu-bm-s1.mp3"
    show rizal netral at right
    ri "Arman, saatnya membuktikan kesetiaanmu. Kita punya misi besar. Sebuah café di Jakarta, Café itu adalah simbol semua yang salah dengan negeri ini—keserakahan Barat, gaya hidup yang menghancurkan moral. Malam ini, kita kirim pesan. Dan kamu yang akan membawanya."
    stop sound fadeout 2.0
    show mc sedih at left
    ar "Ini dia. Titik di mana aku tidak bisa mundur lagi. Tapi… apa aku benar-benar siap untuk ini?"
    hide mc 
    hide rizal
    menu:
        "Ambil tas itu":
            jump a_1
        "Tolak tawaran Pak Rizal":
            jump a_2
        
label a_1:
    play sound "ambil-tas-bm-s1.mp3"
    show mc netral at left
    ar "Apa… apa ini sudah pasti? Maksudku, tidak ada jalan lain"
    show rizal senyum at right
    play sound "KETAWA-TIPIS-BM-S1.mp3"
    ri "Jalan lain? Jalan lain adalah membiarkan mereka terus menghancurkan bangsa kita. Jalan lain adalah menyerah. Dan itu bukan kita, Arman."
    ri "Kamu tahu kenapa kami memilihmu? Karena kami percaya kamu bisa. Ini bukan sekadar tugas. Ini kehormatan."
    
    hide mc
    hide rizal
    show mc sedih
    ar "Dia membuatnya terdengar seperti pilihan yang mulia. Tapi kenapa aku merasa seperti ini… seperti aku berdiri di tepi jurang."
    
    show mc sedih at left
    show rizal netral at right
    ri "Fokus, Arman. Café itu buka sampai tengah malam. Kamu akan masuk dengan tas ini, letakkan di bawah salah satu meja di pojok. Set timer-nya, dan keluar. Sesimpel itu."
   
    play sound "NUNJUK_KE_PETA-BM-S1.mp3"
    ri "Kita sudah siapkan segalanya. Kamu tidak akan dicurigai. Ingat, ini adalah misi besar. Kita tunjukkan pada mereka bahwa kita tidak bisa diremehkan."
    ar "Aku… aku paham. Ini penting. Aku akan melakukannya."
    show rizal senyum at right
    ri "Bagus. Aku tahu aku bisa mengandalkanmu. Setelah malam ini, kamu akan jadi pahlawan bagi perjuangan kita."
    play sound ["AMBIL-JAS-BM-S1.mp3","<silence .5>","JALAN-KE-PINTU-BM-S1.mp3"]
    ri "Jangan pikirkan apa pun lagi. Fokus saja pada tugasmu. Kita akan menang, Arman."
    play sound "PINTU_TUTUP-BM-S1.mp3"
    hide rizal
    "(Rizal keluar dari ruangan tersebut, meninggalkan Arman merenung sendiri.)"
    jump scene_2

label a_2:
    show mc sedih at left
    ar "Rizal… aku nggak bisa. Ini… terlalu jauh. Aku setuju dengan perjuangan kita, tapi menghancurkan nyawa orang-orang nggak masuk akal buatku."
    show rizal marah at right
    ri "Kamu bilang kamu setia. Kamu bilang kamu ingin perubahan. Tapi sekarang kamu mundur? Apa kamu takut?!"
    ar "Bukan soal takut, Rizal. Ini soal hati nurani. Aku nggak mau jadi pembunuh."
    play sound ["KURSI-GERAK-BM-S1.mp3","<silence .5>","JALAN-LAMBAN-BM-S1.mp3"]
    ri "Hati nurani? Kau pikir hati nurani mereka peduli pada kita? Mereka menguasai segalanya, Arman. Mereka membunuh kita secara perlahan—lewat sistem, lewat budaya mereka. Kau pikir kita bisa menang tanpa pengorbanan?"
    ar "Aku tahu mereka salah. Tapi ini bukan caranya, Rizal. Kalau kita membunuh, apa bedanya kita dengan mereka?"
    play sound "PUKUL_MEJA-BM-S1.mp3"
    ri "Bedanya? Bedanya kita berjuang untuk kebenaran! Kau pikir dunia ini akan berubah kalau kita hanya bicara? Kalau kita hanya diam?"
    ar "Pak, aku tahu kamu marah. Aku tahu dunia ini nggak adil. Tapi aku cuma minta satu hal—cari cara lain. Kita bisa melawan tanpa menghancurkan nyawa orang tak bersalah."
    ri "Kamu pikir ini demokrasi, Arman? Kamu pikir kamu bisa memilih cara yang nyaman? Kalau kamu menolak, kamu musuh. Dan kami tidak memberi ampun pada musuh."
    show rizal netral at right
    ri "Sudahlah, memang salah ku menaruh kepercayaan kepadamu Man"
    return

label scene_2:
    stop music
    #Scene 2: Pengeboman Cafe
    scene kantin_siang_ramai with fade
    show mc sedih
    ar "Aku sudah di sini. Rencana sudah jelas. Masuk, letakkan tas, keluar. Tapi kenapa… kenapa langkahku terasa berat?"
    ar "Apakah ini benar? Apakah ini yang aku inginkan? Apa ini cara untuk melawan mereka?"

    hide mc
    menu:
        "Tetap lanjutkan rencana.":
            jump b_1
        "Berhenti sekarang juga.":
            jump b_2

label b_1:
    show mc netral at left
    ar "Mereka terlihat bahagia. Tak ada yang tahu apa yang akan terjadi."
    "(Arman berhenti sejenak, matanya menyapu ruangan.)"
    show mc sedih at left
    ar "Mereka terlihat seperti orang biasa. Bukan musuh. Bukan ancaman. Apa aku benar-benar bisa melakukan ini?"
    play music "bm-s2.mp3"
    ar "Ini demi sesuatu yang lebih besar… kan? Demi perubahan. Tapi kenapa rasanya salah?"
    "(Dia menggigit bibirnya, lalu mengalihkan pandangan, melanjutkan langkahnya ke meja yang ditentukan.)"
    show mc netral at left
    ar "Sudah selesai. Bomnya sudah terpasang. Sekarang aku harus pergi... menjauh dari semua ini."
    "(Dia berjalan menyusuri trotoar, langkahnya berat. Lampu jalan memanjang di kejauhan)"
    "(Arman berhenti di sudut jalan, menoleh sebentar ke arah café yang kini berada jauh di belakangnya. Matanya melirik jam tangan.)"
    ar "Lima menit lagi. Aku harus menjauh lebih jauh. Jangan berhenti, Arman."
    "...."
    play sound ["<silence 1>","BOM-BM-S2.mp3"]
    scene cafe_hancur with fade
    "(Bom meledak di tengah-tengah café)"
    "(Arman berhenti seketika, tubuhnya kaku.)"
    show mc sedih at left
    ar "Sudah selesai... ini benar-benar terjadi. Aku yang melakukannya."
    "(Dia mencoba menarik napas dalam, tapi dadanya terasa sesak.)"
    "Orang-orang di sekitar:" "\"Ada bom!\".... \"Panggil polisi!\".... \"Ya Tuhan, café itu hancur!\"...."
    ar "Ini semua untuk tujuan besar... ini semua demi perubahan. Tapi kenapa suara ini di kepalaku terus berteriak… salah?"

    #Scene 3: Esok hari
    scene ruang_tamu_arman with fade
    play music "bm-s3.mp3"
    "(Cahaya pagi masuk samar melalui celah tirai yang setengah tertutup. Kamar Arman berantakan, dengan pakaian dan barang-barang berserakan. Dia duduk di lantai bersandar pada tempat tidur, ponselnya tergenggam di tangan. Matanya merah, jelas kurang tidur.)"
    show mc sedih
    ar "Semalam... semua itu terasa seperti mimpi. Tapi aku tahu ini nyata. Aku tahu aku yang melakukannya."
    "(Dia menatap ponsel di tangannya, ibu jarinya bergetar saat membuka aplikasi media sosial. Feed-nya penuh dengan berita tentang ledakan café tadi malam. Foto-foto reruntuhan, ambulans, dan korban berseliweran.)"
    ar "Aku tak sanggup melihatnya… tapi aku tak bisa berhenti. Aku harus tahu apa yang terjadi."
    "(Dia menggulir perlahan hingga berhenti di sebuah unggahan story. Temannya, seseorang bernama \"Dani\", telah memposting foto seseorang yang dikenalnya. Tulisan di story itu berbunyi: \“Selamat jalan, Naomi. Dunia kehilangan sinarmu. Rest in peace.\”)"
    show mc kaget
    ar "Tidak... ini tidak mungkin."
    "(Dia menjatuhkan ponselnya ke lantai. Scene menyorot ponsel itu yang kini menampilkan story Dani. Arman menggenggam kepalanya dengan kedua tangan, tubuhnya gemetar.)"
    ar "Naomi... dia ada di sana? Aku yang... aku yang membunuhnya?!"
    ar "TIDAK!!!"
    "(Dia berdiri dengan panik, menghantam dinding dengan tangannya. Napasnya semakin cepat, tubuhnya gemetar hebat.)"
    show mc sedih
    ar "Tujuan besar? Perjuangan suci? Semua itu hanya omong kosong. Aku... aku membunuh temanku sendiri."
    return

label b_2:
    show mc sedih at left
    "(Arman mundur selangkah, napasnya semakin berat. Scene fokus pada wajahnya, penuh dengan konflik batin.)"
    ar "Pelan-pelan..."
    show mc marah at left
    ar "Tidak… aku nggak bisa. Ini salah."
    "(Dia berbalik dan berjalan cepat menjauh dari cafe.)"
    ar "Aku nggak bisa. Aku nggak peduli apa yang Pak Rizal pikirkan. Aku nggak peduli apa yang terjadi selanjutnya. Aku nggak mau jadi pembunuh."
    show mc sedih at left   
    ar "Bagaimana ini? Apa Pak Rizal akan mengejarku? Apakah aku akan aman? Apa aku akan hidup setelah ini?"
    return
