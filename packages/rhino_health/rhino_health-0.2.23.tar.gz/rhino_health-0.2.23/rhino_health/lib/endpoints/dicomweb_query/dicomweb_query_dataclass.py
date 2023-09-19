from typing import Any, Dict, List, Literal, Optional, TypedDict

from pydantic import BaseModel, Extra, Field
from typing_extensions import Annotated

from rhino_health.lib.endpoints.endpoint import RESULT_DATACLASS_EXTRA
from rhino_health.lib.endpoints.user.user_dataclass import User


class DicomwebQueryMetricDefinition(TypedDict):
    """
    @autoapi False
    """

    metric_name: str
    """@autoapi True Name of the metric type to calculate"""
    metric_params: Dict[str, Any]
    """@autoapi True Parameters for the metric"""
    request_arguments: Dict[str, Any]
    """@autoapi True Additional parameters for the metric"""


class DicomwebQueryResult(BaseModel, extra=RESULT_DATACLASS_EXTRA):
    """
    @autoapi False
    """

    metric_definition: DicomwebQueryMetricDefinition
    """@autoapi True Metric of which this is the result"""
    calculated_metric: Any
    """@autoapi True Calculated value"""
    errors: Optional[List[str]]
    """@autoapi True Errors that occurred while calculating this metric"""


class DicomwebQueryBase(BaseModel):
    """
    @autoapi False
    """

    project_uid: Annotated[str, Field(alias="project")]
    """@autoapi True The unique ID of the project in whose context this query is done"""
    workgroup_uid: Annotated[str, Field(alias="workgroup")]
    """@autoapi True The unique ID of the Workgroup in whose context this query is done"""
    dicomweb_server_url: str
    """@autoapi True URL of the DICOMweb server to query"""
    dicomweb_query: Dict[str, Any]
    """@autoapi True Query parameters to be passed to the search_filters param of search_for_studies"""
    dicom_object_level: Literal["Study", "Series", "Instance"]
    metric_definitions: List[DicomwebQueryMetricDefinition]
    """@autoapi True Metrics to calculate on the query results"""

    @property
    def container_image_uri(self):
        return self.config.get("container_image_uri", None)

    @container_image_uri.setter
    def container_image_uri(self, new_value):
        self.config["container_image_uri"] = new_value


class DicomwebQueryCreateInput(DicomwebQueryBase, extra=Extra.forbid):
    """
    @autoapi False
    """

    dicomweb_auth_credentials: Dict[str, str]
    """@autoapi True Credentials for connecting to the target DICOMweb server"""


class DicomwebQuery(DicomwebQueryBase, extra=RESULT_DATACLASS_EXTRA):
    """
    @autoapi False
    """

    uid: str
    """@autoapi True The Unique ID of the DICOMweb Query"""
    status: str
    """The query status"""
    created_at: str
    """@autoapi True When this query was was created"""
    ended_at: Optional[str]
    """@autoapi True When this query ended"""
    creator: User
    """@autoapi True The user who created this query"""
    results: Optional[List[DicomwebQueryResult]]
    """@autoapi True The results of this query"""
    errors: Optional[List[str]]
    """@autoapi True Errors that occurred while running this query"""
