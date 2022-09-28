Name:           fyra-srpm-macros
Version:        0.1.0
Release:        1%{?dist}
Summary:        Fyra Labs extra SRPM macros

License:        MIT
# URL:
Source0:        macros.cargo_extra

Requires:       rust-packaging

%description
%{summary}

%prep


%build

%install
install -D -p -m 0644 -t %{buildroot}%{_rpmmacrodir} %{SOURCE0}



%files
%{_rpmmacrodir}/macros.cargo_extra


%changelog
* Mon Sep 26 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Build
