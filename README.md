Nama: Nafisa Arrasyida
NPM: 2306226391
Kelas: PBP E

Link PWS: http://nafisa-arrasyida-inkandimagination.pbp.cs.ui.ac.id/

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