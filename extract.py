import html
from html.parser import HTMLParser
import http.server
import socketserver
import urllib.request
import urllib.parse
import json
import re
import os
import ssl

PORT = 8000

# HTML parser class to strip code and keep human-readable text
class WebTextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_blocks = []
        self.ignore_tags = {
            'script', 'style', 'head', 'title', 'meta', 'link', 
            'svg', 'path', 'g', 'canvas', 'noscript', 'iframe'
        }
        self.tag_stack = []

    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag.lower())

    def handle_endtag(self, tag):
        if self.tag_stack:
            t = tag.lower()
            if t in self.tag_stack:
                while self.tag_stack:
                    popped = self.tag_stack.pop()
                    if popped == t:
                        break

    def handle_data(self, data):
        if any(ignored in self.tag_stack for ignored in self.ignore_tags):
            return
        
        cleaned = html.unescape(data).strip()
        if cleaned:
            self.text_blocks.append(cleaned)

# Beautiful UI Template
def get_ui_html():
    return """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Text Extractor Pro</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Outfit', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body {
            background-color: #030712;
            font-family: 'Outfit', sans-serif;
        }
        .glow-indigo {
            box-shadow: 0 0 50px -10px rgba(99, 102, 241, 0.3);
        }
        .glass {
            background: rgba(17, 24, 39, 0.7);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        /* Custom modern scrollbar to replace rigid default scrollbar */
        .custom-scrollbar::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
            background: rgba(15, 23, 42, 0.4);
            border-radius: 9999px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
            background: rgba(99, 102, 241, 0.3);
            border-radius: 9999px;
            border: 2px solid transparent;
            background-clip: padding-box;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
            background: rgba(99, 102, 241, 0.6);
            border: 2px solid transparent;
            background-clip: padding-box;
        }
    </style>
</head>
<body class="text-slate-100 min-h-screen flex flex-col justify-between overflow-x-hidden relative">
    <!-- Gradient Blobs -->
    <div class="absolute top-[-20%] left-[-10%] w-[50vw] h-[50vw] rounded-full bg-indigo-500/10 blur-[120px] pointer-events-none"></div>
    <div class="absolute bottom-[-20%] right-[-10%] w-[50vw] h-[50vw] rounded-full bg-rose-500/10 blur-[120px] pointer-events-none"></div>

    <!-- Main Container -->
    <main class="flex-grow flex items-center justify-center p-4 md:p-8 relative z-10">
        <div class="max-w-2xl w-full glass rounded-3xl p-6 md:p-10 glow-indigo transition-all duration-300">
            <!-- Header -->
            <div class="text-center mb-8">
                <div class="w-16 h-16 bg-gradient-to-tr from-indigo-500 to-violet-600 rounded-2xl flex items-center justify-center mx-auto mb-4 shadow-lg shadow-indigo-500/30">
                    <i class="fa-solid fa-wand-magic-sparkles text-white text-2xl"></i>
                </div>
                <h1 class="text-3xl md:text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-white via-slate-100 to-indigo-300 tracking-tight">
                    Web Text Extractor Pro
                </h1>
                <p class="text-sm text-slate-400 mt-2">
                    Ekstrak teks bersih dari URL apa saja secara instan dan unduh hasilnya ke komputer Anda.
                </p>
            </div>

            <!-- Input Form -->
            <div class="space-y-6">
                <div class="relative">
                    <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none text-slate-500">
                        <i class="fa-solid fa-link"></i>
                    </div>
                    <input type="url" id="urlInput" placeholder="Masukkan URL lengkap (contoh: https://example.com)..." 
                           class="w-full pl-11 pr-4 py-4 bg-slate-950/60 border border-slate-800 rounded-2xl focus:outline-none focus:border-indigo-500 text-slate-100 placeholder-slate-500 text-sm transition duration-300">
                </div>

                <button id="extractBtn" onclick="performExtraction()" 
                        class="w-full py-4 bg-gradient-to-r from-indigo-500 to-violet-600 hover:from-indigo-600 hover:to-violet-750 text-white font-semibold text-sm rounded-2xl transition duration-300 flex items-center justify-center gap-2 shadow-lg shadow-indigo-500/20 active:scale-[0.98]">
                    <i class="fa-solid fa-file-export"></i>
                    <span>Extract to TXT</span>
                </button>
            </div>

            <!-- Loading State -->
            <div id="loadingState" class="hidden mt-8 text-center space-y-4">
                <div class="inline-block animate-spin w-8 h-8 border-4 border-indigo-500 border-t-transparent rounded-full"></div>
                <p class="text-xs text-slate-400" id="loadingText">Menghubungi server dan mengunduh konten web...</p>
            </div>

            <!-- Success State -->
            <div id="resultState" class="hidden mt-8 space-y-6 animate-fade-in">
                <div class="h-[1px] bg-slate-800 w-full"></div>
                
                <div class="flex items-center justify-between">
                    <span class="text-xs uppercase font-extrabold text-emerald-400 tracking-wider flex items-center gap-1.5">
                        <i class="fa-solid fa-circle-check"></i> Ekstraksi Berhasil
                    </span>
                    <div class="flex gap-3 text-xs text-slate-400">
                        <span><strong id="charCount" class="text-slate-200">0</strong> Karakter</span>
                        <span>•</span>
                        <span><strong id="wordCount" class="text-slate-200">0</strong> Kata</span>
                    </div>
                </div>

                <!-- Preview Area -->
                <div class="space-y-2">
                    <div class="flex justify-between items-center">
                        <span class="text-xs font-bold text-slate-400">Hasil Ekstraksi (Dapat Diedit)</span>
                        <button onclick="downloadClientSide()" class="text-xs text-indigo-400 hover:text-indigo-300 flex items-center gap-1.5 transition">
                            <i class="fa-solid fa-download"></i> Unduh File via Browser
                        </button>
                    </div>
                    <textarea id="previewArea" class="w-full bg-slate-950/80 border border-slate-850 rounded-2xl p-4 h-80 text-xs font-mono text-slate-300 leading-relaxed focus:outline-none focus:border-indigo-500 custom-scrollbar resize-y select-text whitespace-pre-wrap" placeholder="Hasil ekstraksi teks akan muncul di sini..."></textarea>
                </div>
            </div>

            <!-- Error State -->
            <div id="errorState" class="hidden mt-8 bg-red-950/20 border border-red-500/30 rounded-2xl p-4 flex gap-3 animate-fade-in">
                <div class="text-red-400 text-lg"><i class="fa-solid fa-triangle-exclamation"></i></div>
                <div class="text-xs leading-relaxed text-slate-350">
                    <strong class="text-red-400">Error Ekstraksi:</strong><br>
                    <span id="errorMessage">Gagal memuat URL. Silakan periksa kembali tautan Anda.</span>
                </div>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="py-6 text-center text-xs text-slate-600 border-t border-slate-950 relative z-10">
        <p>© 2026 Web Text Extractor Pro • Berjalan Secara Lokal</p>
    </footer>

    <script>
        let extractedText = '';

        async function performExtraction() {
            const urlInput = document.getElementById('urlInput').value.trim();
            const extractBtn = document.getElementById('extractBtn');
            const loadingState = document.getElementById('loadingState');
            const resultState = document.getElementById('resultState');
            const errorState = document.getElementById('errorState');

            if (!urlInput) {
                showError("URL tidak boleh kosong. Harap masukkan tautan web.");
                return;
            }

            // Hide states
            resultState.classList.add('hidden');
            errorState.classList.add('hidden');
            
            // Show loading
            loadingState.classList.remove('hidden');
            extractBtn.disabled = true;
            extractBtn.classList.add('opacity-50', 'cursor-not-allowed');

            try {
                const response = await fetch('/extract', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ url: urlInput })
                });

                const data = await response.json();

                if (response.ok && data.status === 'success') {
                    // Show success
                    document.getElementById('charCount').textContent = data.char_count.toLocaleString();
                    document.getElementById('wordCount').textContent = data.word_count.toLocaleString();
                    document.getElementById('previewArea').value = data.text;
                    extractedText = data.text;

                    resultState.classList.remove('hidden');
                } else {
                    showError(data.message || "Gagal melakukan ekstraksi teks.");
                }
            } catch (err) {
                showError("Terjadi kesalahan jaringan: " + err.message);
            } finally {
                loadingState.classList.add('hidden');
                extractBtn.disabled = false;
                extractBtn.classList.remove('opacity-50', 'cursor-not-allowed');
            }
        }

        function showError(msg) {
            document.getElementById('errorMessage').textContent = msg;
            document.getElementById('errorState').classList.remove('hidden');
            document.getElementById('resultState').classList.add('hidden');
        }

        function downloadClientSide() {
            if (!extractedText) return;
            const blob = new Blob([extractedText], { type: 'text/plain;charset=utf-8' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'extract.txt';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }
    </script>
</body>
</html>"""

class ExtractorServer(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Silence default logger to keep terminal output clean
        pass

    def do_GET(self):
        if self.path in ('/', '/index.html', ''):
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(get_ui_html().encode('utf-8'))
        else:
            # Fallback for assets or standard static file serving
            super().do_GET()

    def do_POST(self):
        if self.path == '/extract':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                params = json.loads(post_data.decode('utf-8'))
                url = params.get('url', '').strip()
                
                if not url:
                    self.send_error_response("URL tidak boleh kosong.")
                    return

                if not (url.startswith('http://') or url.startswith('https://')):
                    url = 'https://' + url

                # Fetch web page content
                req = urllib.request.Request(
                    url,
                    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
                )
                
                # Bypassing self-signed certificates or SSL issues
                ctx = ssl._create_unverified_context()
                
                with urllib.request.urlopen(req, context=ctx, timeout=15) as response:
                    charset = response.headers.get_content_charset() or 'utf-8'
                    html_content = response.read().decode(charset, errors='ignore')

                # Parse text
                parser = WebTextParser()
                parser.feed(html_content)
                text_content = "\n\n".join(parser.text_blocks)
                
                # Cleanup excessive whitespaces/newlines
                text_content = re.sub(r'\n{3,}', '\n\n', text_content)

                response_data = {
                    'status': 'success',
                    'message': 'Ekstraksi berhasil!',
                    'char_count': len(text_content),
                    'word_count': len(text_content.split()),
                    'text': text_content
                }
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response_data).encode('utf-8'))

            except Exception as e:
                self.send_error_response(f"Terjadi kesalahan saat mengunduh halaman: {str(e)}")

    def send_error_response(self, message):
        self.send_response(400)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'status': 'error', 'message': message}).encode('utf-8'))

def run_server():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), ExtractorServer) as httpd:
        print(f"\n=======================================================")
        print(f" Web Text Extractor Pro Server Aktif!")
        print(f" Silakan buka di browser: http://localhost:{PORT}")
        print(f" Tekan Ctrl+C di terminal ini untuk mematikan server")
        print(f"=======================================================\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer dihentikan.")

if __name__ == '__main__':
    run_server()
