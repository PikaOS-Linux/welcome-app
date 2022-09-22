BuildArch:              noarch

Name:          nobara-welcome
Version:       0.3
Release:       1%{?dist}
License:       GPLv2
Group:         System Environment/Libraries
Summary:       Nobara's Welcome App


URL:           https://github.com/CosmicFusion/cosmo-welcome-glade

Source0:        %{name}-%{version}-%{release}.tar.gz

BuildRequires:	wget
Requires:      /usr/bin/bash
Requires:	python3
Requires:	python
Requires:	gtk3
Requires:	nobara-login
Requires:	nobara-login-config
Requires:	nobara-controller-config
Requires:	nobara-amdgpu-config
Requires:	webapp-manager

%install
tar -xf %{SOURCE0}
mv usr %{buildroot}/
mv etc %{buildroot}/
mkdir -p %{buildroot}/usr/share/licenses/nobara-welcome
wget https://raw.githubusercontent.com/CosmicFusion/cosmo-welcome-glade/main/LICENSE.md -O %{buildroot}/usr/share/licenses/nobara-welcome/LICENSE

%description
Nobara's Python3 & GTK3 built Welcome App
%files
%attr(0755, root, root) "/usr/bin/nobara-welcome"
%attr(0755, root, root) "/etc/nobara/scripts/nobara-welcome/apps.sh"
%attr(0755, root, root) "/etc/nobara/scripts/nobara-welcome/nobara-welcome.py"
%attr(0755, root, root) "/etc/nobara/scripts/nobara-welcome/nvidia.sh"
%attr(0755, root, root) "/etc/nobara/scripts/nobara-welcome/rocm.sh"
%attr(0644, root, root) "/etc/nobara/scripts/nobara-welcome/nobara-welcome.ui"
%attr(0644, root, root) "/usr/share/licenses/nobara-welcome/LICENSE"
%attr(0644, root, root) "/usr/share/applications/nobara-welcome.desktop" 
%attr(0644, root, root) "/usr/share/icons/hicolor/16x16/apps/amd.svg"
%attr(0644, root, root) "/usr/share/icons/hicolor/16x16/apps/nvidia.svg"
