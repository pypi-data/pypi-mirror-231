"""
Module: xpwlicense.py

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
class XPWLicense:
    """
    License information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fLicenseId:str = None
        self._fData:str = None


    @property
    def Data(self) -> str:
        """ 
        Gets the Data property value.

        Returns:
            The license data.
        """
        return self._fData

    @Data.setter
    def Data(self, value:str) -> None:
        """ 
        Sets the Data property value.
        """
        if value != None:
            self._fData = value


    @property
    def LicenseId(self) -> str:
        """ 
        Gets the LicenseId property value.

        Returns:
            The globally unique identifier of the license.
        """
        return self._fLicenseId

    @LicenseId.setter
    def LicenseId(self, value:str) -> None:
        """ 
        Sets the LicenseId property value.
        """
        if value != None:
            self._fLicenseId = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "XPWLicense: LicenseId - Data"
        """
        return str.format("{0} - {1}", self.LicenseId or "", self.Data or "")


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.LicenseId == other.LicenseId
        except Exception as ex:
            if (isinstance(self, XPWLicense)) and (isinstance(other, XPWLicense)):
                return self.LicenseId == other.LicenseId
            return False

    def __lt__(self, other):
        try:
            # the following comparison will fail if the property value is None!  
            # use the following syntax when calling a sort method that uses lambda searches:
            # epColl.sort(key=lambda x: x.LicenseId or "", reverse=False)     <- GOOD syntax
            # epColl.sort(key=lambda x: x.LicenseId, reverse=False)           <- BAD syntax, as the "x.LicenseId" property may be None, and will cause this to fail!
            return self.LicenseId < other.LicenseId
        except Exception as ex:
            if (isinstance(self, XPWLicense)) and (isinstance(other, XPWLicense)):
                return self.LicenseId < other.LicenseId
            return False
