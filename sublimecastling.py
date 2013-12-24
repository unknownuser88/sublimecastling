import sublime, sublime_plugin

class SublimecastlingCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view;
		try:
			view.sel()[1];
			if not (view.sel()[0].empty() and view.sel()[1].empty())
				s1 = view.substr(view.sel()[0]);
				s2 = view.substr(view.sel()[1]);
				self.view.replace(edit, view.sel()[0], s2);
				self.view.replace(edit, view.sel()[1], s1);
			else:
				sublime.status_message('Please Make A Selection');
		except IndexError:
			sublime.status_message('Please Make A Selection');
