# Generated from webmock-1.6.2.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	webmock

Summary:	HTTP regression testing framework
Name:		rubygem-%{rbname}

Version:	1.6.2
Release:	2
Group:		Development/Ruby
License:	GPLv2
URL:		http://github.com/bblimke/webmock
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 

%description
WebMock allows stubbing HTTP requests and setting expectations on HTTP
requests.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(spec|vendor|test)/'

%install
%gem_install

%clean
rm -rf %{buildroot}

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/webmock
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/webmock/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/spec
%{ruby_gemdir}/gems/%{rbname}-%{version}/spec/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/spec/*.txt
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/spec/util
%{ruby_gemdir}/gems/%{rbname}-%{version}/spec/util/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/spec/vendor
%{ruby_gemdir}/gems/%{rbname}-%{version}/spec/vendor/addressable
%{ruby_gemdir}/gems/%{rbname}-%{version}/spec/vendor/crack
%{ruby_gemdir}/gems/%{rbname}-%{version}/spec/vendor/right_http_connection-1.2.4
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.md
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}


%changelog
* Mon Mar 14 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.6.2-1
+ Revision: 644660
- regenerate spec with gem2rpm5
- new release: 1.6.2

* Fri Sep 17 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.3.5-1mdv2011.0
+ Revision: 579220
- import rubygem-webmock


