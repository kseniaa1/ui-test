import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gdk

from pathlib import Path

from tree import view

class Confirmation(Gtk.MessageDialog):
    def __init__(self):
        Gtk.MessageDialog.__init__(self)
        self.set_markup('<b>Вы уверены?</b>')
        self.add_button('да', 1)
        self.add_button('нет', 0)
        #  'Действительно выйти?'

class Window(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        Gtk.ApplicationWindow.__init__(self, *args, **kwargs)

        notebook = Gtk.Notebook()
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path(str(Path(__file__).parent / 'style.css'))
        Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider,
                                                  Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        tab_label = Gtk.Label()
        tab_label.set_text("JSON")
        notebook.append_page(view, tab_label)
        view.set_css_classes(['view'])
        view.show()

        notebook.set_css_classes(['window'])
        self.notebook = notebook

        self.set_child(notebook)
        self.show()

        self.app = kwargs['application']

        self.connect('close-request', self.handle_exit)

    def handle_exit(self, _):
        dialog = Confirmation()
        dialog.set_transient_for(self)
        dialog.present()
        dialog.connect('response', self.exit)
        return True

    def exit(self, widget, response):
        if response == 1:
            self.app.quit()
        widget.destroy()