#
# Conditional build:
%bcond_without 	avfs		# build without A Virtual Filesystem (avfs) support
#
%define		doc_version	2.10.0
%define		doc_release	2
%define		doc_dir		%{name}-%{doc_version}.%{doc_release}-doc
Summary:	A file manager for X in AMIGA style
Summary(pl):	Zarz±dca plików dla X w amigowskim stylu
Name:		worker
Version:	2.14.1
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://www.boomerangsworld.de/worker/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	1e3931a4f7339860ecb0f3124e2e2627
Source1:	http://www.boomerangsworld.de/worker/downloads/%{name}-%{doc_version}.%{doc_release}-doc.tar.bz2
# Source1-md5:	d7df227f6dd43a26651dc07590699148
Source2:	%{name}-48.png
Source3:	%{name}-32.png
Source4:	%{name}-16.png
Source5:	%{name}.desktop
URL:		http://www.boomerangsworld.de/worker/
BuildRequires:	XFree86-devel
%{?with_avfs:BuildRequires:	avfs-static >= 0.9.5}
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
Woker jest graficznym zarz±dc± plików dla X Window System. U¿ywa
klasycznego widoku dwóch paneli z list± plików i katalogów. Wiele
operacji potrafi wykonaæ samodzielnie, ale mo¿e te¿ wykorzystaæ
zewnêtrzne programy do dzia³ania na zaznaczonych elementach. Nowe
opcje mo¿na ³atwo dodawaæ przy u¿yciu wbudowanego programu
konfiguracyjnego.

%prep
%setup -q -a 1

%build
%configure \
	%{!?with_avfs:--with-avfs=no}

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
%lang(fr) %{_mandir}/fr/man1/worker.1*
%lang(it) %{_mandir}/it/man1/worker.1*
%{_pixmapsdir}/*
