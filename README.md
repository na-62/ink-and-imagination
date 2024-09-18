Nama: Nafisa Arrasyida
NPM: 2306226391
Kelas: PBP E

Link PWS: http://nafisa-arrasyida-inkandimagination.pbp.cs.ui.ac.id/

Jawaban Tugas 3
1. Jelaskan mengapa kita memerlukan *data delivery* dalam pengimplementasian sebuah platform?
Data delivery diperlukan untuk bertukar data dari suatu komponen ke komponen lainnya. Biasanya suatu platform memiliki beberapa komponen, data delivery membuat komponen-komponen tersebut bisa bertukar data dengan benar dan efektif.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Saya lebih memilih json karena formatnya lebih ringkas, rapi, dan mudah dipahami. JSON lebih populer kemungkinan karena strukturnya tersebut dan kecepatan kinerjanya yang lebih baik daripada XML.

3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() dibutuhkan untuk memastikan semua yang masuk pada form sudah sesuai dan tidak ada masalah, agar pada tahap proses selanjutnya tidak ada kemungkinan eror yang muncul akibat isian form yang tidak valid.

4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
CSRF atau cross-site request forgery adalah bentuk serangan yang seolah-olah membuat pengguna merequest sesuatu pada website tanpa diketahuinya. csrf_token bermanfaat untuk memastikan request tersebut benar-benar dari pengguna yang sah. Jika tidak memakai csrf_token, penyerang akan dapat mengirim request atas nama pengguna tanpa sepengetahuan mereka.

5. Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).
- Checklist yang pertama adalah membuat form input untuk menambahkan objek model yang ada pada app, yaitu untuk menambahkan product. Dimulai dengan berkas baru dalam main, yang berisi class form tersebut, berisi dengan model dan fields yang akan ditanyakan pada form. Setelah itu membuat fungsi untuk  menampilkan form membuat product yang menerima request pada berkas views.py di main. Dalam berkas tersebut saya juga mengubah method show_main agar menampilkan form tersebut pada halaman utama. Setelah itu saya mengimport dan menambahkan path url form tersebut. Selanjutnya saya membuat berkas html untuk mengatur tampilan halaman form tersebut. Pada halaman main, saya menambahkan tombol untuk redirect ke halaman form untuk menambah produk dan tabel yang akan menampilkan daftar produk yang ada. Terakhir, saya melihat hasilnya di localhost:8000 setelah menjalankan server
- Checklist yang kedua adalah menambahkan 4 fungsi untuk melihat objek dalam format XML dan JSON, dengan filter id dan tidak. Fungsi-fungsi ini ditambahkan pada berkas views.py dalam direktori main. Pada berkas tersebut saya menambahkan import HttpResponse dan serializers lalu membuat fungsi show_xml, show_json, show_xml_by_id, dan show_json_by_id. masing-masing berisikan data semua objek product dan mereturn sebuah HttpResponse.
- Checklist yang ketiga adalah membuat routing URL untuk masing-masing views. routing tersebut saya lakukan pada berkas urls.py di main, dengan menambahkan import show_xml, show_json, show_xml_by_id, dan show_json_by_id, lalu menambahkan path ke fungsi masing-masing views pada urlpatterns. Kemudian saya mengecek hasilnya dengan membuka localhost:8000/xml ataupun json, diikuti dan tidak diikuti id produk setelah menjalankan server.
- Checklist berikutnya adalah mengisi readme dan menjawab pertanyaan-pertanyaan yang jawabannya bisa dilihat disini.
- Checklist berikutnya adalah mengakses keempat url views di poin 2 dengan postman, berikut saya cantumkan screenshotnya: 

    Screenshot Postman
    - XML view
    ![Alt text](images/xml_view.png)

    - JSON view
    ![Alt text](images/json_view.png)

    - XML by id
    ![Alt text](images/xml_by_id.png)

    - JSON by id
    ![Alt text](images/json_by_id.png)


===========================================================================

Jawaban Tugas 2
1. Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial). 
    - Pertama, dengan membuat proyek django, yang dilakukan dengan mengaktifkan environment, lalu membuat serta mendownload dependencies dalam berkas requirements.txt dan memulai project. 
    - Checklist yang kedua dan ketiga adalah membuat aplikasi main dan melakukan routing agar app tersebut bisa dijalankan, yang dilakukan dengan memulai app bernama main, dan mendaftarkan aplikasi tersebut ke dalam proyek dalam installed apps agar bisa dijalankan. 
    - Checklist yang selanjutnya adalah dengan membuat models pada app main, yang berisi suatu class 'Product' dengan beberapa atribut wajib. Ini dilakukan dengan mendaftarkan class Product dalam berkas models.py dalam direktori aplikasi main, beserta atribut-atribut yang diperlukan.
    - Selanjutnya adalah membuat fungsi dalam views.py yang mengembalikan nama app, juga nama dan kelas saya. Dalam berkas views.py pada main, saya membuat fungsi show_main untuk kemudian ditampilkan pada template html. dalam context saya mengisi nama aplikasi, nama saya, npm, dan kelas saya, lalu direturn ke 'main.html' jika ada request.
    - Setelah itu, saya melakukan routing URL dengan mengonfigurasi routing pada aplikasi main, dengan menambahkan fungsi show_main pada berkas urls.py dalam direktori main, dan mengonfigurasi routing proyek dengan menginclude main.urls pada berkas urls.py di direktori proyek.
    - Kemudian adalah checklist untuk deployment ke PWS. Saya melakukan deployment dengan membuat project baru di website PWS, menambahkan URL deployment pada allowed hosts, lalu mengikuti perintah deployment.
    - Checklist yang terakhir adalah mengisi Readme.md, dengan menjawab pertanyaan dan mencantumkan tautan aplikasi PWS.

2. Buatlah bagan yang berisi *request client* ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.

                                  http request                                    ________
       ____               ______               ____              ____            | Model  | (models.py)
     /      \           /        \           /      \          /      \   <----> |________|
    |  User  |  ---->  | Browser  |  ---->  |  URLS  |  ----> |  View  |          __________
     \      /           \        /           \      /          \      /   <----> | Template | (berkas .html)
       ----               ------               ----              ----            |__________|
                                             (urls.py)        (views.py)
                                                                   |
                                                                   V
                                                             http request

3. Jelaskan fungsi `git` dalam pengembangan perangkat lunak!
    git digunakan sebagai version control, yang bermanfaat untuk melacak dan megontrol perubahan versi kode dan untuk merging ataupun branching yang membantu kolaborasi antara developer.
    
4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    Menurut saya framework ini dipilih karena adanya MVT yang sangat membantu dalam mempelajari website development, terutama karena MVT memiliki struktur dan konsep yang jelas, sehingga pemula bisa mempelajari bagaimana sebuah aplikasi web bekerja secara terorganisir, terutama dalam pemisahan pekerjaan setiap bagian dari MVT. Selain itu, django juga memiliki banyak fitur bawaan yang memudahkan pemula untuk memahami konsep arsitektur web secara menyeluruh tanpa harus repot membuat semuanya dari nol.
    
5. Mengapa model pada Django disebut sebagai *ORM*?
    Model disebut ORM (Object-Relational Mapping) pada django karena model merupakan penghubung antara basis data dengan objek.