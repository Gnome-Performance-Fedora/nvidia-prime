Name:           nvidia-prime
Version:        1.0
Release:        1000.gnomeperformance
Summary:        NVIDIA Prime Render Offload configuration and utilities

License:        GPL
URL:            https://www.archlinux.org/packages/extra/any/%{name}
Source0:        https://raw.githubusercontent.com/archlinux/svntogit-packages/86fae38220819922f96c4fba95f5b6aaad2b3706/trunk/prime-run

Requires:       bash
Requires:	xorg-x11-drv-nvidia-cuda

BuildArch:      noarch

%description
NVIDIA Prime Render Offload configuration and utilities

%prep

%build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 prime-run %{buildroot}/%{_bindir}/prime-run

%files
%{_bindir}/prime-run
