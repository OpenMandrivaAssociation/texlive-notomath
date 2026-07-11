%global tl_name notomath
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.031
Release:	%{tl_revision}.1
Summary:	Math support for Noto fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/notomath
License:	ofl lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/notomath.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/notomath.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Math support via newtxmath for Google's NotoSerif and NotoSans. (Regular
and Bold weights only.)

