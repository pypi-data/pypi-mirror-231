import platform
import unittest
from unittest.mock import patch

import pytest

import tabula


class TestReadPdfJarPath(unittest.TestCase):
    def setUp(self):
        self.pdf_path = "tests/resources/data.pdf"

    @patch("tabula.backend.jpype.startJVM")
    def test_read_pdf_with_silent_true(self, jvm_func):
        with pytest.raises(RuntimeError):
            tabula.read_pdf(self.pdf_path, encoding="utf-8", silent=True)

        target_args = []
        if platform.system() == "Darwin":
            target_args += ["-Djava.awt.headless=true"]
        target_args += [
            "-Dfile.encoding=UTF8",
            "-Dorg.slf4j.simpleLogger.defaultLogLevel=off",
            "-Dorg.apache.commons.logging.Log=org.apache.commons.logging.impl.NoOpLog",
        ]
        jvm_func.assert_called_once_with(
            *target_args,
            convertStrings=False,
        )
