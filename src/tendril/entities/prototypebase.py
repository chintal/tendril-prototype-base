#!/usr/bin/env python
# encoding: utf-8

# Copyright (C) 2016 Chintalagiri Shashank
#
# This file is part of tendril.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Primitives for Entity Prototypes
--------------------------------

Unhandled changes :

bom, obom changed to sbom, bom
class names changed
changelog property implementation fleshed out

"""
from copy import copy

from tendril.conventions import status
from tendril.dox.labelmaker import manager as labelmanager
from tendril.validation.base import ValidatableBase
from tendril.validation.files import MissingFileError
from tendril.validation.files import MangledFileError
from tendril.validation.files import FilePolicy

from tendril.utils import log
from tendril.utils.parsers import changelog

logger = log.get_logger(__name__, log.DEFAULT)


class MissingInformationError(Exception):
    pass


class PrototypeBase(ValidatableBase):
    _label_name_property = 'ident'
    _can_have_changelog = False

    def __init__(self, **kwargs):
        super(PrototypeBase, self).__init__(**kwargs)
        self._status = None
        self._strategy = None

    @property
    def ident(self):
        raise NotImplementedError

    @ident.setter
    def ident(self, value):
        raise NotImplementedError

    @property
    def desc(self):
        raise NotImplementedError

    @property
    def status(self):
        if self._status is None:
            st = self._get_status()
            if not isinstance(st, status.Status):
                st = status.get_status(st)
            self._status = st
        return self._status

    def _get_status(self):
        raise NotImplementedError

    @property
    def strategy(self):
        if self._strategy is None:
            raise MissingInformationError(
                "Production / Procurement strategy information missing for {0}"
                "".format(self.ident)
            )
        return self._strategy

    @property
    def labels(self):
        raise NotImplementedError

    def labelinfo(self, sno):
        raise NotImplementedError

    def make_labels(self, sno, label_manager=None):
        if label_manager is None:
            label_manager = labelmanager
        labelinfo = self.labelinfo(sno)
        if labelinfo is not None:
            for l in self.labels:
                label_manager.add_label(
                    l.type, getattr(self, self._label_name_property),
                    labelinfo[0], **labelinfo[1])

    @property
    def changelog(self):
        if not self._can_have_changelog:
            return None

        if self._changelog:
            return self._changelog

        try:
            self._get_changelog()
        except (changelog.ChangeLogNotFoundError,
                changelog.ChangeLogParseError):
            return None

        return self._changelog

    @property
    def _changelogpath(self):
        raise NotImplementedError

    @property
    def _changelog_policy(self):
        ctx = copy(self._validation_context)
        ctx.locality = 'ChangeLog'
        return FilePolicy(ctx, self._changelogpath, False)

    def _get_changelog(self):
        if not self._can_have_changelog:
            return
        try:
            self._changelog = changelog.ChangeLog(self._changelogpath)
        except changelog.ChangeLogNotFoundError:
            raise MissingFileError(self._changelog_policy)
        except changelog.ChangeLogParseError:
            raise MangledFileError(self._changelog_policy)

    def _register_for_changes(self):
        raise NotImplementedError

    def _reload(self):
        raise NotImplementedError

    def _validate(self):
        raise NotImplementedError


class CompositePrototype(PrototypeBase):
    @property
    def sbom(self):
        raise NotImplementedError

    @property
    def bom(self):
        raise NotImplementedError


class StructuredPrototype(CompositePrototype):
    @property
    def psl(self):
        raise NotImplementedError
