from pipython import GCSDevice, pitools, GCS2Commands

class Stepper:
    """Represents an axis connected to a PI controller.

    This class provides methods for connecting to and controlling the axis, 
    including referencing the stage to a known position, moving the stage, 
    querying the position, and configuring the output trigger.

    Parameters
    ----------
    controller_ID : str
        The ID of the PI controller to connect to.
    axis_ID : str
        The ID of the axis to control.

    Attributes
    ----------
    pidevice : GCSDevice
        The underlying PI device object.
    controller_ID : str
        The ID of the PI controller this axis is connected to.
    axis_ID : str
        The ID of this axis.
    """

    def __init__(self, controller_id, axis_id):
        """Initializes the StepperChain class.

        Parameters:
        ----------
        controller_id (str): The ID of the controller.
        axis_id (int): The ID of the axis.
        """
        self.controller_id = controller_id
        self.pidevice = GCSDevice(devname=self.controller_id)
        self.axis_id = axis_id
    
    def usb_plugged_devices(self):
        """
        Returns a list with the devices plugged through USB.
        
        Returns:
        --------
        A list object with the indeces of the connected devices
        """
        return self.pidevice.EnumerateUSB(mask=self.controller_id)
    
    def connect_pidevice(self):
        """
        Finds the plugged devices, activates the I/O interface to select the device of interest and 
        eventually connects to the selected device.        
        """
        devices = self.usb_plugged_devices()
        if not devices:
            raise Exception("There are no plugged devices! Please connect at least one device.")

        selected_device = self.select_device(devices)
        self.startup_USB_device(selected_device)

    def select_device(self, devices):
        """
        Displays the list of devices and prompts the user to select one.
        
        Parameters
        ----------
        devices : list
            List object with the connected devices (as strings)
        
        Returns:
        --------
        A string object with the name of the pi device to be connected.
        """            
        print('Number ---- Device')
        for i, device in enumerate(devices):
            print(f'{i}      ----  {device}')

        item = int(input('Input the index of the device to connect: '))
        return devices[item]

    def startup_USB_device(self, device):
        """
        Connects to the specified device.
        
        Parameters
        ----------
        device : str
            A string object with the name of the pi device to be connected.
        """
        self.pidevice.ConnectUSB(device)
        pitools.startup(self.pidevice, self.axis_id)
        
    def move_stage_to_ref(self, refmode):
        """
        Moves the selected controller towards the reference position.
        
        Parameters
        ----------
        refmode : str
            String defining the referencing position.
        """
        if refmode == 'FNL':
            print("Moving stage towards negative edge...")
            self.pidevice.FNL()
        elif refmode == 'FPL':
            print("Moving stage towards positive edge...")
            self.pidevice.FPL()
        pitools.waitontarget(self.pidevice)
        print(f"Stage: {GCS2Commands.qCST(self.pidevice)['1']} successfully referenced.")
    
    def get_curr_pos(self):
        """
        Returns the current position of the axis
        
        Returns
        --------
        A float object with the current position of the stage

        """
        return self.pidevice.qPOS('1')

    def set_velocity(self,velocity):
        """ 
        Set the velocity of motion in the ROM of the controller
        
        Parameters
        ----------
        velocity : float
            Float defining the velocity of motion
        """
        self.pidevice.VEL('1',velocity)

    def set_acceleration(self,acceleration):
        """ 
        Set the acceleration of motion in the ROM of the controller
        
        Parameters
        ----------
        acceleration : float
            Float defining the acceleration of motion
        """
        self.pidevice.ACC('1',acceleration)
    
    def set_deceleration(self,deceleration):
        """ 
        Set the deceleration of motion in the ROM of the controller
        
        Parameters
        ----------
        deceleration : float
            Float defining the deceleration of motion
        """
        self.pidevice.DEC('1',deceleration)
        
    def get_velocity(self):
        """ 
        Get and returns the velocity of the device
        
        Returns
        ----------
        velocity : float
            Float defining the velocity of motion
        """
        velocity = GCS2Commands.qVEL(self.pidevice)['1']
        return velocity

    def get_acceleration(self):
        """
        Gets and returns the acceleration of the device
               
        Returns
        --------
        A float object defining the acceleration of motion
        """
        acceleration = GCS2Commands.qACC(self.pidevice)['1']
        return acceleration

        
    def move_stage_to_target(self,target):
        """ 
        Moves the device to target position
        
        Parameters
        ----------
        target : float
            Float defining the target position
        """
        self.pidevice.MOV(self.pidevice.axes,target)
        pitools.waitontarget(self.pidevice)

    def enable_out_trigger(self, trigger_type):
        """Configures and activate the output trigger for a given axis.
        
        Parameters
        ----------
        trigger_type : int
            Type of trigger to be output (6 == in Motion, 1 = Line trigger).
        """
        self.pidevice.CTO(1, 2, 1)
        self.pidevice.CTO(1, 3, trigger_type)
        # enable trigger output with the configuration defined above
        self.pidevice.TRO(1, True)
        
    def disable_out_trigger(self, trigger_type):
        """Configures and disable the output trigger for a given axis.
        
        Parameters
        ----------
        trigger_type : int
            Type of trigger to be output (6 == in Motion, 1 = Line trigger).
        """
        self.pidevice.CTO(1, 2, 1)
        self.pidevice.CTO(1, 3, trigger_type)
        # disable trigger output with the configuration defined above
        self.pidevice.TRO(1, False)
        
    def close_connection(self):
        """
        Close the connection and reset the axis property
        """
        self.pidevice.CloseConnection()    
        
    
        
class StepperChain:
    """Handles the connection with two pidevices, making use of the Stepper class
    to control a USB daisy chain of two devices.

    Attributes
    ----------
    controller_id : str
        The ID of the controller.
    axis_id : int
        The ID of the axis.

    Methods
    -------
    connect_daisy(dev_indices) 
        Connects master and servo to form a daisy chain.
    reference_both_stages(ref_modes)
        References both stages.
    configure_both_trig(trigger_types)
        Configures the output trigger modes of the two devices.
    """

    def __init__(self, controller_id: str, axis_id: int):
        """Initializes the StepperChain class.

        Parameters:
        controller_id (str): The ID of the controller.
        axis_id (int): The ID of the axis.
        """
        self.controller_id = controller_id
        self.axis_id = axis_id
        self.master = Stepper(controller_id, axis_id)
        self.servo = Stepper(controller_id, axis_id)
        
    
    def open_daisy_chain(self):
        """Opens the connection with the daisy chain.
        This method opens a daisy chain configuration using the first plugged device.
        """
        devices = self.master.usb_plugged_devices()
        self.master.pidevice.OpenUSBDaisyChain(description=devices[0])
        
    def get_daisy_chain_id(self):
        """Get the ID of the daisy chain.

        Returns
        -------
        daisy_chain_id : int
            The ID of the daisy chain.
        """
        daisy_chain_id = self.master.pidevice.dcid
        return daisy_chain_id

    def connect_daisy_chain(self):
        """Connects the master and servo in the daisy chain.

        This method initializes the daisy chain configuration, connects the master and servo devices,
        performs startup procedures, and sets up the axis for operation.
        """
        self.open_daisy_chain()
        dcid = self.get_daisy_chain_id()
        self.master.pidevice.ConnectDaisyChainDevice(1, dcid)  # maybe '1'
        pitools.startup(self.master.pidevice, self.axis_id)
        self.servo.pidevice.ConnectDaisyChainDevice(2, dcid)  # maybe '2'
        pitools.startup(self.servo.pidevice, self.axis_id)
        
    def close_daisy_chain_connection(self):
        """Close all connections on daisy chain and daisy chain connection itself.
        """
        self.master.pidevice.CloseDaisyChain()
        
        
    def reference_both_stages(self, ref_modes) -> None:
        """References both stages.

        Parameters:
        ref_modes (List[str]): List of two strings defining the referencing modes.
        """
        self.master.move_stage_to_ref(ref_modes[0])
        self.servo.move_stage_to_ref(ref_modes[1])    

