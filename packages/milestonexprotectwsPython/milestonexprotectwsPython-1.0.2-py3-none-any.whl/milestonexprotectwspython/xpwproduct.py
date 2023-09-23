"""
Module: xpwproduct.py

<details>
  <summary>Revision History</summary>

| Date       | Version     | VendorId
| ---------- | ----------- | ----------------------
| 2023/07/11 | 1.0.0.0     | Initial Version.  

</details>
"""

# external package imports.
from datetime import datetime

# our package imports.
# none

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWProduct :
    """
    Product information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fBuildConfiguration:str = None
        self._fBuildDate:datetime = None
        self._fBuildNumber:str = None
        self._fMajorVersion:str = None
        self._fMinorVersion:str = None
        self._fProductCode:str = None
        self._fProductLine:str = None
        self._fProductName:str = None
        self._fServiceVersion:str = None
        self._fSoftwareLicenseCode:str = None
        self._fSubProduct:str = None
        self._fVendorId:str = None


    @property
    def BuildConfiguration(self) -> str:
        """ 
        Build Configuration description (e.g. ReleaseAnsi, ReleaseUnicode, Release, Debug, etc).

        Returns:
            The BuildConfiguration property value.
        """
        return self._fBuildConfiguration

    @BuildConfiguration.setter
    def BuildConfiguration(self, value:str) -> None:
        """ 
        Sets the BuildConfiguration property value.
        """
        if value != None:
            self._fBuildConfiguration = value


    @property
    def BuildDate(self) -> datetime:
        """ 
        Build Date of the product.

        Returns:
            The BuildDate property value.
        """
        return self._fBuildDate

    @BuildDate.setter
    def BuildDate(self, value:datetime) -> None:
        """ 
        Sets the BuildDate property value.
        """
        if value != None:
            self._fBuildDate = value


    @property
    def BuildNumber(self) -> str:
        """ 
        Build Number of the product (e.g. X1234, V1234, etc).

        Returns:
            The BuildNumber property value.
        """
        return self._fBuildNumber

    @BuildNumber.setter
    def BuildNumber(self, value:str) -> None:
        """ 
        Sets the BuildNumber property value.
        """
        if value != None:
            self._fBuildNumber = value


    @property
    def MajorVersion(self) -> str:
        """ 
        Major Version of the product - e.g. 6 (in 6.5a), etc.

        Returns:
            The MajorVersion property value.
        """
        return self._fMajorVersion

    @MajorVersion.setter
    def MajorVersion(self, value:str) -> None:
        """ 
        Sets the MajorVersion property value.
        """
        if value != None:
            self._fMajorVersion = value


    @property
    def MinorVersion(self) -> str:
        """ 
        Minor Version of the product - e.g. 5 (in 6.5a), etc.

        Returns:
            The MinorVersion property value.
        """
        return self._fMinorVersion

    @MinorVersion.setter
    def MinorVersion(self, value:str) -> None:
        """ 
        Sets the MinorVersion property value.
        """
        if value != None:
            self._fMinorVersion = value


    @property
    def ProductCode(self) -> str:
        """ 
        The product code value.

        Returns:
            The ProductCode property value.
        """
        return self._fProductCode

    @ProductCode.setter
    def ProductCode(self, value:str) -> None:
        """ 
        Sets the ProductCode property value.
        """
        if value != None:
            self._fProductCode = value


    @property
    def ProductLine(self) -> str:
        """ 
        The globally unique identifier of the Product Line (e.g. Enterprise, Corporate, Analytics).

        Returns:
            The ProductLine property value.
        """
        return self._fProductLine

    @ProductLine.setter
    def ProductLine(self, value:str) -> None:
        """ 
        Sets the ProductLine property value.
        """
        if value != None:
            self._fProductLine = value


    @property
    def ProductName(self) -> str:
        """ 
        ProductName of the product.

        Returns:
            The ProductName property value.
        """
        return self._fProductName

    @ProductName.setter
    def ProductName(self, value:str) -> None:
        """ 
        Sets the ProductName property value.
        """
        if value != None:
            self._fProductName = value


    @property
    def ServiceVersion(self) -> str:
        """ 
        Service Version of the product - e.g. "a" (in 6.5a), etc.

        Returns:
            The ServiceVersion property value.
        """
        return self._fServiceVersion

    @ServiceVersion.setter
    def ServiceVersion(self, value:str) -> None:
        """ 
        Sets the ServiceVersion property value.
        """
        if value != None:
            self._fServiceVersion = value


    @property
    def SoftwareLicenseCode(self) -> str:
        """ 
        Product Software License Code value.

        Returns:
            The SoftwareLicenseCode property value.
        """
        return self._fSoftwareLicenseCode

    @SoftwareLicenseCode.setter
    def SoftwareLicenseCode(self, value:str) -> None:
        """ 
        Sets the SoftwareLicenseCode property value.
        """
        self._fSoftwareLicenseCode = value


    @property
    def SubProduct(self) -> str:
        """ 
        Sub-Product of the product (Enterprise, Professional, etc.).

        Returns:
            The SubProduct property value.
        """
        return self._fSubProduct

    @SubProduct.setter
    def SubProduct(self, value:str) -> None:
        """ 
        Sets the SubProduct property value.
        """
        if value != None:
            self._fSubProduct = value


    @property
    def VendorId(self) -> str:
        """ 
        The Vendor identifier (e.g. Milestone, OnSSI, Checkpoint, etc).

        Returns:
            The VendorId property value.
        """
        return self._fVendorId

    @VendorId.setter
    def VendorId(self, value:str) -> None:
        """ 
        Sets the VendorId property value.
        """
        if value != None:
            self._fVendorId = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "ProductName (Version MajorVersion.MinorVersion ServiceVersion)"
        """
        return str.format("{0} (Version {1}.{2}{3})", self.ProductName or "", self.MajorVersion or "", self.MinorVersion or "", self.ServiceVersion or "")
