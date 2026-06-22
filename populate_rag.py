import os
import deeplake

# 1. Inisialisasi atau buka dataset DeepLake di VPS Anda
# Ganti path sesuai dengan lokasi dataset DeepLake Anda (bisa lokal atau cloud)
dataset_path = "/home/qwen-venice/obsidian-vault/my_deeplake_vector_db"
status_new = not os.path.exists(dataset_path)

if status_new:
    db = deeplake.empty(dataset_path)
    db.create_tensor('text', htype='text')
    db.create_tensor('metadata', htype='json')
else:
    db = deeplake.load(dataset_path)

# 2. Isi data RAG yang Anda minta
rag_content = (
    "Core Capabilities: Expert coder dengan kemampuan debug maksimal. "
    "Sangat andal dalam melakukan solve problem kompleks. "
    "Menggunakan metodologi dan cara pikir abductive/fable5 untuk pemecahan masalah mendalam. "
    "Bersifat uncensored untuk eksplorasi kode dan arsitektur maksimal tanpa batas batasan."
)

metadata = {"source": "system_core_instruction", "type": "agent_brain"}

# Masukkan ke dalam tensor DeepLake
db.text.append(rag_content)
db.metadata.append(metadata)

print("[-] Sukses memasukkan data ke DeepLake!")

# 3. OTOMATIS: Buat file catatan .md untuk Obsidian agar muncul di Graph View
obsidian_file_path = "/home/qwen-venice/obsidian-vault/rag-deeplake-brain.md"

obsidian_template = f"""# RAG DeepLake Brain Core

Catatan ini berisi data otak pintar yang berhasil di-index ke dalam database DeepLake untuk mengoptimalkan [[aider-bridge]] dan [[openclaw-bridge]].

## Isi Memori RAG:
* **Kemampuan:** Expert coder dengan kemampuan debug max dan penyelesaian masalah (*solve problem*).
* **Metode Berpikir:** Menggunakan cara pikir **fable5** untuk analisis sistem mendalam.
* **Sifat Agen:** Uncensored untuk eksplorasi teknologi dan kode secara maksimal.

---
*Log otomatis dibuat oleh skrip sinkronisasi DeepLake.*
"""

with open(obsidian_file_path, "w") as f:
    f.write(obsidian_template)

print(f"[-] Sukses membuat file log Obsidian di: {obsidian_file_path}")
print("[-] Menunggu sinkronisasi otomatis 5 menit ke Macbook Anda...")
