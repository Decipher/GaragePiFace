#!/usr/bin/env python

from garagepiface.server import Server

def main():
	garagepi = Server()
	garagepi.run()

if __name__ == "__main__":
	main()