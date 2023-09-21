#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2021-2023 Carsten Igel.
#
# This file is part of pdm-bump
# (see https://github.com/carstencodes/pdm-bump).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""

from typing import Protocol, Union, cast, runtime_checkable

from .core.config import Config, ConfigKeys
from .core.logging import logger
from .core.version import Pep440VersionFormatter, Version


# Justification: Minimal protocol
class _ProjectWriter(Protocol):  # pylint: disable=R0903
    """"""

    def write(self, show_message: bool) -> None:
        """

        Parameters
        ----------
        show_message: bool :


        Returns
        -------

        """
        # Method empty: Only a protocol stub
        raise NotImplementedError()


@runtime_checkable
class _ProjectWriterClassic(Protocol):  # pylint: disable=R0903
    """"""

    def write_pyproject(self, show_message: bool) -> None:
        """

        Parameters
        ----------
        show_message: bool :


        Returns
        -------

        """
        # Method empty: Only a protocol stub
        raise NotImplementedError()


# Justification: Minimal protocol
@runtime_checkable
class _ProjectWriterHolder(Protocol):  # pylint: disable=R0903
    """"""

    pyproject: _ProjectWriter


# Justification: Implementation of minimal protocol
class StaticPep621VersionSource:  # pylint: disable=R0903
    """"""

    def __init__(
        self,
        _: Union[_ProjectWriterHolder, _ProjectWriterClassic],
        config: Config,
    ) -> None:
        self.__config = config

    @property
    def is_enabled(self) -> bool:
        """"""
        return (
            self.__config.get_pyproject_metadata(ConfigKeys.VERSION)
            is not None
        )

    def __get_current_version(self) -> Version:
        version: str = cast(
            str, self.__config.get_pyproject_metadata(ConfigKeys.VERSION)
        )
        return Version.from_string(version)

    def __set_current_version(self, ver: Version) -> None:
        formatter: Pep440VersionFormatter = Pep440VersionFormatter()
        version: str = formatter.format(ver)
        logger.debug("Setting new version %s", version)
        self.__config.set_pyproject_metadata(version, ConfigKeys.VERSION)

    current_version = property(__get_current_version, __set_current_version)
