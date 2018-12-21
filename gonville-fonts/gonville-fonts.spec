%global fontname gonville
%global gonville_version 20141025.177659a

Name:           gonville-fonts
Version:        20141025
Release:        2%{?dist}
Summary:        Gonville, a font of symbols for typesetting music

License:        Public Domain
# Note that the source is MIT; only its output is PD.
URL:            https://www.chiark.greenend.org.uk/~sgtatham/gonville/
Source0:        https://www.chiark.greenend.org.uk/~sgtatham/gonville/%{fontname}-%{gonville_version}-src.tar.gz

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  python, fontforge, ghostscript-core
Requires:       fontpackages-filesystem

# The fonts include files labelled "Emmentaler" as well as the "Gonville" ones
# you'd expect, though the glyphs are the same.  It seems that LilyPond loads
# the "Emmentaler" ones, but since they aren't really the Emmentaler font this
# package shouldn't Provide: them.  ("Feta" is similarly fake, and included in
# the Gonville SVG files' metadata too.)
%global __provides_exclude_from ^%{_fontdir}/(.*/emmentaler-.*|svg/.*)$

%description
Gonville is a font of symbols for typesetting music: clefs, note heads, quaver
tails, and so on.  It is compatible with GNU LilyPond.  It was drawn by Simon
Tatham to replace LilyPond's then-standard font Feta.  Gonville has a plainer,
slightly more modern look.

Gonville cannot completely replace the standard LilyPond fonts.  It does not
attempt to reproduce shape note heads, ancient music notation, or the longa
note (which is also unused in modern music).

%prep
%setup -q -n %{fontname}-%{gonville_version}

%build
# Unfortunately, the upstream buildscript is written in a custom language 'bob'
# which is not packaged for Fedora.  But conveniently, the build phase is just
# a Python program anyway.
./glyphs.py --ver=%{gonville_version} -lily

%install
mkdir -p %{buildroot}%{_fontdir}
cp -pr lilyfonts/{otf,svg} %{buildroot}%{_fontdir}
# Type 1 fonts are built as well, but we don't need them.

%_font_pkg otf/*.otf
%dir %{_fontdir}/otf/
%{_fontdir}/svg/
%doc README
%license LICENCE

%changelog
* Fri Dec 21 2018 Peter Simonyi <pts@petersimonyi.ca> - 20141025.177659a-2
- Update URLs to HTTPS, now that upstream supports it
* Tue Jan 26 2016 Peter Simonyi <pts@petersimonyi.ca> - 20141025.177659a
- Initial packaging
