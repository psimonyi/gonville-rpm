%global ly_version 2.25.1
%global lygdata %{_datadir}/%{name}/%{ly_version}

Name:           lilypond-gonville
Version:        %{ly_version}
Release:        1%{?dist}
Summary:        An alternative lilypond command that uses the Gonville fonts

# This package is a one-line script; there is no copyrightable content.
License:        Public Domain
URL:            http://www.chiark.greenend.org.uk/~sgtatham/gonville/
Source0:        lilypond-gonville.in

BuildArch:      noarch
Requires:       gonville-fonts
Requires:       lilypond = %{ly_version}

%description
Gonville is a font of symbols for typesetting music: clefs, note heads, quaver
tails, and so on. It is compatible with GNU Lilypond. (Some features cannot be
set in Gonville, including ancient music notation and shape-note heads.)

This package provides a wrapper script lilypond-gonville to run Lilypond with
the Gonville fonts.

%build
sed -re 's!__path__!%{_datadir}/%{name}/%{ly_version}!' %{SOURCE0} > %{name}
cp -p --attributes-only %{SOURCE0} %{name}

%install
# Install the user command.
mkdir -p %{buildroot}%{_bindir}
cp -p lilypond-gonville %{buildroot}%{_bindir}

# Alias all the non-font data.
mkdir -p %{buildroot}%{lygdata}
for d in ly ps python scm tex; do
    ln -s ../../lilypond/%{ly_version}/$d %{buildroot}%{lygdata}/$d
done

# Alias the two fontconfig files to the original Lilypond version.
mkdir -p %{buildroot}%{lygdata}/fonts
for f in {00,99}-lilypond-fonts.conf; do
    ln -s ../../../lilypond/%{ly_version}/fonts/"$f" %{buildroot}%{lygdata}/fonts/"$f"
done

# Point the font files to the Gonville versions.
for type in otf svg type1; do
    ln -s %{_datadir}/fonts/gonville/$type %{buildroot}%{lygdata}/fonts/$type
done

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/

%changelog
* Wed Nov 01 2017 Peter Simonyi <pts@petersimonyi.ca> - 2.19.80
- Update %prep for f26 macro changes
- Bump Lilypond version number
* Mon May 30 2016 Peter Simonyi <pts@petersimonyi.ca> - 2.19.42
- Bump Lilypond version number
* Fri Mar 11 2016 Peter Simonyi <pts@petersimonyi.ca> - 2.19.37
- Bump Lilypond version number
* Wed Mar 2 2016 Peter Simonyi <pts@petersimonyi.ca> - 2.19.36
- Bump Lilypond version number
* Mon Jan 25 2016 Peter Simonyi <pts@petersimonyi.ca> - 2.19.35
- First package attempt
