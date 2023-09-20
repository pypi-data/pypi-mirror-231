# -*- coding: utf-8 -*-

"""

test_queries

Unit test the queries module

Copyright (C) 2022 Rainer Schwarzbach

This file is part of dryjq.

dryjq is free software: you can redistribute it and/or modify
it under the terms of the MIT License.

dryjq is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the LICENSE file for more details.

"""


from unittest import TestCase

from unittest.mock import patch

from serializable_trees.basics import ListNode, MapNode
from serializable_trees import TraversalPath, Tree

from dryjq import commons
from dryjq import queries


class Itemizer(TestCase):

    """Itemizer class test"""

    def setUp(self):
        """Initialize the itemizer"""
        self.itemizer = queries.Itemizer()

    def test_queries(self):
        """Test queries"""
        for query, expected_items in (
            (
                "",
                [
                    queries.QueryStartItem(),
                    queries.QueryEndItem(),
                ],
            ),
            (
                ".",
                [
                    queries.QueryStartItem(),
                    queries.SeparatorItem("."),
                    queries.QueryEndItem(),
                ],
            ),
            (
                " .",
                [
                    queries.QueryStartItem(),
                    queries.WhitespaceItem(" "),
                    queries.SeparatorItem("."),
                    queries.QueryEndItem(),
                ],
            ),
            (
                ".abc",
                [
                    queries.QueryStartItem(),
                    queries.SeparatorItem("."),
                    queries.LiteralItem("abc"),
                    queries.QueryEndItem(),
                ],
            ),
            (
                ".abc['yes'].xyz = [1, 2, 4]",
                [
                    queries.QueryStartItem(),
                    queries.SeparatorItem("."),
                    queries.LiteralItem("abc"),
                    queries.SubscriptOpenerItem("["),
                    queries.LiteralItem("'yes'"),
                    queries.SubscriptCloserItem("]"),
                    queries.SeparatorItem("."),
                    queries.LiteralItem("xyz"),
                    queries.WhitespaceItem(" "),
                    queries.AssignmentItem("="),
                    queries.WhitespaceItem(" "),
                    queries.SubscriptOpenerItem("["),
                    queries.LiteralItem("1,"),
                    queries.WhitespaceItem(" "),
                    queries.LiteralItem("2,"),
                    queries.WhitespaceItem(" "),
                    queries.LiteralItem("4"),
                    queries.SubscriptCloserItem("]"),
                    queries.QueryEndItem(),
                ],
            ),
        ):
            with self.subTest(query=query):
                self.assertEqual(
                    list(self.itemizer.itemize(query)),
                    expected_items,
                )
            #
        #

    def test_specialchars_variations(self):
        """Test variations of separator and subscript (...)
        ... indicator characters in queries
        """
        for query, separator, subscript_pair, expected_items in (
            (
                "/",
                "/",
                "[]",
                [
                    queries.QueryStartItem(),
                    queries.SeparatorItem("/"),
                    queries.QueryEndItem(),
                ],
            ),
            (
                "?abc",
                "?",
                "<>",
                [
                    queries.QueryStartItem(),
                    queries.SeparatorItem("?"),
                    queries.LiteralItem("abc"),
                    queries.QueryEndItem(),
                ],
            ),
            (
                "!abc('yes')!xyz = [1, 2, 4]",
                "!",
                "()",
                [
                    queries.QueryStartItem(),
                    queries.SeparatorItem("!"),
                    queries.LiteralItem("abc"),
                    queries.SubscriptOpenerItem("("),
                    queries.LiteralItem("'yes'"),
                    queries.SubscriptCloserItem(")"),
                    queries.SeparatorItem("!"),
                    queries.LiteralItem("xyz"),
                    queries.WhitespaceItem(" "),
                    queries.AssignmentItem("="),
                    queries.WhitespaceItem(" "),
                    queries.LiteralItem("[1,"),
                    queries.WhitespaceItem(" "),
                    queries.LiteralItem("2,"),
                    queries.WhitespaceItem(" "),
                    queries.LiteralItem("4]"),
                    queries.QueryEndItem(),
                ],
            ),
        ):
            with self.subTest(query=query):
                itemizer = queries.Itemizer(
                    separator_codepoint=ord(separator),
                    subscript_indicators_pair=commons.CharactersPair(
                        subscript_pair
                    ),
                )
                self.assertEqual(
                    list(itemizer.itemize(query)),
                    expected_items,
                )
            #
        #

    def test_errors(self):
        """Test itemizer errors"""
        for query, expected_exception, position in (
            (".abc[null", queries.UnclosedSubscriptError, 5),
            (".abc['def", queries.UnclosedQuoteError, 6),
        ):
            with self.subTest(query=query):
                self.assertRaisesRegex(
                    expected_exception,
                    f".* character position #{position}",
                    list,
                    self.itemizer.itemize(query),
                )
            #

    def test_warning(self):
        """Test the warning about subscript opener in subscript"""

        with self.assertLogs(None, level="WARNING") as log_cm:
            result = list(self.itemizer.itemize(".abc[def[ghi]jkl]"))
        #
        self.assertIn(
            "Possible error: Found subscript opener",
            log_cm.output[0],
        )
        self.assertEqual(
            result,
            [
                queries.QueryStartItem(),
                queries.SeparatorItem("."),
                queries.LiteralItem("abc"),
                queries.SubscriptOpenerItem("["),
                queries.LiteralItem("def[ghi"),
                queries.SubscriptCloserItem("]"),
                queries.LiteralItem("jkl]"),
                queries.QueryEndItem(),
            ],
        )

    def test_init_errors(self):
        """Test initialization errors"""
        for separator, subscript_pair, expected_exception_regex in (
            ("=", "[]", r"\ASeparator codepoint \d+ \('='\) not allowed"),
            (
                ".",
                "'",
                r"""\ASubscript indicator codepoint \d+ \("'"\) not allowed""",
            ),
            ("/", r"\/", r"\ASeparator codepoint \d+ \('/'\) not allowed"),
        ):
            with self.subTest(
                separator=separator,
                subscript_pair=subscript_pair,
            ):
                self.assertRaisesRegex(
                    ValueError,
                    expected_exception_regex,
                    queries.Itemizer,
                    separator_codepoint=ord(separator),
                    subscript_indicators_pair=commons.CharactersPair(
                        subscript_pair
                    ),
                )
            #
        #

    def test_invalid_components(self):
        """Test invalid query / path components"""
        for invalid_query, expected_exception_regex in (
            (".abc.def.{}", r"\A\{\} is not a valid path component"),
            (
                ".abc.{d,e,f}",
                r"\A\{'d': None, 'e': None, 'f': None\} is not"
                " a valid path component",
            ),
        ):
            with self.subTest(query=invalid_query):
                self.assertRaisesRegex(
                    TypeError,
                    expected_exception_regex,
                    queries.Parser().parse_query,
                    invalid_query,
                )
            #
        #


class ParsedQuery(TestCase):

    """ParsedQuery class"""

    def test_bool(self):
        """__bool__() special method"""
        for path, replacement, expected_result in (
            (TraversalPath(), Tree(1), True),
            (TraversalPath("abc"), Tree(1), True),
            (TraversalPath(), Tree(None), True),
            (TraversalPath("abc"), None, True),
            (TraversalPath(), None, False),
        ):
            with self.subTest(path=path, replacement=replacement):
                if expected_result:
                    self.assertTrue(queries.ParsedQuery(path, replacement))
                else:
                    self.assertFalse(queries.ParsedQuery(path, replacement))
                #
            #
        #

    def test_apply_to(self):
        """apply_to()  method"""
        for path, replacement, source_tree, expected_result in (
            (
                TraversalPath("abc"),
                Tree("def"),
                Tree(MapNode(abc=1, xyz=77)),
                Tree(MapNode(abc="def", xyz=77)),
            ),
            (
                TraversalPath(),
                Tree(MapNode(abc="def")),
                Tree(MapNode(abc=1, xyz=77)),
                Tree(MapNode(abc="def")),
            ),
            (
                TraversalPath("abc"),
                Tree(None),
                Tree(MapNode(abc=1, xyz=77)),
                Tree(MapNode(abc=None, xyz=77)),
            ),
            (
                TraversalPath("abc"),
                None,
                Tree(MapNode(abc=1, xyz=77)),
                Tree(1),
            ),
            (
                TraversalPath(),
                None,
                Tree(MapNode(abc=1, xyz=77)),
                Tree(MapNode(abc=1, xyz=77)),
            ),
        ):
            with self.subTest(path=path, replacement=replacement):
                parsed_query = queries.ParsedQuery(path, replacement)
                self.assertEqual(
                    parsed_query.apply_to(source_tree),
                    expected_result,
                )
            #
        #


class Parser(TestCase):

    """Test the Parser class"""

    def test_error_empty_query(self):
        """Test IllegalState error being raised"""
        parser = queries.Parser()
        self.assertRaisesRegex(
            queries.IllegalStateError,
            "The query must always start with a separator item!",
            parser.parse_query,
            "",
        )

    def test_working_queries(self):
        """Test working queries"""
        parser = queries.Parser()
        for query, expected_path, expected_replacement, warning in (
            (
                ".",
                TraversalPath(),
                None,
                None,
            ),
            (
                " .",
                TraversalPath(),
                None,
                None,
            ),
            (
                ".abc",
                TraversalPath("abc"),
                None,
                None,
            ),
            (
                ".abc[ d e f g h ]",
                TraversalPath("abc", "defgh"),
                None,
                None,
            ),
            (
                ".abc[def[ghi]jkl]",
                TraversalPath("abc", "def[ghi", "jkl]"),
                None,
                "Possible error: Found subscript",
            ),
            (
                ".abc['yes'].xyz = [1, 2, 4]",
                TraversalPath("abc", "yes", "xyz"),
                Tree(ListNode([1, 2, 4])),
                None,
            ),
            (
                ".abc['yes'].xyz = ",
                TraversalPath("abc", "yes", "xyz"),
                Tree(None),
                "Assuming empty replacement value",
            ),
        ):
            with self.subTest(query=query):
                if warning:
                    with self.assertLogs(None, level="WARNING") as log_cm:
                        self.assertEqual(
                            parser.parse_query(query),
                            queries.ParsedQuery(
                                expected_path, expected_replacement
                            ),
                        )
                    self.assertIn(warning, log_cm.output[0])
                else:
                    self.assertEqual(
                        parser.parse_query(query),
                        queries.ParsedQuery(
                            expected_path, expected_replacement
                        ),
                    )
                #
            #
        #

    def test_separator_variations(self):
        """Test working queries"""
        parser = queries.Parser()
        for query, expected_path, expected_replacement, separator in (
            (
                "/",
                TraversalPath(),
                None,
                "/",
            ),
            (
                " ~",
                TraversalPath(),
                None,
                "~",
            ),
            (
                "§abc",
                TraversalPath("abc"),
                None,
                "§",
            ),
            (
                "|abc | d e f g h ",
                TraversalPath("abc", "defgh"),
                None,
                "|",
            ),
            (
                ":abc['yes']:xyz = [1, 2, 4]",
                TraversalPath("abc", "yes", "xyz"),
                Tree(ListNode([1, 2, 4])),
                ":",
            ),
        ):
            with self.subTest(query=query, separator=separator):
                self.assertEqual(
                    parser.parse_query(
                        query, separator_codepoint=ord(separator)
                    ),
                    queries.ParsedQuery(expected_path, expected_replacement),
                )
            #
        #

    def test_illegal_states(self):
        """Test illegal states"""
        for mock_items, expected_error_regex in (
            (
                # before start
                [queries.LiteralItem("x")],
                "(?s)Parser phase: 'before start'.+"
                r"Expected QueryStartItem\(\)",
            ),
            (
                # started
                [
                    queries.QueryStartItem(),
                    queries.LiteralItem("x"),
                ],
                "(?s)Parser phase: 'started'.+"
                "The query must always start with a separator item",
            ),
            (
                # address
                [
                    queries.QueryStartItem(),
                    queries.SeparatorItem("."),
                    queries.LiteralItem("x"),
                    queries.QueryStartItem(),
                ],
                "(?s)Parser phase: 'address'.+"
                r"QueryStartItem\(\) not allowed here",
            ),
            (
                # replacement
                [
                    queries.QueryStartItem(),
                    queries.SeparatorItem("."),
                    queries.LiteralItem("x"),
                    queries.AssignmentItem("="),
                    queries.QueryStartItem(),
                ],
                "(?s)Parser phase: 'replacement'.+"
                r"QueryStartItem\(\) not allowed here",
            ),
            (
                # ended
                [
                    queries.QueryStartItem(),
                    queries.SeparatorItem("."),
                    queries.LiteralItem("x"),
                    queries.AssignmentItem("="),
                    queries.QueryEndItem(),
                    queries.WhitespaceItem(" "),
                ],
                "(?s)Parser phase: 'ended'.+No items allowed anymore",
            ),
        ):
            with self.subTest(expected_error_regex=expected_error_regex):
                with patch.object(
                    queries.Itemizer, "itemize", return_value=mock_items
                ):
                    parser = queries.Parser()
                    self.assertRaisesRegex(
                        queries.IllegalStateError,
                        expected_error_regex,
                        parser.parse_query,
                        "…",
                    )
                #
            #
        #

    @patch.object(queries.Parser, "phase", new="not implemented")
    def test_phase_not_implemented(self):
        """Test illegal states"""
        parser = queries.Parser()
        self.assertRaisesRegex(
            queries.IllegalStateError,
            "(?s)Parser phase: 'not implemented'.+"
            "Item handler for this phase not implemented",
            parser.parse_query,
            "…",
        )


# vim: fileencoding=utf-8 ts=4 sts=4 sw=4 autoindent expandtab syntax=python:
