"""
Module: xpwoutput.py

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
from .xpwdevice import XPWDevice
from .xpwoutputsecurity import XPWOutputSecurity

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWOutput(XPWDevice):
    """
    Output device information.
    
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
        self._fCoverageDepth:float = None
        self._fCoverageDirection:float = None
        self._fCoverageFieldOfView:float = None
        self._fOutputSecurity:XPWOutputSecurity = XPWOutputSecurity()
        self._fStopManualRecordingSeconds:int = None


    @property
    def CoverageDepth(self) -> float:
        """ 
        Depth. Indicates the viewing depth of the device.

        Returns:
            The CoverageDepth property value.
        """
        return self._fCoverageDepth

    @CoverageDepth.setter
    def CoverageDepth(self, value:float) -> None:
        """ 
        Sets the CoverageDepth property value.
        """
        if value != None:
            self._fCoverageDepth = value


    @property
    def CoverageDirection(self) -> float:
        """ 
        Direction. Indicate the viewing direction of the device.

        Returns:
            The CoverageDirection property value.
        """
        return self._fCoverageDirection

    @CoverageDirection.setter
    def CoverageDirection(self, value:float) -> None:
        """ 
        Sets the CoverageDirection property value.
        """
        if value != None:
            self._fCoverageDirection = value


    @property
    def CoverageFieldOfView(self) -> float:
        """ 
        Field of view. Indicate the field of view of the device.

        Returns:
            The CoverageFieldOfView property value.
        """
        return self._fCoverageFieldOfView

    @CoverageFieldOfView.setter
    def CoverageFieldOfView(self, value:float) -> None:
        """ 
        Sets the CoverageFieldOfView property value.
        """
        if value != None:
            self._fCoverageFieldOfView = value


    @property
    def OutputSecurity(self) -> XPWOutputSecurity:
        """ 
        Security settings.

        Returns:
            The OutputSecurity property value.
        """
        return self._fOutputSecurity


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.Name == other.Name
        except Exception as ex:
            if (isinstance(self, XPWOutput )) and (isinstance(other, XPWOutput )):
                return self.Name == other.Name
            return False

    def __lt__(self, other):
        try:
            # the following comparison will fail if the property value is None!  
            # use the following syntax when calling a sort method that uses lambda searches:
            # epColl.sort(Name=lambda x: x.Name or "", reverse=False)     <- GOOD syntax
            # epColl.sort(Name=lambda x: x.Name, reverse=False)           <- BAD syntax, as the "x.Name" property may be None, and will cause this to fail!
            return self.Name < other.Name
        except Exception as ex:
            if (isinstance(self, XPWOutput )) and (isinstance(other, XPWOutput )):
                return self.Name < other.Name
            return False
