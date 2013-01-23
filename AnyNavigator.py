import sublime, sublime_plugin
import re

class AnyNavigateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        def on_done(result):
            self.navigate(result)

        self.view.window().show_input_panel('pattern', '', on_done, None, None)

    def navigate(self, pattern):
        regions = self.view.find_all(pattern)
        items   = map(lambda _: self.view.substr(self.view.line(_)), regions)

        def on_done(index):
            if index >= 0:
                self.view.sel().clear()
                region = regions[index]
                e = self.view.begin_edit()
                self.view.sel().clear()
                self.view.sel().add(region)
                self.view.show(region)
                self.view.end_edit(e)

        self.view.window().show_quick_panel(items, on_done)
