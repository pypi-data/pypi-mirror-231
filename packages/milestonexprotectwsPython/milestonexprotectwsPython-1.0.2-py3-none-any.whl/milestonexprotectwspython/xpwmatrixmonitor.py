"""
Module: xpwmatrixmonitor.py

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
class XPWMatrixMonitor:
    """
    Matrix Monitor information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fMatrixMonitorId:str = None
        self._fDisplayName:str = None


    @property
    def MatrixMonitorId(self) -> str:
        """ 
        The globally unique identifier of the matrix monitor.

        Returns:
            The MatrixMonitorId property value.
        """
        return self._fMatrixMonitorId

    @MatrixMonitorId.setter
    def MatrixMonitorId(self, value:str) -> None:
        """ 
        Sets the MatrixMonitorId property value.
        """
        if value != None:
            self._fMatrixMonitorId = value


    @property
    def DisplayName(self) -> str:
        """ 
        DisplayName of the matrix monitor.

        Returns:
            The DisplayName property value.
        """
        return self._fDisplayName

    @DisplayName.setter
    def DisplayName(self, value:str) -> None:
        """ 
        Sets the DisplayName property value.
        """
        if value != None:
            self._fDisplayName = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "DisplayName - MatrixMonitorId"
        """
        return str.format("{0} - {1}", self.DisplayName or "", self.MatrixMonitorId or "")


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.DisplayName == other.DisplayName
        except Exception as ex:
            if (isinstance(self, XPWMatrixMonitor)) and (isinstance(other, XPWMatrixMonitor)):
                return self.DisplayName == other.DisplayName
            return False

    def __lt__(self, other):
        try:
            # the following comparison will fail if the property value is None!  
            # use the following syntax when calling a sort method that uses lambda searches:
            # epColl.sort(DisplayName=lambda x: x.DisplayName or "", reverse=False)     <- GOOD syntax
            # epColl.sort(DisplayName=lambda x: x.DisplayName, reverse=False)           <- BAD syntax, as the "x.DisplayName" property may be None, and will cause this to fail!
            return self.DisplayName < other.DisplayName
        except Exception as ex:
            if (isinstance(self, XPWMatrixMonitor)) and (isinstance(other, XPWMatrixMonitor)):
                return self.DisplayName < other.DisplayName
            return False
