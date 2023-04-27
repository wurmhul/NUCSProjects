import socket

def scan_for_open_ports(ip_address):
  """Scans the specified IP address for open ports.

  Args:
    ip_address: The IP address to scan.

  Returns:
    A list of open ports.
  """

  # Create a socket.
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Try to connect to port 80.
  try:
    sock.connect((ip_address, 80))
    print('Port 80 is open.')
    return [80]
  except socket.error:
    pass

  # Try to connect to port 443.
  try:
    sock.connect((ip_address, 443))
    print('Port 443 is open.')
    return [443]
  except socket.error:
    pass

  # No ports are open.
  print('No ports are open.')
  return []

if __name__ == "__main__":
  # Scan for open ports on Google.
  open_ports = scan_for_open_ports('https://www.google.com')

  # Print the open ports.
  if open_ports:
    print('The following ports are open: {}'.format(', '.join(open_ports)))
  else:
    print('No ports are open.')