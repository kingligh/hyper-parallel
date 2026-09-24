# Copyright 2026 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Keep eager export lists aligned with the lazy RL module registries."""

import unittest

import rl
import rl.agentic as agentic


class TestLazyExports(unittest.TestCase):
    """Check that public export lists match their lazy lookup registries."""

    def test_root_exports_match_registry_order(self) -> None:
        """Keep root exports in the registry's insertion order."""
        expected = list(rl._EXPORTS)
        self.assertEqual(
            rl.__all__, expected,
            f"Root exports differ: expected={expected}, actual={rl.__all__}",
        )

    def test_agentic_exports_match_sorted_registry(self) -> None:
        """Keep agentic exports sorted as before the import-order change."""
        expected = sorted(agentic._EXPORTS)
        self.assertEqual(
            agentic.__all__, expected,
            f"Agentic exports differ: expected={expected}, actual={agentic.__all__}",
        )
