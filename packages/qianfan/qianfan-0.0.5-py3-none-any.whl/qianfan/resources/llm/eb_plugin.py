# Copyright (c) 2023 Baidu, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import qianfan.errors as errors

from typing import Any, Dict, Optional, Set
from qianfan.resources.typing import QfLLMInfo
from qianfan.resources.llm.base import BaseResource, UNSPECIFIED_MODEL


class EBPlugin(BaseResource):
    """
    QianFan Plugin API Resource

    """

    def __init__(
        self,
        model: Optional[str] = None,
        endpoint: Optional[str] = None,
        **kwargs: Dict[str, Any]
    ) -> None:
        """
        Init for Plugin
        `model` will not be accepted
        """
        if model is not None or endpoint is not None:
            raise errors.InvalidArgumentError("`model` is not supported for plugin")
        super().__init__(model, endpoint, **kwargs)

    def _supported_models(self):
        """
        Only one endpoint provided for plugins

        Args:
            None

        Returns:
            a dict which key is preset model and value is the endpoint

        """
        return {
            UNSPECIFIED_MODEL: QfLLMInfo(
                endpoint="/erniebot/plugins",
                required_keys={"messages", "plugins"},
                optional_keys={
                    "user_id",
                },
            ),
        }

    def _default_model(self):
        """
        no default model for EBPlugin

        """
        return UNSPECIFIED_MODEL

    def _convert_endpoint(self, endpoint: str) -> str:
        """
        convert endpoint to ChatCompletion API endpoint
        """
        return "/erniebot/plugins"

    def _check_params(
        self,
        model: Optional[str],
        endpoint: Optional[str],
        stream: bool,
        retry_count: int,
        request_timeout: float,
        backoff_factor: float,
        **kwargs
    ):
        """
        check params
        plugin does not support model and endpoint arguments
        """
        if model is not None or endpoint is not None:
            raise errors.InvalidArgumentError("model is not supported in plugin")
        return super()._check_params(
            model, endpoint, stream, retry_count, request_timeout, backoff_factor, **kwargs
        )
