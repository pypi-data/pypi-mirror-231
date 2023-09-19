# Generated by CodiumAI
from bencher.bench_report import BenchReport
import unittest
import panel as pn


class TestBenchReport(unittest.TestCase):
    # Tests that the BenchReport instance is initialized with the provided bench_name parameter
    def test_init_with_bench_name(self):
        bench_name = "Test Bench"
        bench_report = BenchReport(bench_name)
        self.assertEqual(bench_report.bench_name, bench_name)

    # Tests that a Markdown pane with a custom name is appended to the BenchReport instance
    def test_append_markdown_with_custom_name(self):
        bench_report = BenchReport()
        markdown = "# Test Markdown"
        name = "Custom Markdown"
        md_pane = bench_report.append_markdown(markdown, name=name)
        self.assertEqual(md_pane.name, name)
        self.assertEqual(md_pane.object, markdown)

    # Tests that a panel with a custom name is appended to the BenchReport instance
    def test_append_panel_with_custom_name(self):
        bench_report = BenchReport()
        panel = pn.panel("Test Panel")
        name = "Custom Panel"
        bench_report.append(panel, name=name)
        self.assertEqual(bench_report.pane[-1].name, name)
        self.assertEqual(bench_report.pane[-1].objects[0], panel)

    def test_append__col_panel_with_custom_name(self):
        bench_report = BenchReport()
        panel = pn.panel("Test Panel")
        name = "Custom Panel"
        bench_report.append_col(panel, name=name)
        self.assertEqual(bench_report.pane[-1].name, name)
        self.assertEqual(bench_report.pane[-1].objects[0], panel)

    def test_append_column(self):
        bench_report = BenchReport()
        panel = pn.panel("Test Panel")
        bench_report.append_col(panel)
        self.assertEqual(bench_report.pane[-1].name, panel.name)

    def test_append_tab(self):
        bench_report = BenchReport()
        panel = pn.panel("Test Panel")
        bench_report.append_tab(panel)
        self.assertEqual(bench_report.pane[-1].name, panel.name)
