Summary:	Check HTML documents for broken links
Summary(pl.UTF-8):	Sprawdzanie dokumentów HTML pod kątem zerwanych odnośników
Name:		linkchecker
Version:	4.8
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/linkchecker/%{name}-%{version}.tar.gz
# Source0-md5:	0473839d4c263ffeb98dc44e59026339
URL:		http://linkchecker.sourceforge.net/
BuildRequires:	pydoc
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linkchecker features:
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

%description -l pl.UTF-8
Cechy linkcheckera:
- sprawdzanie rekurencyjne
- wielowątkowość
- wyjście w kolorowanym lub zwykłym tekście, HTML-u, SQL-u, CSV lub
  jako mapa serwisu w GML-u lub XML-u
- obsługa odnośników HTTP/1.1, HTTPS, FTP, mailto:, news:, nntp:,
  Gopher, Telnet i lokalnych plików
- restrykcje sprawdzania odnośników przy pomocy filtrów URL-i opartych
  o wyrażenia regularne
- obsługa proxy
- autoryzacja użytkownik/hasło dla HTTP i FTP
- obsługa protokołu wyłączeń robots.txt
- obsługa ciasteczek
- obsługa wielu języków (i18n)
- interfejs z linii poleceń
- interfejs WWW (Fast)CGI (wymagający serwera HTTP)

%prep
%setup -q

%build
env CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

# omitted by setup install
cp -a build/share/locale $RPM_BUILD_ROOT%{_datadir}

%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog TODO doc/en/*.{html,css,ico,jpg,png}
%attr(755,root,root) %{_bindir}/linkchecker
%dir %{py_sitedir}/linkcheck
%{py_sitedir}/linkcheck/*.py[co]
%dir %{py_sitedir}/linkcheck/HtmlParser
%{py_sitedir}/linkcheck/HtmlParser/*.py[co]
%attr(755,root,root) %{py_sitedir}/linkcheck/HtmlParser/htmlsax.so
%dir %{py_sitedir}/linkcheck/cache
%{py_sitedir}/linkcheck/cache/*.py[co]
%dir %{py_sitedir}/linkcheck/checker
%{py_sitedir}/linkcheck/checker/*.py[co]
%dir %{py_sitedir}/linkcheck/configuration
%{py_sitedir}/linkcheck/configuration/*.py[co]
%dir %{py_sitedir}/linkcheck/director
%{py_sitedir}/linkcheck/director/*.py[co]
%dir %{py_sitedir}/linkcheck/dns
%{py_sitedir}/linkcheck/dns/*.py[co]
%dir %{py_sitedir}/linkcheck/dns/rdtypes
%{py_sitedir}/linkcheck/dns/rdtypes/*.py[co]
%dir %{py_sitedir}/linkcheck/dns/rdtypes/ANY
%{py_sitedir}/linkcheck/dns/rdtypes/ANY/*.py[co]
%dir %{py_sitedir}/linkcheck/dns/rdtypes/IN
%{py_sitedir}/linkcheck/dns/rdtypes/IN/*.py[co]
%dir %{py_sitedir}/linkcheck/ftpparse
%{py_sitedir}/linkcheck/ftpparse/*.py[co]
%attr(755,root,root) %{py_sitedir}/linkcheck/ftpparse/_ftpparse.so
%dir %{py_sitedir}/linkcheck/logger
%{py_sitedir}/linkcheck/logger/*.py[co]
%{py_sitedir}/linkchecker-*.egg-info
%dir %{_datadir}/linkchecker
%{_datadir}/linkchecker/linkcheckerrc
%{_datadir}/linkchecker/logging.conf
%dir %{_datadir}/linkchecker/examples
%attr(755,root,root) %{_datadir}/linkchecker/examples/*.sh
%attr(755,root,root) %{_datadir}/linkchecker/examples/*cgi
%{_datadir}/linkchecker/examples/check.js
%{_datadir}/linkchecker/examples/index.html
%lang(de) %{_datadir}/linkchecker/examples/lc_cgi.html.de
%{_datadir}/linkchecker/examples/lc_cgi.html.en
%lang(de) %{_datadir}/linkchecker/examples/leer.html.de
%{_datadir}/linkchecker/examples/leer.html.en
%{_datadir}/linkchecker/examples/linkchecker-completion
%{_mandir}/man1/linkchecker.1*
%{_mandir}/man5/linkcheckerrc.5*
%lang(de) %{_mandir}/de/man1/linkchecker.1*
%lang(de) %{_mandir}/de/man5/linkcheckerrc.5*
