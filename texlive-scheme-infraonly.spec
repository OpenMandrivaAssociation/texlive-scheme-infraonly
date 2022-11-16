Name:		texlive-scheme-infraonly
Version:	54191
Release:	1
Summary:	infrastructure-only scheme (no TeX at all)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/scheme-infraonly
License:	
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scheme-infraonly.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is the TeX Live scheme for infrastructure only, with no
TeX engines at all. It is useful for automated testing, where
the actual programs and packages to be tested are installed
separately afterwards, with tlmgr install.

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
