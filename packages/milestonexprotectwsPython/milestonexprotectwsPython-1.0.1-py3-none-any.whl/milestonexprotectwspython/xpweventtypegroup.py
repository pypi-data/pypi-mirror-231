"""
Module: xpweventtypegroup.py

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
from .xpwcollection import XPWCollection
from .xpwgroup import XPWGroup

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWEventTypeGroup(XPWGroup):
    """
    EventType Group information.
    
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
        self._fEventTypes:list[str] = []
        self._fEventTypeGroups:XPWCollection = XPWCollection((XPWEventTypeGroup))


    @property
    def EventTypeGroups(self) -> XPWCollection:
        """ 
        A collection of XPEventTypeGroupsInfo objects.

        Returns:
            The EventTypeGroups property value.
        """
        return self._fEventTypeGroups


    @property
    def EventTypes(self) -> list[str]:
        """ 
        A list of EventType device identifiers associated with this group.

        Returns:
            The EventTypes property value.
        """
        return self._fEventTypes


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.Name == other.Name
        except Exception as ex:
            if (isinstance(self, XPWEventTypeGroup)) and (isinstance(other, XPWEventTypeGroup)):
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
            if (isinstance(self, XPWEventTypeGroup)) and (isinstance(other, XPWEventTypeGroup)):
                return self.Name < other.Name
            return False
