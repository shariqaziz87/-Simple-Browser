
import sys
from PyQt5.QtCore import QUrl

from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QLineEdit, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView

# Main Browser Window
class SimpleBrowser(QMainWindow):

    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("Simple Browser")
        self.setGeometry(100, 100, 800, 600)

        # Create a web view widget to display web pages
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))  # Set default homepage
        self.setCentralWidget(self.browser)

        # Create a navigation toolbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back button
        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Forward button
        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # reload button
        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)

        navbar.addAction(reload_btn)


        # Address bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Update URL bar when the page changes
        self.browser.urlChanged.connect(self.update_url_bar)

    # Navigate to the URL entered in the address bar
    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "https://" + url
        self.browser.setUrl(QUrl(url))

    # Update the URL bar when the page changes
    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleBrowser()
    window.show()
    sys.exit(app.exec_())






