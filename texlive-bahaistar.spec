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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a Metafont-based implementation of the Baha'i
nine-pointed star [?] for usage in LaTeX documents, while still
providing proper copy behavior with the official Unicode codepoints and
supporting the usage of the character directly.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/source
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/bahaistar
%dir %{_datadir}/texmf-dist/fonts/source/public
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/tex/latex/bahaistar
%dir %{_datadir}/texmf-dist/fonts/source/public/bahaistar
%dir %{_datadir}/texmf-dist/fonts/tfm/public/bahaistar
%doc %{_datadir}/texmf-dist/doc/fonts/bahaistar/LICENSE
%doc %{_datadir}/texmf-dist/doc/fonts/bahaistar/MANIFEST
%doc %{_datadir}/texmf-dist/doc/fonts/bahaistar/README
%doc %{_datadir}/texmf-dist/doc/fonts/bahaistar/bahaistar-example.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/bahaistar/bahaistar-example.tex
%doc %{_datadir}/texmf-dist/fonts/source/public/bahaistar/bahaistar.mf
%{_datadir}/texmf-dist/fonts/tfm/public/bahaistar/bahaistar.tfm
%{_datadir}/texmf-dist/tex/latex/bahaistar/bahaistar.sty
