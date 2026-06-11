const modulesData = [
  {
    "title": "Literasi Digital",
    "description": "Panduan bijak menggunakan internet dan menjaga keamanan data pribadi kita.",
    "author": "By. Abu Kafa",
    "category": "informatika",
    "path": "informatika/literasi-digital/index.html",
    "icon": "shield-check",
    "color": "blue"
  },
  {
    "title": "Evolusi Informasi",
    "description": "Melihat sejarah perkembangan informasi dari zaman dulu hingga serba digital sekarang.",
    "author": "By. Abu Kafa",
    "category": "informatika",
    "path": "informatika/evolusi-informasi/index.html",
    "icon": "history",
    "color": "blue"
  },
  {
    "title": "Prompt Mastery",
    "description": "Cara jago berkomunikasi dengan AI agar mendapatkan hasil yang paling akurat.",
    "author": "By. Abu Kafa",
    "category": "informatika",
    "path": "informatika/prompt-mastery/index.html",
    "icon": "message-square-code",
    "color": "blue"
  },
  {
    "title": "Cyber Security",
    "description": "Dasar-dasar keamanan siber untuk melindungi diri dari ancaman digital.",
    "author": "By. Abu Kafa",
    "category": "informatika",
    "path": "informatika/cyber-security/index.html",
    "icon": "shield",
    "color": "blue"
  },
  {
    "title": "Cryptography & Blockchain",
    "description": "Memahami cara kerja enkripsi dan teknologi blockchain yang mendasari banyak inovasi digital saat ini.",
    "author": "By. Abu Kafa",
    "category": "informatika",
    "path": "informatika/cryptography-blockchain/index.html",
    "icon": "lock",
    "color": "blue"
  },
  {
    "title": "AI Learning",
    "description": "Mengenal dasar kecerdasan buatan dan bagaimana mesin belajar dari data.",
    "author": "By. Abu Kafa",
    "category": "informatika",
    "path": "informatika/ai-learning/index.html",
    "icon": "brain-circuit",
    "color": "blue"
  },
  {
    "title": "Code Freedom",
    "description": "Memahami konsep merdeka dalam berkarya lewat pemrograman sumber terbuka (Open Source).",
    "author": "By. Abu Kafa",
    "category": "informatika",
    "path": "informatika/code-freedom/index.html",
    "icon": "code-2",
    "color": "blue"
  },
  {
    "title": "Data Visualization",
    "description": "Eksplorasi interaktif berbagai tipe chart berdasarkan jenis data dan tujuannya.",
    "author": "By. Abu Kafa",
    "category": "informatika",
    "path": "informatika/data-visualization/index.html",
    "icon": "bar-chart-3",
    "color": "blue"
  },
  {
    "title": "Editing Toolkit",
    "description": "Alat bantu kreatif untuk mengolah video dan audio menjadi karya yang menarik.",
    "author": "By. Abu Kafa",
    "category": "informatika",
    "path": "informatika/editing-toolkit/index.html",
    "icon": "video",
    "color": "blue"
  },
  {
    "title": "Ensiklopedi Syariah",
    "description": "Pusat istilah dan pengetahuan dasar tentang hukum-hukum Islam secara umum.",
    "author": "By. Abu Kafa",
    "category": "tsaqofah",
    "path": "tsaqofah/syariah/index.html",
    "icon": "library",
    "color": "rose"
  },
  {
    "title": "Decoding Al-Kahfi",
    "description": "Algoritma Ilahi & Arsitektur Informasi di era Post-Truth, AI, dan disrupsi digital.",
    "author": "By. Abu Kafa",
    "category": "tsaqofah",
    "path": "tsaqofah/alkahfi/index.html",
    "icon": "library",
    "color": "orange"
  },
  {
    "title": "Thariqul Iman",
    "description": "Rangkuman Bab 1 Nizham al-Islam Karya Syaikh Taqiyuddin An-Nabhani.",
    "author": "By. Abu Kafa",
    "category": "tsaqofah",
    "path": "tsaqofah/thariqul-iman/index.html",
    "icon": "target",
    "color": "orange"
  },
  {
    "title": "Qadha & Qadar",
    "description": "Rangkuman Bab 2 Nizham al-Islam Karya Syaikh Taqiyuddin An-Nabhani.",
    "author": "By. Abu Kafa",
    "category": "tsaqofah",
    "path": "tsaqofah/qadha-qadar/index.html",
    "icon": "zap",
    "color": "orange"
  },
  {
    "title": "Qiyadah Fikriyah",
    "description": "Rangkuman Bab 3 Nizham al-Islam Karya Syaikh Taqiyuddin An-Nabhani.",
    "author": "By. Abu Kafa",
    "category": "tsaqofah",
    "path": "tsaqofah/qiyadah-fikriyah/index.html",
    "icon": "brain-circuit",
    "color": "orange"
  },
  {
    "title": "Pengemban Dakwah",
    "description": "Rangkuman Bab 4 Nizham al-Islam Karya Syaikh Taqiyuddin An-Nabhani.",
    "author": "By. Abu Kafa",
    "category": "tsaqofah",
    "path": "tsaqofah/pengemban-dakwah/index.html",
    "icon": "message-circle-plus",
    "color": "orange"
  },
  {
    "title": "Hadhoroh Islam",
    "description": "Rangkuman Bab 5 Nizham al-Islam tentang konsep peradaban Islam dan penolakan terhadap sekularisme.",
    "author": "By. Abu Kafa",
    "category": "tsaqofah",
    "path": "tsaqofah/hadhoroh/index.html",
    "icon": "globe",
    "color": "orange"
  },
  {
    "title": "Peraturan Hidup",
    "description": "Rangkuman Bab 6 Nizham al-Islam tentang keteraturan seluruh dimensi hubungan dalam Islam.",
    "author": "By. Abu Kafa",
    "category": "tsaqofah",
    "path": "tsaqofah/peraturan-hidup/index.html",
    "icon": "gavel",
    "color": "orange"
  },
  {
    "title": "Hukum Syara'",
    "description": "Rangkuman Bab 7 Nizham al-Islam tentang hakikat seruan Pembuat Hukum dan lima hukum taklif.",
    "author": "By. Abu Kafa",
    "category": "tsaqofah",
    "path": "tsaqofah/hukum-syara/index.html",
    "icon": "scale",
    "color": "orange"
  },
  {
    "title": "Teladan Hidup",
    "description": "Rangkuman Bab 8 Nizham al-Islam tentang kedudukan perbuatan Rasulullah saw. dan adopsi hukum.",
    "author": "By. Abu Kafa",
    "category": "tsaqofah",
    "path": "tsaqofah/teladan-hidup/index.html",
    "icon": "users",
    "color": "orange"
  },
  {
    "title": "Prinsip Keuangan Islam",
    "description": "Dasar-dasar mengelola uang secara halal dan berkah dalam pandangan Islam.",
    "author": "By. Abu Kafa",
    "category": "muamalah",
    "path": "muamalah/prinsip-keuangan/index.html",
    "icon": "landmark",
    "color": "emerald"
  },
  {
    "title": "Jual Beli",
    "description": "Aturan dasar dalam berdagang agar transaksi sah dan saling menguntungkan.",
    "author": "By. Abu Kafa",
    "category": "muamalah",
    "path": "muamalah/jual-beli/index.html",
    "icon": "shopping-cart",
    "color": "emerald"
  },
  {
    "title": "Akad-Akad Muamalah",
    "description": "Mengenal berbagai jenis perjanjian dalam kerjasama ekonomi islami.",
    "author": "By. Abu Kafa",
    "category": "muamalah",
    "path": "muamalah/akad-akad/index.html",
    "icon": "scroll",
    "color": "emerald"
  },
  {
    "title": "Barang Ribawi",
    "description": "Daftar barang-barang yang memiliki aturan khusus dalam pertukarannya agar terhindar dari riba.",
    "author": "By. Abu Kafa",
    "category": "muamalah",
    "path": "muamalah/barang-ribawi/index.html",
    "icon": "package-search",
    "color": "emerald"
  },
  {
    "title": "Jenis-Jenis Riba",
    "description": "Waspada terhadap macam-macam riba dalam transaksi sehari-hari agar harta tetap bersih.",
    "author": "By. Abu Kafa",
    "category": "muamalah",
    "path": "muamalah/jenis-riba/index.html",
    "icon": "alert-triangle",
    "color": "emerald"
  },
  {
    "title": "Munakahat",
    "description": "Ilmu tentang membangun keluarga yang sakinah dan penuh tanggung jawab sosial.",
    "author": "By. Abu Kafa",
    "category": "muamalah",
    "path": "muamalah/munakahat/index.html",
    "icon": "heart-handshake",
    "color": "emerald"
  },
  {
    "title": "Mindset & Keputusan",
    "description": "Panduan berpikir jernih dan mengambil keputusan berdasarkan preferensi dan referensi.",
    "author": "By. Abu Kafa",
    "category": "self-development",
    "path": "self-development/mindset-keputusan/index.html",
    "icon": "brain",
    "color": "indigo"
  },
  {
    "title": "Filsafat & Logika",
    "description": "Belajar filsafat dan logika untuk berpikir kritis dan mengambil keputusan berdasarkan preferensi dan referensi.",
    "author": "By. Abu Kafa",
    "category": "self-development",
    "path": "self-development/filsafat-logika/index.html",
    "icon": "lightbulb",
    "color": "indigo"
  }
];
