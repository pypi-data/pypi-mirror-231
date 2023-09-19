# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os
import sys

import voluptuous as vp
import yaml


def get_user_config(path=None):
    if not path:
        home_dir = os.path.expanduser("~")
        path = os.path.join(home_dir, ".stestr.yaml")
        if not os.path.isfile(path):
            path = os.path.join(os.path.join(home_dir, ".config"), "stestr.yaml")
            if not os.path.isfile(path):
                path = None
        if not path:
            return None
    else:
        if not os.path.isfile(path):
            msg = "The specified stestr user config is not a valid path"
            sys.exit(msg)

    return UserConfig(path)


class UserConfig:
    def __init__(self, path):
        self.schema = vp.Schema(
            {
                vp.Optional("run"): {
                    vp.Optional("concurrency"): int,
                    vp.Optional("random"): bool,
                    vp.Optional("no-subunit-trace"): bool,
                    vp.Optional("color"): bool,
                    vp.Optional("abbreviate"): bool,
                    vp.Optional("slowest"): bool,
                    vp.Optional("suppress-attachments"): bool,
                    vp.Optional("all-attachments"): bool,
                },
                vp.Optional("failing"): {
                    vp.Optional("list"): bool,
                },
                vp.Optional("last"): {
                    vp.Optional("no-subunit-trace"): bool,
                    vp.Optional("color"): bool,
                    vp.Optional("suppress-attachments"): bool,
                    vp.Optional("all-attachments"): bool,
                },
                vp.Optional("load"): {
                    vp.Optional("force-init"): bool,
                    vp.Optional("subunit-trace"): bool,
                    vp.Optional("color"): bool,
                    vp.Optional("abbreviate"): bool,
                    vp.Optional("suppress-attachments"): bool,
                    vp.Optional("all-attachments"): bool,
                },
                vp.Optional("history-list"): {
                    vp.Optional("show-metadata"): bool,
                },
                vp.Optional("history-show"): {
                    vp.Optional("no-subunit-trace"): bool,
                    vp.Optional("color"): bool,
                    vp.Optional("suppress-attachments"): bool,
                    vp.Optional("all-attachments"): bool,
                },
            }
        )
        with open(path) as fd:
            self.config = yaml.safe_load(fd.read())
        if self.config is None:
            self.config = {}
        try:
            self.schema(self.config)
        except vp.MultipleInvalid as e:
            msg = "Provided user config file {} is invalid " "because:\n{}".format(
                path, str(e)
            )
            sys.exit(msg)

    @property
    def run(self):
        return self.config.get("run")

    @property
    def failing(self):
        return self.config.get("failing")

    @property
    def last(self):
        return self.config.get("last")

    @property
    def load(self):
        return self.config.get("load")

    @property
    def history_list(self):
        return self.config.get("history-list")

    @property
    def history_show(self):
        return self.config.get("history-show")
