import os
import grpc
import user_pb2
import user_pb2_grpc

def run():
    # Ambil alamat server dari environment variable, default ke localhost jika dijalankan manual
    server_address = os.getenv('GRPC_SERVER', 'localhost:50051')
    print(f"Menghubungkan ke gRPC Server di {server_address}...")
    
    with grpc.insecure_channel(server_address) as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)
        response = stub.GetUserProfile(user_pb2.UserRequest(user_id=1))
        print(f"Nama: {response.name}")
        print(f"Email: {response.email}")
        print(f"Telepon: {response.phone}")

if __name__ == '__main__':
    run()