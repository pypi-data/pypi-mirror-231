"""
Module: xpwposition.py

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
class XPWPosition:
    """
    Device Position information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fPan:float = None
        self._fTilt:float = None
        self._fZoom:float = None


    @property
    def Pan(self) -> float:
        """ 
        Gets the Pan property value.

        Returns:
            The Pan property value.
        """
        return self._fPan

    @Pan.setter
    def Pan(self, value:float) -> None:
        """ 
        Sets the Pan property value.
        """
        if value != None:
            self._fPan = value


    @property
    def Tilt(self) -> float:
        """ 
        Gets the Tilt property value.

        Returns:
            The Tilt property value.
        """
        return self._fTilt

    @Tilt.setter
    def Tilt(self, value:float) -> None:
        """ 
        Sets the Tilt property value.
        """
        if value != None:
            self._fTilt = value


    @property
    def Zoom(self) -> float:
        """ 
        Gets the Zoom property value.

        Returns:
            The Zoom property value.
        """
        return self._fZoom

    @Zoom.setter
    def Zoom(self, value:float) -> None:
        """ 
        Sets the Zoom property value.
        """
        if value != None:
            self._fZoom = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "Pan = {0}"
        """
        return str.format("Pan = {0}", self.Pan or "")
