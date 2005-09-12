Summary: 	wxWidgets/wxPython/wxPerl GUI designer
Summary(pl):	Projektant GUI dla wxWidgets/wxPython/wxPerl
Name: 		wxGlade
Version: 	0.4
Release: 	1
License:	MIT
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/wxglade/wxglade-%{version}.tar.gz
# Source0-md5:	424f408bd641795f866dcd01740885f2
URL:		http://wxglade.sourceforge.net/
BuildRequires:	python-modules >= 2.2
Requires:	python-modules >= 2.2
Requires: 	python-wxPython >= 2.4.2.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wxGlade is a GUI designer written in Python with the popular GUI
toolkit wxPython, that helps you create wxWidgets/wxPython/wxPerl user
interfaces. At the moment it can generate Python, C++, Perl and XRC
(wxWidgets' XML resources) code.

%description -l pl
wxGlade jest projektantem GUI napisanym w Pythonie i wxPythonie,
popularnym zbiorem narz�dzi GUI. Pomaga tworzy� interfejsy u�ytkownika
wxWidgets/wxPython/wxPerl. Obecnie mo�e generowa� kod Pythona, C++,
Perla oraz XRC (zasoby XML wxWidgets).

%prep
%setup -q

%build
%py_comp .
%py_ocomp .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_examplesdir}/%{name}-%{version}}

for dir in "codegen" "edit_sizers" "widgets"; do
	find "$dir" -name '*.py' -exec rm -rf '{}' ';'
done

cp -pr codegen		$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr edit_sizers	$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr icons		$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr widgets		$RPM_BUILD_ROOT%{_datadir}/%{name}
install *.py[co]	$RPM_BUILD_ROOT%{_datadir}/%{name}
install credits.txt	$RPM_BUILD_ROOT%{_datadir}/%{name}
install license.txt	$RPM_BUILD_ROOT%{_datadir}/%{name}

cat > $RPM_BUILD_ROOT%{_bindir}/wxglade <<EOF
#!/bin/sh
exec %{__python} %{_datadir}/%{name}/wxglade.pyc \$@
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs CHANGES.txt README.txt TODO.txt credits.txt
%attr(755,root,root) %{_bindir}/wxglade
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/codegen
%{_datadir}/%{name}/edit_sizers
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/widgets
%{_datadir}/%{name}/*.py[co]
%{_datadir}/%{name}/credits.txt
%{_datadir}/%{name}/license.txt