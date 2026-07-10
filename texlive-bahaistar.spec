%global tl_name bahaistar
%global tl_revision 76351

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Metafont source and macros for the Bahai nine-pointed star
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/bahaistar
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bahaistar.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bahaistar.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a Metafont-based implementation of the Baha'i
nine-pointed star [?] for usage in LaTeX documents, while still
providing proper copy behavior with the official Unicode codepoints and
supporting the usage of the character directly.

