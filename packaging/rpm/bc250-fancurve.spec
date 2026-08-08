Name:           bc250-fancurve
Version:        0.1.0
Release:        1%{?dist}
Summary:        Temperature-based fan curve controller for AMD BC-250
License:        Unknown

# The source archive is produced by packaging/rpm/build.sh.
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
Requires:       python3
Requires:       systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
Temperature-based fan curve controller for AMD BC-250 systems. It uses the
nct6686 fan controller and k10temp CPU temperature sensor.

%prep
%autosetup -n %{name}-%{version}

%build
# The utilities are Python scripts and require no compilation.

%install
install -Dpm 0755 cooling/bc250-fancurve \
    %{buildroot}%{_bindir}/bc250-fancurve
install -Dpm 0644 cooling/bc250-fancurve.conf \
    %{buildroot}%{_sysconfdir}/bc250-fancurve.conf
install -Dpm 0644 cooling/bc250-fancurve.service \
    %{buildroot}%{_unitdir}/bc250-fancurve.service
install -Dpm 0644 cooling/README.md \
    %{buildroot}%{_docdir}/%{name}/cooling-README.md

%post
%systemd_post bc250-fancurve.service

%preun
%systemd_preun bc250-fancurve.service

%postun
%systemd_postun_with_restart bc250-fancurve.service

%files
%doc README.md PROJECT.md
%{_docdir}/%{name}/cooling-README.md
%{_bindir}/bc250-fancurve
%config(noreplace) %{_sysconfdir}/bc250-fancurve.conf
%{_unitdir}/bc250-fancurve.service

%changelog
* Sat Aug 08 2026 BC250 Maintainers <noreply@example.invalid> - 0.1.0-1
- Package the BC250 fan curve controller.
