import socket
import struct
import cv2

SERVER_IP = '192.168.1.42'  # Replace with your Raspberry Pi's IP
PORT = 5000

def send_image(sock, path):
    img = cv2.imread(path)
    _, img_encoded = cv2.imencode('.jpg', img)
    data = img_encoded.tobytes()
    # Send the length (4 bytes) then the image data
    sock.sendall(struct.pack('!I', len(data)))
    sock.sendall(data)
    print(f"Sent {path} ({len(data)} bytes)")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((SERVER_IP, PORT))
        send_image(sock, 'image1.jpg')
        send_image(sock, 'image2.jpg')

if __name__ == '__main__':
    main()
