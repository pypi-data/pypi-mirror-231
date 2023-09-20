from abc import ABC, abstractmethod
from enum import Enum
from typing import TypeVar

from minio import Minio
from pydantic import SecretStr

T = TypeVar("T", bound="WorkspaceAdapter")


class StorageType(Enum):
    MINIO = "minio"


class WorkspaceAdapter(ABC):
    @staticmethod
    def create_adapter(
        tenant_url: str = None,
        storage_type: StorageType = StorageType.MINIO,
        credentials: dict[str, str] = None,
    ) -> T:
        if storage_type == StorageType.MINIO:
            return MinIOAdapter(
                url=tenant_url,
                access_key=credentials["access_key"],
                secret_key=credentials["secret_key"],
            )
        else:
            return None

    @abstractmethod
    def create_workspace(self, workspace_name) -> None:
        pass

    @abstractmethod
    def delete_workspace(self, workspace_name) -> None:
        pass

    @abstractmethod
    def workspace_exists(self, workspace_name) -> bool:
        pass

    @abstractmethod
    def update_workspace(self, workspace_name, **kwargs) -> None:
        pass

    @abstractmethod
    def list_workspaces(self) -> list[str]:
        pass

    @abstractmethod
    def list_workspace_files(self, workspace_name) -> list[str]:
        pass


class MinIOAdapter(WorkspaceAdapter):
    minio_client: Minio

    def __init__(self, url: str, access_key: SecretStr, secret_key: SecretStr):
        self.minio_client = Minio(
            url, access_key=access_key, secret_key=secret_key, secure=False
        )

    def create_workspace(self, workspace_name):
        """
        raises S3Error
        """
        self.minio_client.make_bucket(workspace_name)

    def delete_workspace(self, workspace_name):
        """
        raises S3Error
        """
        self.minio_client.remove_bucket(workspace_name)

    def workspace_exists(self, workspace_name) -> bool:
        return self.minio_client.bucket_exists(workspace_name)

    def list_workspaces(self):
        buckets = self.minio_client.list_buckets()
        return [bucket.name for bucket in buckets]

    def list_workspace_files(self, workspace_name):
        return [
            obj.object_name for obj in self.minio_client.list_objects(workspace_name)
        ]

    def update_workspace(self, workspace_name, **kwargs):
        pass
