# -*- coding: utf-8 -*-

"""

test.test_commandline

Unit test the commandline module

Copyright (C) 2022 Rainer Schwarzbach

This file is part of dryjq.

dryjq is free software: you can redistribute it and/or modify
it under the terms of the MIT License.

dryjq is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the LICENSE file for more details.

"""


import io
import itertools
import os
import secrets
import tempfile
import time

from unittest import TestCase

from unittest.mock import patch

from serializable_trees import TraversalPath, Tree

from dryjq import commandline
from dryjq import queries

from . import data
from .commons import GenericCallResult


class ExecResult(GenericCallResult):

    """Program execution result"""

    @classmethod
    def do_call(cls, *args, **kwargs):
        """Do the real function call"""
        program = commandline.Program(list(args))
        return program.execute(parsed_query=kwargs.get("parsed_query"))


class Program(TestCase):

    """Test the Program class"""

    def test_complete_format(self):
        """Test completing a format, all combinations"""
        for target_format in ("input", "toggle", "JSON", "YAML"):
            combinations = [
                (char.lower(), char.upper()) for char in target_format
            ]
            matching_abbreviations = set()
            for index in range(len(target_format)):
                matching_abbreviations.update(
                    set(itertools.product(*combinations[: index + 1]))
                )
            #
            for current_input in matching_abbreviations:
                format_str = "".join(current_input)
                with self.subTest(format_str=format_str):
                    self.assertEqual(
                        commandline.Program.complete_format(format_str),
                        target_format,
                    )
                #
            #
        #

    def test_unsupported_format(self):
        """Test unsupported formats"""
        for target_format in ("XML", "xml", "ini", "toml"):
            with self.subTest(target_format=target_format):
                self.assertRaisesRegex(
                    ValueError,
                    f"Unsupported format {target_format!r}!",
                    commandline.Program.complete_format,
                    target_format,
                )
            #
        #
        #

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_exec_stdin_extract(self, mock_stdout):
        """Test execute function, reading stdin, extract mode"""
        with self.assertLogs(level="INFO") as log_cm:
            result = ExecResult.from_call(
                "--verbose",
                stdin_data=data.INPUT_YAML_ANIMALS,
                stdout=mock_stdout,
                parsed_query=queries.ParsedQuery(
                    TraversalPath("felines", "cats", "big", 1), None
                ),
            )
        self.assertEqual(
            log_cm.records[0].message, "Operating in extract mode."
        )
        self.assertEqual(result.stdout, data.EXPECT_CATS_BIG_1)
        self.assertEqual(result.returncode, data.RETURNCODE_OK)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_exec_stdin_replace_none_path(self, mock_stdout):
        """Test execute function, reading stdin, replace mode, None path"""
        with self.assertLogs(level="INFO") as log_cm:
            result = ExecResult.from_call(
                "--verbose",
                stdin_data=data.INPUT_YAML_ANIMALS,
                stdout=mock_stdout,
                parsed_query=queries.ParsedQuery(
                    TraversalPath(),
                    Tree("xyz"),
                ),
            )
        self.assertEqual(
            log_cm.records[0].message,
            "Operating in replace mode.",
        )
        self.assertEqual(result.stdout, "xyz\n")
        self.assertEqual(result.returncode, data.RETURNCODE_OK)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_exec_stdin_replace(self, mock_stdout):
        """Test execute function, reading stdin, replace mode"""
        with self.assertLogs(level="INFO") as log_cm:
            result = ExecResult.from_call(
                "--debug",
                stdin_data=data.INPUT_YAML_ANIMALS,
                stdout=mock_stdout,
                parsed_query=queries.ParsedQuery(
                    TraversalPath("felines", "cats", "big", 2),
                    Tree("panther"),
                ),
            )
        self.assertEqual(
            log_cm.records[0].message, "Operating in replace mode."
        )
        self.assertEqual(result.stdout, data.EXPECT_YAML_JAGUAR2PANTHER)
        self.assertEqual(result.returncode, data.RETURNCODE_OK)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_exec_stdin_passthru(self, mock_stdout):
        """Test execute function, reading stdin, extract mode (passthru)"""
        with self.assertLogs(level="INFO") as log_cm:
            result = ExecResult.from_call(
                "--verbose",
                stdin_data=data.INPUT_YAML_ANIMALS,
                stdout=mock_stdout,
            )
        #
        self.assertEqual(
            log_cm.records[0].message,
            "Operating in extract mode (passthrough).",
        )
        self.assertEqual(result.stdout, data.INPUT_YAML_ANIMALS)
        self.assertEqual(result.returncode, data.RETURNCODE_OK)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_exec_invalid_input(self, mock_stdout):
        """Test execute function, reading stdin, invalid input"""
        with self.assertLogs(level="ERROR") as log_cm:
            result = ExecResult.from_call(
                stdin_data="a: b: c",
                stdout=mock_stdout,
            )
        #
        self.assertIn(
            # FIXME: PyYAML specific error message, might change
            "mapping values are not allowed here",
            log_cm.records[0].message,
        )
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.returncode, data.RETURNCODE_ERROR)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_exec_not_found(self, mock_stdout):
        """Test execute function, reading stdin, value not found"""
        wrong_index = "HUGE"
        with self.assertLogs(level="ERROR") as log_cm:
            result = ExecResult.from_call(
                stdin_data=data.INPUT_YAML_ANIMALS,
                stdout=mock_stdout,
                parsed_query=queries.ParsedQuery(
                    TraversalPath("felines", "cats", wrong_index),
                    None,
                ),
            )
        #
        self.assertEqual(
            log_cm.records[0].message,
            f"TraversalPath('felines', 'cats', {wrong_index!r}) not found!",
        )
        self.assertEqual(result.stdout.rstrip(), "")
        self.assertEqual(result.returncode, data.RETURNCODE_ERROR)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_exec_stdin_inplace(self, mock_stdout):
        """Test execute function, reading stdin, replace mode with --inplace"""
        with self.assertLogs(level="WARNING") as log_cm:
            result = ExecResult.from_call(
                "--inplace",
                stdin_data=data.INPUT_YAML_ANIMALS,
                stdout=mock_stdout,
                parsed_query=queries.ParsedQuery(
                    TraversalPath("felines", "cats", "big", 2),
                    Tree("panther"),
                ),
            )
        self.assertEqual(
            log_cm.records[0].message, "Cannot modify <stdin> in place"
        )
        self.assertEqual(result.stdout, data.EXPECT_YAML_JAGUAR2PANTHER)
        self.assertEqual(result.returncode, data.RETURNCODE_OK)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_exec_file_read(self, mock_stdout):
        """Test reading a file"""
        with tempfile.TemporaryDirectory() as temporary_directory:
            yaml_file_name = os.path.join(
                temporary_directory, f"{secrets.token_urlsafe(6)}.yaml"
            )
            with open(
                yaml_file_name, mode="w", encoding="utf-8"
            ) as source_file:
                source_file.write(data.INPUT_YAML_ANIMALS)
            #
            time.sleep(0.1)
            creation_time = os.stat(yaml_file_name).st_mtime
            result = ExecResult.from_call(
                "",
                yaml_file_name,
                stdout=mock_stdout,
                parsed_query=queries.ParsedQuery(
                    TraversalPath("felines", "cats", "big", 2),
                    Tree("panther"),
                ),
            )
            check_time = os.stat(yaml_file_name).st_mtime
        #
        self.assertEqual(result.stdout, data.EXPECT_YAML_JAGUAR2PANTHER)
        self.assertEqual(result.returncode, data.RETURNCODE_OK)
        self.assertEqual(check_time, creation_time)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_exec_file_write(self, mock_stdout):
        """Test modifying a file in place"""
        with tempfile.TemporaryDirectory() as temporary_directory:
            yaml_file_name = os.path.join(
                temporary_directory, f"{secrets.token_urlsafe(6)}.yaml"
            )
            with open(
                yaml_file_name, mode="w", encoding="utf-8"
            ) as source_file:
                source_file.write(data.INPUT_YAML_ANIMALS)
            #
            time.sleep(0.1)
            creation_time = os.stat(yaml_file_name).st_mtime
            result = ExecResult.from_call(
                "--inplace",
                "",
                yaml_file_name,
                stdout=mock_stdout,
                parsed_query=queries.ParsedQuery(
                    TraversalPath("felines", "cats", "big", 2),
                    Tree("panther"),
                ),
            )
            check_time = os.stat(yaml_file_name).st_mtime
            self.assertGreater(check_time, creation_time)
            with open(
                yaml_file_name, mode="r", encoding="utf-8"
            ) as changed_file:
                written_data = changed_file.read()
            #
            self.assertEqual(written_data, data.EXPECT_YAML_JAGUAR2PANTHER)
        #
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.returncode, data.RETURNCODE_OK)


# vim: fileencoding=utf-8 ts=4 sts=4 sw=4 autoindent expandtab syntax=python:
