from fbs_runtime.application_context import ApplicationContext
import sys
from libro.ui.mainwindow import MainWindow


class AppContext(ApplicationContext):
    def run(self):
        resources = {}
        resources['default_config'] = self.get_resource('fb2cdefault.toml')
        resources['default_css'] = self.get_resource('default.css')

        window = MainWindow(resources)
        window.show()
        return self.app.exec_()


if __name__ == '__main__':
    appctxt = AppContext()
    exit_code = appctxt.run()
    sys.exit(exit_code)
