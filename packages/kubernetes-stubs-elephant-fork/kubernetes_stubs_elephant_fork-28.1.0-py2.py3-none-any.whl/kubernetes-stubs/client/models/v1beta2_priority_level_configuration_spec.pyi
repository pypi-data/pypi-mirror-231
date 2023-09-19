import datetime
import typing

import kubernetes.client

class V1beta2PriorityLevelConfigurationSpec:
    exempt: typing.Optional[kubernetes.client.V1beta2ExemptPriorityLevelConfiguration]
    limited: typing.Optional[kubernetes.client.V1beta2LimitedPriorityLevelConfiguration]
    type: str
    
    def __init__(self, *, exempt: typing.Optional[kubernetes.client.V1beta2ExemptPriorityLevelConfiguration] = ..., limited: typing.Optional[kubernetes.client.V1beta2LimitedPriorityLevelConfiguration] = ..., type: str) -> None:
        ...
    def to_dict(self) -> V1beta2PriorityLevelConfigurationSpecDict:
        ...
class V1beta2PriorityLevelConfigurationSpecDict(typing.TypedDict, total=False):
    exempt: typing.Optional[kubernetes.client.V1beta2ExemptPriorityLevelConfigurationDict]
    limited: typing.Optional[kubernetes.client.V1beta2LimitedPriorityLevelConfigurationDict]
    type: str
