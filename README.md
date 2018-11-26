# profiling
Profiling for Instagram Caption.

Kebutuhan:
1. Python versi 3.x
2. Python Library Pandas. Cara install: "pip install pandas" (https://pandas.pydata.org/)
3. convo.csv (berisi tentang user, post, dan caption)
4. lib2.csv (berisi keyword dan interest)


Pengaturan untuk "lib2.csv":
1. Pastikan Header untuk keyword adalah "keywords"
2. Pastikan Header untuk kategori/interest adalah "interest"
3. Simbol ",/() akan dihapus dari keyword
4. Keyword tidak case sensitive
5. Keyword tidak bisa menegnali apabila ada typo (salah ketik). Pastikan Keyword sudah benar
6. Pastikan interest nya adalah salah satu dari "Music", "Culinary", "Traveling", dan "Fashion"

Pengaturan untuk "convo.csv":
1. Pastikan Header untuk username adalah "username"
2. Pastikan Header untuk caption adalah "caption"
3. Pastikan Header untuk jumlah like adalah "like_count"
4. Pastikan Header untuk jumlah komen adalah "comment_count"
5. Simbol , dan \u yang ada di caption akan dihapus


Tata cara penggunaan:
1. Pastikan "Kebutuhan" sudah disiapkan
2. Pastikan pengaturan untuk lib2.csv dan convo.csv sudah benar, dan berada dalam satu folder dengan skrip.
3. Jalankan skrip "kol2.py". Bisa lewat CMD bisa langsung.
4. Tunggu sampai prosesnya selesai. Akan ada 3 file output.

Output:
1. tb_convo_count_percent.csv (berisi tentang masing-masing convo/caption dengan persentase interest nya)
2. tb_pivot_percent.csv (berisi tentang username dengan total percent interest nya, bisa dimasukan sebagai input Power BI)
3. tb_user_statistics.csv (berisi tentang jumlah post*, komen*, follower, dan following setiap akun)
*dihitung berdasarkan data dari convo.csv

Menambahkan keyword:
1. Tambahkan langsung kedalam lib2.csv
