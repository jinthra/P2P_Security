from torpy import TorClient

hostname = 'ifconfig.me'  # It's possible use onion hostname here as well
with TorClient() as tor:
    print("Starting...")
    # Choose random guard node and create 3-hops circuit
    with tor.create_circuit(3) as circuit:
        print("Creating circuit...")
        # Create tor stream to host
        with circuit.create_stream((hostname, 80)) as stream:
            "Created circuits..."
            # Now we can communicate with host
            stream.send(b'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % hostname.encode())
            recv = stream.recv(1024)
            test = recv.decode("utf-8")
            print("Receiving...")
            print(test)