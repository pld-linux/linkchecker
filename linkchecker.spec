Summary:	Check HTML documents for broken links
Name:		linkchecker
Version:	1.12.3
Release:	1
Source0:	http://dl.sourceforge.net/linkchecker/%{name}-%{version}.tar.gz
# Source0-md5:	6a40d830781507fc6b70d3f2d4d381ec
License:	GPL
Group:		Applications/Networking
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Url:		http://linkchecker.sourceforge.net/

%description
Linkchecker features
- recursive checking
- multithreading
- output in colored or normal text, HTML, SQL, CSV or a sitemap graph
  in GML or XML.
- HTTP/1.1, HTTPS, FTP, mailto:, news:, nntp:, Gopher, Telnet and
  local file links support
- restriction of link checking with regular expression filters for
  URLs
- proxy support
- username/password authorization for HTTP and FTP
- robots.txt exclusion protocol support
- Cookie support
- i18n support
- a command line interface
- a (Fast)CGI web interface (requires HTTP server)

%prep
%setup -q

%build
env CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README TODO lconline/ test/
%{py_sitedir}/_linkchecker_configdata.py
%{py_sitedir}/linkcheck/AnsiColor.py
%{py_sitedir}/linkcheck/Config.py
%{py_sitedir}/linkcheck/FileUrlData.py
%{py_sitedir}/linkcheck/FtpUrlData.py
%{py_sitedir}/linkcheck/GopherUrlData.py
%{py_sitedir}/linkcheck/HostCheckingUrlData.py
%{py_sitedir}/linkcheck/HttpUrlData.py
%{py_sitedir}/linkcheck/HttpsUrlData.py
%{py_sitedir}/linkcheck/IgnoredUrlData.py
%{py_sitedir}/linkcheck/LRU.py
%{py_sitedir}/linkcheck/MailtoUrlData.py
%{py_sitedir}/linkcheck/NntpUrlData.py
%{py_sitedir}/linkcheck/ProxyUrlData.py
%{py_sitedir}/linkcheck/StringUtil.py
%{py_sitedir}/linkcheck/TelnetUrlData.py
%{py_sitedir}/linkcheck/Threader.py
%{py_sitedir}/linkcheck/UrlData.py
%{py_sitedir}/linkcheck/XmlUtils.py
%{py_sitedir}/linkcheck/__init__.py
%{py_sitedir}/linkcheck/containers.py
%{py_sitedir}/linkcheck/debug.py
%{py_sitedir}/linkcheck/fcgi.py
%{py_sitedir}/linkcheck/httplib2.py
%{py_sitedir}/linkcheck/i18n.py
%{py_sitedir}/linkcheck/lc_cgi.py
%{py_sitedir}/linkcheck/linkname.py
%{py_sitedir}/linkcheck/linkparse.py
%{py_sitedir}/linkcheck/optcomplete.py
%{py_sitedir}/linkcheck/robotparser2.py
%{py_sitedir}/linkcheck/sz_fcgi.py
%{py_sitedir}/linkcheck/test_support.py
%{py_sitedir}/linkcheck/url.py
%{py_sitedir}/linkcheck/util1.py
%{py_sitedir}/linkcheck/log/BlacklistLogger.py
%{py_sitedir}/linkcheck/log/CSVLogger.py
%{py_sitedir}/linkcheck/log/ColoredLogger.py
%{py_sitedir}/linkcheck/log/GMLLogger.py
%{py_sitedir}/linkcheck/log/HtmlLogger.py
%{py_sitedir}/linkcheck/log/Logger.py
%{py_sitedir}/linkcheck/log/NoneLogger.py
%{py_sitedir}/linkcheck/log/SQLLogger.py
%{py_sitedir}/linkcheck/log/StandardLogger.py
%{py_sitedir}/linkcheck/log/XMLLogger.py
%{py_sitedir}/linkcheck/log/__init__.py
%{py_sitedir}/linkcheck/parser/__init__.py
%{py_sitedir}/linkcheck/parser/htmllib.py
%{py_sitedir}/linkcheck/DNS/Base.py
%{py_sitedir}/linkcheck/DNS/Class.py
%{py_sitedir}/linkcheck/DNS/Lib.py
%{py_sitedir}/linkcheck/DNS/Opcode.py
%{py_sitedir}/linkcheck/DNS/Status.py
%{py_sitedir}/linkcheck/DNS/Type.py
%{py_sitedir}/linkcheck/DNS/__init__.py
%{py_sitedir}/linkcheck/DNS/lazy.py
%{py_sitedir}/linkcheck/DNS/winreg.py
%{py_sitedir}/_linkchecker_configdata.pyc
%{py_sitedir}/linkcheck/AnsiColor.pyc
%{py_sitedir}/linkcheck/Config.pyc
%{py_sitedir}/linkcheck/FileUrlData.pyc
%{py_sitedir}/linkcheck/FtpUrlData.pyc
%{py_sitedir}/linkcheck/GopherUrlData.pyc
%{py_sitedir}/linkcheck/HostCheckingUrlData.pyc
%{py_sitedir}/linkcheck/HttpUrlData.pyc
%{py_sitedir}/linkcheck/HttpsUrlData.pyc
%{py_sitedir}/linkcheck/IgnoredUrlData.pyc
%{py_sitedir}/linkcheck/LRU.pyc
%{py_sitedir}/linkcheck/MailtoUrlData.pyc
%{py_sitedir}/linkcheck/NntpUrlData.pyc
%{py_sitedir}/linkcheck/ProxyUrlData.pyc
%{py_sitedir}/linkcheck/StringUtil.pyc
%{py_sitedir}/linkcheck/TelnetUrlData.pyc
%{py_sitedir}/linkcheck/Threader.pyc
%{py_sitedir}/linkcheck/UrlData.pyc
%{py_sitedir}/linkcheck/XmlUtils.pyc
%{py_sitedir}/linkcheck/__init__.pyc
%{py_sitedir}/linkcheck/containers.pyc
%{py_sitedir}/linkcheck/debug.pyc
%{py_sitedir}/linkcheck/fcgi.pyc
%{py_sitedir}/linkcheck/httplib2.pyc
%{py_sitedir}/linkcheck/i18n.pyc
%{py_sitedir}/linkcheck/lc_cgi.pyc
%{py_sitedir}/linkcheck/linkname.pyc
%{py_sitedir}/linkcheck/linkparse.pyc
%{py_sitedir}/linkcheck/optcomplete.pyc
%{py_sitedir}/linkcheck/robotparser2.pyc
%{py_sitedir}/linkcheck/sz_fcgi.pyc
%{py_sitedir}/linkcheck/test_support.pyc
%{py_sitedir}/linkcheck/url.pyc
%{py_sitedir}/linkcheck/util1.pyc
%{py_sitedir}/linkcheck/log/BlacklistLogger.pyc
%{py_sitedir}/linkcheck/log/CSVLogger.pyc
%{py_sitedir}/linkcheck/log/ColoredLogger.pyc
%{py_sitedir}/linkcheck/log/GMLLogger.pyc
%{py_sitedir}/linkcheck/log/HtmlLogger.pyc
%{py_sitedir}/linkcheck/log/Logger.pyc
%{py_sitedir}/linkcheck/log/NoneLogger.pyc
%{py_sitedir}/linkcheck/log/SQLLogger.pyc
%{py_sitedir}/linkcheck/log/StandardLogger.pyc
%{py_sitedir}/linkcheck/log/XMLLogger.pyc
%{py_sitedir}/linkcheck/log/__init__.pyc
%{py_sitedir}/linkcheck/parser/__init__.pyc
%{py_sitedir}/linkcheck/parser/htmllib.pyc
%{py_sitedir}/linkcheck/DNS/Base.pyc
%{py_sitedir}/linkcheck/DNS/Class.pyc
%{py_sitedir}/linkcheck/DNS/Lib.pyc
%{py_sitedir}/linkcheck/DNS/Opcode.pyc
%{py_sitedir}/linkcheck/DNS/Status.pyc
%{py_sitedir}/linkcheck/DNS/Type.pyc
%{py_sitedir}/linkcheck/DNS/__init__.pyc
%{py_sitedir}/linkcheck/DNS/lazy.pyc
%{py_sitedir}/linkcheck/DNS/winreg.pyc
%{py_sitedir}/linkcheck/parser/htmlsax.so
%attr(755,root,root) %{_bindir}/linkchecker
%{_datadir}/locale/de/LC_MESSAGES/linkcheck.mo
%{_datadir}/locale/fr/LC_MESSAGES/linkcheck.mo
%{_datadir}/locale/nl/LC_MESSAGES/linkcheck.mo
%{_datadir}/linkchecker/linkcheckerrc
%{_datadir}/linkchecker/examples/leer.html.en
%{_datadir}/linkchecker/examples/leer.html.de
%{_datadir}/linkchecker/examples/index.html
%{_datadir}/linkchecker/examples/lc_cgi.html.en
%{_datadir}/linkchecker/examples/lc_cgi.html.de
%{_datadir}/linkchecker/examples/check.js
%{_datadir}/linkchecker/examples/lc.cgi
%{_datadir}/linkchecker/examples/lc.fcgi
%{_datadir}/linkchecker/examples/lc.sz_fcgi
%{_datadir}/linkchecker/examples/linkchecker.bat
%{_datadir}/linkchecker/examples/linkchecker-completion
%{_datadir}/linkchecker/examples/linkcheck-cron.sh
%{_mandir}/man1/linkchecker.1.gz
