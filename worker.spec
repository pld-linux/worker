%define		doc_version	2.0.0
%define		doc_release	3
Summary:	A file manager for X in AMIGA style
Summary(pl):	Manager plików dla X w amigowskim stylu
Name:		worker
Version:	2.8.1
Release:	1
Source0:	http://www.boomerangsworld.de/worker/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	1820cfa10e6de565b94dbf002b92b5a5
Source1:	http://www.boomerangsworld.de/worker/downloads/%{name}-%{doc_version}_%{doc_release}-doc.tar.bz2
# Source1-md5:	782093a33feafb70fef35da1d6457a3f
Source2:	%{name}-48.png
Source3:	%{name}-32.png
Source4:	%{name}-16.png
License:	GPL
Group:		Applications/File
URL:		http://www.boomerangsworld.de/worker/
BuildRequires:	XFree86-devel
BuildRequires:	bzip2-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Worker is a graphical filemanager for the X Window System. It uses the
classical two-panel-view of the files and directories. It has many
intern operations while any extern program can also be used for
operate on the selected items. You can easily add actions to filetypes
or buttons with the builtin configuration program.

%description -l pl
Woker jest graficznym managerem plików dla X Window System. U¿ywa
klasycznego widoku dwóch paneli z list± plików i katalogów. Wiele
operacji potrafi wykonaæ samodzielnie ale mo¿e te¿ wykorzystaæ
zewnêtrzne programy do dzia³ania na zaznaczonch elementach. Nowe opcje
mo¿na ³atwo dodawaæ przy u¿yciu wbudowanego programu konfiguracyjnego.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -a 1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_datadir}/worker/scripts/*
%doc README NEWS AUTHORS ChangeLog
%doc worker-2.0.0/docs/*
%{_datadir}/worker/catalogs/
%{_datadir}/worker/config-*
%{_mandir}/man1/worker.1*
%{_pixmapsdir}/*
