Summary: 	wxWidgets/wxPython/wxPerl GUI designer
Summary(pl):	Projektant GUI dla wxWidgets/wxPython/wxPerl
Name: 		wxGlade
Version: 	0.3.2
Release: 	0.1
License:	MIT
Group:		Development/Tools
Source0: 	http://dl.sourceforge.net/wxglade/%{name}-%{version}.tgz
# Source0-md5:	dda7f2cd7b725e1545f49705ddbf9a4e
URL:		http://wxglade.sourceforge.net/
BuildRequires:	python-modules >= 2.2
Requires:	python-modules >= 2.2
Requires: 	python-wxPython >= 2.4.2.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wxGlade is a GUI designer written in Python with the popular GUI
toolkit wxPython, that helps you create wxWidgets/wxPython/wxPerl
user interfaces. At the moment it can generate Python, C++, Perl
and XRC (wxWidgets' XML resources) code.

%description -l pl
wxGlade jest projektantem GUI napisanym w Pythonie i wxPythonie,
popularnym zbiorem narzêdzi GUI. Pomaga tworzyæ interfejsy
u¿ytkownika wxWidgets/wxPython/wxPerl. Obecnie mo¿e generowaæ
kod Pythona, C++, Perla oraz XRC (¼ród³a XML wxWidgets).

%package examples
Summary:	wxGlade example GUI designs
Summary(pl):	Przyk³adowe projekty GUI wxGlade
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description examples
wxGlade example GUI designs

%description examples -l pl
Przyk³adowe projekty GUI wxGlade

%prep
%setup -q

%build
%{__python} -c 'import compileall; compileall.compile_dir(".")'

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
install *.pyc		$RPM_BUILD_ROOT%{_datadir}/%{name}
install credits.txt	$RPM_BUILD_ROOT%{_datadir}/%{name}
install license.txt	$RPM_BUILD_ROOT%{_datadir}/%{name}

cp -pr examples		$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

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
%{_datadir}/%{name}/codegen/*.pyc
%{_datadir}/%{name}/edit_sizers/*.pyc
%{_datadir}/%{name}/icons/gtk/*.xpm
%{_datadir}/%{name}/icons/msw/*.xpm
%{_datadir}/%{name}/icons/*.xpm
%{_datadir}/%{name}/icons/wxglade_small.png
%{_datadir}/%{name}/icons/wxglade.ico
%{_datadir}/%{name}/widgets/bitmap_button/*.pyc
%{_datadir}/%{name}/widgets/button/*.pyc
%{_datadir}/%{name}/widgets/checkbox/*.pyc
%{_datadir}/%{name}/widgets/choice/*.pyc
%{_datadir}/%{name}/widgets/combo_box/*.pyc
%{_datadir}/%{name}/widgets/custom_widget/*.pyc
%{_datadir}/%{name}/widgets/dialog/*.pyc
%{_datadir}/%{name}/widgets/frame/*.pyc
%{_datadir}/%{name}/widgets/gauge/*.pyc
%{_datadir}/%{name}/widgets/grid/*.pyc
%{_datadir}/%{name}/widgets/list_box/*.pyc
%{_datadir}/%{name}/widgets/list_ctrl/*.pyc
%{_datadir}/%{name}/widgets/menubar/*.pyc
%{_datadir}/%{name}/widgets/notebook/*.pyc
%{_datadir}/%{name}/widgets/panel/*.pyc
%{_datadir}/%{name}/widgets/radio_box/*.pyc
%{_datadir}/%{name}/widgets/radio_button/*.pyc
%{_datadir}/%{name}/widgets/slider/*.pyc
%{_datadir}/%{name}/widgets/spacer/*.pyc
%{_datadir}/%{name}/widgets/spin_ctrl/*.pyc
%{_datadir}/%{name}/widgets/splitter_window/*.pyc
%{_datadir}/%{name}/widgets/static_bitmap/*.pyc
%{_datadir}/%{name}/widgets/static_line/*.pyc
%{_datadir}/%{name}/widgets/static_text/*.pyc
%{_datadir}/%{name}/widgets/text_ctrl/*.pyc
%{_datadir}/%{name}/widgets/toggle_button/*.pyc
%{_datadir}/%{name}/widgets/toolbar/*.pyc
%{_datadir}/%{name}/widgets/tree_ctrl/*.pyc
%{_datadir}/%{name}/widgets/*.pyc
%{_datadir}/%{name}/widgets/widgets.txt
%{_datadir}/%{name}/*.pyc
%{_datadir}/%{name}/credits.txt
%{_datadir}/%{name}/license.txt

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
