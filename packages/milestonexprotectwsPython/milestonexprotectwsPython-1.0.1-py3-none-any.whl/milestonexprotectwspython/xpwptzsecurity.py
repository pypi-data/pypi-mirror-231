"""
Module: xpwptzsecurity.py

<details>
  <summary>Revision History</summary>

| Date       | Version     | Description
| ---------- | ----------- | ----------------------
| 2023/07/11 | 1.0.0.0     | Initial Version.  

</details>
"""


# external package imports.
# none.

# our package imports.
# none.

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWPtzSecurity:
    """
    Camera PTZ Security information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fManualControl:bool = False
        self._fPresetControl:bool = False
        self._fReserveControl:bool = False


    @property
    def ManualControl(self) -> bool:
        """ 
        Gets the ManualControl property value.

        Returns:
            The ManualControl property value.
        """
        return self._fManualControl

    @ManualControl.setter
    def ManualControl(self, value:bool) -> None:
        """ 
        Sets the ManualControl property value.
        """
        if value != None:
            self._fManualControl = value


    @property
    def PresetControl(self) -> bool:
        """ 
        Gets the PresetControl property value.

        Returns:
            The PresetControl property value.
        """
        return self._fPresetControl

    @PresetControl.setter
    def PresetControl(self, value:bool) -> None:
        """ 
        Sets the PresetControl property value.
        """
        if value != None:
            self._fPresetControl = value


    @property
    def ReserveControl(self) -> bool:
        """ 
        Gets the ReserveControl property value.

        Returns:
            The ReserveControl property value.
        """
        return self._fReserveControl

    @ReserveControl.setter
    def ReserveControl(self, value:bool) -> None:
        """ 
        Sets the ReserveControl property value.
        """
        if value != None:
            self._fReserveControl = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "ManualControl = {ManualControl}"
        """
        return str.format("ManualControl = {0}", self.ManualControl or "")


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.ManualControl == other.ManualControl
        except Exception as ex:
            if (isinstance(self, XPWPtzSecurity)) and (isinstance(other, XPWPtzSecurity)):
                return self.ManualControl == other.ManualControl
            return False

    def __lt__(self, other):
        try:
            # the following comparison will fail if the property value is None!  
            # use the following syntax when calling a sort method that uses lambda searches:
            # epColl.sort(ManualControl=lambda x: x.ManualControl or "", reverse=False)     <- GOOD syntax
            # epColl.sort(ManualControl=lambda x: x.ManualControl, reverse=False)           <- BAD syntax, as the "x.ManualControl" property may be None, and will cause this to fail!
            return self.ManualControl < other.ManualControl
        except Exception as ex:
            if (isinstance(self, XPWPtzSecurity)) and (isinstance(other, XPWPtzSecurity)):
                return self.ManualControl < other.ManualControl
            return False
