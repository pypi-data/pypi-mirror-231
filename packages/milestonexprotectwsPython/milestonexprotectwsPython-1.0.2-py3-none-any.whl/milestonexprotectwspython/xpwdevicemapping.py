"""
Module: XPWDeviceMapping.py

<details>
  <summary>Revision History</summary>

| Date       | Version     | Description
| ---------- | ----------- | ----------------------
| 2023/07/11 | 1.0.0.0     | Initial Version.  

</details>
"""


# external package imports.
# none

# our package imports.
# none

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWDeviceMapping():
    """
    Device Mapping information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize base class instance.
        super().__init__()

        # initialize instance.
        self._fDeviceA:str = None
        self._fDeviceB:str = None


    @property
    def DeviceA(self) -> bool:
        """ 
        The globally unique identifier of the FROM device.

        Returns:
            The DeviceA property value.
        """
        return self._fDeviceA

    @DeviceA.setter
    def DeviceA(self, value:bool) -> None:
        """ 
        Sets the DeviceA property value.
        """
        if value != None:
            self._fDeviceA = value


    @property
    def DeviceB(self) -> bool:
        """ 
        The globally unique identifier of the TO device.

        Returns:
            The DeviceB property value.
        """
        return self._fDeviceB

    @DeviceB.setter
    def DeviceB(self, value:bool) -> None:
        """ 
        Sets the DeviceB property value.
        """
        if value != None:
            self._fDeviceB = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "DeviceA - DeviceB"
        """
        return str.format("{0} - {1}", self.DeviceA or "", self.DeviceB or "")


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.DeviceA == other.DeviceA
        except Exception as ex:
            if (isinstance(self, XPWDeviceMapping)) and (isinstance(other, XPWDeviceMapping)):
                return self.DeviceA == other.DeviceA
            return False

    def __lt__(self, other):
        try:
            # the following comparison will fail if the property value is None!  
            # use the following syntax when calling a sort method that uses lambda searches:
            # epColl.sort(DeviceA=lambda x: x.DeviceA or "", reverse=False)     <- GOOD syntax
            # epColl.sort(DeviceA=lambda x: x.DeviceA, reverse=False)           <- BAD syntax, as the "x.DeviceA" property may be None, and will cause this to fail!
            return self.DeviceA < other.DeviceA
        except Exception as ex:
            if (isinstance(self, XPWDeviceMapping)) and (isinstance(other, XPWDeviceMapping)):
                return self.DeviceA < other.DeviceA
            return False
