"""
Module: xpwapplicationsecurity.py

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
from .xpwsmartclientsecurity import XPWSmartClientSecurity

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWApplicationSecurity:
    """
    Application Security information.
    
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
        self._fSmartClientSecurity:XPWSmartClientSecurity = XPWSmartClientSecurity()


    @property
    def SmartClientSecurity(self) -> XPWSmartClientSecurity:
        """ 
        Smart Client Security settings.

        Returns:
            The SmartClientSecurity property value.
        """
        return self._fSmartClientSecurity
