"""
Module: xpwappmessages.py

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
class XPWAppMessages:
    """
    A strongly-typed resource class, for looking up localized strings, etc.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    UNHANDLED_EXCEPTION:str = "XPW0001E - An unhandled exception occured while processing method \"{0}\".\n{1}\n"
    """
    XPW0001E - An unhandled exception occured while processing method \"{0}\".
    {1}
    """

    EXCEPTION_SERVICE_PARSE_RESULTS:str = "XPW0002E - An exception occured while parsing XProtect web-service results for \"{0}\" details. \n{1}\n"
    """
    XPW0002E - An exception occured while parsing XProtect web-service results for \"{0}\" details.
    {1}
    """

    EXCEPTION_SERVICE_ERROR_BASE:str = "XPW0003E - \"{0}\" method call failed due to a failure response returned by XProtect web services."
    """
    XPW0003E - \"{0}\" method call failed due to a failure response returned by XProtect web services.
    """

    EXCEPTION_SERVICE_STATUS_UNKNOWN:str = "XPW0004E - An unknown XProtect web-service response status code was returned:\nStatus Code = {0}\nJSON Response:\n{1}\n\n"
    """
    XPW0004E - An unknown XProtect web-service response code and body was returned:
    Status Code = {0}
    JSON Response:
    {1}
    """

    LOGININFO_NOT_SUPPLIED:str = "XPW0005E - LoginInfo object not established.  You must first issue a Login call to establish a LoginInfo object that will be used on subsequent calls to XProtect web services."
    """
    XPW0005E - LoginInfo object not established.  You must first issue a Login call to 
    establish a LoginInfo object that will be used on subsequent calls to XProtect web services.
    """

    ARGUMENT_TYPE_ERROR:str = "XPW0006E - {0} argument must be of type \"{1}\"; the \"{2}\" type is not supported for this argument."
    """
    XPW0006E - {0} argument must be of type \"{1}\"; the \"{2}\" type not is supported for this argument.
    """

    ARGUMENT_REQUIRED_ERROR:str = "XPW0007E - The \"{0}\" argument is required, and cannot be null / None."
    """
    XPW0007E - The \"{0}\" argument is required, and cannot be null / None.
    """

    COLLECTION_ARGUMENT_TYPE_ERROR:str = "XPW0008E - Collection \"{0}\" method \"{1}\" argument must be of type \"{2}\"; an object of type \"{3}\" is not supported for this method argument."
    """
    XPW0008E - Collection \"{0}\" method \"{1}\" argument must be of type \"{2}\"; an object of type \"{3}\" is not supported for this method argument.
    """

    DICTIONARY_KEY_NOT_FOUND_ERROR:str = "XPW0009E - Could not locate key \"{0}\" in response dictionary."
    """
    XPW0009E - Could not locate key \"{0}\" in response dictionary.
    """
    
    LOGININFO_AUTHTYPE_NOTIMPLEMENTED:str = "XPW0010E - Login authentication type \"{0}\" support has not been implemented in the \"{1}\" method."
    """
    XPW0010E - Login authentication type \"{0}\" support has not been implemented in the \"{1}\" method.
    """

    ARGUMENT_TYPE_ERROR_DATETIME:str = "XPW0011E - The \"{0}\" argument must be a datetime object, and the year greater than 1800."
    """
    XPW0011E - The \"{0}\" argument must be a datetime object, and the year greater than 1800.
    """

    DICTIONARY_VALUE_NOT_CONVERTIBLE:str = "XPW0012E - Could not convert response dictionary key \"{0}\" value \"{1}\" to type \"{2}\"."
    """
    XPW0012E - Could not convert response dictionary key \"{0}\" value \"{1}\" to type \"{2}\".
    """
    
