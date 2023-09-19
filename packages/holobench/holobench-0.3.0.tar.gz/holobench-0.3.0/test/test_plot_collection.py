# (Mostly) Generated by CodiumAI, sanity checked and fixed by a human
import unittest
from typing import Optional

import panel as pn

from bencher.plotting.plot_collection import PlotCollection, PlotProvider


class TestPlotProvider:
    def plot_1(self) -> Optional[pn.panel]:
        return [pn.pane.Markdown("Test plot 1", name="plot_1")]

    def plot_2(self) -> Optional[pn.panel]:
        return [pn.pane.Markdown("Test plot 2", name="plot_2")]


class TestPlotCollection(unittest.TestCase):
    # Tests that adding a plotter source successfully adds all the plotting methods of the class to the dictionary of available plotting functions
    def test_add_plotter_source_success(self):
        plot_coll = PlotCollection()

        plot_coll.add_plotter_source(TestPlotProvider())
        assert len(plot_coll.plotter_providers) == 2
        assert "plot_1" in plot_coll.plotter_providers
        assert "plot_2" in plot_coll.plotter_providers

    # Tests that adding a plot successfully adds the plot to the list of active plotting functions
    def test_add_plot_success(self):
        plot_coll = PlotCollection()

        plot_coll.add_plotter_source(TestPlotProvider())
        plot_coll.add("plot_1")
        assert len(plot_coll.plotters) == 1
        assert "plot_1" in plot_coll.plotters

    # Tests that removing a plot successfully removes the plot from the list of active plotting functions
    def test_remove_plot_success(self):
        plot_coll = PlotCollection()

        plot_coll.add_plotter_source(TestPlotProvider())
        plot_coll.add("plot_1")
        plot_coll.remove("plot_1")
        assert len(plot_coll.plotters) == 0

    # Tests that adding a plotter source with no plotting methods does not add any plotting methods to the dictionary of available plotting functions
    def test_add_plotter_source_no_methods(self):
        plot_coll = PlotCollection()

        class TestPlotProviderEmpty(PlotProvider):
            pass

        plot_coll.add_plotter_source(TestPlotProviderEmpty())
        assert len(plot_coll.plotter_providers) == 0

    # Tests that adding a non-existent plot does not add the plot to the list of active plotting functions
    def test_add_nonexistent_plot(self):
        plot_coll = PlotCollection()

        plot_coll.add_plotter_source(TestPlotProvider())
        with self.assertRaises(ValueError):
            plot_coll.add("plot_3")
        assert len(plot_coll.plotters) == 0

    # Tests that removing a non-existent plot does not remove any plot from the list of active plotting functions
    def test_remove_nonexistent_plot(self):
        plot_coll = PlotCollection()

        plot_coll.add_plotter_source(TestPlotProvider())
        plot_coll.add("plot_1")
        try:
            plot_coll.remove("plot_3")
        except KeyError:
            pass
        assert len(plot_coll.plotters) == 1

    def test_add_uninitialised_class(self):
        plot_coll = PlotCollection()
        with self.assertRaises(ValueError):
            plot_coll.add_plotter_source(TestPlotProvider)

    def test_add_not_a_list(self):
        plot_coll = PlotCollection()

        plot_coll.add_plotter_source(TestPlotProvider())
        with self.assertRaises(ValueError):
            # try adding a variable that is not a list
            plot_coll.add_list("plot_1")

    def test_add_list_empty(self):
        plot_coll = PlotCollection()
        plot_coll.add_plotter_source(TestPlotProvider())
        plot_coll.add_list([])
        assert len(plot_coll.plotters) == 0
