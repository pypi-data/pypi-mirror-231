"""Helper classes for scripts for cluster support packages."""

from cyberfusion.ClusterSupport._interfaces import (
    APIObjectInterface,
    sort_lists,
)

ENDPOINT_DOMAIN_ROUTERS = "domain-routers"
MODEL_DOMAIN_ROUTERS = "domain_routers"


class DomainRouter(APIObjectInterface):
    """Represents object."""

    _TABLE_HEADERS = [
        "ID",
        "Domain",
        "Force SSL",
        "Cluster",
    ]
    _TABLE_HEADERS_DETAILED = [
        "Node",
        "Virtual Host",
        "URL Redirect",
        "Certificate",
        "Security TXT Policy",
    ]

    _TABLE_FIELDS = [
        "id",
        "domain",
        "force_ssl",
        "_cluster_name",
    ]
    _TABLE_FIELDS_DETAILED = [
        "_node_hostname",
        "_virtual_host_domain",
        "_url_redirect_domain",
        "certificate_id",
        "security_txt_policy_id",
    ]

    @sort_lists  # type: ignore[misc]
    def _set_attributes_from_model(
        self,
        obj: dict,
    ) -> None:
        """Set class attributes from API output."""
        self.id = obj["id"]
        self.domain = obj["domain"]
        self.node_id = obj["node_id"]
        self.force_ssl = obj["force_ssl"]
        self.certificate_id = obj["certificate_id"]
        self.security_txt_policy_id = obj["security_txt_policy_id"]
        self.url_redirect_id = obj["url_redirect_id"]
        self.virtual_host_id = obj["virtual_host_id"]
        self.cluster_id: int = obj["cluster_id"]
        self.created_at = obj["created_at"]
        self.updated_at = obj["updated_at"]

        self.cluster = self.support.get_clusters(id_=self.cluster_id)[0]

        self.node = None
        self.virtual_host = None
        self.url_redirect = None
        self.certificate = None
        self.security_txt_policy = None

        self._node_hostname = None
        self._virtual_host_domain = None
        self._url_redirect_domain = None
        self._cluster_name = self.cluster.name

        if self.node_id:
            self.node = self.support.get_nodes(id_=self.node_id)[0]
            self._node_hostname = self.node.hostname

        if self.virtual_host_id:
            self.virtual_host = self.support.get_virtual_hosts(
                id_=self.virtual_host_id
            )[0]
            self._virtual_host_domain = self.virtual_host.domain

        if self.url_redirect_id:
            self.url_redirect = self.support.get_url_redirects(
                id_=self.url_redirect_id
            )[0]
            self._url_redirect_domain = self.url_redirect.domain

        if self.certificate_id:
            self.certificate = self.support.get_certificates(
                id_=self.certificate_id
            )[0]

        if self.security_txt_policy_id:
            self.security_txt_policy = self.support.get_security_txt_policies(
                id_=self.security_txt_policy_id
            )[0]

    def update(self) -> None:
        """Update object."""
        url = f"/api/v1/{ENDPOINT_DOMAIN_ROUTERS}/{self.id}"
        data = {
            "id": self.id,
            "domain": self.domain,
            "node_id": self.node_id,
            "force_ssl": self.force_ssl,
            "certificate_id": self.certificate_id,
            "security_txt_policy_id": self.security_txt_policy_id,
            "url_redirect_id": self.url_redirect_id,
            "virtual_host_id": self.virtual_host_id,
            "cluster_id": self.cluster_id,
        }

        self.support.request.PUT(url, data)
        response = self.support.request.execute()

        self._set_attributes_from_model(response)
