"""
Module: xpwimmervision.py

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
class XPWImmerVision:
    """
    Camera Immer Vision information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fLensProfileData:str = None
        self._fLensProfileName:str = None
        self._fLensProfileRpl:str = None


    @property
    def LensProfileData(self) -> str:
        """ 
        Gets the LensProfileData property value.

        Returns:
            The LensProfileData property value.
        """
        return self._fLensProfileData

    @LensProfileData.setter
    def LensProfileData(self, value:str) -> None:
        """ 
        Sets the LensProfileData property value.
        """
        if value != None:
            self._fLensProfileData = value


    @property
    def LensProfileName(self) -> str:
        """ 
        Gets the LensProfileName property value.

        Returns:
            The LensProfileName property value.
        """
        return self._fLensProfileName

    @LensProfileName.setter
    def LensProfileName(self, value:str) -> None:
        """ 
        Sets the LensProfileName property value.
        """
        if value != None:
            self._fLensProfileName = value


    @property
    def LensProfileRpl(self) -> str:
        """ 
        Gets the LensProfileRpl property value.

        Returns:
            The LensProfileRpl property value.
        """
        return self._fLensProfileRpl

    @LensProfileRpl.setter
    def LensProfileRpl(self, value:str) -> None:
        """ 
        Sets the LensProfileRpl property value.
        """
        if value != None:
            self._fLensProfileRpl = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "LensProfileName = {0}"
        """
        return str.format("LensProfileName = {0}", self.LensProfileName or "")
