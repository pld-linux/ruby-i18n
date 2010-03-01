%define pkgname i18n
Summary:	Add Internationalization support to your Ruby application
Name:		ruby-%{pkgname}
Version:	0.3.5
Release:	1
License:	MIT/Ruby License
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	4c082d1c55b5998796173c86db2a8ca3
Patch0:		%{name}-cldr-data.patch
URL:		http://rails-i18n.org/
Group:		Development/Languages
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
Add Internationalization support to your Ruby application.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README.textile -o -print | xargs touch --reference %{SOURCE0}
%patch0 -p1

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -r ri/{Hash,KeyError,String}
rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

cp -a vendor $RPM_BUILD_ROOT%{ruby_rubylibdir}/i18n

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.textile README.textile
%{ruby_rubylibdir}/%{pkgname}.rb
%{ruby_rubylibdir}/%{pkgname}

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/I18n
