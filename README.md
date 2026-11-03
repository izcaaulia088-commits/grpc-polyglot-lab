# gRPC Polyglot Lab

## Menjalankan Proyek dengan Docker

### 1. Persiapan

Pastikan aplikasi berikut sudah terinstal:
- Docker Desktop
- Git

Jalankan Docker Desktop sebelum memulai proses.

### 2. Clone Repository

Download project dari GitHub:

```bash
git clone https://github.com/masyitahhusnul2-ux/grpc-polyglot-lab.git
```

Masuk ke folder proyek:

```bash
cd grpc-polyglot-lab
```

### 3. Build Docker Image

Buat image untuk masing-masing aplikasi:

```bash
docker build -f Dockerfile.server -t grpc-go-server .
docker build -f Dockerfile.node -t grpc-node-client .
docker build -f Dockerfile.python -t grpc-python-client .
```

Periksa image yang berhasil dibuat:

```bash
docker images
```

### 4. Membuat Docker Network

Buat jaringan untuk menghubungkan server dan client:

```bash
docker network create grpc-network
```

### 5. Menjalankan Go Server

Aktifkan server dengan perintah:

```bash
docker run -d --name grpc-go-server --network grpc-network grpc-go-server
```

Periksa apakah server berjalan:

```bash
docker logs grpc-go-server
```

### 6. Menjalankan Node.js Client

Lakukan pengujian menggunakan client Node.js:

```bash
docker run --rm --network grpc-network -e GRPC_SERVER=grpc-go-server:50051 grpc-node-client
```

### 7. Menjalankan Python Client

Selanjutnya, jalankan client Python:

```bash
docker run --rm --network grpc-network -e GRPC_SERVER=grpc-go-server:50051 grpc-python-client
```

### 8. Hasil Pengujian

Setelah client berhasil dijalankan, diperoleh hasil output sebagai berikut:

```text
Menghubungkan ke gRPC Server di grpc-go-server:50051...
Nama: izca aulia dewi
Email: izca_aulia088@student.pnl.ac.id
Telepon: 081234567890
```

Hasil tersebut menunjukkan bahwa client berhasil terhubung dengan Go Server dan menerima data pengguna melalui komunikasi gRPC.

Dengan demikian, komunikasi antara server Go dan client Python berhasil dilakukan menggunakan kontrak protokol `user.proto`.

### 9. Menghentikan Server

Setelah pengujian selesai, hentikan server menggunakan perintah:

```bash
docker stop grpc-go-server
```

Untuk menjalankannya kembali:

```bash
docker start grpc-go-server
```

---

**Catatan:** Seluruh komponen menggunakan Docker Image masing-masing dan terhubung melalui `grpc-network` dengan port komunikasi gRPC `50051`.