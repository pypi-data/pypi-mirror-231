"""
Module: xpwalerttype.py

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
class XPWAlertType:
    """
    Alert Type information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fAlertTypeId:str = None
        self._fDescription:str = None
        self._fName:str = None


    @property
    def AlertTypeId(self) -> str:
        """ 
        The globally unique identifier of the alert type.

        Returns:
            The AlertTypeId property value.
        """
        return self._fAlertTypeId

    @AlertTypeId.setter
    def AlertTypeId(self, value:str) -> None:
        """ 
        Sets the AlertTypeId property value.
        """
        if value != None:
            self._fAlertTypeId = value


    @property
    def Description(self) -> str:
        """ 
        A description of the alert type.

        Returns:
            The Description property value.
        """
        return self._fDescription

    @Description.setter
    def Description(self, value:str) -> None:
        """ 
        Sets the Description property value.
        """
        if value != None:
            self._fDescription = value


    @property
    def Name(self) -> str:
        """ 
        Name of the alert type.

        Returns:
            The Name property value.
        """
        return self._fName

    @Name.setter
    def Name(self, value:str) -> None:
        """ 
        Sets the Name property value.
        """
        if value != None:
            self._fName = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "Name - Description"
        """
        return str.format("{0} - {1}", self.Name or "", self.Description or "")


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.Name == other.Name
        except Exception as ex:
            if (isinstance(self, XPWAlertType)) and (isinstance(other, XPWAlertType)):
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
            if (isinstance(self, XPWAlertType)) and (isinstance(other, XPWAlertType)):
                return self.Name < other.Name
            return False
