pip install PyQt5

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebEngineCore import *
from PyQt5.QtNetwork import QNetworkProxy  # Add this import statement

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Unrestricted and Proxy-enabled Web Browser")
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.showMaximized()


        # Create a profile with unrestricted settings
        profile = QWebEngineProfile.defaultProfile()
        profile.setPersistentCookiesPolicy(QWebEngineProfile.NoPersistentCookies)
        profile.setHttpCacheType(QWebEngineProfile.NoCache)
        profile.setPersistentStoragePath("")

        # Set the unrestricted profile for the browser
        self.browser.setPage(QWebEnginePage(profile, self.browser))

        # Add proxies
        proxy = QNetworkProxy()
        proxy.setType(QNetworkProxy.HttpProxy)
        proxy.setHostName("182.253.109.21")  # Replace with your proxy server
        proxy.setPort(8080)  # Replace with the proxy port
        QNetworkProxy.setApplicationProxy(proxy)

        # Create a toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # Add navigation actions
        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        toolbar.addAction(back_btn)

        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        toolbar.addAction(forward_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        toolbar.addAction(reload_btn)

        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.navigate_home)
        toolbar.addAction(home_btn)

        # Add an address bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        toolbar.addWidget(self.url_bar)

        # Load a default homepage
        self.browser.setUrl(QUrl("https://www.google.com"))

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

app = QApplication(sys.argv)
window = WebBrowser()
sys.exit(app.exec_())