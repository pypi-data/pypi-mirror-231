"""
Module: xpwoutputsecurity.py

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
# none

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWOutputSecurity:
    """
    Output device Security information.

    Supplemental documentation can be found at:
    https://doc.milestonesys.com/2023R2/en-US/standard_features/sf_mc/sf_ui/mc_roles_security.htm?cshid=9902#Outputrelatedpermissions
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fActivate:bool = False


    @property
    def Activate(self) -> bool:
        """ 
        True if the user has access to activate the output device from the management client; otherwise, False.

        Returns:
            The Activate property value.
        """
        return self._fActivate

    @Activate.setter
    def Activate(self, value:bool) -> None:
        """ 
        Sets the Activate property value.
        """
        if value != None:
            self._fActivate = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "Activate = {0}"
        """
        return str.format("Activate = {0}", self.Activate or "")
