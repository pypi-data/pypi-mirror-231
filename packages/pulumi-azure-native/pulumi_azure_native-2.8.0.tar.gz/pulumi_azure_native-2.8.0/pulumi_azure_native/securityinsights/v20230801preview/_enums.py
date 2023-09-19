# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ActionType',
    'AlertDetail',
    'AlertProperty',
    'AlertRuleKind',
    'AlertSeverity',
    'AttackTactic',
    'AutomationRuleBooleanConditionSupportedOperator',
    'AutomationRulePropertyArrayChangedConditionSupportedArrayType',
    'AutomationRulePropertyArrayChangedConditionSupportedChangeType',
    'AutomationRulePropertyArrayConditionSupportedArrayConditionType',
    'AutomationRulePropertyArrayConditionSupportedArrayType',
    'AutomationRulePropertyChangedConditionSupportedChangedType',
    'AutomationRulePropertyChangedConditionSupportedPropertyType',
    'AutomationRulePropertyConditionSupportedOperator',
    'AutomationRulePropertyConditionSupportedProperty',
    'ConditionType',
    'ConnectivityType',
    'CustomEntityQueryKind',
    'DataConnectorDefinitionKind',
    'DataConnectorKind',
    'DataTypeState',
    'EntityMappingType',
    'EntityProviders',
    'EntityTimelineKind',
    'EntityType',
    'EventGroupingAggregationKind',
    'FileFormat',
    'FileImportContentType',
    'Flag',
    'HypothesisStatus',
    'IncidentClassification',
    'IncidentClassificationReason',
    'IncidentSeverity',
    'IncidentStatus',
    'IncidentTaskStatus',
    'IngestionMode',
    'Kind',
    'MatchingMethod',
    'MicrosoftSecurityProductName',
    'Mode',
    'MtpProvider',
    'Operator',
    'OwnerType',
    'PackageKind',
    'PermissionProviderScope',
    'PollingFrequency',
    'ProviderName',
    'ProviderPermissionsScope',
    'SecurityMLAnalyticsSettingsKind',
    'SettingKind',
    'SettingType',
    'SettingsStatus',
    'SourceKind',
    'SourceType',
    'Status',
    'SupportTier',
    'ThreatIntelligenceResourceInnerKind',
    'TriggerOperator',
    'TriggersOn',
    'TriggersWhen',
    'UebaDataSources',
]


class ActionType(str, Enum):
    """
    The type of the automation rule action.
    """
    MODIFY_PROPERTIES = "ModifyProperties"
    """
    Modify an object's properties
    """
    RUN_PLAYBOOK = "RunPlaybook"
    """
    Run a playbook on an object
    """
    ADD_INCIDENT_TASK = "AddIncidentTask"
    """
    Add a task to an incident object
    """


class AlertDetail(str, Enum):
    """
    Alert detail
    """
    DISPLAY_NAME = "DisplayName"
    """
    Alert display name
    """
    SEVERITY = "Severity"
    """
    Alert severity
    """


class AlertProperty(str, Enum):
    """
    The V3 alert property
    """
    ALERT_LINK = "AlertLink"
    """
    Alert's link
    """
    CONFIDENCE_LEVEL = "ConfidenceLevel"
    """
    Confidence level property
    """
    CONFIDENCE_SCORE = "ConfidenceScore"
    """
    Confidence score
    """
    EXTENDED_LINKS = "ExtendedLinks"
    """
    Extended links to the alert
    """
    PRODUCT_NAME = "ProductName"
    """
    Product name alert property
    """
    PROVIDER_NAME = "ProviderName"
    """
    Provider name alert property
    """
    PRODUCT_COMPONENT_NAME = "ProductComponentName"
    """
    Product component name alert property
    """
    REMEDIATION_STEPS = "RemediationSteps"
    """
    Remediation steps alert property
    """
    TECHNIQUES = "Techniques"
    """
    Techniques alert property
    """


class AlertRuleKind(str, Enum):
    """
    The kind of the alert rule
    """
    SCHEDULED = "Scheduled"
    MICROSOFT_SECURITY_INCIDENT_CREATION = "MicrosoftSecurityIncidentCreation"
    FUSION = "Fusion"
    ML_BEHAVIOR_ANALYTICS = "MLBehaviorAnalytics"
    THREAT_INTELLIGENCE = "ThreatIntelligence"
    NRT = "NRT"


class AlertSeverity(str, Enum):
    """
    The severity for alerts created by this alert rule.
    """
    HIGH = "High"
    """
    High severity
    """
    MEDIUM = "Medium"
    """
    Medium severity
    """
    LOW = "Low"
    """
    Low severity
    """
    INFORMATIONAL = "Informational"
    """
    Informational severity
    """


class AttackTactic(str, Enum):
    """
    The severity for alerts created by this alert rule.
    """
    RECONNAISSANCE = "Reconnaissance"
    RESOURCE_DEVELOPMENT = "ResourceDevelopment"
    INITIAL_ACCESS = "InitialAccess"
    EXECUTION = "Execution"
    PERSISTENCE = "Persistence"
    PRIVILEGE_ESCALATION = "PrivilegeEscalation"
    DEFENSE_EVASION = "DefenseEvasion"
    CREDENTIAL_ACCESS = "CredentialAccess"
    DISCOVERY = "Discovery"
    LATERAL_MOVEMENT = "LateralMovement"
    COLLECTION = "Collection"
    EXFILTRATION = "Exfiltration"
    COMMAND_AND_CONTROL = "CommandAndControl"
    IMPACT = "Impact"
    PRE_ATTACK = "PreAttack"
    IMPAIR_PROCESS_CONTROL = "ImpairProcessControl"
    INHIBIT_RESPONSE_FUNCTION = "InhibitResponseFunction"


class AutomationRuleBooleanConditionSupportedOperator(str, Enum):
    AND_ = "And"
    """
    Evaluates as true if all the item conditions are evaluated as true
    """
    OR_ = "Or"
    """
    Evaluates as true if at least one of the item conditions are evaluated as true
    """


class AutomationRulePropertyArrayChangedConditionSupportedArrayType(str, Enum):
    ALERTS = "Alerts"
    """
    Evaluate the condition on the alerts
    """
    LABELS = "Labels"
    """
    Evaluate the condition on the labels
    """
    TACTICS = "Tactics"
    """
    Evaluate the condition on the tactics
    """
    COMMENTS = "Comments"
    """
    Evaluate the condition on the comments
    """


class AutomationRulePropertyArrayChangedConditionSupportedChangeType(str, Enum):
    ADDED = "Added"
    """
    Evaluate the condition on items added to the array
    """


class AutomationRulePropertyArrayConditionSupportedArrayConditionType(str, Enum):
    ANY_ITEM = "AnyItem"
    """
    Evaluate the condition as true if any item fulfills it
    """


class AutomationRulePropertyArrayConditionSupportedArrayType(str, Enum):
    CUSTOM_DETAILS = "CustomDetails"
    """
    Evaluate the condition on the custom detail keys
    """
    CUSTOM_DETAIL_VALUES = "CustomDetailValues"
    """
    Evaluate the condition on a custom detail's values
    """


class AutomationRulePropertyChangedConditionSupportedChangedType(str, Enum):
    CHANGED_FROM = "ChangedFrom"
    """
    Evaluate the condition on the previous value of the property
    """
    CHANGED_TO = "ChangedTo"
    """
    Evaluate the condition on the updated value of the property
    """


class AutomationRulePropertyChangedConditionSupportedPropertyType(str, Enum):
    INCIDENT_SEVERITY = "IncidentSeverity"
    """
    Evaluate the condition on the incident severity
    """
    INCIDENT_STATUS = "IncidentStatus"
    """
    Evaluate the condition on the incident status
    """
    INCIDENT_OWNER = "IncidentOwner"
    """
    Evaluate the condition on the incident owner
    """


class AutomationRulePropertyConditionSupportedOperator(str, Enum):
    EQUALS = "Equals"
    """
    Evaluates if the property equals at least one of the condition values
    """
    NOT_EQUALS = "NotEquals"
    """
    Evaluates if the property does not equal any of the condition values
    """
    CONTAINS = "Contains"
    """
    Evaluates if the property contains at least one of the condition values
    """
    NOT_CONTAINS = "NotContains"
    """
    Evaluates if the property does not contain any of the condition values
    """
    STARTS_WITH = "StartsWith"
    """
    Evaluates if the property starts with any of the condition values
    """
    NOT_STARTS_WITH = "NotStartsWith"
    """
    Evaluates if the property does not start with any of the condition values
    """
    ENDS_WITH = "EndsWith"
    """
    Evaluates if the property ends with any of the condition values
    """
    NOT_ENDS_WITH = "NotEndsWith"
    """
    Evaluates if the property does not end with any of the condition values
    """


class AutomationRulePropertyConditionSupportedProperty(str, Enum):
    """
    The property to evaluate in an automation rule property condition.
    """
    INCIDENT_TITLE = "IncidentTitle"
    """
    The title of the incident
    """
    INCIDENT_DESCRIPTION = "IncidentDescription"
    """
    The description of the incident
    """
    INCIDENT_SEVERITY = "IncidentSeverity"
    """
    The severity of the incident
    """
    INCIDENT_STATUS = "IncidentStatus"
    """
    The status of the incident
    """
    INCIDENT_RELATED_ANALYTIC_RULE_IDS = "IncidentRelatedAnalyticRuleIds"
    """
    The related Analytic rule ids of the incident
    """
    INCIDENT_TACTICS = "IncidentTactics"
    """
    The tactics of the incident
    """
    INCIDENT_LABEL = "IncidentLabel"
    """
    The labels of the incident
    """
    INCIDENT_PROVIDER_NAME = "IncidentProviderName"
    """
    The provider name of the incident
    """
    INCIDENT_UPDATED_BY_SOURCE = "IncidentUpdatedBySource"
    """
    The update source of the incident
    """
    INCIDENT_CUSTOM_DETAILS_KEY = "IncidentCustomDetailsKey"
    """
    The incident custom detail key
    """
    INCIDENT_CUSTOM_DETAILS_VALUE = "IncidentCustomDetailsValue"
    """
    The incident custom detail value
    """
    ACCOUNT_AAD_TENANT_ID = "AccountAadTenantId"
    """
    The account Azure Active Directory tenant id
    """
    ACCOUNT_AAD_USER_ID = "AccountAadUserId"
    """
    The account Azure Active Directory user id
    """
    ACCOUNT_NAME = "AccountName"
    """
    The account name
    """
    ACCOUNT_NT_DOMAIN = "AccountNTDomain"
    """
    The account NetBIOS domain name
    """
    ACCOUNT_PUID = "AccountPUID"
    """
    The account Azure Active Directory Passport User ID
    """
    ACCOUNT_SID = "AccountSid"
    """
    The account security identifier
    """
    ACCOUNT_OBJECT_GUID = "AccountObjectGuid"
    """
    The account unique identifier
    """
    ACCOUNT_UPN_SUFFIX = "AccountUPNSuffix"
    """
    The account user principal name suffix
    """
    ALERT_PRODUCT_NAMES = "AlertProductNames"
    """
    The name of the product of the alert
    """
    ALERT_ANALYTIC_RULE_IDS = "AlertAnalyticRuleIds"
    """
    The analytic rule ids of the alert
    """
    AZURE_RESOURCE_RESOURCE_ID = "AzureResourceResourceId"
    """
    The Azure resource id
    """
    AZURE_RESOURCE_SUBSCRIPTION_ID = "AzureResourceSubscriptionId"
    """
    The Azure resource subscription id
    """
    CLOUD_APPLICATION_APP_ID = "CloudApplicationAppId"
    """
    The cloud application identifier
    """
    CLOUD_APPLICATION_APP_NAME = "CloudApplicationAppName"
    """
    The cloud application name
    """
    DNS_DOMAIN_NAME = "DNSDomainName"
    """
    The dns record domain name
    """
    FILE_DIRECTORY = "FileDirectory"
    """
    The file directory full path
    """
    FILE_NAME = "FileName"
    """
    The file name without path
    """
    FILE_HASH_VALUE = "FileHashValue"
    """
    The file hash value
    """
    HOST_AZURE_ID = "HostAzureID"
    """
    The host Azure resource id
    """
    HOST_NAME = "HostName"
    """
    The host name without domain
    """
    HOST_NET_BIOS_NAME = "HostNetBiosName"
    """
    The host NetBIOS name
    """
    HOST_NT_DOMAIN = "HostNTDomain"
    """
    The host NT domain
    """
    HOST_OS_VERSION = "HostOSVersion"
    """
    The host operating system
    """
    IO_T_DEVICE_ID = "IoTDeviceId"
    """
    "The IoT device id
    """
    IO_T_DEVICE_NAME = "IoTDeviceName"
    """
    The IoT device name
    """
    IO_T_DEVICE_TYPE = "IoTDeviceType"
    """
    The IoT device type
    """
    IO_T_DEVICE_VENDOR = "IoTDeviceVendor"
    """
    The IoT device vendor
    """
    IO_T_DEVICE_MODEL = "IoTDeviceModel"
    """
    The IoT device model
    """
    IO_T_DEVICE_OPERATING_SYSTEM = "IoTDeviceOperatingSystem"
    """
    The IoT device operating system
    """
    IP_ADDRESS = "IPAddress"
    """
    The IP address
    """
    MAILBOX_DISPLAY_NAME = "MailboxDisplayName"
    """
    The mailbox display name
    """
    MAILBOX_PRIMARY_ADDRESS = "MailboxPrimaryAddress"
    """
    The mailbox primary address
    """
    MAILBOX_UPN = "MailboxUPN"
    """
    The mailbox user principal name
    """
    MAIL_MESSAGE_DELIVERY_ACTION = "MailMessageDeliveryAction"
    """
    The mail message delivery action
    """
    MAIL_MESSAGE_DELIVERY_LOCATION = "MailMessageDeliveryLocation"
    """
    The mail message delivery location
    """
    MAIL_MESSAGE_RECIPIENT = "MailMessageRecipient"
    """
    The mail message recipient
    """
    MAIL_MESSAGE_SENDER_IP = "MailMessageSenderIP"
    """
    The mail message sender IP address
    """
    MAIL_MESSAGE_SUBJECT = "MailMessageSubject"
    """
    The mail message subject
    """
    MAIL_MESSAGE_P1_SENDER = "MailMessageP1Sender"
    """
    The mail message P1 sender
    """
    MAIL_MESSAGE_P2_SENDER = "MailMessageP2Sender"
    """
    The mail message P2 sender
    """
    MALWARE_CATEGORY = "MalwareCategory"
    """
    The malware category
    """
    MALWARE_NAME = "MalwareName"
    """
    The malware name
    """
    PROCESS_COMMAND_LINE = "ProcessCommandLine"
    """
    The process execution command line
    """
    PROCESS_ID = "ProcessId"
    """
    The process id
    """
    REGISTRY_KEY = "RegistryKey"
    """
    The registry key path
    """
    REGISTRY_VALUE_DATA = "RegistryValueData"
    """
    The registry key value in string formatted representation
    """
    URL = "Url"
    """
    The url
    """


class ConditionType(str, Enum):
    PROPERTY = "Property"
    """
    Evaluate an object property value
    """
    PROPERTY_ARRAY = "PropertyArray"
    """
    Evaluate an object array property value
    """
    PROPERTY_CHANGED = "PropertyChanged"
    """
    Evaluate an object property changed value
    """
    PROPERTY_ARRAY_CHANGED = "PropertyArrayChanged"
    """
    Evaluate an object array property changed value
    """
    BOOLEAN = "Boolean"
    """
    Apply a boolean operator (e.g AND, OR) to conditions
    """


class ConnectivityType(str, Enum):
    """
    type of connectivity
    """
    IS_CONNECTED_QUERY = "IsConnectedQuery"


class CustomEntityQueryKind(str, Enum):
    """
    the entity query kind
    """
    ACTIVITY = "Activity"


class DataConnectorDefinitionKind(str, Enum):
    """
    The data connector kind
    """
    CUSTOMIZABLE = "Customizable"


class DataConnectorKind(str, Enum):
    """
    The data connector kind
    """
    AZURE_ACTIVE_DIRECTORY = "AzureActiveDirectory"
    AZURE_SECURITY_CENTER = "AzureSecurityCenter"
    MICROSOFT_CLOUD_APP_SECURITY = "MicrosoftCloudAppSecurity"
    THREAT_INTELLIGENCE = "ThreatIntelligence"
    THREAT_INTELLIGENCE_TAXII = "ThreatIntelligenceTaxii"
    OFFICE365 = "Office365"
    OFFICE_ATP = "OfficeATP"
    OFFICE_IRM = "OfficeIRM"
    OFFICE365_PROJECT = "Office365Project"
    MICROSOFT_PURVIEW_INFORMATION_PROTECTION = "MicrosoftPurviewInformationProtection"
    OFFICE_POWER_BI = "OfficePowerBI"
    AMAZON_WEB_SERVICES_CLOUD_TRAIL = "AmazonWebServicesCloudTrail"
    AMAZON_WEB_SERVICES_S3 = "AmazonWebServicesS3"
    AZURE_ADVANCED_THREAT_PROTECTION = "AzureAdvancedThreatProtection"
    MICROSOFT_DEFENDER_ADVANCED_THREAT_PROTECTION = "MicrosoftDefenderAdvancedThreatProtection"
    DYNAMICS365 = "Dynamics365"
    MICROSOFT_THREAT_PROTECTION = "MicrosoftThreatProtection"
    MICROSOFT_THREAT_INTELLIGENCE = "MicrosoftThreatIntelligence"
    GENERIC_UI = "GenericUI"
    API_POLLING = "APIPolling"
    IOT = "IOT"
    GCP = "GCP"


class DataTypeState(str, Enum):
    """
    Describe whether this data type connection is enabled or not.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class EntityMappingType(str, Enum):
    """
    The V3 type of the mapped entity
    """
    ACCOUNT = "Account"
    """
    User account entity type
    """
    HOST = "Host"
    """
    Host entity type
    """
    IP = "IP"
    """
    IP address entity type
    """
    MALWARE = "Malware"
    """
    Malware entity type
    """
    FILE = "File"
    """
    System file entity type
    """
    PROCESS = "Process"
    """
    Process entity type
    """
    CLOUD_APPLICATION = "CloudApplication"
    """
    Cloud app entity type
    """
    DNS = "DNS"
    """
    DNS entity type
    """
    AZURE_RESOURCE = "AzureResource"
    """
    Azure resource entity type
    """
    FILE_HASH = "FileHash"
    """
    File-hash entity type
    """
    REGISTRY_KEY = "RegistryKey"
    """
    Registry key entity type
    """
    REGISTRY_VALUE = "RegistryValue"
    """
    Registry value entity type
    """
    SECURITY_GROUP = "SecurityGroup"
    """
    Security group entity type
    """
    URL = "URL"
    """
    URL entity type
    """
    MAILBOX = "Mailbox"
    """
    Mailbox entity type
    """
    MAIL_CLUSTER = "MailCluster"
    """
    Mail cluster entity type
    """
    MAIL_MESSAGE = "MailMessage"
    """
    Mail message entity type
    """
    SUBMISSION_MAIL = "SubmissionMail"
    """
    Submission mail entity type
    """


class EntityProviders(str, Enum):
    """
    The entity provider that is synced.
    """
    ACTIVE_DIRECTORY = "ActiveDirectory"
    AZURE_ACTIVE_DIRECTORY = "AzureActiveDirectory"


class EntityTimelineKind(str, Enum):
    """
    The entity query kind
    """
    ACTIVITY = "Activity"
    """
    activity
    """
    BOOKMARK = "Bookmark"
    """
    bookmarks
    """
    SECURITY_ALERT = "SecurityAlert"
    """
    security alerts
    """
    ANOMALY = "Anomaly"
    """
    anomaly
    """


class EntityType(str, Enum):
    """
    The type of the query's source entity
    """
    ACCOUNT = "Account"
    """
    Entity represents account in the system.
    """
    HOST = "Host"
    """
    Entity represents host in the system.
    """
    FILE = "File"
    """
    Entity represents file in the system.
    """
    AZURE_RESOURCE = "AzureResource"
    """
    Entity represents azure resource in the system.
    """
    CLOUD_APPLICATION = "CloudApplication"
    """
    Entity represents cloud application in the system.
    """
    DNS = "DNS"
    """
    Entity represents dns in the system.
    """
    FILE_HASH = "FileHash"
    """
    Entity represents file hash in the system.
    """
    IP = "IP"
    """
    Entity represents ip in the system.
    """
    MALWARE = "Malware"
    """
    Entity represents malware in the system.
    """
    PROCESS = "Process"
    """
    Entity represents process in the system.
    """
    REGISTRY_KEY = "RegistryKey"
    """
    Entity represents registry key in the system.
    """
    REGISTRY_VALUE = "RegistryValue"
    """
    Entity represents registry value in the system.
    """
    SECURITY_GROUP = "SecurityGroup"
    """
    Entity represents security group in the system.
    """
    URL = "URL"
    """
    Entity represents url in the system.
    """
    IO_T_DEVICE = "IoTDevice"
    """
    Entity represents IoT device in the system.
    """
    SECURITY_ALERT = "SecurityAlert"
    """
    Entity represents security alert in the system.
    """
    HUNTING_BOOKMARK = "HuntingBookmark"
    """
    Entity represents HuntingBookmark in the system.
    """
    MAIL_CLUSTER = "MailCluster"
    """
    Entity represents mail cluster in the system.
    """
    MAIL_MESSAGE = "MailMessage"
    """
    Entity represents mail message in the system.
    """
    MAILBOX = "Mailbox"
    """
    Entity represents mailbox in the system.
    """
    SUBMISSION_MAIL = "SubmissionMail"
    """
    Entity represents submission mail in the system.
    """
    NIC = "Nic"
    """
    Entity represents network interface in the system.
    """


class EventGroupingAggregationKind(str, Enum):
    """
    The event grouping aggregation kinds
    """
    SINGLE_ALERT = "SingleAlert"
    ALERT_PER_RESULT = "AlertPerResult"


class FileFormat(str, Enum):
    """
    The format of the file
    """
    CSV = "CSV"
    """
    A CSV file.
    """
    JSON = "JSON"
    """
    A JSON file.
    """
    UNSPECIFIED = "Unspecified"
    """
    A file of other format.
    """


class FileImportContentType(str, Enum):
    """
    The content type of this file.
    """
    BASIC_INDICATOR = "BasicIndicator"
    """
    File containing records with the core fields of an indicator, plus the observables to construct the STIX pattern.
    """
    STIX_INDICATOR = "StixIndicator"
    """
    File containing STIX indicators.
    """
    UNSPECIFIED = "Unspecified"
    """
    File containing other records.
    """


class Flag(str, Enum):
    """
    Flag indicates if this package is in preview.
    """
    TRUE = "true"
    FALSE = "false"


class HypothesisStatus(str, Enum):
    """
    The hypothesis status of the hunt.
    """
    UNKNOWN = "Unknown"
    INVALIDATED = "Invalidated"
    VALIDATED = "Validated"


class IncidentClassification(str, Enum):
    """
    The reason the incident was closed
    """
    UNDETERMINED = "Undetermined"
    """
    Incident classification was undetermined
    """
    TRUE_POSITIVE = "TruePositive"
    """
    Incident was true positive
    """
    BENIGN_POSITIVE = "BenignPositive"
    """
    Incident was benign positive
    """
    FALSE_POSITIVE = "FalsePositive"
    """
    Incident was false positive
    """


class IncidentClassificationReason(str, Enum):
    """
    The classification reason the incident was closed with
    """
    SUSPICIOUS_ACTIVITY = "SuspiciousActivity"
    """
    Classification reason was suspicious activity
    """
    SUSPICIOUS_BUT_EXPECTED = "SuspiciousButExpected"
    """
    Classification reason was suspicious but expected
    """
    INCORRECT_ALERT_LOGIC = "IncorrectAlertLogic"
    """
    Classification reason was incorrect alert logic
    """
    INACCURATE_DATA = "InaccurateData"
    """
    Classification reason was inaccurate data
    """


class IncidentSeverity(str, Enum):
    """
    The severity of the incident
    """
    HIGH = "High"
    """
    High severity
    """
    MEDIUM = "Medium"
    """
    Medium severity
    """
    LOW = "Low"
    """
    Low severity
    """
    INFORMATIONAL = "Informational"
    """
    Informational severity
    """


class IncidentStatus(str, Enum):
    """
    The status of the incident
    """
    NEW = "New"
    """
    An active incident which isn't being handled currently
    """
    ACTIVE = "Active"
    """
    An active incident which is being handled
    """
    CLOSED = "Closed"
    """
    A non-active incident
    """


class IncidentTaskStatus(str, Enum):
    NEW = "New"
    """
    A new task
    """
    COMPLETED = "Completed"
    """
    A completed task
    """


class IngestionMode(str, Enum):
    """
    Describes how to ingest the records in the file.
    """
    INGEST_ONLY_IF_ALL_ARE_VALID = "IngestOnlyIfAllAreValid"
    """
    No records should be ingested when invalid records are detected.
    """
    INGEST_ANY_VALID_RECORDS = "IngestAnyValidRecords"
    """
    Valid records should still be ingested when invalid records are detected.
    """
    UNSPECIFIED = "Unspecified"
    """
    Unspecified
    """


class Kind(str, Enum):
    """
    Type of the content item we depend on
    """
    DATA_CONNECTOR = "DataConnector"
    DATA_TYPE = "DataType"
    WORKBOOK = "Workbook"
    WORKBOOK_TEMPLATE = "WorkbookTemplate"
    PLAYBOOK = "Playbook"
    PLAYBOOK_TEMPLATE = "PlaybookTemplate"
    ANALYTICS_RULE_TEMPLATE = "AnalyticsRuleTemplate"
    ANALYTICS_RULE = "AnalyticsRule"
    HUNTING_QUERY = "HuntingQuery"
    INVESTIGATION_QUERY = "InvestigationQuery"
    PARSER = "Parser"
    WATCHLIST = "Watchlist"
    WATCHLIST_TEMPLATE = "WatchlistTemplate"
    SOLUTION = "Solution"
    AZURE_FUNCTION = "AzureFunction"
    LOGIC_APPS_CUSTOM_CONNECTOR = "LogicAppsCustomConnector"
    AUTOMATION_RULE = "AutomationRule"


class MatchingMethod(str, Enum):
    """
    Grouping matching method. When method is Selected at least one of groupByEntities, groupByAlertDetails, groupByCustomDetails must be provided and not empty.
    """
    ALL_ENTITIES = "AllEntities"
    """
    Grouping alerts into a single incident if all the entities match
    """
    ANY_ALERT = "AnyAlert"
    """
    Grouping any alerts triggered by this rule into a single incident
    """
    SELECTED = "Selected"
    """
    Grouping alerts into a single incident if the selected entities, custom details and alert details match
    """


class MicrosoftSecurityProductName(str, Enum):
    """
    The alerts' productName on which the cases will be generated
    """
    MICROSOFT_CLOUD_APP_SECURITY = "Microsoft Cloud App Security"
    AZURE_SECURITY_CENTER = "Azure Security Center"
    AZURE_ADVANCED_THREAT_PROTECTION = "Azure Advanced Threat Protection"
    AZURE_ACTIVE_DIRECTORY_IDENTITY_PROTECTION = "Azure Active Directory Identity Protection"
    AZURE_SECURITY_CENTER_FOR_IO_T = "Azure Security Center for IoT"
    OFFICE_365_ADVANCED_THREAT_PROTECTION = "Office 365 Advanced Threat Protection"
    MICROSOFT_DEFENDER_ADVANCED_THREAT_PROTECTION = "Microsoft Defender Advanced Threat Protection"


class Mode(str, Enum):
    """
    The current mode of the workspace manager configuration
    """
    ENABLED = "Enabled"
    """
    The workspace manager configuration is enabled
    """
    DISABLED = "Disabled"
    """
    The workspace manager configuration is disabled
    """


class MtpProvider(str, Enum):
    """
    The available data providers.
    """
    MICROSOFT_DEFENDER_FOR_CLOUD_APPS = "microsoftDefenderForCloudApps"
    MICROSOFT_DEFENDER_FOR_IDENTITY = "microsoftDefenderForIdentity"


class Operator(str, Enum):
    """
    Operator used for list of dependencies in criteria array.
    """
    AND_ = "AND"
    OR_ = "OR"


class OwnerType(str, Enum):
    """
    The type of the owner the incident is assigned to.
    """
    UNKNOWN = "Unknown"
    """
    The incident owner type is unknown
    """
    USER = "User"
    """
    The incident owner type is an AAD user
    """
    GROUP = "Group"
    """
    The incident owner type is an AAD group
    """


class PackageKind(str, Enum):
    """
    the packageKind of the package contains this template
    """
    SOLUTION = "Solution"
    STANDALONE = "Standalone"


class PermissionProviderScope(str, Enum):
    """
    Permission provider scope
    """
    RESOURCE_GROUP = "ResourceGroup"
    SUBSCRIPTION = "Subscription"
    WORKSPACE = "Workspace"


class PollingFrequency(str, Enum):
    """
    The polling frequency for the TAXII server.
    """
    ONCE_A_MINUTE = "OnceAMinute"
    """
    Once a minute
    """
    ONCE_AN_HOUR = "OnceAnHour"
    """
    Once an hour
    """
    ONCE_A_DAY = "OnceADay"
    """
    Once a day
    """


class ProviderName(str, Enum):
    """
    Provider name
    """
    MICROSOFT_OPERATIONAL_INSIGHTS_SOLUTIONS = "Microsoft.OperationalInsights/solutions"
    MICROSOFT_OPERATIONAL_INSIGHTS_WORKSPACES = "Microsoft.OperationalInsights/workspaces"
    MICROSOFT_OPERATIONAL_INSIGHTS_WORKSPACES_DATASOURCES = "Microsoft.OperationalInsights/workspaces/datasources"
    MICROSOFT_AADIAM_DIAGNOSTIC_SETTINGS = "microsoft.aadiam/diagnosticSettings"
    MICROSOFT_OPERATIONAL_INSIGHTS_WORKSPACES_SHARED_KEYS = "Microsoft.OperationalInsights/workspaces/sharedKeys"
    MICROSOFT_AUTHORIZATION_POLICY_ASSIGNMENTS = "Microsoft.Authorization/policyAssignments"


class ProviderPermissionsScope(str, Enum):
    """
    The scope on which the user should have permissions, in order to be able to create connections.
    """
    SUBSCRIPTION = "Subscription"
    RESOURCE_GROUP = "ResourceGroup"
    WORKSPACE = "Workspace"


class SecurityMLAnalyticsSettingsKind(str, Enum):
    """
    The kind of security ML Analytics Settings
    """
    ANOMALY = "Anomaly"


class SettingKind(str, Enum):
    """
    The kind of the setting
    """
    ANOMALIES = "Anomalies"
    EYES_ON = "EyesOn"
    ENTITY_ANALYTICS = "EntityAnalytics"
    UEBA = "Ueba"


class SettingType(str, Enum):
    """
    The kind of the setting
    """
    COPYABLE_LABEL = "CopyableLabel"
    INSTRUCTION_STEPS_GROUP = "InstructionStepsGroup"
    INFO_MESSAGE = "InfoMessage"


class SettingsStatus(str, Enum):
    """
    The anomaly SecurityMLAnalyticsSettings status
    """
    PRODUCTION = "Production"
    """
    Anomaly settings status in Production mode
    """
    FLIGHTING = "Flighting"
    """
    Anomaly settings status in Flighting mode
    """


class SourceKind(str, Enum):
    """
    Source type of the content
    """
    LOCAL_WORKSPACE = "LocalWorkspace"
    COMMUNITY = "Community"
    SOLUTION = "Solution"
    SOURCE_REPOSITORY = "SourceRepository"


class SourceType(str, Enum):
    """
    The sourceType of the watchlist
    """
    LOCAL_FILE = "Local file"
    REMOTE_STORAGE = "Remote storage"


class Status(str, Enum):
    """
    The status of the hunt.
    """
    NEW = "New"
    ACTIVE = "Active"
    CLOSED = "Closed"
    BACKLOG = "Backlog"
    APPROVED = "Approved"


class SupportTier(str, Enum):
    """
    Type of support for content item
    """
    MICROSOFT = "Microsoft"
    PARTNER = "Partner"
    COMMUNITY = "Community"


class ThreatIntelligenceResourceInnerKind(str, Enum):
    """
    The kind of the entity.
    """
    INDICATOR = "indicator"
    """
    Entity represents threat intelligence indicator in the system.
    """


class TriggerOperator(str, Enum):
    """
    The operation against the threshold that triggers alert rule.
    """
    GREATER_THAN = "GreaterThan"
    LESS_THAN = "LessThan"
    EQUAL = "Equal"
    NOT_EQUAL = "NotEqual"


class TriggersOn(str, Enum):
    INCIDENTS = "Incidents"
    """
    Trigger on Incidents
    """
    ALERTS = "Alerts"
    """
    Trigger on Alerts
    """


class TriggersWhen(str, Enum):
    CREATED = "Created"
    """
    Trigger on created objects
    """
    UPDATED = "Updated"
    """
    Trigger on updated objects
    """


class UebaDataSources(str, Enum):
    """
    The data source that enriched by ueba.
    """
    AUDIT_LOGS = "AuditLogs"
    AZURE_ACTIVITY = "AzureActivity"
    SECURITY_EVENT = "SecurityEvent"
    SIGNIN_LOGS = "SigninLogs"
