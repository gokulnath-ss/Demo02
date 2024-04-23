from _typeshed import Incomplete

class TemplateSummaryDiffLabelMappings:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        status: Incomplete | None = None,
        resource_type: Incomplete | None = None,
        resource_id: Incomplete | None = None,
        resource_template_meta_name: Incomplete | None = None,
        resource_name: Incomplete | None = None,
        label_id: Incomplete | None = None,
        label_template_meta_name: Incomplete | None = None,
        label_name: Incomplete | None = None,
    ) -> None: ...
    @property
    def status(self): ...
    @status.setter
    def status(self, status) -> None: ...
    @property
    def resource_type(self): ...
    @resource_type.setter
    def resource_type(self, resource_type) -> None: ...
    @property
    def resource_id(self): ...
    @resource_id.setter
    def resource_id(self, resource_id) -> None: ...
    @property
    def resource_template_meta_name(self): ...
    @resource_template_meta_name.setter
    def resource_template_meta_name(self, resource_template_meta_name) -> None: ...
    @property
    def resource_name(self): ...
    @resource_name.setter
    def resource_name(self, resource_name) -> None: ...
    @property
    def label_id(self): ...
    @label_id.setter
    def label_id(self, label_id) -> None: ...
    @property
    def label_template_meta_name(self): ...
    @label_template_meta_name.setter
    def label_template_meta_name(self, label_template_meta_name) -> None: ...
    @property
    def label_name(self): ...
    @label_name.setter
    def label_name(self, label_name) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...