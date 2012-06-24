%define		doc_version	2.9.0
%define		doc_release	1
%define		doc_dir		%{name}-%{doc_version}_%{doc_release}-doc
Summary:	A file manager for X in AMIGA style
Summary(pl):	Zarz�dca plik�w dla X w amigowskim stylu
Name:		worker
Version:	2.9.0
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://www.boomerangsworld.de/worker/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	cc34a21b0445eb42fe6fb7df3e78b59b
Source1:	http://www.boomerangsworld.de/worker/downloads/%{name}-%{doc_version}_%{doc_release}-doc.tar.bz2
# Source1-md5:	5b6c8b8d85dc06563ea856c22361dd57
Source2:	%{name}-48.png
Source3:	%{name}-32.png
Source4:	%{name}-16.png
Source5:	%{name}.desktop
URL:		http://www.boomerangsworld.de/worker/
BuildRequires:	XFree86-devel
BuildRequires:	bzip2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Worker is a graphical filemanager for the X Window System. It uses the
classical two-panel-view of the files and directories. It has many
intern operations while any extern program can also be used for
operate on the selected items. You can easily add actions to filetypes
or buttons with the builtin configuration program.

%description -l pl
Woker jest graficznym zarz�dc� plik�w dla X Window System. U�ywa
klasycznego widoku dw�ch paneli z list� plik�w i katalog�w. Wiele
operacji potrafi wykona� samodzielnie, ale mo�e te� wykorzysta�
zewn�trzne programy do dzia�ania na zaznaczonych elementach. Nowe opcje
mo�na �atwo dodawa� przy u�yciu wbudowanego programu konfiguracyjnego.

%prep
%setup -q -a 1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE5} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS ChangeLog %{doc_dir}/English %{doc_dir}/Deutsch %{doc_dir}/pics %{doc_dir}/index.html
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/worker
%attr(755,root,root) %{_datadir}/worker/scripts
%{_desktopdir}/*.desktop
%{_datadir}/worker/catalogs
%{_datadir}/worker/config-*
%{_mandir}/man1/worker.1*
%{_pixmapsdir}/*
