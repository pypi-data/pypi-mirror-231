import datetime
import typing

import kubernetes.client

class V1beta2ExemptPriorityLevelConfiguration:
    lendable_percent: typing.Optional[int]
    nominal_concurrency_shares: typing.Optional[int]
    
    def __init__(self, *, lendable_percent: typing.Optional[int] = ..., nominal_concurrency_shares: typing.Optional[int] = ...) -> None:
        ...
    def to_dict(self) -> V1beta2ExemptPriorityLevelConfigurationDict:
        ...
class V1beta2ExemptPriorityLevelConfigurationDict(typing.TypedDict, total=False):
    lendablePercent: typing.Optional[int]
    nominalConcurrencyShares: typing.Optional[int]
