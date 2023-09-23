"""
Module: xpwwebservicebase.py

<details>
  <summary>Revision History</summary>

| Date       | Version     | Description
| ---------- | ----------- | ----------------------
| 2023/07/11 | 1.0.0.0     | Initial Version.  

</details>
"""

# external package imports.
import _threading_local
from datetime import datetime, timedelta
import inspect
import json
from requests import Response, Request, Session
from smartinspectpython.sisourceid import SISourceId 
from urllib import parse
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
import xmltodict

# our package imports.
from .xpwappmessages import XPWAppMessages
from .xpwauthenticationtype import XPWAuthenticationType
from .xpwexception import XPWException
from .xpwlogininfo import XPWLoginInfo
from .xpwlogintokenexpiredexception import XPWLoginTokenExpiredException
from .xpwwebserviceexception import XPWWebServiceException

# our package constants.
from .xpwconst import (
    MSG_TRACE_PROCESSING_DICTIONARY,
    MSG_TRACE_METHOD_REQUEST,
    MSG_TRACE_METHOD_REQUEST_HEADERS,
    MSG_TRACE_METHOD_REQUEST_BODY,
    MSG_TRACE_METHOD_RESPONSE,
    MSG_TRACE_METHOD_RESPONSE_BODY,
    MSG_TRACE_METHOD_RESPONSE_DICTIONARY
)

# get smartinspect logger reference.
from smartinspectpython.siauto import SISession, SILevel, SIAuto
_logsi:SISession = SIAuto.Main

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export

@export
class XPWWebServiceBase:
    """
    The XPWWebServiceBase class provides properties common to all XProtect web-services.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self, loginInfo:XPWLoginInfo=None) -> None:
        """
        Initializes a new instance of the class.

        Args:
            loginInfo (XPWLoginInfo):
                Login Information class that contains login token information.  This class is returned 
                on a successful call to any of the LoginX methods from classes that inherit from
                XPWWebServiceBase.  This allows you to share the same Login Information (token, etc)
                between service classes.  
                Specify null / None to not share Login Information; if doing so, then your first call
                must be to one of the Login methods (e.g. LoginBasicUser, LoginWindowsUser, etc).  
                Default is null / None.                                

        Raises:
            XPWException:
                If supplied, the loginInfo argument was not of type XPWLoginInfo.  
                The method fails for any reason.  
        """
        serviceMethodName:str = "__init__"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug) 

            # validations.
            if (loginInfo != None):
                # is loginInfo argument type a XPWLoginInfo type of object?  if not, then we are done.
                if (not isinstance(loginInfo, type(XPWLoginInfo))):
                    raise XPWException(XPWAppMessages.ARGUMENT_TYPE_ERROR.format("loginInfo", type(XPWLoginInfo).__name__, type(loginInfo).__name__), None, _logsi)

            # initialize instance.
            self._fInstanceId:str = "00000000-0000-0000-0000-000000000000"
            self._fIsAutoTokenRenewalEnabled:bool = True
            self._fIsSslVerifyEnabled:bool = True
            self._fLoginInfo = loginInfo
            self._fLock = _threading_local.RLock()
            self._fManagementServerUrlPrefix:str = None
            self._fServerApiUrlPrefix:str = None
           
        except Exception as ex:

            # trace.
            _logsi.LogException(None, ex)
            raise

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    @property
    def InstanceId(self) -> str:
        """ 
        Instance identifier that uniquely identifies the calling application.

        Returns:
            The InstanceId property value.

        The Instance Identifier is a GUID that uniquely identifies the calling application.
        Typically, each ID should refer to a specific machine running an integration.
        """
        return self._fInstanceId

    @InstanceId.setter
    def InstanceId(self, value:bool) -> None:
        """ 
        Sets the InstanceId property value.
        """
        if value != None:
            self._fInstanceId = value


    @property
    def IsAutoTokenRenewalEnabled(self) -> bool:
        """ 
        Enables / disables the automatic token renewal check logic check that is
        made prior to making a call to the XProtect web service.  

        Returns:
            The IsAutoTokenRenewalEnabled property value.        

        If True, the LoginInfo.ExpireTime value is checked to see if the XProtect token is
        within 1 minute of expiring PRIOR to processing the desired API method (e.g. GetCameras, etc).
        If the token is about to expire, then it will be automatically renewed via a call to the XProtect
        web-services Login method (e.g. LoginBasicUser, LoginBasicWindows) that was previously used to login and
        establish the authentication token.  The desired API method (e.g. GetCameras, etc) is then
        processed as requested.
        
        If False, the desired API method (e.g. GetCameras, etc) is processed normally, though it will
        probably fail with a XPWLoginTokenExpiredException due to an expired token!
        """
        return self._fIsAutoTokenRenewalEnabled

    @IsAutoTokenRenewalEnabled.setter
    def IsAutoTokenRenewalEnabled(self, value:bool) -> None:
        """ 
        Sets the IsAutoTokenRenewalEnabled property value.
        """
        if value != None:
            self._fIsAutoTokenRenewalEnabled = value


    @property
    def IsSslVerifyEnabled(self) -> bool:
        """ 
        SSL Verify flag used on all request GET / POST method calls.
        Default Value is True.        

        Returns:
            The IsSslVerifyEnabled property value.        

        This setting will be added to all request GET / POST calls made to the XProtect web services.

        If False, it will ignore SSL Certificate warnings (e.g. certificate expired, self-signed certificate, etc).
        It also makes a call to "urllib3.disable_warnings(category=InsecureRequestWarning)" to suppress
        terminal messages.
        """
        return self._fIsSslVerifyEnabled

    @IsSslVerifyEnabled.setter
    def IsSslVerifyEnabled(self, value:bool) -> None:
        """ 
        Sets the IsSslVerifyEnabled property value.
        """
        if value != None:
            self._fIsSslVerifyEnabled = value
            if (value == False):
                # suppress only the single warning from urllib3 needed.
                disable_warnings(category=InsecureRequestWarning)


    @property
    def LoginInfo(self) -> XPWLoginInfo:
        """ 
        LoginInfo object that was specified when the class was initialized, or when
        a Login method (e.g. LoginBasicUser, LoginWindowsUser) was called successfully.

        Returns:
            The LoginInfo property value.

        This property is read-only.
        """
        return self._fLoginInfo


    @property
    def ManagementServerUrlPrefix(self) -> str:
        """ 
        URL prefix of the XProtect Management Server.

        Returns:
            The ManagementServerUrlPrefix property value.

        This url prefix is used to call various web-services that are hosted by the 
        XProtect Management Server.  These services include the ServerCommandService.svc, etc.  

        It should only contain the server name (and port number if required) portion of
        the server url (e.g. "https://xprotectmanagementserver.example.com", or
        "https://xprotectmanagementserver.example.com:443").  

        It should NOT contain any of the server web-service method names or paths (e.g. 
        "https://xprotectmanagementserver.example.com/ManagementServer/ServerCommandService.svc").
        """
        return self._fManagementServerUrlPrefix

    @ManagementServerUrlPrefix.setter
    def ManagementServerUrlPrefix(self, value:str) -> None:
        """ 
        Sets the ManagementServerUrlPrefix property value.
        """
        if (value != None):
            if (value.endswith("/")):
                value = value[0:len(value)-1]
            if (value != None):
                self._fManagementServerUrlPrefix = value

                # also set the ServerApiUrlPrefix with the same if it has not been set.
                if (self._fServerApiUrlPrefix == None):
                    self._fServerApiUrlPrefix = value                


    @property
    def ServerApiUrlPrefix(self) -> str:
        """ 
        URL prefix of the XProtect Server API Server.

        Returns:
            The ServerApiUrlPrefix property value.

        This url prefix is used to call various web-services that are hosted by the 
        XProtect Server API Server.  These services include the ServerCommandService.asmx, etc.  

        It should only contain the server name (and port number if required) portion of
        the server url (e.g. "https://xprotectmanagementserver.example.com", or
        "https://xprotectmanagementserver.example.com:443").  

        It should NOT contain any of the server web-service method names or paths (e.g. 
        "https://xprotectmanagementserver.example.com/ServerAPI/ServerCommandService.asmx").
        """
        return self._fServerApiUrlPrefix

    @ServerApiUrlPrefix.setter
    def ServerApiUrlPrefix(self, value:str) -> None:
        """ 
        Sets the ServerApiUrlPrefix property value.
        """
        if (value != None):
            if (value.endswith("/")):
                value = value[0:len(value)-1]
            if (value != None):
                self._fServerApiUrlPrefix = value


    def _AutoTokenRenewalCheck(self, serviceMethodName:str) -> None:
        """
        Checks the LoginInfo.ExpireTime value to see if the XProtect token needs to be renewed.
        Also checks to ensure the LoginInfo property value is set (e.g. a LoginX method has been
        performed).        

        Args:
            serviceMethodName (str):
                Name of the service method that was called.  
                Example: "GetCameras", etc.

        Raises:
            XPWException:
                The method fails for any reason.  
        
        The IsAutoTokenRenewalEnabled property controls if the token is checked or not.
        If True, the LoginInfo.ExpireTime value is checked to see if the XProtect token is
        within 1 minute of expiring PRIOR to processing the desired API method (e.g. GetCameras, etc).
        If the token is about to expire, then it will be automatically renewed via a call to the XProtect
        web-service Login method (e.g. LoginBasicUser, LoginBasicWindows) that was previously used to login and
        establish the authentication token.  The desired API method (e.g. GetCameras, etc) is then
        processed as requested.
        """
        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug) 
   
            # validations.
            if (self._fLoginInfo == None):
                raise XPWException(XPWAppMessages.LOGININFO_NOT_SUPPLIED, None, _logsi)

            # are we auto-renewing the token?  if not, then we are done.
            if (self.IsAutoTokenRenewalEnabled == False):
                return
            
            # is token within 60 seconds of expiring?
            diffInSeconds:int = (self._fLoginInfo.ExpireTime - datetime.utcnow()).total_seconds() 
            if (diffInSeconds < 60):

                _logsi.LogVerbose("Login token is about to expire; the token will be auto renewed.")

                # yes - renew the token using the appropriate login method.
                if (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Basic):    
                    self.LoginBasicUser(self._fLoginInfo.UserName, self._fLoginInfo.Password, self._fLoginInfo.Token)

                elif (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Windows):
                    self.LoginWindowsUser(self._fLoginInfo.UserName, self._fLoginInfo.Password, self._fLoginInfo.Token)

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)
                    

    def _Parse_Login(self, oDict:dict) -> XPWLoginInfo:
        """
        Converts a Login XML response to a class.

        Args:
            oDict (dict):
                A dictionary object that represents the XML response.

        Returns:
            An XPWLoginInfo class that represents the XML response.

        Raises:
            Exception:
                The method fails for any reason.  
        """
        methodKeyName:str = "LoginInfo"
        loginInfo:XPWLoginInfo = XPWLoginInfo()

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            # <LoginResponse xmlns="http://videoos.net/2/XProtectCSServerCommand">
            #   <LoginResult>
            #     <Token>TOKEN#2eca3f71-0ab6-4553-b7d1-1c622d8d5085#win10vm//ServerConnector#</Token>
            #     <RegistrationTime>2023-07-12T05:13:34.237Z</RegistrationTime>
            #     <TimeToLive>
            #       <MicroSeconds>14400000000</MicroSeconds>
            #     </TimeToLive>
            #     <TimeToLiveLimited>false</TimeToLiveLimited>
            #   </LoginResult>
            # </LoginResponse>

            # note - "TimeToLive" is expressed in microseconds (e.g. 14400000000 microseconds / 100,000 = 144000 seconds = 2400 minutes = 40 hours).

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # we will drop microseconds from the RegistrationTime value, as they were causing
                # issues when converting to a datetime object.  the xprotect web-service does NOT
                # provide a 6-digit (e.g. leading zeros) microseconds value, and it was causing
                # the "GetDictKeyValueDateTime" method to fail when trying to convert the datetime
                # string to a datetime object.  so we just dropped the microseconds value in this
                # case, as it's not really relevant.

                # parse response result.
                loginInfo.RegistrationTime = self.GetDictKeyValueDateTime(oDict, "RegistrationTime", True, excludeMicroseconds=True, excludeTimeZoneInfo=True)
                loginInfo.Scope = "managementserver"
                loginInfo.TimeToLiveLimited = self.GetDictKeyValueBool(oDict, "TimeToLiveLimited", True)
                loginInfo.Token = self.GetDictKeyValueString(oDict, "Token", True)
                loginInfo.TokenType = "Bearer"

                # does dictionary contain the TimeToLive key with a MicroSeconds subkey?
                oDictSubKey:dict = self.GetDictKeyValueDict(oDict, "TimeToLive", True)
                value:int = self.GetDictKeyValueInt(oDictSubKey, "MicroSeconds", True)
                if (value > 0):
                    loginInfo.TimeToLiveSeconds = int(value / 1000000)   # convert microseconds to seconds

                # remove timezone awareness from RegistrationTime, as it will always be in UTC format.
                # this prevents "can't subtract offset-naive and offset-aware datetimes" exceptions 
                # later when comparing datetimes!
                if (loginInfo.RegistrationTime != None):
                    loginInfo.RegistrationTime = loginInfo.RegistrationTime.replace(tzinfo=None)

                # calculate expire time from registration time and time to live properties.
                loginInfo.ExpireTime = (loginInfo.RegistrationTime + timedelta(seconds=loginInfo.TimeToLiveSeconds))
  
            # return login info object.
            return loginInfo

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    @staticmethod
    def AddDictKeyValueArrayStrings(oDict:dict, keyName:str, arrayListStrings:list[str], raiseExceptionIfNotFound:bool=False) -> None:
        """
        Checks a dictionary for the specified key name, ensures that it defines a list of strings, 
        and then appends them to the arrayListStrings argument list; otherwise, no values are appended
        to the arrayListStrings argument.        

        Args:
            oDict (dict):
                Dictionary to check for the specified key name.
            keyName (str):
                Key name to check for.
            arrayListStrings (str):
                An array list of strings to append found values to.
            raiseExceptionIfNotFound (bool):
                True to raise an Exception if the specified keyName is not found in the dictionary;  
                otherwise, False.  
                Default value: False  
        """
        # does dictionary contain the key?
        if (XPWWebServiceBase.DictHasKey(oDict, keyName)):

            valueArray = oDict[keyName]
            
            # is it a list of strings? if so, then append all values to the arrayListStrings argument.
            if (isinstance(valueArray, list)):
                for value in valueArray:
                    if (isinstance(value, str)):
                        arrayListStrings.append(value)
                return      

        else:

            # key was not found - are we raising an exception?  if so, then do it!
            if (raiseExceptionIfNotFound):
                raise Exception(XPWAppMessages.DICTIONARY_KEY_NOT_FOUND_ERROR.format(keyName))


    def CheckResponseStatusCode(self, serviceMethodName:str, req:Request, resp:Response, serviceResultKeyName:str, serviceResultNamespaces:dict, raiseExceptionIfServiceResultKeyNameNotFound:bool=False) -> dict:
        """
        Check the web-service HTTP response code for error values (4xx, 5xx, etc).
        An XPWWebServiceException will be thrown if the HTTP status code does not
        equal 200 or 201.

        Args:
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.
                Example: "GetCameras"
            req (Request):
                HTTP request object that contains the web server request.
            resp (Response):
                HTTP response object that contains the web server response.
            serviceResultKeyName (str):
                Name of the XProtect web-service results node that contains response details.
                Example: "LoginResult"
            serviceResultNamespaces (dict):
                XML namespaces to override on the xmltodict parse method.  This allows the
                xmltodict parser to correctly process XML namespaces in the response.  You may
                also specify null / None if no namespace references are present in the response.                  
                Example: { 'http://videoos.net/2/XProtectCSServiceRegistration':None, 'http://schemas.microsoft.com/2003/10/Serialization/Arrays':None }
            raiseExceptionIfServiceResultKeyNameNotFound (bool):
                True to raise an Exception if the specified serviceResultKeyName argument value is 
                not found in the responseXml; otherwise, False.  
                Default value: False

        Returns:
            If HTTP status is unsuccessful (e.g. not 200, 201) then an XPWWebServiceException
            is raised.  
            
            If HTTP status is successful (e.g. 200, 201) then the soap XML response is
            searched for a node that is specified by the serviceResultKeyName argument value.  
            If found, the XML node is converted to a dictionary via XMLTODICT and returned to the caller.  
            If not found, then it denotes that no results were found for the request; in this case, an
            exception will be raised if the raiseExceptionIfServiceResultKeyNameNotFound argument
            is True; otherwise, a null / None value is returned.

        Raises:
            XPWWebServiceException:
                Raised if the HTTP status returned indicated failue (e.g. 4xx, 5xx, etc).
        """
        oDict:dict = None

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)
            if (_logsi.IsOn(SILevel.Verbose)):
                _logsi.LogObject(SILevel.Verbose, MSG_TRACE_METHOD_RESPONSE.format(serviceMethodName), resp)
                _logsi.LogSource(SILevel.Verbose, MSG_TRACE_METHOD_RESPONSE_BODY.format(serviceMethodName), resp.text, SISourceId.Xml)

            # was it an OK response?
            if (resp.status_code == 200) or (resp.status_code == 201):

                # convert xml response body to dictionary.
                oDict:dict = self.GetXmlResponseDictionary(resp.text, serviceMethodName, serviceResultKeyName, serviceResultNamespaces, raiseExceptionIfServiceResultKeyNameNotFound)

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_METHOD_RESPONSE_DICTIONARY.format(serviceMethodName, serviceResultKeyName), json.dumps(oDict, indent=2))
                
                # return dictionary to caller.
                return oDict

            # check for web-service errors that are caused by our client request.
            # for 4xx errors, the response body will contain an XML object that describes one or more errors.

            # HTTP status code 400 - Client Error, Bad Request.
            if (resp.status_code == 400):
                self.RaiseWebServiceException(serviceMethodName, req, resp)

            # HTTP status code 401 - Client Error, Unauthorized.
            elif (resp.status_code == 401):
                self.RaiseWebServiceException(serviceMethodName, req, resp)

            # HTTP status code 403 - Client Error, Forbidden.
            elif (resp.status_code == 403):
                self.RaiseWebServiceException(serviceMethodName, req, resp)

            # HTTP status code 404 - Client Error, Not Found.
            elif (resp.status_code == 404):
                self.RaiseWebServiceException(serviceMethodName, req, resp)

            # HTTP status code 4xx - Client Error.
            elif (resp.status_code >= 400) and (resp.status_code <= 499):
                self.RaiseWebServiceException(serviceMethodName, req, resp)

            # check for web-service errors that are caused by the XProtect web server.
            # for 5xx errors, the response body MAY contain (not guaranteed) one or more error descriptions
            # in plain text (not XML data) format.

            # HTTP status code 503 - "The service is unavailable."

            # check for HTTP status code 500 - Server Error, Internal Server Error.
            elif (resp.status_code >= 500) and (resp.status_code <= 599):
                self.RaiseWebServiceException(serviceMethodName, req, resp)

            # if we did not process any of the above status codes, then it's an unknown.
            # in this case, we will simply populate the exception details with the HTTP status
            # code and the body of the response object unparsed.
            else:
                raise Exception(XPWAppMessages.EXCEPTION_SERVICE_STATUS_UNKNOWN.format(str(resp.status_code), resp.text))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def RaiseWebServiceException(self, serviceMethodName:str, req:Request, resp:Response) -> None:
        """
        Parses XProtect web-services failed HTTP response and raises the XPWWebServiceException
        to indicate the requested call failed.

        Args:
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.
                Example: "GetCameras"
            req (Request):
                HTTP request object that contains the web server request.
            resp (Response):
                HTTP response object that contains the web server response.

        Raises:
            XPWWebServiceException:
                Thrown if XProtext web-service error response details were parsed successfully.
            XPWException:
                Thrown if XProtext web-service error response details could not be parsed successfully.
        """
        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # initialize exception parameters.
            message:str = XPWAppMessages.EXCEPTION_SERVICE_ERROR_BASE.format(serviceMethodName)
            errorText:str = None
            errorTextId:str = None
            httpCode:int = resp.status_code
            httpReason:str = resp.reason
            propertyName:str = None

            # initialize working storage.
            tempXml:str = resp.text
            oDict:dict = None
            soapFaultNamespaces:dict = { 'http://schemas.xmlsoap.org/soap/envelope/':None, 
                                         'http://www.w3.org/2001/XMLSchema-instance':None,
                                         'http://www.w3.org/2001/XMLSchema':None,
                                         'http://schemas.datacontract.org/2004/07/System.ServiceModel':None,
                                         'http://www.w3.org/1999/xhtml':None,
                                         'http://www.w3.org/2003/05/soap-envelope':None
                                       }

            # does response contain server error fieldset nodes?
            # Windows ".ASMX" web-services communicate faults via standardized HTTP responses that contain <fieldset> nodes.
            if (tempXml.find("<fieldset>") > -1) and (tempXml.find("Server Error") > -1):
                
                try:

                    # convert xml to dictionary.
                    oDict = xmltodict.parse(tempXml,
                                            process_namespaces=True,
                                            namespaces=soapFaultNamespaces)

                    # trace.
                    _logsi.LogText(SILevel.Verbose, "Service Error dictionary (<fieldset>)", json.dumps(oDict, indent=2))

                    # dictionary example: invalid username or password (http status=401)
                    # "html": {
                    #   "head": {
                    #     "title": "401 - Unauthorized: Access is denied due to invalid credentials.",
                    #   },
                    #   "body": {
                    #     "div": [
                    #       {
                    #         "@id": "header",
                    #         "h1": "Server Error"
                    #       },
                    #       {
                    #         "@id": "content",
                    #         "div": {
                    #           "@class": "content-container",
                    #           "fieldset": {
                    #             "h2": "401 - Unauthorized: Access is denied due to invalid credentials.",
                    #             "h3": "You do not have permission to view this directory or page using the credentials that you supplied."

                    # process html standardized response dictionary.
                    oDict = self.GetDictKeyValueDict(oDict, "html", False)
                    oDict = self.GetDictKeyValueDict(oDict, "head", False)
                    httpReason = self.GetDictKeyValueString(oDict, "title", False)
                    if (httpReason == None):
                        httpReason = resp.reason

                    # process fieldset fault dictionary.
                    oDict = self.GetXmlResponseDictionary(tempXml, serviceMethodName, "fieldset", None, False)
                    if (httpReason == None):
                        httpReason = self.GetDictKeyValueString(oDict, "h2", False)
                    errorText = self.GetDictKeyValueString(oDict, "h3", False)

                except Exception as ex:
                    pass  # ignore exceptions                                        

            # does response contain "<s:Fault>" nodes?
            if (tempXml.find("s:Fault") > -1) and (tempXml.find("<faultcode") > -1) and (tempXml.find("<faultstring") > -1):
                
                try:

                    # convert xml to dictionary.
                    oDict = xmltodict.parse(tempXml,
                                            process_namespaces=True,
                                            namespaces=soapFaultNamespaces)

                    # trace.
                    _logsi.LogText(SILevel.Verbose, "Service Error dictionary (<s:Fault>)", json.dumps(oDict, indent=2))

                    # SOAP Fault dictionary example: invalid username or password (http status=401)
                    # "Envelope": {
                    #   "Body": {
                    #     "Fault": {
                    #       "faultcode": "a:InternalServiceFault",
                    #       "faultstring": {
                    #         "@http://www.w3.org/XML/1998/namespace:lang": "en-US",
                    #         "@xmlns": {
                    #           "s": "http://schemas.xmlsoap.org/soap/envelope/",
                    #           "a": "http://schemas.microsoft.com/net/2005/12/windowscommunicationfoundation/dispatcher"
                    #         },
                    #         "#text": "Value cannot be null.\r\nParameter name: parameters"
        
                    # SOAP Fault dictionary example: insufficient permissions (http status=500)
                    # "Envelope": {
                    #     "Body": {
                    #         "Fault": {
                    #             "faultcode": "s:51000",
                    #             "faultstring": {
                    #                 "@http://www.w3.org/XML/1998/namespace:lang": "en-US",
                    #                 "@xmlns": {
                    #                     "s": "http://schemas.xmlsoap.org/soap/envelope/"
                    #                 },
                    #                 "#text": "VMO61008: You do not have sufficient permissions to complete the operation."

                    # process soap fault dictionary.
                    oDict = self.GetDictKeyValueDict(oDict, "Envelope", False)
                    oDict = self.GetDictKeyValueDict(oDict, "Body", False)
                    oDict = self.GetDictKeyValueDict(oDict, "Fault", False)
                    propertyName = self.GetDictKeyValueString(oDict, "faultcode", False)
                    oDict = self.GetDictKeyValueDict(oDict, "faultstring", False)
                    errorText = self.GetDictKeyValueString(oDict, "#text", False)

                    # if error text is prefixed with a message id (e.g. "VMO6100"), 
                    # then store message id in separate field.
                    if (errorText != None) and (len(errorText) > 10):
                        idx:int = errorText.find(":")                    
                        if (idx < 10):
                            errorTextId = errorText[0:idx]
                            errorText = errorText[idx + 2:]

                    # cleanup the property name.
                    if (propertyName != None) and (len(propertyName) > 2):
                        if (propertyName.startswith("s:")) or (propertyName.startswith("a:")):
                            propertyName = propertyName[2:]

                except Exception as ex:
                    pass  # ignore exceptions                                        

            # does response contain "<soap:Fault>" nodes?
            if (tempXml.find("soap:Fault") > -1) and (tempXml.find("<soap:Value") > -1) and (tempXml.find("<soap:Text") > -1):
                
                try:

                    # convert xml to dictionary.
                    oDict = xmltodict.parse(tempXml,
                                            process_namespaces=True,
                                            namespaces=soapFaultNamespaces)

                    # trace.
                    _logsi.LogText(SILevel.Verbose, "Service Error dictionary (<soap:Fault>)", json.dumps(oDict, indent=2))

                    # SOAP Fault dictionary example: insufficient permissions (http status=500)
                    # "Envelope": {
                    #   "Body": {
                    #     "Fault": {
                    #       "Code": {
                    #         "Value": "UnauthorizedAccessException",
                    #         }
                    #       },
                    #       "detail": {
                    #         "@ErrorNumber": "51000",
                    #         "@BaseExceptionName": "System.UnauthorizedAccessException",
                    #         "@ExceptionMessage": "VMO61008: You do not have sufficient permissions to complete the operation.",
                    #         "ErrorNumber": "51000"
          
                    # process soap fault dictionary.
                    oDict = self.GetDictKeyValueDict(oDict, "Envelope", False)
                    oDict = self.GetDictKeyValueDict(oDict, "Body", False)
                    oDict = self.GetDictKeyValueDict(oDict, "Fault", False)
                    oDictCode = self.GetDictKeyValueDict(oDict, "Code", False)
                    codeValue:str = self.GetDictKeyValueString(oDictCode, "Value", False)
                    oDictDtl = self.GetDictKeyValueDict(oDict, "detail", False)
                    errorText = self.GetDictKeyValueString(oDictDtl, "@ExceptionMessage", False)
                    propertyName:str = self.GetDictKeyValueString(oDictDtl, "@ErrorNumber", False)

                    # if error text is prefixed with a message id (e.g. "VMO6100"), 
                    # then store message id in separate field.
                    if (errorText != None) and (len(errorText) > 10):
                        idx:int = errorText.find(":")                    
                        if (idx < 10):
                            errorTextId = errorText[0:idx]
                            errorText = errorText[idx + 2:]

                    # cleanup the property name.
                    if (propertyName != None) and (len(propertyName) > 2):
                        if (propertyName.startswith("s:")) or (propertyName.startswith("a:")):
                            propertyName = propertyName[2:]

                except Exception as ex:
                    pass  # ignore exceptions                                        

            # 401 status-code post-processing:
            if (httpCode == 401):
                # is this a login token expired event?  if so, then raise a special exception for it.
                if (errorText != None):
                    if (errorText.find("token is expired") > -1):
                        raise XPWLoginTokenExpiredException(errorText, _logsi)

            # 404 status-code post-processing:
            if (httpCode == 404):
                # is this a 404 resource not found event?  if so, then add the request URL to the PropertyName field if it's not set.
                if (propertyName == None):
                    propertyName = req.url

            # drop the http status code value from the http reason text if present.
            if (httpReason != None):
                if httpReason.startswith("{0} - ".format(str(httpCode))):
                    httpReason = httpReason[6:]

            # raise exception.
            raise XPWWebServiceException(message, errorText, errorTextId, propertyName, httpCode, httpReason, _logsi)

        except XPWException: raise  # pass formatted exception on thru
        except Exception as ex:

            # trace and ignore exceptions.
            _logsi.LogObject(SILevel.Error, MSG_TRACE_METHOD_RESPONSE.format(serviceMethodName), resp)
            _logsi.LogSource(SILevel.Error, MSG_TRACE_METHOD_RESPONSE_BODY, resp.text, SISourceId.Xml)
            raise XPWException("An exception occured while processing web-service response \"errorText\" details for method \"{0}\"!".format(serviceMethodName), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    @staticmethod
    def DictHasKey(oDict:dict, keyName:str) -> bool:
        """
        Checks a dictionary for the specified key name.

        Args:
            oDict (dict):
                Dictionary to check for the specified key name.
            keyName (str):
                Key name to check for.

        Returns:
            True if the specified key name exists in the dictionary; otherwise, False.
        """
        # validations.
        if (oDict == None):
            return False
        if (keyName == None) or (len(keyName) ==0):
            return False

        # prepare for comparison.
        keyName = keyName.lower()

        # check dictionary for the key name.
        for key in oDict.keys():
            if (key.lower() == keyName):
                return True

        # key name not found - return False.
        return False


    @staticmethod
    def GetDictCollectionItems(oDict:dict, keyNameCollection:str, keyNameItem:str) -> dict:
        """
        Checks a dictionary for the specified collection key name, and verifies
        it contains at least one key underneath it with the specified KeyNameItem name.

        Args:
            oDict (dict):
                Dictionary to check for the specified collection key and child item key.
            keyNameCollection (str):
                Key name to check for that contains a collection of nodes.
            keyNameItem (str):
                Item Key name to check for that contains a child item.

        Returns:
            A dictionary of item key names, or an empty dictionary if none were found.

        This method is useful for parsing collection responses and their underlying item nodes.  
        For example:  

        <Cameras>  
          <CameraInfo />  
          <CameraInfo />  
        </Cameras>  
        """
        # by default, return an empty dictionary.
        oResult = {}

        # validations.
        if (oDict == None):
            return oResult
        if (keyNameCollection == None) or (len(keyNameCollection) == 0):
            return oResult

        # does results dictionary contain the specified collection key?
        if (not XPWWebServiceBase.DictHasKey(oDict, keyNameCollection)):
            return oResult

        # map the collection node.
        collNode:dict = oDict[keyNameCollection]

        # does collection key contain any item keys?
        if (not XPWWebServiceBase.DictHasKey(collNode, keyNameItem)):
            return oResult

        # trace.
        _logsi.LogVerbose("Processing dictionary collection node \"<{0}>\" and any \"<{1}>\" item nodes".format(keyNameCollection, keyNameItem))

        # if only one item in the collection, then it's a single string.
        # in this case, make it an array so it can be processed the same as an array.
        if (not isinstance(collNode[keyNameItem],list)):
            oResult = [collNode[keyNameItem]]
            return oResult

        # return a reference to the collection items.
        return collNode[keyNameItem]


    @staticmethod
    def GetDictItems(oDict:dict, keyNameItem:str) -> dict:
        """
        Checks a dictionary for the specified item key name, and verifies it contains at 
        least one occurance.

        Args:
            oDict (dict):
                Dictionary to check for the specified collection key and child item key.
            keyNameItem (str):
                Item Key name to check for that contains a child item.

        Returns:
            A dictionary of item key names, or an empty dictionary if none were found.

        This method is useful for parsing collection responses and their underlying item nodes.  
        For example:  

        <ServiceInfo>  
          <Name />  
        </ServiceInfo>  
        <ServiceInfo>  
          <Name />  
        </ServiceInfo>  
        """
        # by default, return an empty dictionary.
        oResult = {}

        # validations.
        if (oDict == None):
            return oResult
        if (keyNameItem == None) or (len(keyNameItem) == 0):
            return oResult

        # does results dictionary contain the specified collection key?
        if (not XPWWebServiceBase.DictHasKey(oDict, keyNameItem)):
            return oResult

        # trace.
        #_logsi.LogVerbose(MSG_TRACE_PROCESSING_DICTIONARY.format(keyNameItem))  # TODO - remove?

        # if only one item in the collection, then it's a single string.
        # in this case, make it an array so it can be processed the same as an array.
        if (not isinstance(oDict[keyNameItem],list)):
            oResult = [oDict[keyNameItem]]
            return oResult

        # return a reference to the collection items.
        return oDict[keyNameItem]


    @staticmethod
    def GetDictKeyValueBool(oDict:dict, keyName:str, raiseExceptionIfNotFound:bool=False) -> bool:
        """
        Checks a dictionary for the specified key name and returns a boolean value if the
        key exists; otherwise, null is returned.

        Args:
            oDict (dict):
                Dictionary to check for the specified key name.
            keyName (str):
                Key name to check for.
            raiseExceptionIfNotFound (bool):
                True to raise an Exception if the specified keyName is not found in the dictionary;  
                otherwise, False.  
                Default value: False  

        Returns:
            The boolean value of the specified key name if the key exists; otherwise, null.
        """
        # does dictionary contain the key?
        if (XPWWebServiceBase.DictHasKey(oDict, keyName)):

            value = str(oDict[keyName])
            return value.lower() in ("yes", "true", "t", "1")

        else:

            # key was not found - are we raising an exception?  if so, then do it!
            if (raiseExceptionIfNotFound):
                raise Exception(XPWAppMessages.DICTIONARY_KEY_NOT_FOUND_ERROR.format(keyName))

        # otherwise, return null.
        return None


    @staticmethod
    def GetDictKeyValueDateTime(oDict:dict, keyName:str, raiseExceptionIfNotFound:bool=False, excludeMicroseconds:bool=False, excludeTimeZoneInfo:bool=True) -> datetime:
        """
        Checks a dictionary for the specified key name and returns a datetime value if the
        key exists; otherwise, null is returned.

        Args:
            oDict (dict):
                Dictionary to check for the specified key name.
            keyName (str):
                Key name to check for.
            raiseExceptionIfNotFound (bool):
                True to raise an Exception if the specified keyName is not found in the dictionary  
                or the value could not be converted to a datetime object; otherwise, False.  
                Default value: False  
            excludeMicroseconds (bool):
                If True, only the first 19 characters of the date string will be kept - this
                assumes that the datetime string is in "YYYY-MM-DDTHH:MM:SS" format.  
                Default value: False  
            excludeTimeZoneInfo (bool):
                If True, then timezone info (tzinfo) is removed from the datetime value.  
                This can prevent "can't subtract offset-naive and offset-aware datetimes" exceptions 
                when comparing datetimes.  
                Default value: True  

        Returns:
            The datetime value of the specified key name if the key exists; otherwise, null.

        Supported examples for datetime string are:
        - "0001-01-01T00:00:00.0000000"  
        - "2023-07-24T17:12:31.0210000Z"  
        - "2023-07-24T17:12:31.0210Z"  
        - "2023-07-24T17:12:31Z"  
        """
        oResult:datetime = None
                
        # does dictionary contain the key?
        if (XPWWebServiceBase.DictHasKey(oDict, keyName)):

            datetime_str = oDict[keyName]

            # is it a datetime value? if so, then return the value.
            if (isinstance(datetime_str, datetime)):
                oResult = datetime_str

            # is it a string value? if so, then convert it to a datetime.
            elif (isinstance(datetime_str, str)):

                try:

                    datetime_len:int = len(datetime_str)
                    
                    # if datetime is "0001-00-00 ..." then it denotes an uninitialized datetime;
                    # don't bother parsing it - just create the datetime object and return it.
                    if (datetime_len > 9) and (datetime_str.startswith("0001-01-01")):
                        return datetime(1,1,1,0,0,0,0)
                    
                    # figure out which format the datetime is in based upon it's string representation:
                    if (datetime_len == 28):     # e.g. "2023-07-24T17:12:31.0210000Z"
                        oResult = datetime.strptime(datetime_str[:-4]+"Z", "%Y-%m-%dT%H:%M:%S.%f%z")
                    elif (datetime_len == 23):   # e.g. "2023-06-26T23:49:14.05Z"
                        oResult = datetime.strptime(datetime_str[:-1]+"Z", "%Y-%m-%dT%H:%M:%S.%f%z")
                    elif (datetime_len == 24):   # e.g. "2023-06-26T23:49:14.051Z"
                        oResult = datetime.strptime(datetime_str[:-2]+"Z", "%Y-%m-%dT%H:%M:%S.%f%z")
                    elif (datetime_len == 20):   # e.g. "2023-07-24T17:12:31Z"
                        oResult = datetime.strptime(datetime_str[:-4]+"Z", "%Y-%m-%dT%H:%M:%S%z")
                    elif (datetime_len == 19):   # e.g. "2023-07-24T17:12:31"
                        oResult = datetime.strptime(datetime_str+"Z", "%Y-%m-%dT%H:%M:%S%z")
                    elif (datetime_len == 33) and (datetime_str[datetime_len-3:datetime_len-2] == ":"):
                        # 7 digit MS to 6 digits # e.g. "2023-09-07T12:55:54.3970000-05:00"                        
                        # only use first 6 digits of microseconds value, and then try to convert it.
                        tzOffset = datetime_str[datetime_len-6:datetime_len]
                        dtValue6MS =  datetime_str[0:datetime_len-7]
                        oResult = datetime.strptime(dtValue6MS + tzOffset, "%Y-%m-%dT%H:%M:%S.%f%z")
                    else:                        # e.g. "2023-07-24T17:12:31.0210Z"
                        oResult = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%f%Z")

                except Exception as ex:

                    # if datetime could not be parsed then just set it to null / None.
                    oResult = None

            else:
                
                # if key value is not a datetime nor a string, then just set it to null / None.
                oResult = None
                
            # if key value could not be converted to a datetime then raise an exception
            # if asked to do so; otherwise, just return null / None.
            if (oResult == None):
                if (raiseExceptionIfNotFound):
                    raise Exception("The \"<{0}>\" value contains a value that is either null or not a recognized datetime.".format(keyName))

            else:
                    
                # at this point we have a valid datetime result!

                # are we dropping microseconds?
                if (excludeMicroseconds):
                    oResult = datetime(oResult.year, oResult.month, oResult.day, oResult.hour, oResult.minute, oResult.second, 0)
                
                # are we removing timezone info?
                # this can prevent "can't subtract offset-naive and offset-aware datetimes" exceptions 
                # when comparing datetimes.
                if (excludeTimeZoneInfo):
                    oResult = oResult.replace(tzinfo=None)

            # return datetime to caller.
            return oResult
        
        else:

            # key was not found - are we raising an exception?  if so, then do it!
            if (raiseExceptionIfNotFound):
                raise Exception(XPWAppMessages.DICTIONARY_KEY_NOT_FOUND_ERROR.format(keyName))

        # otherwise, return null.
        return None


    @staticmethod
    def GetDictKeyValueDict(oDict:dict, keyName:str, raiseExceptionIfNotFound:bool=False) -> datetime:
        """
        Checks a dictionary for the specified key name and returns the value if the
        key exists; otherwise, null is returned.

        Args:
            oDict (dict):
                Dictionary to check for the specified key name.
            keyName (str):
                Key name to check for.
            raiseExceptionIfNotFound (bool):
                True to raise an Exception if the specified keyName is not found in the dictionary;  
                otherwise, False.  
                Default value: False  

        Returns:
            The value of the specified key name if the key exists; otherwise, null.
        """
        # does dictionary contain the key?
        if (XPWWebServiceBase.DictHasKey(oDict, keyName)):

            value = oDict[keyName]

            # is it a dict value? if so, then return the value.
            if (isinstance(value, dict)):
                return value

            # if not a dict, then return None.
            return None

        else:

            # key was not found - are we raising an exception?  if so, then do it!
            if (raiseExceptionIfNotFound):
                raise Exception(XPWAppMessages.DICTIONARY_KEY_NOT_FOUND_ERROR.format(keyName))

        # otherwise, return null.
        return None


    @staticmethod
    def GetDictKeyValueFloat(oDict:dict, keyName:str, raiseExceptionIfNotFound:bool=False) -> float:
        """
        Checks a dictionary for the specified key name and returns a float value if the
        key exists; otherwise, null is returned.

        Args:
            oDict (dict):
                Dictionary to check for the specified key name.
            keyName (str):
                Key name to check for.
            raiseExceptionIfNotFound (bool):
                True to raise an Exception if the specified keyName is not found in the dictionary;  
                otherwise, False.  
                Default value: False  

        Returns:
            The float value of the specified key name if the key exists; otherwise, null.
        """
        # does dictionary contain the key?
        if (XPWWebServiceBase.DictHasKey(oDict, keyName)):

            value = oDict[keyName]

            # is it a float value? if so, then return the value.
            if (isinstance(value, float)):
                return value

            # is it an integer value? if so, then convert it to float and return the value.
            if (isinstance(value, int)):
                return float(value)

            # is it an string value? if so, then convert it to a float.
            if (isinstance(value, str)):

                try:
                    return float(value)
                except Exception as ex:
                    return None

        else:

            # key was not found - are we raising an exception?  if so, then do it!
            if (raiseExceptionIfNotFound):
                raise Exception(XPWAppMessages.DICTIONARY_KEY_NOT_FOUND_ERROR.format(keyName))

        # otherwise, return null.
        return None


    @staticmethod
    def GetDictKeyValueInt(oDict:dict, keyName:str, raiseExceptionIfNotFound:bool=False) -> int:
        """
        Checks a dictionary for the specified key name and returns a integer value if the
        key exists; otherwise, null is returned.

        Args:
            oDict (dict):
                Dictionary to check for the specified key name.
            keyName (str):
                Key name to check for.
            raiseExceptionIfNotFound (bool):
                True to raise an Exception if the specified keyName is not found in the dictionary;  
                otherwise, False.  
                Default value: False  

        Returns:
            The integer value of the specified key name if the key exists; otherwise, null.
        """
        # does dictionary contain the key?
        if (XPWWebServiceBase.DictHasKey(oDict, keyName)):

            value = oDict[keyName]

            # is it an integer value? if so, then return the value.
            if (isinstance(value, int)):
                return value

            # is it an string value? if so, then convert it to an integer.
            if (isinstance(value, str)):

                try:
                    return int(value)
                except Exception as ex:
                    return None

        else:

            # key was not found - are we raising an exception?  if so, then do it!
            if (raiseExceptionIfNotFound):
                raise Exception(XPWAppMessages.DICTIONARY_KEY_NOT_FOUND_ERROR.format(keyName))

        # otherwise, return null.
        return None


    @staticmethod
    def GetDictKeyValueString(oDict:dict, keyName:str, raiseExceptionIfNotFound:bool=False) -> str:
        """
        Checks a dictionary for the specified key name and returns a string value if the
        key exists; otherwise, null is returned.

        Args:
            oDict (dict):
                Dictionary to check for the specified key name.
            keyName (str):
                Key name to check for.
            raiseExceptionIfNotFound (bool):
                True to raise an Exception if the specified keyName is not found in the dictionary;  
                otherwise, False.  
                Default value: False  

        Returns:
            The string value of the specified key name if the key exists; otherwise, null.
        """
        # does dictionary contain the key?
        if (XPWWebServiceBase.DictHasKey(oDict, keyName)):

            value = oDict[keyName]

            # is it a string value? if so, then return the value.
            if (isinstance(value, str)):
                return value

        else:

            # key was not found - are we raising an exception?  if so, then do it!
            if (raiseExceptionIfNotFound):
                raise Exception(XPWAppMessages.DICTIONARY_KEY_NOT_FOUND_ERROR.format(keyName))

        # otherwise, return null.
        return None


    def GetXmlResponseDictionary(self, responseXml:str, webserviceMethod:str, searchNode:str, searchNamespaces:dict=None, raiseExceptionIfNotFound:bool=True) -> dict:
        """
        Parses XProtect web-services response for the given block of XML that is specified 
        by the searchNode argument, and uses the xmltodict package to convert the
        found result to a dictionary.

        Args:
            responseXml (str):
                String that contains the XML response of the called web-service method.
            webserviceMethod (str):
                Name of the XProtect web-service method that was called.
                Example: "LoginBasicUser"
            searchNode (str):
                XML node to search for in the response (case-sensitive).
                Example: "LoginResult"
            searchNamespaces (dict):
                XML namespaces to override on the xmltodict parse method.  This allows the
                xmltodict parser to correctly process XML namespaces in the response.
                Example: { 'http://videoos.net/2/XProtectCSServiceRegistration':None, 'http://schemas.microsoft.com/2003/10/Serialization/Arrays':None }
            raiseExceptionIfNotFound (bool):
                True to raise an Exception if the specified searchNode is not found in the responseXml;  
                otherwise, False.  
                Default value: True  

        Raises:
            Exception:
                If the start or end nodes could not be found, or if xmltodict could not
                create a dictionary from the found block of xml.

        Returns:
            An dictionary that represents the desired XML response node, or null (None)
            if no items were returned.
        """
        dictRslt:dict = None

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)
            _logsi.LogSource(SILevel.Debug, "Searching xml for \"{0}\" node".format(searchNode), responseXml, SISourceId.Xml)

            # formulate search keys.
            keyStart:str = "<{0} xmlns".format(searchNode)      # search node start with namespace (e.g. "<xxxResult xmlns").
            keyStartNoNS:str = "<{0}>".format(searchNode)       # search node start with no namespace (e.g. "<xxxResult>").
            keyStartNoHtml:str = searchNode                     # search node start with no html decoration.
            keyEnd:str = "</{0}>".format(searchNode)            # search node end with no namespace (e.g. "</xxxResult>").
            keyStartNoItems:str = "<{0} />".format(searchNode)  # search node start and end with no items (e.g. "<xxxResult />").

            # find the starting position of the xml node (e.g. "<xxxResult xmlns").
            # it should be the 4th entry deep (SoapEnvelope, SoapBody, xxxResponse, xxxResult).
            idxStart:int = responseXml.find(keyStart)

            # if not found, then search for the key with no namespace (e.g. "<xxxResult>").
            if (idxStart == -1):
                idxStart = responseXml.find(keyStartNoNS)

            # if not found, then search for the key with no items (e.g. "<xxxResult />").
            if (idxStart == -1):
                idxStart = responseXml.find(keyStartNoItems)

                # if found, then it denotes that no matching items were returned.
                if (idxStart > -1):
                    idxEnd = idxStart + len(keyStartNoItems)

                    # trace.
                    if (_logsi.IsOn(SILevel.Debug)):
                        _logsi.LogSource(SILevel.Debug, "{0} node found, but no child nodes were returned".format(searchNode), responseXml[idxStart:idxEnd], SISourceId.Xml)

                    # return None, as there were no items returned by the web-service.
                    return None

            # find the ending position of the xml node (e.g. "</xxxResult>").
            idxEnd:int = responseXml.rfind(keyEnd)

            # did we find the desired node in the xml?
            if (idxStart > -1) and (idxEnd > -1):

                # yes - include the ending key.
                idxEnd = idxEnd + len(keyEnd)

                # trace.
                if (_logsi.IsOn(SILevel.Debug)):
                    _logsi.LogSource(SILevel.Debug, "{0} node found".format(searchNode), responseXml[idxStart:idxEnd], SISourceId.Xml)
                    _logsi.LogDebug("Converting {0} node inner xml to dictionary".format(searchNode))

                # convert xml to dictionary.
                # this will also process namespaces if desired.
                dictRslt = xmltodict.parse(responseXml[idxStart:idxEnd],
                                           process_namespaces=True,
                                           namespaces=searchNamespaces)

                # trace.
                _logsi.LogObjectValue(SILevel.Debug, "{0} node dictionary".format(searchNode), dictRslt[searchNode])
                _logsi.LogDebug("Parsing XProtect {0} web-service method response dictionary".format(webserviceMethod))

                # return dictionary.
                return dictRslt[searchNode]

            else:

                if (raiseExceptionIfNotFound):
                    # if we did not find the desired node then it's an error.
                    raise Exception("Could not locate \"{0}\" node in XML response.".format(searchNode))
                else:
                    return None

        except Exception as ex:

            _logsi.LogException("Could not parse web-service response.", ex)
            raise 

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def LoginBasicUser(self, username:str, password:str, currentToken:str="") -> XPWLoginInfo:
        """
        Authenticates a user with the specified Basic User login account.

        Args:
            username (str):
                Basic account type User Name to authenticate.
            password (str):
                Basic account type Password for the specified User Name to authenticate.
            currentToken (str):
                If renewing an existing login token, the value of a previously generated login token;
                otherwise, an empty string if this is a new Login or you don't wish to renew a token.

        Raises:
            XPWWebServiceException:
                The XProtect Web Server returned a failed response.
            XPWException:
                userName argument was not supplied.  
                password argument was not supplied.  
                The method fails for any reason.  

        Returns:
            An XPWLoginInfo class that contains Login details.

        The ManagementServer/ServerCommandService.svc Login method is used to authenticate the user credentials.
        
        This method can also be used to renew a token that was generated by a previous call to 
        this method.

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/XPWWebServiceBase/LoginBasicUser.py
        ```
        </details>
        """
        serviceMethodName:str = "LoginBasicUser"
        loginInfo:XPWLoginInfo = None

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            with self._fLock:

                # trace.
                _logsi.LogMessage("Logging into XProtect Management Server using Basic User credentials")

                # validations.
                if (username == None) or (len(username) == 0):
                    raise Exception(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("userName"))
                if (password == None) or (len(password) == 0):
                    raise Exception(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("password"))
                if (currentToken == None):
                    currentToken = ""

                # SOAP request example(url, headers, body):

                # POST https://localhost/ManagementServer/ServerCommandService.svc

                #Authorization: Basic eHBhZG1pbjpDcmF6eSQxeHBh
                #User-Agent: PostmanRuntime/7.32.3
                #Accept: */*
                #Host: win10vm.netlucas.com
                #Accept-Encoding: gzip, deflate, br
                #Connection: keep-alive
                #Content-Type: text/xml; charset=utf-8
                #Content-Length: 413
                #SOAPAction: http://videoos.net/2/XProtectCSServerCommand/IServerCommandService/Login

                #<?xml version="1.0" encoding="utf-8"?>
                #<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                #  <s:Body>
                #    <Login xmlns="http://videoos.net/2/XProtectCSServerCommand">
                #      <instanceId>00000000-0000-0000-0000-000000000001</instanceId>
                #      <currentToken>TOKEN#287d9304-9482-4c67-94ef-dc12bd5b4722#win10vm//ServerConnector#</currentToken>
                #    </Login>
                #  </s:Body>
                #</s:Envelope>

                # formulate xprotect svc service request parameters (url, headers, body).
                requrl:str = "{0}/ManagementServer/ServerCommandService.svc".format(self.ManagementServerUrlPrefix)

                reqheaders:list[str] = {
                    "Accept": "*/*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Connection": "keep-alive",
                    "Content-Type": "text/xml; charset=utf-8",
                    "SOAPAction": "http://videoos.net/2/XProtectCSServerCommand/IServerCommandService/Login",
                    }

                reqbody:str = \
                    """
                    <?xml version="1.0" encoding="utf-8"?>
                    <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                      <s:Body>
                        <Login xmlns="http://videoos.net/2/XProtectCSServerCommand">
                          <instanceId>{instanceId}</instanceId>
                          <currentToken>{currentToken}</currentToken>
                        </Login>
                      </s:Body>
                    </s:Envelope>
                    """.format(instanceId=self.InstanceId, 
                               currentToken=currentToken)

                # create request object.
                req:Request = Request('POST', requrl, headers=reqheaders, data=inspect.cleandoc(reqbody), auth=(username, password))

                # prepare the request.
                reqSess = Session()
                reqprep = reqSess.prepare_request(req)

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST.format(serviceMethodName), reqprep)
                    _logsi.LogSource(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_BODY.format(serviceMethodName), reqprep.body, SISourceId.Xml)
                    _logsi.LogDictionary(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_HEADERS.format(serviceMethodName), reqprep.headers)

                # send the request.
                resp = reqSess.send(reqprep, verify=self.IsSslVerifyEnabled)

                # check response code, and raise an exception if it failed.
                oDict:dict = self.CheckResponseStatusCode(serviceMethodName, req, resp, "LoginResult", None, True)

                # process service response dictionary item node(s).
                loginInfo:XPWLoginInfo = self._Parse_Login(oDict)

                # set additional login info properties.
                loginInfo.AuthenticationType = XPWAuthenticationType.Basic
                loginInfo.UserName = username
                loginInfo.Password = password

                # trace.
                _logsi.LogObject(SILevel.Verbose, "LoginInfo object created", loginInfo, excludeNonPublic=True)

                # set internal reference.
                self._fLoginInfo = loginInfo

                # return login info to caller.
                return loginInfo

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def LoginWindowsUser(self, username:str, password:str, currentToken:str="") -> XPWLoginInfo:
        """
        Authenticates a user with the specified Windows User login account.

        Args:
            username (str):
                Basic account type User Name to authenticate.
            password (str):
                Basic account type Password for the specified User Name to authenticate.
            currentToken (str):
                If renewing an existing login token, the value of a previously generated login token;
                otherwise, an empty string if this is a new Login or you don't wish to renew a token.

        Raises:
            XPWWebServiceException:
                The XProtect Web Server returned a failed response.
            XPWException:
                userName argument was not supplied.  
                password argument was not supplied.  
                The method fails for any reason.  

        Returns:
            An XPWLoginInfo class that contains Login details.

        The ServerAPI/ServerCommandService.asmx Login method is used to authenticate the user credentials.
        
        This method can also be used to renew a token that was generated by a previous call to 
        this method.

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/XPWWebServiceBase/LoginWindowsUser.py
        ```
        </details>
        """
        serviceMethodName:str = "LoginWindowsUser"
        loginInfo:XPWLoginInfo = None

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            with self._fLock:

                # trace.
                _logsi.LogMessage("Logging into XProtect Management Server using Windows User credentials")

                # validations.
                if (username == None) or (len(username) == 0):
                    raise Exception(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("userName"))
                if (password == None) or (len(password) == 0):
                    raise Exception(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("password"))
                if (currentToken == None):
                    currentToken = ""

                # SOAP request example(url, headers, body):

                # POST http://localhost/ServerAPI/ServerCommandService.asmx

                #Authorization: Basic WFByb3RlY3RBZG1pbjpYUEFVc2VyJDE=
                #User-Agent: PostmanRuntime/7.32.3
                #Accept: */*
                #Host: win10vm.netlucas.com:80
                #Accept-Encoding: gzip, deflate, br
                #Connection: keep-alive
                #Content-Length: 345
                #Content-Type: text/xml; charset=utf-8
                #SOAPAction: http://videoos.net/2/XProtectCSServerCommand/Login

                #<?xml version="1.0" encoding="utf-8"?>
                #<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
                #  <soap:Body>
                #    <Login xmlns="http://videoos.net/2/XProtectCSServerCommand">
                #      <instanceId>00000000-0000-0000-0000-000000000001</instanceId>
                #      <currentToken>TOKEN#287d9304-9482-4c67-94ef-dc12bd5b4722#win10vm//ServerConnector#</currentToken>
                #    </Login>
                #  </soap:Body>
                #</soap:Envelope>

                # formulate xprotect asmx service request parameters (url, headers, body).
                requrl:str = "{0}/ServerAPI/ServerCommandService.asmx".format(self.ServerApiUrlPrefix)

                reqheaders:list[str] = { 
                    "Accept": "*/*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Connection": "keep-alive",
                    "Content-Type": "text/xml; charset=utf-8",
                    "SOAPAction": "http://videoos.net/2/XProtectCSServerCommand/Login",
                    }

                reqbody:str = \
                    """
                    <?xml version="1.0" encoding="utf-8"?>
                    <s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope">
                      <s:Body>
                        <Login xmlns="http://videoos.net/2/XProtectCSServerCommand">
                          <instanceId>{instanceId}</instanceId>
                          <currentToken>{currentToken}</currentToken>
                        </Login>
                      </s:Body>
                    </s:Envelope>
                    """.format(instanceId=self.InstanceId, 
                               currentToken=currentToken)

                # create request object.
                req:Request = Request('POST', requrl, headers=reqheaders, data=inspect.cleandoc(reqbody), auth=(username, password))

                # prepare the request.
                reqSess = Session()
                reqprep = reqSess.prepare_request(req)

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST.format(serviceMethodName), reqprep)
                    _logsi.LogSource(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_BODY.format(serviceMethodName), reqprep.body, SISourceId.Xml)
                    _logsi.LogDictionary(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_HEADERS.format(serviceMethodName), reqprep.headers)

                # send the request.
                resp = reqSess.send(reqprep, verify=self.IsSslVerifyEnabled)

                # check response code, and raise an exception if it failed.
                oDict:dict = self.CheckResponseStatusCode(serviceMethodName, req, resp, "LoginResult", None, True)

                # process service response dictionary item node(s).
                loginInfo:XPWLoginInfo = self._Parse_Login(oDict)

                # set additional login info properties.
                loginInfo.AuthenticationType = XPWAuthenticationType.Windows
                loginInfo.UserName = username
                loginInfo.Password = password

                # trace.
                _logsi.LogObject(SILevel.Verbose, "LoginInfo object created", loginInfo, excludeNonPublic=True)

                # set internal reference.
                self._fLoginInfo = loginInfo

                # return login info to caller.
                return loginInfo

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    @staticmethod
    def ParseCollectionItemStrings(arrayList:list[str], oDict:dict, keyNameCollection:str, keyNameItem:str) -> None:
        """
        Checks a dictionary for the specified outer key name, and returns
        a string array of values from the inner key name.

        Args:
            arrayList (list[str]):
                String array to add the found strings to.
            oDict (dict):
                Dictionary to check for the specified key name.
            keyNameCollection (str):
                Key name to check for that contains a collection of nodes.
            keyNameInner (str):
                Inner Key name to check for that contains the strings to add.

        Returns:
            An array of string values from the inner key.
            An array will always be returned, even if it is empty.

        This method is useful for parsing repeated occurances of single string
        values in a parent node.  For example:

        <DeviceIds>
          <guid>0c60e7bf-9d57-4047-b623-e76d375a1fe6</guid>
          <guid>8a381bcc-7752-45dd-91f2-3aa8345d37db</guid>
        </DeviceIds>
        """
        # validations.
        if (arrayList == None):
            return
        if (oDict == None):
            return
        if (keyNameCollection == None) or (len(keyNameCollection) ==0):
            return
        if (keyNameItem == None) or (len(keyNameItem) ==0):
            return

        # does the dictionary contain the collection key?
        if (XPWWebServiceBase.DictHasKey(oDict, keyNameCollection)):

            # yes - map the collection key.  If it's value is null, then there's nothing to do.
            nodeList = oDict[keyNameCollection]
            if (nodeList == None):
                return

            # does the collection contain a child item key?
            if (XPWWebServiceBase.DictHasKey(nodeList, keyNameItem)):

                # yes - map the child key.  If it's value is null, then there's nothing to do.
                nodeList = nodeList[keyNameItem]
                if (nodeList == None):
                    return

                # The following checks are necessary due to the way xmltodict converts xml child nodes
                # to dictionary items.  
                # If there are multiple child nodes, then it converts them to an array of string items.  
                # If there is a single child node, then it converts it to a string (no array).  
                    
                # xmltodict conversion example, multiple child nodes:
                #<DeviceIds>
                #  <guid>3be8e5c6-939a-4a31-bb89-2205e5d54d15</guid>
                #  <guid>f0f31f69-36a2-46a3-80b6-48e4bf617db8</guid>
                #</DeviceIds>
                # Dictionary Result:
                # { 'guid': ['3be8e5c6-939a-4a31-bb89-2205e5d54d15','f0f31f69-36a2-46a3-80b6-48e4bf617db8'] }

                # xmltodict conversion example, single child node:
                #<DeviceIds>
                #  <guid>3be8e5c6-939a-4a31-bb89-2205e5d54d15</guid>
                #</DeviceIds>
                # Dictionary Result:
                # { 'guid': '3be8e5c6-939a-4a31-bb89-2205e5d54d15' }

                # is the value a single string?
                if (isinstance(nodeList, str)):
                    arrayList.append(nodeList)
                    return

                # is the value an array of strings?
                if (isinstance(nodeList, list)):
                    for node in nodeList:
                        arrayList.append(node)

        return
