import socket
import struct
import cv2
import numpy as np

# Configuration
HOST = ''  # Empty string means listen on all available interfaces
PORT = 5000  # You can choose any open port

def recv_all(sock, length):
    """Receive exactly 'length' bytes from the socket."""
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError("Socket closed before receiving all data.")
        data += more
    return data

def receive_image(sock):
    """Receive a single image."""
    # First receive the 4-byte size prefix (unsigned long)
    data_len = struct.unpack('!I', recv_all(sock, 4))[0]
    print(f"Receiving image of {data_len} bytes...")
    # Then receive the actual image bytes
    image_data = recv_all(sock, data_len)
    # Decode image bytes into a numpy array
    image = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)
    return image

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"Listening for connections on port {PORT}...")

        conn, addr = s.accept()
        print(f"Connection established from {addr}")

        with conn:
            for i in range(2):
                print(f"Waiting for image {i+1}/2...")
                img = receive_image(conn)
                if img is not None:
                    cv2.imshow(f"Image {i+1}", img)
                    cv2.waitKey(1000)  # Show each for 1 second
                else:
                    print("Failed to decode image.")

        print("Done. Closing.")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
