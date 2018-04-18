import sublime
import sublime_plugin


class ToggleSix(sublime_plugin.WindowCommand):
    def run(self):
        setts = sublime.load_settings('Preferences.sublime-settings')
        ignored = setts.get('ignored_packages')

        if 'Six' in ignored:
            ignored.remove('Six')
        else:
            ignored.append('Six')
