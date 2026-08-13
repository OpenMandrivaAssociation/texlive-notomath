%global tl_name notomath
%global tl_revision 77682
%global tl_version 1.031

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Math support for Noto fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/notomath
License:	ofl lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/notomath.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/notomath.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Math support via newtxmath for Google's NotoSerif and NotoSans. (Regular
and Bold weights only.)


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from notomath:
Map NotoMath.map
TL_DROPIN_EOF
