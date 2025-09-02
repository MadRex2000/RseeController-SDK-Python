from rsee_controller import RseeController
import time

def main():
    """
    Example for controlling a PM-D-4TE/8TE series controller.
    """
    # --- Connection Settings ---
    # Choose your connection mode: 'net' or 'serial'
    CONNECTION_MODE = 'net'

    # Network settings (if CONNECTION_MODE is 'net')
    IP_ADDRESS = "192.168.1.100"  # !!! Change to your controller's IP
    PORT = 8899                   # !!! Change to your controller's port

    # Serial port settings (if CONNECTION_MODE is 'serial')
    COM_PORT_NAME = "COM3"  # !!! Change to your controller's COM port name
    BAUD_RATE = 19200

    print(f"Initializing Rsee Controller for PM-D-8TE (mode: {CONNECTION_MODE})...")
    try:
        controller = RseeController()
        print("Controller instance created.")
    except Exception as e:
        print(f"Error creating controller: {e}")
        return

    net_handle = 0
    com_handle = 0
    try:
        # --- Connect ---
        if CONNECTION_MODE == 'net':
            print(f"\nConnecting to {IP_ADDRESS}:{PORT}...")
            net_handle = controller.connect_net(IP_ADDRESS, PORT)
            if net_handle == 0:
                print("Failed to connect via network.")
                return
            print(f"Successfully connected. Net Handle: {net_handle}")
        elif CONNECTION_MODE == 'serial':
            print(f"\nConnecting to {COM_PORT_NAME}...")
            com_handle = controller.connect_serial(COM_PORT_NAME, BAUD_RATE)
            if com_handle == 0:
                print("Failed to connect via serial port.")
                return
            print(f"Successfully connected. COM Handle: {com_handle}")
        else:
            print(f"Invalid CONNECTION_MODE: {CONNECTION_MODE}")
            return

        # --- Control Example ---
        channel = 1
        print(f"\n--- Controlling Channel {channel} ---")

        # Set controller to constant light mode
        print("Setting mode to Constant Light")
        controller.pmd_8te_set_strobe_mode(com_handle, net_handle, is_strobe=False)
        time.sleep(0.2)

        # Turn on the light output
        print("Turning light output ON")
        controller.pmd_8te_set_onoff_mode(com_handle, net_handle, is_on=True)
        time.sleep(0.2)

        # Set brightness to 255
        brightness = 255
        print(f"Setting channel {channel} brightness to {brightness}")
        controller.pmd_8te_set_brightness(com_handle, net_handle, channel, brightness)
        time.sleep(0.5)

        # Read brightness
        read_value = controller.pmd_8te_read_brightness(com_handle, net_handle, channel)
        print(f"Read brightness from channel {channel}: {read_value}")
        time.sleep(0.2)

        # Set brightness to 100
        brightness = 100
        print(f"Setting channel {channel} brightness to {brightness}")
        controller.pmd_8te_set_brightness(com_handle, net_handle, channel, brightness)
        time.sleep(0.5)

        # Read brightness again
        read_value = controller.pmd_8te_read_brightness(com_handle, net_handle, channel)
        print(f"Read brightness from channel {channel}: {read_value}")

    finally:
        # --- Disconnect ---
        print("\nClosing connection...")
        if net_handle != 0:
            controller.close_net(net_handle)
            print("Network connection closed.")
        if com_handle != 0:
            controller.close_serial(COM_PORT_NAME, com_handle)
            print("Serial connection closed.")

if __name__ == "__main__":
    main()
