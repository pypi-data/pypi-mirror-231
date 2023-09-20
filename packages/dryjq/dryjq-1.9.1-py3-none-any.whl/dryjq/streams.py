# -*- coding: utf-8 -*-

"""

dryjq.streams

Stream and file handlers

Copyright (C) 2022 Rainer Schwarzbach

This file is part of dryjq.

dryjq is free software: you can redistribute it and/or modify
it under the terms of the MIT License.

dryjq is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the LICENSE file for more details.

"""


import json
import logging
import sys

from typing import TextIO

from serializable_trees import Tree

from dryjq import commons

from dryjq.queries import ParsedQuery


class StreamReader:

    """YAML or JSON stream reader and data handler.
    Can operate on all forms of (text) streams.
    """

    def __init__(self, stream_io: TextIO) -> None:
        """Read all data from the provided stream,
        detect if the format is JSON or YAML,
        and deserialize it into an internal data structure.

        :param stream_io: the stream to operate on.
        """
        if stream_io.seekable():
            stream_io.seek(0)
        #
        self.__input_contents = stream_io.read()
        logging.info("----- Finished reading data")
        try:
            self.__filtered_data = Tree.from_json(self.__input_contents)
        except json.JSONDecodeError:
            self.__filtered_data = Tree.from_yaml(self.__input_contents)
            self.__input_format = commons.FORMAT_YAML
        else:
            self.__input_format = commons.FORMAT_JSON
        #
        # self.__output_contents = self.__input_contents
        self.__output_format = self.__input_format
        self.__indent = commons.DEFAULT_INDENT
        self.__sort_keys = False
        self.__stream_io = stream_io

    @property
    def input_contents(self) -> str:
        """Property: the original contents read from the stream

        :returns: the original contents as a string.
        """
        return self.__input_contents

    @property
    def input_format(self) -> str:
        """Property: the detected input format

        :returns: the input format
        """
        return self.__input_format

    @property
    def output_contents(self) -> str:
        """Property: the internal data structure,
        serialized as JSON or YAML.

        :returns: the serialized data structure as a string
        """
        if self.__output_format == commons.FORMAT_JSON:
            return self.__filtered_data.to_json(
                indent=self.__indent,
                sort_keys=self.__sort_keys,
            )
        #
        output = self.__filtered_data.to_yaml(
            indent=self.__indent,
            sort_keys=self.__sort_keys,
        )
        if not isinstance(
            self.__filtered_data.root, (dict, list)
        ) and output.rstrip().endswith("\n..."):
            output = output.rstrip()[:-3]
        #
        return output

    @property
    def output_format(self) -> str:
        """Property: the output format

        :returns: the output format
        """
        return self.__output_format

    @property
    def stream_io(self) -> TextIO:
        """Property: the stream handle

        :returns: the TextIO instance of the stream
        """
        return self.__stream_io

    def set_serialization_format(
        self,
        output_format: str = commons.FORMAT_INPUT,
        indent: int = commons.DEFAULT_INDENT,
        sort_keys: bool = False,
    ) -> None:
        """Set the serialization format for the internal data structure.

        :param output_format: the output format
            (JSON, YAML, input or toggle).
        :param indent: the indent width.
        :param sort_keys: whether to sort mapping keys.
        """
        if output_format in commons.SUPPORTED_FORMATS:
            self.__output_format = output_format
        elif output_format == commons.FORMAT_INPUT:
            self.__output_format = self.input_format
        elif output_format == commons.FORMAT_TOGGLE:
            self.__output_format = commons.SUPPORTED_FORMATS[
                1 - commons.SUPPORTED_FORMATS.index(self.input_format)
            ]
        else:
            raise ValueError(f"Output format {output_format!r} not supported!")
        #
        self.__indent = indent
        self.__sort_keys = sort_keys

    def execute_merge(self, updating_data_structure: Tree) -> None:
        """merge updating_data_structure into the internal data structure.

        :param updating_data_structure: a data structure
            to be merged into self.__filtered_data
        """
        logging.debug("Filtered data before executing the merge:")
        logging.debug("%r", self.__filtered_data)
        self.__filtered_data = self.__filtered_data.joined_tree(
            updating_data_structure
        )
        logging.debug("Filtered data after executing the merge:")
        logging.debug("%r", self.__filtered_data)

    def execute_single_query(
        self,
        parsed_query: ParsedQuery,
    ) -> None:
        """Apply the provided Path to the internal data structure.

        :param access_path: an access.Path subclass instance
        """
        logging.debug("Filtered data before executing the query:")
        logging.debug("%r", self.__filtered_data)
        try:
            self.__filtered_data = parsed_query.apply_to(self.__filtered_data)
        except (IndexError, KeyError) as error:
            logging.debug(str(error))
            raise ValueError(f"{parsed_query.path} not found!") from error
        #
        logging.debug("Filtered data after executing the query:")
        logging.debug("%r", self.__filtered_data)

    def write_output(self) -> None:
        """Write output to stdout with a trailing Newline"""
        serialized_data = self.output_contents.rstrip()
        sys.stdout.write(f"{serialized_data}\n")


class FileWriter(StreamReader):

    """File writer.
    StreamReader subclass operating on text files opened
    for reading and writing (mode 'r+').
    """

    def write_output(self) -> None:
        """Write output to the file as is, but only if:
        - data has changed, and
        - the serialization format did not change.
        Log an error if one of these two hindsights applies.
        """
        not_writing = "Not writing file:"
        serialized_data = self.output_contents
        if serialized_data == self.input_contents:
            logging.error("%s contents did not change.", not_writing)
            return
        #
        if self.output_format != self.input_format:
            logging.error("%s data format changed.", not_writing)
            return
        #
        self.stream_io.seek(0)
        self.stream_io.truncate(0)
        self.stream_io.write(serialized_data)


# vim: fileencoding=utf-8 ts=4 sts=4 sw=4 autoindent expandtab syntax=python:
