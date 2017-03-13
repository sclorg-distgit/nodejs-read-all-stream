%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global module_name read-all-stream
#%global commit0 65f188a592577e590e2be30ff9d7b17d3c8e444c
#%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        3.1.0
Release:        1%{?dist}
Summary:        Read all stream content and pass it to callback

License:        MIT
URL:            https://github.com/floatdrop/read-all-stream
Source0:        https://github.com/floatdrop/%{module_name}/archive/v%{version}.tar.gz#/%{module_name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(mocha)
%endif

%description
%{summary}.

%prep
%setup -q -n %{module_name}-%{version}
rm -rf node_modules

%nodejs_fixdep pinkie-promise

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json *.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
mocha
%endif

%files
%{!?_licensedir:%global license %doc}
%doc readme.md 
%doc license
%{nodejs_sitelib}/%{module_name}

%changelog
* Tue Nov 01 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.1.0-1
- Update

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.1-7
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.1-6
- Rebuilt with updated metapackage

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 3.0.1-5
- Use macro to find provides and requires

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 3.0.1-4
- Enable scl macros, fix license macro for el6

* Thu Nov 26 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.0.1-3
- fixdep npm(pinkie-promise)

* Fri Aug 07 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.0.1-2
- Update to 3.0.1

* Sat Jul 18 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.0.0-2
- Add missing BR:npm(readable-stream)

* Wed Jul 15 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.0.0-1
- Update to 3.0.0

* Thu Jan 22 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0.1-1
- Update to 1.0.1

* Sun Dec 07 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.1.2-2
- Add test.js from upstream and enable tests

* Thu Dec 04 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.1.2-1
- Initial packaging
