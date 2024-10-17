Name:		texlive-notomath
Version:	71429
Release:	1
Summary:	Math support for Noto fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/notomath
License:	ofl lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/notomath.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/notomath.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Math support via newtxmath for Google's NotoSerif and NotoSans.
(Regular and Bold weights only.)

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/notomath
%{_texmfdistdir}/fonts/vf/public/notomath
%{_texmfdistdir}/fonts/type1/public/notomath
%{_texmfdistdir}/fonts/tfm/public/notomath
%{_texmfdistdir}/fonts/map/dvips/notomath
%doc %{_texmfdistdir}/doc/fonts/notomath

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
