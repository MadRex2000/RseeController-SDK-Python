# Rsee Light Controller SDK - Python Wrapper

This package provides a Python interface for the Rsee Light Controller SDK, allowing you to control your light controller using Python. This wrapper is specifically configured for the **PM-D-4TE/8TE series** controllers.

## Installation

To install the package, navigate to the root of this directory (`RseeController_SDK_Python`) and run the following command:

```bash
pip install .
```

This command will install the `rsee_controller` package into your Python environment. The necessary `RseeController.dll` is included in the package.

## Quick Start

Here is a basic example of how to import the library, connect to a controller via the network, and control a channel.

```python
from rsee_controller import RseeController
import time

# 1. Settings
IP_ADDRESS = "192.168.1.100"  # !!! Change to your controller's IP
PORT = 8899                   # !!! Change to your controller's port

# 2. Initialize Controller
print("Initializing Rsee Controller...")
try:
    controller = RseeController()
    print("Controller instance created.")
except Exception as e:
    print(f"Error creating controller: {e}")
    exit()

# 3. Connect, Control, and Disconnect
net_handle = 0
com_handle = 0 # Unused in network mode
try:
    # Connect via Network
    net_handle = controller.connect_net(IP_ADDRESS, PORT)
    if net_handle == 0:
        print("Failed to connect via network.")
    else:
        print(f"Successfully connected. Net Handle: {net_handle}")

        # Control a channel
        channel = 1
        brightness = 255
        print(f"Setting channel {channel} brightness to {brightness}")
        controller.pmd_8te_set_brightness(com_handle, net_handle, channel, brightness)
        time.sleep(0.5)

        read_value = controller.pmd_8te_read_brightness(com_handle, net_handle, channel)
        print(f"Read brightness from channel {channel}: {read_value}")

finally:
    # Disconnect
    if net_handle != 0:
        print("\nClosing network connection...")
        controller.close_net(net_handle)
        print("Connection closed.")
```

For a more detailed example, including how to use a serial port connection, see `examples/test_pmd_controller.py`.

## API Overview

The `RseeController` class provides high-level methods to interact with your controller.

### Connection

-   `connect_net(ip_address, port)`: Connect via Ethernet. Returns a `net_handle`.
-   `close_net(net_handle)`: Close the Ethernet connection.
-   `connect_serial(port_name, baud_rate)`: Connect via a serial port (e.g., `port_name="COM3"`). Returns a `com_handle`.
-   `close_serial(port_name, com_handle)`: Close the serial connection.

### PM-D-8TE Control

All control functions require both `com_handle` and `net_handle` to be passed as the first two arguments. The handle for the unused connection mode should be `0`.

-   `pmd_8te_set_brightness(com_handle, net_handle, channel, brightness)`
-   `pmd_8te_read_brightness(com_handle, net_handle, channel)`
-   `pmd_8te_set_pulse(com_handle, net_handle, channel, pulse_width)`
-   `pmd_8te_read_pulse(com_handle, net_handle, channel)`
-   `pmd_8te_set_onoff_mode(com_handle, net_handle, is_on)`
-   `pmd_8te_set_strobe_mode(com_handle, net_handle, is_strobe)`

For more details on the function parameters, please refer to the official programming manual (`编程手册V1.5.1.docx`).

## Project Structure

```
/RseeController_SDK_Python
├── /examples
│   └── test_pmd_controller.py  # Detailed example script
├── /rsee_controller
│   ├── __init__.py             # Makes the directory a Python package
│   ├── wrapper.py              # The main Python wrapper class
│   └── RseeController.dll      # The required 64-bit DLL
├── README.md                   # This documentation file
└── setup.py                    # Installation script
```