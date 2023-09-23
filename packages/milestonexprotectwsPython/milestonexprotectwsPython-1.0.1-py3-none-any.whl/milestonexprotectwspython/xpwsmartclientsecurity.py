"""
Module: xpwsmartclientsecurity.py

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
class XPWSmartClientSecurity:
    """
    SmartClient Security information.
    
    Supplemental documentation can be found at:
    https://doc.milestonesys.com/2023R2/en-US/portal/htm/chapter-page-sc.htm?tocpath=XProtect%20Smart%20Client%7C_____0

    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fSmartClientBrowse:bool = False
        self._fSmartClientLive:bool = False
        self._fSmartClientReport:bool = False
        self._fSmartClientSetup:bool = False

    @property
    def SmartClientBrowse(self) -> bool:
        """ 
        True if the user has access to browse functionality; otherwise, False.

        Returns:
            The SmartClientBrowse property value.
        """
        return self._fSmartClientBrowse

    @SmartClientBrowse.setter
    def SmartClientBrowse(self, value:bool) -> None:
        """ 
        Sets the SmartClientBrowse property value.
        """
        if value != None:
            self._fSmartClientBrowse = value


    @property
    def SmartClientLive(self) -> bool:
        """ 
        True if the user has access to live feed functionality; otherwise, False.

        Returns:
            The SmartClientLive property value.
        """
        return self._fSmartClientLive

    @SmartClientLive.setter
    def SmartClientLive(self, value:bool) -> None:
        """ 
        Sets the SmartClientLive property value.
        """
        if value != None:
            self._fSmartClientLive = value


    @property
    def SmartClientReport(self) -> bool:
        """ 
        True if the user has access to report functionality; otherwise, False.

        Returns:
            The SmartClientReport property value.
        """
        return self._fSmartClientReport

    @SmartClientReport.setter
    def SmartClientReport(self, value:bool) -> None:
        """ 
        Sets the SmartClientReport property value.
        """
        if value != None:
            self._fSmartClientReport = value


    @property
    def SmartClientSetup(self) -> bool:
        """ 
        True if the user has access to setup configuration functionality; otherwise, False.

        Returns:
            The SmartClientSetup property value.
        """
        return self._fSmartClientSetup

    @SmartClientSetup.setter
    def SmartClientSetup(self, value:bool) -> None:
        """ 
        Sets the SmartClientSetup property value.
        """
        if value != None:
            self._fSmartClientSetup = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "Browse = {0}"
        """
        return str.format("Browse = {0}", self.SmartClientBrowse or "")
