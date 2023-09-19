"""Helper classes for scripts for cluster support packages."""

from enum import Enum
from typing import List, Optional

from cyberfusion.ClusterSupport._interfaces import (
    APIObjectInterface,
    sort_lists,
)

ENDPOINT_NODES = "nodes"
MODEL_NODES = "nodes"


class NodeGroup(str, Enum):
    """Node groups."""

    ADMIN: str = "Admin"
    APACHE: str = "Apache"
    PROFTPD: str = "ProFTPD"
    NGINX: str = "nginx"
    DOVECOT: str = "Dovecot"
    MARIADB: str = "MariaDB"
    POSTGRESQL: str = "PostgreSQL"
    MAIN: str = "Main"
    PHP: str = "PHP"
    BORG: str = "Borg"
    NODEJS: str = "NodeJS"
    FAST_REDIRECT: str = "Fast Redirect"
    PASSENGER: str = "Passenger"
    REDIS: str = "Redis"
    HAPROXY: str = "HAProxy"
    WP_CLI: str = "WP-CLI"
    COMPOSER: str = "Composer"
    KERNELCARE: str = "KernelCare"
    IMAGEMAGICK: str = "ImageMagick"
    WKHTMLTOPDF: str = "wkhtmltopdf"
    GNU_MAILUTILS: str = "GNU Mailutils"
    PUPPETEER: str = "Puppeteer"
    LIBREOFFICE: str = "LibreOffice"
    GHOSTSCRIPT: str = "Ghostscript"
    FFMPEG: str = "FFmpeg"
    MALDET: str = "maldet"


class Node(APIObjectInterface):
    """Represents object."""

    _TABLE_HEADERS = [
        "ID",
        "Hostname",
        "Groups",
        "Comment",
        "Cluster",
    ]
    _TABLE_HEADERS_DETAILED: List[str] = []

    _TABLE_FIELDS = [
        "id",
        "hostname",
        "groups",
        "comment",
        "_cluster_name",
    ]
    _TABLE_FIELDS_DETAILED: List[str] = []

    @sort_lists  # type: ignore[misc]
    def _set_attributes_from_model(
        self,
        obj: dict,
    ) -> None:
        """Set class attributes from API output."""
        self.id = obj["id"]
        self.hostname = obj["hostname"]
        self.comment = obj["comment"]
        self.groups = [NodeGroup(x).value for x in obj["groups"]]
        self.load_balancer_health_checks_groups_pairs = obj[
            "load_balancer_health_checks_groups_pairs"
        ]
        self.groups_properties = obj["groups_properties"]
        self.cluster_id: int = obj["cluster_id"]
        self.created_at = obj["created_at"]
        self.updated_at = obj["updated_at"]

        self.cluster = self.support.get_clusters(id_=self.cluster_id)[0]
        self._cluster_name = self.cluster.name

    def create(
        self,
        *,
        comment: Optional[str],
        groups: List[NodeGroup],
        load_balancer_health_checks_groups_pairs: dict,
        groups_properties: dict,
        cluster_id: int,
    ) -> None:
        """Create object."""
        url = f"/api/v1/{ENDPOINT_NODES}"
        data = {
            "comment": comment,
            "groups": groups,
            "load_balancer_health_checks_groups_pairs": load_balancer_health_checks_groups_pairs,
            "groups_properties": groups_properties,
            "cluster_id": cluster_id,
        }

        self.support.request.POST(url, data)
        response = self.support.request.execute()

        self._set_attributes_from_model(response)

        self.support.nodes.append(self)

    def update(self) -> None:
        """Update object."""
        url = f"/api/v1/{ENDPOINT_NODES}/{self.id}"
        data = {
            "id": self.id,
            "hostname": self.hostname,
            "comment": self.comment,
            "groups": self.groups,
            "load_balancer_health_checks_groups_pairs": self.load_balancer_health_checks_groups_pairs,
            "groups_properties": self.groups_properties,
            "cluster_id": self.cluster_id,
        }

        self.support.request.PUT(url, data)
        response = self.support.request.execute()

        self._set_attributes_from_model(response)

    def delete(self) -> None:
        """Delete object."""
        url = f"/api/v1/{ENDPOINT_NODES}/{self.id}"

        self.support.request.DELETE(url)
        self.support.request.execute()

        self.support.nodes.remove(self)
