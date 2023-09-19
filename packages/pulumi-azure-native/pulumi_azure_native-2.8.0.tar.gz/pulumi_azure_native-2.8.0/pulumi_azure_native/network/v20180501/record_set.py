# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['RecordSetArgs', 'RecordSet']

@pulumi.input_type
class RecordSetArgs:
    def __init__(__self__, *,
                 record_type: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 zone_name: pulumi.Input[str],
                 a_records: Optional[pulumi.Input[Sequence[pulumi.Input['ARecordArgs']]]] = None,
                 aaaa_records: Optional[pulumi.Input[Sequence[pulumi.Input['AaaaRecordArgs']]]] = None,
                 caa_records: Optional[pulumi.Input[Sequence[pulumi.Input['CaaRecordArgs']]]] = None,
                 cname_record: Optional[pulumi.Input['CnameRecordArgs']] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 mx_records: Optional[pulumi.Input[Sequence[pulumi.Input['MxRecordArgs']]]] = None,
                 ns_records: Optional[pulumi.Input[Sequence[pulumi.Input['NsRecordArgs']]]] = None,
                 ptr_records: Optional[pulumi.Input[Sequence[pulumi.Input['PtrRecordArgs']]]] = None,
                 relative_record_set_name: Optional[pulumi.Input[str]] = None,
                 soa_record: Optional[pulumi.Input['SoaRecordArgs']] = None,
                 srv_records: Optional[pulumi.Input[Sequence[pulumi.Input['SrvRecordArgs']]]] = None,
                 target_resource: Optional[pulumi.Input['SubResourceArgs']] = None,
                 ttl: Optional[pulumi.Input[float]] = None,
                 txt_records: Optional[pulumi.Input[Sequence[pulumi.Input['TxtRecordArgs']]]] = None):
        """
        The set of arguments for constructing a RecordSet resource.
        :param pulumi.Input[str] record_type: The type of DNS record in this record set. Record sets of type SOA can be updated but not created (they are created when the DNS zone is created).
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] zone_name: The name of the DNS zone (without a terminating dot).
        :param pulumi.Input[Sequence[pulumi.Input['ARecordArgs']]] a_records: The list of A records in the record set.
        :param pulumi.Input[Sequence[pulumi.Input['AaaaRecordArgs']]] aaaa_records: The list of AAAA records in the record set.
        :param pulumi.Input[Sequence[pulumi.Input['CaaRecordArgs']]] caa_records: The list of CAA records in the record set.
        :param pulumi.Input['CnameRecordArgs'] cname_record: The CNAME record in the  record set.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: The metadata attached to the record set.
        :param pulumi.Input[Sequence[pulumi.Input['MxRecordArgs']]] mx_records: The list of MX records in the record set.
        :param pulumi.Input[Sequence[pulumi.Input['NsRecordArgs']]] ns_records: The list of NS records in the record set.
        :param pulumi.Input[Sequence[pulumi.Input['PtrRecordArgs']]] ptr_records: The list of PTR records in the record set.
        :param pulumi.Input[str] relative_record_set_name: The name of the record set, relative to the name of the zone.
        :param pulumi.Input['SoaRecordArgs'] soa_record: The SOA record in the record set.
        :param pulumi.Input[Sequence[pulumi.Input['SrvRecordArgs']]] srv_records: The list of SRV records in the record set.
        :param pulumi.Input['SubResourceArgs'] target_resource: A reference to an azure resource from where the dns resource value is taken.
        :param pulumi.Input[float] ttl: The TTL (time-to-live) of the records in the record set.
        :param pulumi.Input[Sequence[pulumi.Input['TxtRecordArgs']]] txt_records: The list of TXT records in the record set.
        """
        pulumi.set(__self__, "record_type", record_type)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "zone_name", zone_name)
        if a_records is not None:
            pulumi.set(__self__, "a_records", a_records)
        if aaaa_records is not None:
            pulumi.set(__self__, "aaaa_records", aaaa_records)
        if caa_records is not None:
            pulumi.set(__self__, "caa_records", caa_records)
        if cname_record is not None:
            pulumi.set(__self__, "cname_record", cname_record)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if mx_records is not None:
            pulumi.set(__self__, "mx_records", mx_records)
        if ns_records is not None:
            pulumi.set(__self__, "ns_records", ns_records)
        if ptr_records is not None:
            pulumi.set(__self__, "ptr_records", ptr_records)
        if relative_record_set_name is not None:
            pulumi.set(__self__, "relative_record_set_name", relative_record_set_name)
        if soa_record is not None:
            pulumi.set(__self__, "soa_record", soa_record)
        if srv_records is not None:
            pulumi.set(__self__, "srv_records", srv_records)
        if target_resource is not None:
            pulumi.set(__self__, "target_resource", target_resource)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)
        if txt_records is not None:
            pulumi.set(__self__, "txt_records", txt_records)

    @property
    @pulumi.getter(name="recordType")
    def record_type(self) -> pulumi.Input[str]:
        """
        The type of DNS record in this record set. Record sets of type SOA can be updated but not created (they are created when the DNS zone is created).
        """
        return pulumi.get(self, "record_type")

    @record_type.setter
    def record_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "record_type", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="zoneName")
    def zone_name(self) -> pulumi.Input[str]:
        """
        The name of the DNS zone (without a terminating dot).
        """
        return pulumi.get(self, "zone_name")

    @zone_name.setter
    def zone_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "zone_name", value)

    @property
    @pulumi.getter(name="aRecords")
    def a_records(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ARecordArgs']]]]:
        """
        The list of A records in the record set.
        """
        return pulumi.get(self, "a_records")

    @a_records.setter
    def a_records(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ARecordArgs']]]]):
        pulumi.set(self, "a_records", value)

    @property
    @pulumi.getter(name="aaaaRecords")
    def aaaa_records(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AaaaRecordArgs']]]]:
        """
        The list of AAAA records in the record set.
        """
        return pulumi.get(self, "aaaa_records")

    @aaaa_records.setter
    def aaaa_records(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AaaaRecordArgs']]]]):
        pulumi.set(self, "aaaa_records", value)

    @property
    @pulumi.getter(name="caaRecords")
    def caa_records(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CaaRecordArgs']]]]:
        """
        The list of CAA records in the record set.
        """
        return pulumi.get(self, "caa_records")

    @caa_records.setter
    def caa_records(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CaaRecordArgs']]]]):
        pulumi.set(self, "caa_records", value)

    @property
    @pulumi.getter(name="cnameRecord")
    def cname_record(self) -> Optional[pulumi.Input['CnameRecordArgs']]:
        """
        The CNAME record in the  record set.
        """
        return pulumi.get(self, "cname_record")

    @cname_record.setter
    def cname_record(self, value: Optional[pulumi.Input['CnameRecordArgs']]):
        pulumi.set(self, "cname_record", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The metadata attached to the record set.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter(name="mxRecords")
    def mx_records(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MxRecordArgs']]]]:
        """
        The list of MX records in the record set.
        """
        return pulumi.get(self, "mx_records")

    @mx_records.setter
    def mx_records(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MxRecordArgs']]]]):
        pulumi.set(self, "mx_records", value)

    @property
    @pulumi.getter(name="nsRecords")
    def ns_records(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NsRecordArgs']]]]:
        """
        The list of NS records in the record set.
        """
        return pulumi.get(self, "ns_records")

    @ns_records.setter
    def ns_records(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NsRecordArgs']]]]):
        pulumi.set(self, "ns_records", value)

    @property
    @pulumi.getter(name="ptrRecords")
    def ptr_records(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PtrRecordArgs']]]]:
        """
        The list of PTR records in the record set.
        """
        return pulumi.get(self, "ptr_records")

    @ptr_records.setter
    def ptr_records(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PtrRecordArgs']]]]):
        pulumi.set(self, "ptr_records", value)

    @property
    @pulumi.getter(name="relativeRecordSetName")
    def relative_record_set_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the record set, relative to the name of the zone.
        """
        return pulumi.get(self, "relative_record_set_name")

    @relative_record_set_name.setter
    def relative_record_set_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "relative_record_set_name", value)

    @property
    @pulumi.getter(name="soaRecord")
    def soa_record(self) -> Optional[pulumi.Input['SoaRecordArgs']]:
        """
        The SOA record in the record set.
        """
        return pulumi.get(self, "soa_record")

    @soa_record.setter
    def soa_record(self, value: Optional[pulumi.Input['SoaRecordArgs']]):
        pulumi.set(self, "soa_record", value)

    @property
    @pulumi.getter(name="srvRecords")
    def srv_records(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SrvRecordArgs']]]]:
        """
        The list of SRV records in the record set.
        """
        return pulumi.get(self, "srv_records")

    @srv_records.setter
    def srv_records(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SrvRecordArgs']]]]):
        pulumi.set(self, "srv_records", value)

    @property
    @pulumi.getter(name="targetResource")
    def target_resource(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        A reference to an azure resource from where the dns resource value is taken.
        """
        return pulumi.get(self, "target_resource")

    @target_resource.setter
    def target_resource(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "target_resource", value)

    @property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[float]]:
        """
        The TTL (time-to-live) of the records in the record set.
        """
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "ttl", value)

    @property
    @pulumi.getter(name="txtRecords")
    def txt_records(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TxtRecordArgs']]]]:
        """
        The list of TXT records in the record set.
        """
        return pulumi.get(self, "txt_records")

    @txt_records.setter
    def txt_records(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TxtRecordArgs']]]]):
        pulumi.set(self, "txt_records", value)


class RecordSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 a_records: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ARecordArgs']]]]] = None,
                 aaaa_records: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AaaaRecordArgs']]]]] = None,
                 caa_records: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CaaRecordArgs']]]]] = None,
                 cname_record: Optional[pulumi.Input[pulumi.InputType['CnameRecordArgs']]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 mx_records: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MxRecordArgs']]]]] = None,
                 ns_records: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NsRecordArgs']]]]] = None,
                 ptr_records: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PtrRecordArgs']]]]] = None,
                 record_type: Optional[pulumi.Input[str]] = None,
                 relative_record_set_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 soa_record: Optional[pulumi.Input[pulumi.InputType['SoaRecordArgs']]] = None,
                 srv_records: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SrvRecordArgs']]]]] = None,
                 target_resource: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 ttl: Optional[pulumi.Input[float]] = None,
                 txt_records: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TxtRecordArgs']]]]] = None,
                 zone_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Describes a DNS record set (a collection of DNS records with the same name and type).

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ARecordArgs']]]] a_records: The list of A records in the record set.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AaaaRecordArgs']]]] aaaa_records: The list of AAAA records in the record set.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CaaRecordArgs']]]] caa_records: The list of CAA records in the record set.
        :param pulumi.Input[pulumi.InputType['CnameRecordArgs']] cname_record: The CNAME record in the  record set.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: The metadata attached to the record set.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MxRecordArgs']]]] mx_records: The list of MX records in the record set.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NsRecordArgs']]]] ns_records: The list of NS records in the record set.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PtrRecordArgs']]]] ptr_records: The list of PTR records in the record set.
        :param pulumi.Input[str] record_type: The type of DNS record in this record set. Record sets of type SOA can be updated but not created (they are created when the DNS zone is created).
        :param pulumi.Input[str] relative_record_set_name: The name of the record set, relative to the name of the zone.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[pulumi.InputType['SoaRecordArgs']] soa_record: The SOA record in the record set.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SrvRecordArgs']]]] srv_records: The list of SRV records in the record set.
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] target_resource: A reference to an azure resource from where the dns resource value is taken.
        :param pulumi.Input[float] ttl: The TTL (time-to-live) of the records in the record set.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TxtRecordArgs']]]] txt_records: The list of TXT records in the record set.
        :param pulumi.Input[str] zone_name: The name of the DNS zone (without a terminating dot).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RecordSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Describes a DNS record set (a collection of DNS records with the same name and type).

        :param str resource_name: The name of the resource.
        :param RecordSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RecordSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 a_records: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ARecordArgs']]]]] = None,
                 aaaa_records: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AaaaRecordArgs']]]]] = None,
                 caa_records: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CaaRecordArgs']]]]] = None,
                 cname_record: Optional[pulumi.Input[pulumi.InputType['CnameRecordArgs']]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 mx_records: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MxRecordArgs']]]]] = None,
                 ns_records: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NsRecordArgs']]]]] = None,
                 ptr_records: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PtrRecordArgs']]]]] = None,
                 record_type: Optional[pulumi.Input[str]] = None,
                 relative_record_set_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 soa_record: Optional[pulumi.Input[pulumi.InputType['SoaRecordArgs']]] = None,
                 srv_records: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SrvRecordArgs']]]]] = None,
                 target_resource: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 ttl: Optional[pulumi.Input[float]] = None,
                 txt_records: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TxtRecordArgs']]]]] = None,
                 zone_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RecordSetArgs.__new__(RecordSetArgs)

            __props__.__dict__["a_records"] = a_records
            __props__.__dict__["aaaa_records"] = aaaa_records
            __props__.__dict__["caa_records"] = caa_records
            __props__.__dict__["cname_record"] = cname_record
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["mx_records"] = mx_records
            __props__.__dict__["ns_records"] = ns_records
            __props__.__dict__["ptr_records"] = ptr_records
            if record_type is None and not opts.urn:
                raise TypeError("Missing required property 'record_type'")
            __props__.__dict__["record_type"] = record_type
            __props__.__dict__["relative_record_set_name"] = relative_record_set_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["soa_record"] = soa_record
            __props__.__dict__["srv_records"] = srv_records
            __props__.__dict__["target_resource"] = target_resource
            __props__.__dict__["ttl"] = ttl
            __props__.__dict__["txt_records"] = txt_records
            if zone_name is None and not opts.urn:
                raise TypeError("Missing required property 'zone_name'")
            __props__.__dict__["zone_name"] = zone_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["fqdn"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:RecordSet"), pulumi.Alias(type_="azure-native:network/v20150504preview:RecordSet"), pulumi.Alias(type_="azure-native:network/v20160401:RecordSet"), pulumi.Alias(type_="azure-native:network/v20170901:RecordSet"), pulumi.Alias(type_="azure-native:network/v20171001:RecordSet"), pulumi.Alias(type_="azure-native:network/v20180301preview:RecordSet"), pulumi.Alias(type_="azure-native:network/v20230701preview:RecordSet")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(RecordSet, __self__).__init__(
            'azure-native:network/v20180501:RecordSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RecordSet':
        """
        Get an existing RecordSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RecordSetArgs.__new__(RecordSetArgs)

        __props__.__dict__["a_records"] = None
        __props__.__dict__["aaaa_records"] = None
        __props__.__dict__["caa_records"] = None
        __props__.__dict__["cname_record"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["fqdn"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["mx_records"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["ns_records"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["ptr_records"] = None
        __props__.__dict__["soa_record"] = None
        __props__.__dict__["srv_records"] = None
        __props__.__dict__["target_resource"] = None
        __props__.__dict__["ttl"] = None
        __props__.__dict__["txt_records"] = None
        __props__.__dict__["type"] = None
        return RecordSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aRecords")
    def a_records(self) -> pulumi.Output[Optional[Sequence['outputs.ARecordResponse']]]:
        """
        The list of A records in the record set.
        """
        return pulumi.get(self, "a_records")

    @property
    @pulumi.getter(name="aaaaRecords")
    def aaaa_records(self) -> pulumi.Output[Optional[Sequence['outputs.AaaaRecordResponse']]]:
        """
        The list of AAAA records in the record set.
        """
        return pulumi.get(self, "aaaa_records")

    @property
    @pulumi.getter(name="caaRecords")
    def caa_records(self) -> pulumi.Output[Optional[Sequence['outputs.CaaRecordResponse']]]:
        """
        The list of CAA records in the record set.
        """
        return pulumi.get(self, "caa_records")

    @property
    @pulumi.getter(name="cnameRecord")
    def cname_record(self) -> pulumi.Output[Optional['outputs.CnameRecordResponse']]:
        """
        The CNAME record in the  record set.
        """
        return pulumi.get(self, "cname_record")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        The etag of the record set.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[str]:
        """
        Fully qualified domain name of the record set.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The metadata attached to the record set.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter(name="mxRecords")
    def mx_records(self) -> pulumi.Output[Optional[Sequence['outputs.MxRecordResponse']]]:
        """
        The list of MX records in the record set.
        """
        return pulumi.get(self, "mx_records")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the record set.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nsRecords")
    def ns_records(self) -> pulumi.Output[Optional[Sequence['outputs.NsRecordResponse']]]:
        """
        The list of NS records in the record set.
        """
        return pulumi.get(self, "ns_records")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        provisioning State of the record set.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="ptrRecords")
    def ptr_records(self) -> pulumi.Output[Optional[Sequence['outputs.PtrRecordResponse']]]:
        """
        The list of PTR records in the record set.
        """
        return pulumi.get(self, "ptr_records")

    @property
    @pulumi.getter(name="soaRecord")
    def soa_record(self) -> pulumi.Output[Optional['outputs.SoaRecordResponse']]:
        """
        The SOA record in the record set.
        """
        return pulumi.get(self, "soa_record")

    @property
    @pulumi.getter(name="srvRecords")
    def srv_records(self) -> pulumi.Output[Optional[Sequence['outputs.SrvRecordResponse']]]:
        """
        The list of SRV records in the record set.
        """
        return pulumi.get(self, "srv_records")

    @property
    @pulumi.getter(name="targetResource")
    def target_resource(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        A reference to an azure resource from where the dns resource value is taken.
        """
        return pulumi.get(self, "target_resource")

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[Optional[float]]:
        """
        The TTL (time-to-live) of the records in the record set.
        """
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter(name="txtRecords")
    def txt_records(self) -> pulumi.Output[Optional[Sequence['outputs.TxtRecordResponse']]]:
        """
        The list of TXT records in the record set.
        """
        return pulumi.get(self, "txt_records")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the record set.
        """
        return pulumi.get(self, "type")

