"""
File: resource.py
Purpose: This file contains the definition of the Resource class, which represents a resource in the project.
Author: Stackers
Date: 2026-09-03
Version: 1.0.0
License: MIT License

This file defines the Resource class, which is used to represent and manage resources within the project. The Resource
class provides methods for creating, updating, and deleting resources, as well as for retrieving resource information.
It serves as a foundational component for resource management in the application.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from enum import StrEnum

class ResourceType(StrEnum):
    """
    Enum class representing different types of resources.
    """
    CONSUMABLE = "Consumable"
    USABLE = "Usable"


class Resource(ABC):
    """Abstract base class representing a resource in the project."""

    __slots__ = ("_name", "_is_available", "_resource_type")

    def __init__(self, name: str, resource_type: ResourceType):
        """Initialize a new Resource instance.

        Args:
            name (str): The name of the resource.
            resource_type (ResourceType): The type of the resource.
        """

        self._name = name
        self._is_available = True
        self._resource_type = resource_type

    @property
    def name(self) -> str:
        """Get the name of the resource."""
        return self._name

    @property
    def is_available(self) -> bool:
        """Get the availability of the resource."""
        return self._is_available

    @property
    def resource_type(self) -> ResourceType:
        """Get the type of the resource."""
        return self._resource_type

    @abstractmethod
    def allocate(self) -> None:
        """Allocate the resource.

        This method should be implemented by subclasses to define how the resource is allocated.
        """
        pass

    @abstractmethod
    def release(self) -> None:
        """Release the resource.

        This method should be implemented by subclasses to define how the resource is released.
        """
        pass

    @abstractmethod
    def use(self) -> None:
        """Use the resource.

        This method should be implemented by subclasses to define how the resource is used.
        """
        pass