"""
Module: xpwserviceregistrationservice.py

<details>
  <summary>Revision History</summary>

| Date       | Version     | Description
| ---------- | ----------- | ----------------------
| 2023/07/11 | 1.0.0.0     | Initial Version.  

</details>
"""


# external package imports.
import inspect
import json
from requests import Request, Session
from smartinspectpython.sisourceid import SISourceId 

# our package imports.
from .xpwappmessages import XPWAppMessages
from .xpwauthenticationtype import XPWAuthenticationType
from .xpwcollection import XPWCollection
from .xpwexception import XPWException
from .xpwlogininfo import XPWLoginInfo
from .xpwservice import XPWService
from .xpwserviceendpoint import XPWServiceEndpoint
from .xpwwebservicebase import XPWWebServiceBase

# our package constants.
from .xpwconst import (
    MSG_TRACE_METHOD_REQUEST,
    MSG_TRACE_METHOD_REQUEST_BODY,
    MSG_TRACE_METHOD_REQUEST_HEADERS,
    MSG_TRACE_PROCESSING_DICTIONARY,
    MSG_TRACE_RESULT_OBJECT
)

# get smartinspect logger reference.
from smartinspectpython.siauto import SISession, SILevel, SIAuto
_logsi:SISession = SIAuto.Main

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWServiceRegistrationService(XPWWebServiceBase):
    """
    The Service Registration SOAP web service provides access to a dictionary of 
    services available in a given installation.

    It can be used to retrieve all installed services and their URLs. When multiple 
    services of the same type are installed, it can be used as a round-robin access 
    for load sharing.

    The service also enables you to register your own services and thus make them 
    available for lookup by other components in your integration or by other 
    integrations wanting to utilize your service.
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
                The method fails for any reason.  
        """
        serviceMethodName:str = "__init__"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug) 

            # initialize the base class.
            super().__init__(loginInfo)

            # trace.
            _logsi.LogObject(SILevel.Verbose, "XPWServiceRegistrationService Object Initialized", self)

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_ServiceEndpoint(self, oDict:dict, serviceMethodName:str) -> XPWServiceEndpoint:
        """
        Parses dictionary data for ServiceEndpoint details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetServices", etc.

        Returns:
            An XPWServiceEndpoint class that represents the dictionary details.
        """
        oItem:XPWServiceEndpoint = None
        methodKeyName:str = "ServiceEndpoint"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            # <ServiceEndpoint>
            #   <uri>http://win10vm/ManagementServer/ServerCommandService.svc</uri>
            #   <authentication>Windows</authentication>
            #   <name>ServerCommandService</name>
            #   <description>Endpoint for ServerCommandService using windows authentication</description>
            # </ServiceEndpoint>
            # <ServiceEndpoint>
            #   <uri>https://win10vm/ManagementServer/ServerCommandService.svc</uri>
            #   <authentication>Basic</authentication>
            #   <name>ServerCommandService</name>
            #   <description>Endpoint for ServerCommandService using basic user authentication</description>
            # </ServiceEndpoint>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWServiceEndpoint = XPWServiceEndpoint()
                oItem.Authentication = self.GetDictKeyValueString(oDict, "authentication")
                oItem.Description = self.GetDictKeyValueString(oDict, "description")
                oItem.Name = self.GetDictKeyValueString(oDict, "name")
                oItem.Uri = self.GetDictKeyValueString(oDict, "uri")

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

            # return object to caller.
            return oItem

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_ServiceInfo(self, oDict:dict, serviceMethodName:str) -> XPWService:
        """
        Parses dictionary data for ServiceInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetServices", etc.

        Returns:
            An XPWService class that represents the dictionary details.
        """
        oItem:XPWService = None
        methodKeyName:str = "XPWService"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            # <ServiceInfo>
            #   <type>a10cd823-bb4e-4d31-a162-dd236fc78fa6</type>
            #   <instance>fc9e48ce-a39b-4327-8b92-32b012688944</instance>
            #   <uri>
            #     <string>https://win10vm/</string>
            #     <string>http://win10vm/</string>
            #   </uri>
            #   <name>Management Server</name>
            #   <description />
            #   <trusted>true</trusted>
            #   <enabled>true</enabled>
            #   <endpoints>
            #     <ServiceEndpoint>
            #       ...
            #     </ServiceEndpoint>
            #   </endpoints>
            #   <endpointdefinition>&lt;endpoints&gt;&lt;endpoint&gt;...&lt;/endpoint&gt;&lt;/endpoints&gt;</endpointdefinition>
            # </ServiceInfo>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # create new service info object and load base properties.
                oItem:XPWService = XPWService()
                oItem.Description = self.GetDictKeyValueString(oDict, "description")
                oItem.Enabled = self.GetDictKeyValueBool(oDict, "enabled")
                oItem.EndpointDefinition = self.GetDictKeyValueString(oDict, "endpointdefinition")
                oItem.Instance = self.GetDictKeyValueString(oDict, "instance")
                oItem.Name = self.GetDictKeyValueString(oDict, "name")
                oItem.Trusted = self.GetDictKeyValueBool(oDict, "trusted")
                oItem.Type = self.GetDictKeyValueString(oDict, "type")
                self.ParseCollectionItemStrings(oItem.Uri, oDict, "uri", "string")

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "endpoints", "ServiceEndpoint")
                for itemNode in collNodes:
                    oItem.Endpoints.append(self._Parse_ServiceEndpoint(itemNode, serviceMethodName))

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

            # return object to caller.
            return oItem

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def GetServices(self) -> XPWCollection:
        """
        Retrieves a list of services available in a given installation.

        Returns:
            A collection of XPWService objects that contain available service details.

        Raises:
            XPWWebServiceException:
                The XProtect Web-Services Server returned a failed response.
            XPWException:
                The method fails for any other reason.  

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/XPWServiceRegistrationService/GetServices.py
        ```
        </details>
        """
        serviceMethodName:str = "GetServices"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug) 

            with self._fLock:

                # trace.
                _logsi.LogMessage("Retrieving list of available XProtect services")

                # automatic token renewal check and logininfo validation.
                self._AutoTokenRenewalCheck(serviceMethodName)

                # call method based upon authentication type.
                if (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Basic):

                    # formulate xprotect svc service request parameters (url, headers, body).
                    requrl:str = "{0}/ManagementServer/ServiceRegistrationService.svc".format(self.ManagementServerUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://schemas.videoos/ServiceRegistrationService/2008/06/Vmo/01/IServiceRegistrationService/GetServices",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <GetServices xmlns="http://schemas.videoos/ServiceRegistrationService/2008/06/Vmo/01">
                            </GetServices>
                          </s:Body>
                        </s:Envelope>
                        """

                elif (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Windows):
                    
                    # formulate xprotect asmx service request parameters (url, headers, body).
                    requrl:str = "{0}/ServerAPI/ServiceRegistrationService.asmx".format(self.ServerApiUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSServiceRegistration/GetServices",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <GetServices xmlns="http://videoos.net/2/XProtectCSServiceRegistration">
                            </GetServices>
                          </s:Body>
                        </s:Envelope>
                        """
                                       
                else:
                    
                    # raise authentication type not implemented exception.
                    raise XPWException(XPWAppMessages.LOGININFO_AUTHTYPE_NOTIMPLEMENTED.format(str(self.LoginInfo.AuthenticationType), serviceMethodName), None, _logsi)

                # create request object.
                req:Request = Request('POST', requrl, headers=reqheaders, data=inspect.cleandoc(reqbody), auth=(self.LoginInfo.UserName, self.LoginInfo.Password))

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

                # namespaces used in the response xml for this method.
                rsltNamespaces = { 'http://videoos.net/2/XProtectCSServiceRegistration':None,
                                   'http://schemas.microsoft.com/2003/10/Serialization/Arrays':None,
                                   'http://www.w3.org/2001/XMLSchema-instance':None
                                 }
                
                # check response code; raise an exception if it failed, or return a dictionary with results if it succeeded.
                oDict:dict = self.CheckResponseStatusCode(serviceMethodName, req, resp, "GetServicesResult", rsltNamespaces, True)

                # SOAP response example:
                # <GetServicesResult>
                #   <ServiceInfo>
                #      ...
                #   </ServiceInfo>
                #   <ServiceInfo>
                #      ...
                #   </ServiceInfo>
                # </GetServicesResult>

                # create results collection.
                oResult:XPWCollection = XPWCollection((XPWService))

                # were any results returned?
                if (oDict != None):

                    # process xml result collection item node(s).
                    baseNodes:dict = self.GetDictItems(oDict, "ServiceInfo")
                    for itemNode in baseNodes:
                        oResult.append(self._Parse_ServiceInfo(itemNode, serviceMethodName))
  
                    # trace.
                    _logsi.LogText(SILevel.Verbose, "XPWService Items Summary", str(oResult))

                # return object to caller.
                return oResult

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)
