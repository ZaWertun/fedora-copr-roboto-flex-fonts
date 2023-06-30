%global priority 60
%global fontname roboto-flex

%define catalogue %{_sysconfdir}/X11/fontpath.d

Name:    roboto-flex-fonts
Version: 3.200
Release: 1%{?dist}
Summary: Roboto Flex font family

License: OFL
URL:     https://github.com/googlefonts/%{fontname}
Source0: https://github.com/googlefonts/%{fontname}/archive/refs/tags/%{version}/%{fontname}-%{version}.tar.gz
Source1: %{fontname}.metainfo.xml
Source2: %{fontname}-fonts.conf
BuildArch: noarch

BuildRequires: /usr/bin/install
BuildRequires: /usr/bin/mkfontdir, /usr/bin/mkfontscale
BuildRequires: /usr/bin/appstream-util
BuildRequires: fontpackages-devel

%description
Roboto Flex upgrades Roboto so it becomes a more powerful typeface system. With
Flex, you can customize Roboto to express and finesse your text in ways never
before possible. Today, people are constantly switching between devices,
resizing browsers, and spreading our viewports across multiple screens. So
Google commissioned Font Bureau to re-imagine Roboto to “flex” along with us,
with a special emphasis on large-screen capabilities. This was achieved by
amplifying the original design to an extreme range of weights, grades, widths
and optical sizes.

%prep
%setup -q -n %{fontname}-%{version}


%install
# Install *.ttf
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p fonts/RobotoFlex*.ttf %{buildroot}%{_fontdir}/RobotoFlex.ttf

install -m 0755 -d %{buildroot}%{catalogue}
ln -s %{_datadir}/fonts/%{fontname} %{buildroot}%{catalogue}/%{name}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{priority}-%{fontname}.conf

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

ln -s %{_fontconfig_templatedir}/%{priority}-%{fontname}.conf \
      %{buildroot}%{_fontconfig_confdir}/%{priority}-%{fontname}.conf

# fonts.{dir,scale}
mkfontscale %{buildroot}%{_fontdir}
mkfontdir %{buildroot}%{_fontdir}


%check
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml


%files
%doc README.md
%license OFL.txt
%dir %{_datadir}/fonts/%{fontname}
%{_datadir}/fonts/%{fontname}/RobotoFlex.ttf
%{_datadir}/appdata/%{fontname}.metainfo.xml
%{_datadir}/fontconfig/conf.avail/*-%{fontname}.conf
%config(noreplace) %{_sysconfdir}/fonts/conf.d/*-%{fontname}.conf
%verify(not md5 size mtime) %{_fontdir}/fonts.dir
%verify(not md5 size mtime) %{_fontdir}/fonts.scale
%{catalogue}/%{name}


%changelog
* Fri Jun 30 2023 Yaroslav Sidlovsky <zawertun@gmail.com> - 3.200-1
- version 3.200

* Tue May 10 2022 Yaroslav Sidlovsky <zawertun@gmail.com> - 3.100-1
- initial spec for version 3.100


