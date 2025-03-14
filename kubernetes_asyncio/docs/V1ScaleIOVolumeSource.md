# V1ScaleIOVolumeSource

ScaleIOVolumeSource represents a persistent ScaleIO volume

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_type** | **str** | Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Default is \&quot;xfs\&quot;. | [optional] 
**gateway** | **str** | The host address of the ScaleIO API Gateway. | 
**protection_domain** | **str** | The name of the ScaleIO Protection Domain for the configured storage. | [optional] 
**read_only** | **bool** | Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. | [optional] 
**secret_ref** | [**V1LocalObjectReference**](V1LocalObjectReference.md) |  | 
**ssl_enabled** | **bool** | Flag to enable/disable SSL communication with Gateway, default false | [optional] 
**storage_mode** | **str** | Indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned. | [optional] 
**storage_pool** | **str** | The ScaleIO Storage Pool associated with the protection domain. | [optional] 
**system** | **str** | The name of the storage system as configured in ScaleIO. | 
**volume_name** | **str** | The name of a volume already created in the ScaleIO system that is associated with this volume source. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


