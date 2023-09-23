"""
Module: xpwretentionoption.py

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
class XPWRetentionOption:
    """
    Retention Option information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fRetentionOptionType:str = None
        self._fRetentionUnits:str = None


    @property
    def RetentionUnits(self) -> str:
        """ 
        Gets the RetentionUnits property value.

        Returns:
            The retention units value.
        """
        return self._fRetentionUnits

    @RetentionUnits.setter
    def RetentionUnits(self, value:str) -> None:
        """ 
        Sets the RetentionUnits property value.
        """
        if value != None:
            self._fRetentionUnits = value


    @property
    def RetentionOptionType(self) -> str:
        """ 
        Gets the RetentionOptionType property value.

        Returns:
            The retention option type (e.g. "Days", "Weeks", etc).
        """
        return self._fRetentionOptionType

    @RetentionOptionType.setter
    def RetentionOptionType(self, value:str) -> None:
        """ 
        Sets the RetentionOptionType property value.
        """
        if value != None:
            self._fRetentionOptionType = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "RetentionOptionType = RetentionUnits"
        """
        return str.format("{0} = {1}", self.RetentionOptionType or "", self.RetentionUnits or "")


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.RetentionOptionType == other.RetentionOptionType
        except Exception as ex:
            if (isinstance(self, XPWRetentionOption)) and (isinstance(other, XPWRetentionOption)):
                return self.RetentionOptionType == other.RetentionOptionType
            return False

    def __lt__(self, other):
        try:
            # the following comparison will fail if the property value is None!  
            # use the following syntax when calling a sort method that uses lambda searches:
            # epColl.sort(RetentionOptionType=lambda x: x.RetentionOptionType or "", reverse=False)     <- GOOD syntax
            # epColl.sort(RetentionOptionType=lambda x: x.RetentionOptionType, reverse=False)           <- BAD syntax, as the "x.RetentionOptionType" property may be None, and will cause this to fail!
            return self.RetentionOptionType < other.RetentionOptionType
        except Exception as ex:
            if (isinstance(self, XPWRetentionOption)) and (isinstance(other, XPWRetentionOption)):
                return self.RetentionOptionType < other.RetentionOptionType
            return False
