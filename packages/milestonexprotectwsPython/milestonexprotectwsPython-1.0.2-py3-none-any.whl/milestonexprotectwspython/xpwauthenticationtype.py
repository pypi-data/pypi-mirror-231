"""
Module: xpwauthenticationtype.py

<details>
  <summary>Revision History</summary>

| Date       | Version     | Description
| ---------- | ----------- | ----------------------
| 2023/05/30 | 3.0.0.0     | Initial Version.  

</details>
"""


# our package imports.
from .xpwenumcomparable import XPWEnumComparable

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWAuthenticationType(XPWEnumComparable):
    """
    Authentication Types.
    """

    Unknown = 0
    """
    Authentication type could not be determined.
    """

    Basic = 1
    """
    User was authenticated with XProtect Basic User type credentials.
    """

    Windows = 2
    """
    User was authenticated with XProtect Windows User type credentials.
    """

    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "{name}"
        """
        return self.name
