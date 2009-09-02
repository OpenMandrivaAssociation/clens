%define name    clens
%define version 0.2
%define release %mkrel 6

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Corrects lens barrel distortion
Source0:        %{name}-%{version}.tar.bz2
# grabbed from http://www.epaperpress.com/ptlens/download/PTLensProfiles.zip
Source1:	PTLensProfiles.tar.bz2
Patch0:		clens-mdk-profile.patch.bz2
License:        GPL
Group:          Graphics
Url:         	http://panotools.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  pano12-devel

%description
A command-line version of PTLens. Compares your JPEG images with a lens 
database and automatically corrects lens barrel distortion.

%prep
%setup -q
%patch0 -p0 

%build
mkdir profiles
cd profiles
tar xvfj %{SOURCE1}
mv PTLensProfiles.pdf ../
cd ..
echo "Lens Profiles are aviable at %{_datadir}/%{name}" >> README
perl -pi -e "s|\@\@PROFILE\@\@|%{_datadir}/%{name}/profile.txt|" src/main.c
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

rm -rf $RPM_BUILD_ROOT/usr/doc
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}
mv profiles $RPM_BUILD_ROOT%{_datadir}/%{name}
# why provide .h since there are no library ?!
rm -rf $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%doc PTLensProfiles.pdf README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
%{_datadir}/%{name}
