import socket
import struct
import util


class UDPPunch:

	def __init__(self, addr):
		"""
		initialize the puncher
		:param addr: server's address (IP, PORT) tuple
		"""
		self.server_addr = addr
		self.addresses = dict()


	def get_addr(self, socket):
		"""
		get address of the socket
		:param socket: socket connection
		"""

		if socket in self.addresses:
			return self.addresses[socket]

		data = struct.pack(">B", 200)
		socket.sendto(data, self.server_addr)
		resp, addr = socket.recvfrom(6)
		return util.byte2ip(resp)


IP, PORT = "0.0.0.0", 8081
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((IP, PORT))

puncher = UDPPunch(("0.0.0.0", 5700))
print(puncher.get_addr(sock))



