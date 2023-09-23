"""
Module: xpwhemisphere.py

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
class XPWHemisphere:
    """
    Camera Hemishpere information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fCenterX:float = None
        self._fCenterY:float = None
        self._fRadiusX:float = None
        self._fRadiusY:float = None


    @property
    def CenterX(self) -> float:
        """ 
        Gets the CenterX property value.

        Returns:
            The CenterX property value.
        """
        return self._fCenterX

    @CenterX.setter
    def CenterX(self, value:float) -> None:
        """ 
        Sets the CenterX property value.
        """
        if value != None:
            self._fCenterX = value


    @property
    def CenterY(self) -> float:
        """ 
        Gets the CenterY property value.

        Returns:
            The CenterY property value.
        """
        return self._fCenterY

    @CenterY.setter
    def CenterY(self, value:float) -> None:
        """ 
        Sets the CenterY property value.
        """
        if value != None:
            self._fCenterY = value


    @property
    def RadiusX(self) -> float:
        """ 
        Gets the RadiusX property value.

        Returns:
            The RadiusX property value.
        """
        return self._fRadiusX

    @RadiusX.setter
    def RadiusX(self, value:float) -> None:
        """ 
        Sets the RadiusX property value.
        """
        if value != None:
            self._fRadiusX = value


    @property
    def RadiusY(self) -> float:
        """ 
        Gets the RadiusY property value.

        Returns:
            The RadiusY property value.
        """
        return self._fRadiusY

    @RadiusY.setter
    def RadiusY(self, value:float) -> None:
        """ 
        Sets the RadiusY property value.
        """
        if value != None:
            self._fRadiusY = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "CenterX = {0}"
        """
        return str.format("CenterX = {0}", self.CenterX or "")
