import subprocess
import time

def check_network_connectivity():
  """Checks the network connectivity of the computer.

  Returns:
    True if the computer is connected to the network, False otherwise.
  """

  # Get the output of the `ping` command.
  output = subprocess.check_output(['ping', 'google.com'])

  # Check if the output contains the string "Reply from".
  if b'Reply from' in output:
    return True
  else:
    return False

def main():
  # Check the network connectivity.
  is_connected = check_network_connectivity()

  # If the computer is not connected to the network, print an error message.
  if not is_connected:
    print('The computer is not connected to the network.')
  else:
    print(subprocess.check_output(['ping', 'google.com']))

if __name__ == "__main__":
  main()