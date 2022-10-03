Name:           fedora-extras-srpm-macros
Version:        0.1.1
Release:        1%{?dist}
Summary:        Fyra Labs extra SRPM macros

License:        MIT
# URL:
Source0:        macros.cargo_extra
Source1:        macros.caching

Requires:       rust-packaging
Obsoletes:      fyra-srpm-macros < 0.1.1-1
Provides:       fyra-srpm-macros

%description
%{summary}

%prep


%build

%install
install -D -p -m 0644 -t %{buildroot}%{_rpmmacrodir} %{SOURCE0}
install -D -p -m 0644 -t %{buildroot}%{_rpmmacrodir} %{SOURCE1}



%files
%{_rpmmacrodir}/macros.cargo_extra
%{_rpmmacrodir}/macros.caching


%changelog
* Mon Sep 26 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Build
