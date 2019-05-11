import socket
import util
import struct


def process_call(sock):
	msg, addr = sock.recvfrom(1)
	if struct.unpack(">B", msg)[0] != 200:
		return;

	addr_str = f"{addr[0]}:{addr[1]}"
	addr_bin = util.ip2byte(addr_str)
	sock.sendto(addr_bin, addr)


def main():

	IP, PORT = "0.0.0.0", 5700
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((IP, PORT))

	print(f"Running udp server {IP}:{PORT}")
	while True:
		process_call(sock)


if __name__ == '__main__':
	main()