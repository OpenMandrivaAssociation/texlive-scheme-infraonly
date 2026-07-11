%global tl_name scheme-infraonly
%global tl_revision 54191

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	infrastructure-only scheme (no TeX at all)
Group:		Publishing
URL:		https://www.ctan.org/pkg/scheme-infraonly
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scheme-infraonly.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyphen-base)
Requires:	texlive(kpathsea)
Requires:	texlive(texlive-scripts)
Requires:	texlive(texlive.infra)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is the TeX Live scheme for infrastructure only, with no TeX engines
at all. It is useful for automated testing, where the actual programs
and packages to be tested are installed separately afterwards, with
tlmgr install.

