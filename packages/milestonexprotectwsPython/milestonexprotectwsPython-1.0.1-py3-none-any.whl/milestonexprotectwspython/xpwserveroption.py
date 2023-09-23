"""
Module: xpwserveroption.py

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
class XPWServerOption:
    """
    Server Option information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fKey:str = None
        self._fValue:str = None


    @property
    def Value(self) -> str:
        """ 
        Gets the Value property value.

        Returns:
            The server option value.
        """
        return self._fValue

    @Value.setter
    def Value(self, value:str) -> None:
        """ 
        Sets the Value property value.
        """
        if value != None:
            self._fValue = value


    @property
    def Key(self) -> str:
        """ 
        Gets the Key property value.

        Returns:
            The server option key (e.g. "Bookmark", "PrivacyMask", etc).
        """
        return self._fKey

    @Key.setter
    def Key(self, value:str) -> None:
        """ 
        Sets the Key property value.
        """
        if value != None:
            self._fKey = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "Key - Value"
        """
        return str.format("{0} - {1}", self.Key or "", self.Value or "")


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.Key == other.Key
        except Exception as ex:
            if (isinstance(self, XPWServerOption)) and (isinstance(other, XPWServerOption)):
                return self.Key == other.Key
            return False

    def __lt__(self, other):
        try:
            # the following comparison will fail if the property value is None!  
            # use the following syntax when calling a sort method that uses lambda searches:
            # epColl.sort(key=lambda x: x.Key or "", reverse=False)     <- GOOD syntax
            # epColl.sort(key=lambda x: x.Key, reverse=False)           <- BAD syntax, as the "x.Key" property may be None, and will cause this to fail!
            return self.Key < other.Key
        except Exception as ex:
            if (isinstance(self, XPWServerOption)) and (isinstance(other, XPWServerOption)):
                return self.Key < other.Key
            return False
