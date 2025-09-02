
import ctypes
import os
import platform

class RseeController:
    """
    Python wrapper for the RseeController.dll library, providing an interface
    to control various Rsee light controllers.
    """
    def __init__(self, dll_path=None):
        """
        Initializes the controller and loads the DLL.
        Args:
            dll_path (str, optional): The path to RseeController.dll. 
                                      If None, it searches within the package directory.
        """
        if dll_path is None:
            arch = platform.architecture()[0]
            if arch != '64bit':
                raise Exception("Unsupported architecture. Only 64-bit is supported.")
            
            # The DLL is expected to be in the same directory as this wrapper
            dll_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'RseeController.dll')

        if not os.path.exists(dll_path):
            raise FileNotFoundError(f"RseeController.dll not found at the specified path: {dll_path}")

        self.dll = ctypes.cdll.LoadLibrary(dll_path)
        self._define_functions()

    def _define_functions(self):
        """
        Defines the function prototypes (argtypes and restype) for all functions
        in the RseeController DLL.
        """
        # Helper types
        HANDLE = ctypes.c_void_p
        BOOL = ctypes.c_bool
        INT = ctypes.c_int
        UINT = ctypes.c_uint
        CHAR_P = ctypes.c_char_p
        
        # Generic Array Types
        self.INT_ARRAY_8 = INT * 8

        # Communication Functions
        self.dll.RseeController_OpenCom.argtypes = [CHAR_P, INT, BOOL]
        self.dll.RseeController_OpenCom.restype = HANDLE
        self.dll.RseeController_CloseCom.argtypes = [CHAR_P, HANDLE]
        self.dll.RseeController_CloseCom.restype = BOOL
        # Communication Functions based on the C# NPC Demo
        self.dll.RseeController_OpenCom.argtypes = [CHAR_P, INT, BOOL]
        self.dll.RseeController_OpenCom.restype = INT # Returns Com_Handle
        self.dll.RseeController_CloseCom.argtypes = [CHAR_P, INT]
        self.dll.RseeController_CloseCom.restype = BOOL
        self.dll.RseeController_ConnectNet.argtypes = [CHAR_P, INT]
        self.dll.RseeController_ConnectNet.restype = UINT # Returns Net_Handle
        self.dll.RseeController_CloseNet.argtypes = [UINT]
        self.dll.RseeController_CloseNet.restype = BOOL

        # DPS2 Series
        self.dll.RseeController_DPS2_SetChannel.argtypes = [HANDLE, INT, INT]
        self.dll.RseeController_DPS2_SetChannel.restype = INT
        self.dll.RseeController_DPS2_6T_Setting.argtypes = [HANDLE, INT, BOOL, INT, BOOL, INT, BOOL, INT, BOOL, INT, BOOL, INT, BOOL]
        self.dll.RseeController_DPS2_6T_Setting.restype = INT
        self.dll.RseeController_DPS2_8T_Setting.argtypes = [HANDLE, INT, BOOL, INT, BOOL, INT, BOOL, INT, BOOL, INT, BOOL, INT, BOOL, INT, BOOL, INT, BOOL]
        self.dll.RseeController_DPS2_8T_Setting.restype = INT
        self.dll.RseeController_DPS2_8TE_Setting.argtypes = [UINT, INT, BOOL, INT, BOOL, INT, BOOL, INT, BOOL, INT, BOOL, INT, BOOL, INT, BOOL, INT, BOOL]
        self.dll.RseeController_DPS2_8TE_Setting.restype = INT
        self.dll.RseeController_DPS2_ReadChannel.argtypes = [HANDLE, INT]
        self.dll.RseeController_DPS2_ReadChannel.restype = INT

        # DPS3 Series
        self.dll.RseeController_DPS3_BRTSetChannel.argtypes = [HANDLE, INT, INT]
        self.dll.RseeController_DPS3_BRTSetChannel.restype = INT
        self.dll.RseeController_DPS3_PLSSetChannel.argtypes = [HANDLE, INT, INT]
        self.dll.RseeController_DPS3_PLSSetChannel.restype = INT
        self.dll.RseeController_DPS3_BRTReadChannel.argtypes = [HANDLE, INT]
        self.dll.RseeController_DPS3_BRTReadChannel.restype = INT
        self.dll.RseeController_DPS3_PLSReadChannel.argtypes = [HANDLE, INT]
        self.dll.RseeController_DPS3_PLSReadChannel.restype = INT

        # PM-D Series
        self.dll.RseeController_PM_D_BRTSetChannel.argtypes = [HANDLE, INT, INT]
        self.dll.RseeController_PM_D_BRTSetChannel.restype = INT
        self.dll.RseeController_PM_D_BRTReadChannel.argtypes = [HANDLE, INT]
        self.dll.RseeController_PM_D_BRTReadChannel.restype = INT
        self.dll.RseeController_PM_D_PLSSetChannel.argtypes = [HANDLE, INT, INT]
        self.dll.RseeController_PM_D_PLSSetChannel.restype = INT
        self.dll.RseeController_PM_D_PLSReadChannel.argtypes = [HANDLE, INT]
        self.dll.RseeController_PM_D_PLSReadChannel.restype = INT
        self.dll.RseeController_PM_D_SetOnoff.argtypes = [HANDLE, BOOL]
        self.dll.RseeController_PM_D_SetOnoff.restype = INT
        self.dll.RseeController_PM_D_ChangeMode.argtypes = [HANDLE, BOOL]
        self.dll.RseeController_PM_D_ChangeMode.restype = INT

        # PM-D-8TE Series
        self.dll.RseeController_PM_D_8TE_BRTSetChannel.argtypes = [HANDLE, UINT, INT, INT]
        self.dll.RseeController_PM_D_8TE_BRTSetChannel.restype = INT
        self.dll.RseeController_PM_D_8TE_BRTSetAll.argtypes = [HANDLE, UINT, self.INT_ARRAY_8]
        self.dll.RseeController_PM_D_8TE_BRTSetAll.restype = INT
        self.dll.RseeController_PM_D_8TE_BRTReadChannel.argtypes = [HANDLE, UINT, INT]
        self.dll.RseeController_PM_D_8TE_BRTReadChannel.restype = INT
        self.dll.RseeController_PM_D_8TE_PLSSetChannel.argtypes = [HANDLE, UINT, INT, INT]
        self.dll.RseeController_PM_D_8TE_PLSSetChannel.restype = INT
        self.dll.RseeController_PM_D_8TE_PLSSetAll.argtypes = [HANDLE, UINT, self.INT_ARRAY_8]
        self.dll.RseeController_PM_D_8TE_PLSSetAll.restype = INT
        self.dll.RseeController_PM_D_8TE_PLSReadChannel.argtypes = [HANDLE, UINT, INT]
        self.dll.RseeController_PM_D_8TE_PLSReadChannel.restype = INT
        self.dll.RseeController_PM_D_8TE_SetIP.argtypes = [HANDLE, UINT, INT, INT, INT, INT, CHAR_P]
        self.dll.RseeController_PM_D_8TE_SetIP.restype = INT
        self.dll.RseeController_PM_D_8TE_SetPort.argtypes = [HANDLE, UINT, INT, CHAR_P]
        self.dll.RseeController_PM_D_8TE_SetPort.restype = INT
        self.dll.RseeController_PM_D_8TE_SetMac.argtypes = [HANDLE, UINT, INT, INT, INT, INT, INT, INT, CHAR_P]
        self.dll.RseeController_PM_D_8TE_SetMac.restype = INT
        self.dll.RseeController_PM_D_8TE_ChangeMode.argtypes = [HANDLE, UINT, INT]
        self.dll.RseeController_PM_D_8TE_ChangeMode.restype = INT
        self.dll.RseeController_PM_D_8TE_ReadInfo.argtypes = [HANDLE, UINT, CHAR_P]
        self.dll.RseeController_PM_D_8TE_ReadInfo.restype = INT

        # MDPS-24W75 Series
        self.dll.RseeController_MDPS_24W75_BRTSetChannel.argtypes = [HANDLE, INT, INT]
        self.dll.RseeController_MDPS_24W75_BRTSetChannel.restype = INT
        self.dll.RseeController_MDPS_24W75_PLSSetChannel.argtypes = [HANDLE, INT, INT]
        self.dll.RseeController_MDPS_24W75_PLSSetChannel.restype = INT
        self.dll.RseeController_MDPS_24W75_BRTReadChannel.argtypes = [HANDLE, INT]
        self.dll.RseeController_MDPS_24W75_BRTReadChannel.restype = INT
        self.dll.RseeController_MDPS_24W75_PLSReadChannel.argtypes = [HANDLE, INT]
        self.dll.RseeController_MDPS_24W75_PLSReadChannel.restype = INT
        self.dll.RseeController_MDPS_24W75_SetOnoff.argtypes = [HANDLE, BOOL]
        self.dll.RseeController_MDPS_24W75_SetOnoff.restype = INT
        self.dll.RseeController_MDPS_24W75_ChangeMode.argtypes = [HANDLE, BOOL]
        self.dll.RseeController_MDPS_24W75_ChangeMode.restype = INT

        # MDPS-24W96 Series
        self.dll.RseeController_MDPS_24W96_BRTSetChannel.argtypes = [HANDLE, INT, INT]
        self.dll.RseeController_MDPS_24W96_BRTSetChannel.restype = INT
        self.dll.RseeController_MDPS_24W96_PLSSetChannel.argtypes = [HANDLE, INT, INT]
        self.dll.RseeController_MDPS_24W96_PLSSetChannel.restype = INT
        self.dll.RseeController_MDPS_24W96_BRTReadChannel.argtypes = [HANDLE, INT]
        self.dll.RseeController_MDPS_24W96_BRTReadChannel.restype = INT
        self.dll.RseeController_MDPS_24W96_PLSReadChannel.argtypes = [HANDLE, INT]
        self.dll.RseeController_MDPS_24W96_PLSReadChannel.restype = INT
        self.dll.RseeController_MDPS_24W96_SetOnoff.argtypes = [HANDLE, BOOL]
        self.dll.RseeController_MDPS_24W96_SetOnoff.restype = INT
        self.dll.RseeController_MDPS_24W96_ChangeMode.argtypes = [HANDLE, BOOL]
        self.dll.RseeController_MDPS_24W96_ChangeMode.restype = INT

        # NPC Series
        self.dll.RseeController_NPC_SetChannel.argtypes = [HANDLE, UINT, INT, INT]
        self.dll.RseeController_NPC_SetChannel.restype = INT
        self.dll.RseeController_NPC_ReadChannel.argtypes = [HANDLE, UINT, INT]
        self.dll.RseeController_NPC_ReadChannel.restype = INT
        self.dll.RseeController_NPC_SetOnoff.argtypes = [HANDLE, UINT, INT, BOOL]
        self.dll.RseeController_NPC_SetOnoff.restype = INT

        # AHC Series
        self.dll.RseeController_AHC_SetChannel.argtypes = [HANDLE, INT, INT]
        self.dll.RseeController_AHC_SetChannel.restype = INT
        self.dll.RseeController_AHC_ReadChannel.argtypes = [HANDLE, INT]
        self.dll.RseeController_AHC_ReadChannel.restype = INT
        self.dll.RseeController_AHC_SetOnoff.argtypes = [HANDLE, BOOL]
        self.dll.RseeController_AHC_SetOnoff.restype = INT

        # PM-C Series
        self.dll.RseeController_PM_C_SetChannel.argtypes = [HANDLE, INT, INT]
        self.dll.RseeController_PM_C_SetChannel.restype = INT
        self.dll.RseeController_PM_C_ReadChannel.argtypes = [HANDLE, INT]
        self.dll.RseeController_PM_C_ReadChannel.restype = INT
        self.dll.RseeController_PM_C_SetOnoff.argtypes = [HANDLE, BOOL]
        self.dll.RseeController_PM_C_SetOnoff.restype = INT

        # SPS Series
        self.dll.RseeController_SPS_SetChannel.argtypes = [HANDLE, INT, INT]
        self.dll.RseeController_SPS_SetChannel.restype = INT
        self.dll.RseeController_SPS_ReadChannel.argtypes = [HANDLE, INT]
        self.dll.RseeController_SPS_ReadChannel.restype = INT
        self.dll.RseeController_SPS_SetMode.argtypes = [HANDLE, BOOL]
        self.dll.RseeController_SPS_SetMode.restype = INT
        self.dll.RseeController_SPS_SetInt.argtypes = [HANDLE, INT]
        self.dll.RseeController_SPS_SetInt.restype = INT
        self.dll.RseeController_SPS_ReadInt.argtypes = [HANDLE]
        self.dll.RseeController_SPS_ReadInt.restype = INT

        # PM-S Series
        self.dll.RseeController_PM_S_SetChannel.argtypes = [HANDLE, UINT, INT, INT]
        self.dll.RseeController_PM_S_SetChannel.restype = INT
        self.dll.RseeController_PM_S_SetInt.argtypes = [HANDLE, UINT, INT]
        self.dll.RseeController_PM_S_SetInt.restype = INT
        self.dll.RseeController_PM_S_SetMode.argtypes = [HANDLE, UINT, BOOL]
        self.dll.RseeController_PM_S_SetMode.restype = INT
        self.dll.RseeController_PM_S_ReadChannel.argtypes = [HANDLE, UINT, INT]
        self.dll.RseeController_PM_S_ReadChannel.restype = INT
        self.dll.RseeController_PM_S_ReadInt.argtypes = [HANDLE, UINT]
        self.dll.RseeController_PM_S_ReadInt.restype = INT

        # CPL-8T Series
        self.dll.RseeController_CPL_8T_SetChannel.argtypes = [UINT, INT, INT]
        self.dll.RseeController_CPL_8T_SetChannel.restype = INT
        self.dll.RseeController_CPL_8T_ReadChannel.argtypes = [UINT, INT]
        self.dll.RseeController_CPL_8T_ReadChannel.restype = INT
        self.dll.RseeController_CPL_8T_SetOnoff.argtypes = [UINT, BOOL]
        self.dll.RseeController_CPL_8T_SetOnoff.restype = INT
        self.dll.RseeController_CPL_8T_SetCurrent.argtypes = [UINT, INT, INT]
        self.dll.RseeController_CPL_8T_SetCurrent.restype = INT

    def _to_bytes(self, string):
        return string.encode('ascii')

    # --- Communication Methods ---
    def open_com(self, port_name, baud_rate=115200, overlapped=False):
        """Opens a serial port connection."""
        return self.dll.RseeController_OpenCom(self._to_bytes(port_name), baud_rate, overlapped)

    def close_com(self, port_name, com_handle):
        """Closes a serial port connection."""
        return self.dll.RseeController_CloseCom(self._to_bytes(port_name), com_handle)

    def connect_net(self, ip_address, port):
        """
        Establishes a network connection.
        Returns a non-zero handle on success.
        """
        return self.dll.RseeController_ConnectNet(self._to_bytes(ip_address), port)

    def close_net(self, net_handle):
        """Closes a network connection."""
        return self.dll.RseeController_CloseNet(net_handle)

    def connect_serial(self, port_name, baud_rate=19200, overlapped=True):
        """
        Establishes a serial connection.
        Args:
            port_name (str): The name of the COM port (e.g., "COM3").
        Returns a non-zero handle on success.
        """
        return self.dll.RseeController_OpenCom(self._to_bytes(port_name), baud_rate, overlapped)

    def close_serial(self, port_name, com_handle):
        """Closes a serial connection."""
        return self.dll.RseeController_CloseCom(self._to_bytes(port_name), com_handle)

    # --- DPS2 Series ---
    def dps2_set_channel(self, com_handle, channel, value):
        return self.dll.RseeController_DPS2_SetChannel(com_handle, channel, value)

    def dps2_6t_setting(self, com_handle, settings):
        """ settings: list of 6 tuples, each (range, onoff_bool) """
        args = [com_handle]
        for r, o in settings:
            args.extend([r, o])
        return self.dll.RseeController_DPS2_6T_Setting(*args)

    def dps2_8t_setting(self, com_handle, settings):
        """ settings: list of 8 tuples, each (range, onoff_bool) """
        args = [com_handle]
        for r, o in settings:
            args.extend([r, o])
        return self.dll.RseeController_DPS2_8T_Setting(*args)

    def dps2_8te_setting(self, socket_handle, settings):
        """ settings: list of 8 tuples, each (range, onoff_bool) """
        args = [socket_handle]
        for r, o in settings:
            args.extend([r, o])
        return self.dll.RseeController_DPS2_8TE_Setting(*args)

    def dps2_read_channel(self, com_handle, channel):
        return self.dll.RseeController_DPS2_ReadChannel(com_handle, channel)

    # --- DPS3 Series ---
    def dps3_brt_set_channel(self, com_handle, channel, value):
        return self.dll.RseeController_DPS3_BRTSetChannel(com_handle, channel, value)

    def dps3_pls_set_channel(self, com_handle, channel, time):
        return self.dll.RseeController_DPS3_PLSSetChannel(com_handle, channel, time)

    def dps3_brt_read_channel(self, com_handle, channel):
        return self.dll.RseeController_DPS3_BRTReadChannel(com_handle, channel)

    def dps3_pls_read_channel(self, com_handle, channel):
        return self.dll.RseeController_DPS3_PLSReadChannel(com_handle, channel)

    # --- PM-D Series ---
    def pmd_brt_set_channel(self, com_handle, channel, value):
        return self.dll.RseeController_PM_D_BRTSetChannel(com_handle, channel, value)

    def pmd_brt_read_channel(self, com_handle, channel):
        return self.dll.RseeController_PM_D_BRTReadChannel(com_handle, channel)

    def pmd_pls_set_channel(self, com_handle, channel, value):
        return self.dll.RseeController_PM_D_PLSSetChannel(com_handle, channel, value)

    def pmd_pls_read_channel(self, com_handle, channel):
        return self.dll.RseeController_PM_D_PLSReadChannel(com_handle, channel)

    def pmd_set_onoff(self, com_handle, state):
        return self.dll.RseeController_PM_D_SetOnoff(com_handle, state)

    def pmd_change_mode(self, com_handle, mode):
        return self.dll.RseeController_PM_D_ChangeMode(com_handle, mode)

    # --- PM-D-8TE Series ---
    def pmd_8te_brt_set_channel(self, socket_handle, channel, value, com_handle=None):
        return self.dll.RseeController_PM_D_8TE_BRTSetChannel(com_handle, socket_handle, channel, value)

    def pmd_8te_brt_set_all(self, socket_handle, values, com_handle=None):
        """ values: list of 8 integers """
        arr = self.INT_ARRAY_8(*values)
        return self.dll.RseeController_PM_D_8TE_BRTSetAll(com_handle, socket_handle, arr)

    def pmd_8te_brt_read_channel(self, socket_handle, channel, com_handle=None):
        return self.dll.RseeController_PM_D_8TE_BRTReadChannel(com_handle, socket_handle, channel)

    def pmd_8te_pls_set_channel(self, socket_handle, channel, time, com_handle=None):
        return self.dll.RseeController_PM_D_8TE_PLSSetChannel(com_handle, socket_handle, channel, time)

    def pmd_8te_pls_set_all(self, socket_handle, values, com_handle=None):
        """ values: list of 8 integers """
        arr = self.INT_ARRAY_8(*values)
        return self.dll.RseeController_PM_D_8TE_PLSSetAll(com_handle, socket_handle, arr)

    def pmd_8te_pls_read_channel(self, socket_handle, channel, com_handle=None):
        return self.dll.RseeController_PM_D_8TE_PLSReadChannel(com_handle, socket_handle, channel)

    def pmd_8te_set_ip(self, socket_handle, ip_parts, com_handle=None):
        """ ip_parts: list of 4 integers """
        buff = ctypes.create_string_buffer(1024)
        res = self.dll.RseeController_PM_D_8TE_SetIP(com_handle, socket_handle, *ip_parts, buff)
        return res, buff.value.decode('ascii', errors='ignore')

    def pmd_8te_set_port(self, socket_handle, port, com_handle=None):
        buff = ctypes.create_string_buffer(1024)
        res = self.dll.RseeController_PM_D_8TE_SetPort(com_handle, socket_handle, port, buff)
        return res, buff.value.decode('ascii', errors='ignore')

    def pmd_8te_set_mac(self, socket_handle, mac_parts, com_handle=None):
        """ mac_parts: list of 6 integers """
        buff = ctypes.create_string_buffer(1024)
        res = self.dll.RseeController_PM_D_8TE_SetMac(com_handle, socket_handle, *mac_parts, buff)
        return res, buff.value.decode('ascii', errors='ignore')

    def pmd_8te_change_mode(self, socket_handle, mode, com_handle=None):
        return self.dll.RseeController_PM_D_8TE_ChangeMode(com_handle, socket_handle, mode)

    def pmd_8te_read_info(self, socket_handle, com_handle=None):
        buff = ctypes.create_string_buffer(1024)
        res = self.dll.RseeController_PM_D_8TE_ReadInfo(com_handle, socket_handle, buff)
        return res, buff.value.decode('ascii', errors='ignore')

    # --- MDPS-24W75 Series ---
    def mdps_24w75_brt_set_channel(self, com_handle, channel, value):
        return self.dll.RseeController_MDPS_24W75_BRTSetChannel(com_handle, channel, value)

    def mdps_24w75_pls_set_channel(self, com_handle, channel, value):
        return self.dll.RseeController_MDPS_24W75_PLSSetChannel(com_handle, channel, value)

    def mdps_24w75_brt_read_channel(self, com_handle, channel):
        return self.dll.RseeController_MDPS_24W75_BRTReadChannel(com_handle, channel)

    def mdps_24w75_pls_read_channel(self, com_handle, channel):
        return self.dll.RseeController_MDPS_24W75_PLSReadChannel(com_handle, channel)

    def mdps_24w75_set_onoff(self, com_handle, state):
        return self.dll.RseeController_MDPS_24W75_SetOnoff(com_handle, state)

    def mdps_24w75_change_mode(self, com_handle, mode):
        return self.dll.RseeController_MDPS_24W75_ChangeMode(com_handle, mode)

    # --- MDPS-24W96 Series ---
    def mdps_24w96_brt_set_channel(self, com_handle, channel, value):
        return self.dll.RseeController_MDPS_24W96_BRTSetChannel(com_handle, channel, value)

    def mdps_24w96_pls_set_channel(self, com_handle, channel, value):
        return self.dll.RseeController_MDPS_24W96_PLSSetChannel(com_handle, channel, value)

    def mdps_24w96_brt_read_channel(self, com_handle, channel):
        return self.dll.RseeController_MDPS_24W96_BRTReadChannel(com_handle, channel)

    def mdps_24w96_pls_read_channel(self, com_handle, channel):
        return self.dll.RseeController_MDPS_24W96_PLSReadChannel(com_handle, channel)

    def mdps_24w96_set_onoff(self, com_handle, state):
        return self.dll.RseeController_MDPS_24W96_SetOnoff(com_handle, state)

    def mdps_24w96_change_mode(self, com_handle, mode):
        return self.dll.RseeController_MDPS_24W96_ChangeMode(com_handle, mode)

    # --- PM-D-8TE Series Methods ---
    def pmd_8te_set_brightness(self, com_handle, net_handle, channel, brightness):
        """Sets the brightness for a channel in constant light mode."""
        return self.dll.RseeController_PM_D_8TE_BRTSetChannel(com_handle, net_handle, channel, brightness)

    def pmd_8te_read_brightness(self, com_handle, net_handle, channel):
        """Reads the brightness for a channel in constant light mode."""
        return self.dll.RseeController_PM_D_8TE_BRTReadChannel(com_handle, net_handle, channel)

    def pmd_8te_set_pulse(self, com_handle, net_handle, channel, pulse_width):
        """Sets the pulse width for a channel in strobe mode."""
        return self.dll.RseeController_PM_D_8TE_PLSSetChannel(com_handle, net_handle, channel, pulse_width)

    def pmd_8te_read_pulse(self, com_handle, net_handle, channel):
        """Reads the pulse width for a channel in strobe mode."""
        return self.dll.RseeController_PM_D_8TE_PLSReadChannel(com_handle, net_handle, channel)

    def pmd_8te_set_onoff_mode(self, com_handle, net_handle, is_on):
        """Sets the overall output ON or OFF. 1=OFF, 2=ON."""
        mode = 2 if is_on else 1
        return self.dll.RseeController_PM_D_8TE_ChangeMode(com_handle, net_handle, mode)

    def pmd_8te_set_strobe_mode(self, com_handle, net_handle, is_strobe):
        """Sets the controller to constant light or strobe mode. 1=Constant, 2=Strobe."""
        mode = 2 if is_strobe else 1
        return self.dll.RseeController_PM_D_8TE_ChangeMode_New(com_handle, net_handle, mode)

    # --- AHC Series ---
    def ahc_set_channel(self, com_handle, channel, value):
        return self.dll.RseeController_AHC_SetChannel(com_handle, channel, value)

    def ahc_read_channel(self, com_handle, channel):
        return self.dll.RseeController_AHC_ReadChannel(com_handle, channel)

    def ahc_set_onoff(self, com_handle, mode):
        return self.dll.RseeController_AHC_SetOnoff(com_handle, mode)

    # --- PM-C Series ---
    def pmc_set_channel(self, com_handle, channel, value):
        return self.dll.RseeController_PM_C_SetChannel(com_handle, channel, value)

    def pmc_read_channel(self, com_handle, channel):
        return self.dll.RseeController_PM_C_ReadChannel(com_handle, channel)

    def pmc_set_onoff(self, com_handle, mode):
        return self.dll.RseeController_PM_C_SetOnoff(com_handle, mode)

    # --- SPS Series ---
    def sps_set_channel(self, com_handle, channel, value):
        return self.dll.RseeController_SPS_SetChannel(com_handle, channel, value)

    def sps_read_channel(self, com_handle, channel):
        return self.dll.RseeController_SPS_ReadChannel(com_handle, channel)

    def sps_set_mode(self, com_handle, mode):
        return self.dll.RseeController_SPS_SetMode(com_handle, mode)

    def sps_set_int(self, com_handle, time):
        return self.dll.RseeController_SPS_SetInt(com_handle, time)

    def sps_read_int(self, com_handle):
        return self.dll.RseeController_SPS_ReadInt(com_handle)

    # --- PM-S Series ---
    def pms_set_channel(self, socket_handle, channel, value, com_handle=None):
        return self.dll.RseeController_PM_S_SetChannel(com_handle, socket_handle, channel, value)

    def pms_set_int(self, socket_handle, value, com_handle=None):
        return self.dll.RseeController_PM_S_SetInt(com_handle, socket_handle, value)

    def pms_set_mode(self, socket_handle, mode, com_handle=None):
        return self.dll.RseeController_PM_S_SetMode(com_handle, socket_handle, mode)

    def pms_read_channel(self, socket_handle, channel, com_handle=None):
        return self.dll.RseeController_PM_S_ReadChannel(com_handle, socket_handle, channel)

    def pms_read_int(self, socket_handle, com_handle=None):
        return self.dll.RseeController_PM_S_ReadInt(com_handle, socket_handle)

    # --- CPL-8T Series ---
    def cpl_8t_set_channel(self, socket_handle, channel, value):
        return self.dll.RseeController_CPL_8T_SetChannel(socket_handle, channel, value)

    def cpl_8t_read_channel(self, socket_handle, channel):
        return self.dll.RseeController_CPL_8T_ReadChannel(socket_handle, channel)

    def cpl_8t_set_onoff(self, socket_handle, state):
        return self.dll.RseeController_CPL_8T_SetOnoff(socket_handle, state)

    def cpl_8t_set_current(self, socket_handle, channel, current):
        return self.dll.RseeController_CPL_8T_SetCurrent(socket_handle, channel, current)
