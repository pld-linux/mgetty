Summary:	A getty replacement for use with data and fax modems
Summary(de):	Intelligenter Ersatz für Daten- und Faxmodems
Summary(es):	Un substituto mejor que el getty para módems de datos y fax
Summary(fr):	Remplacement de getty pour les modems données et fax
Summary(pl):	Zamiennik getty dla modemów i faxmodemów
Summary(pt_BR):	Um substituto melhor do que o getty para modems de dados e fax
Summary(tr):	Veri ve faks modemleri için yeni ve akýllý bir getty
Name:		mgetty
Version:	1.1.30
Release:	2
License:	distributable
Group:		Applications/Communications
Source0:	ftp://alpha.greenie.net/pub/mgetty/source/1.1/%{name}%{version}-Dec16.tar.gz
# Source0-md5:	4b80c418bc58add3e40de3be0ac6c02a
Source1:	%{name}-sendfax.logrotate
Source2:	%{name}-vm.logrotate
Source3:	%{name}-ttyS.logrotate
Patch0:		%{name}-config.patch
Patch1:		%{name}-makekvg.patch
Patch2:		%{name}-policy.patch
Patch3:		%{name}-imakefile.patch
Patch4:		%{name}-install.patch
Patch5:		%{name}-manpages.patch
Patch6:		%{name}-info.patch
Patch7:		%{name}-makedoc.patch
Patch8:		%{name}-faxprint.patch
Patch9:		%{name}-called-id-patch-current
Patch10:	%{name}-voiceconfig.patch
Patch11:	%{name}-issue.patch
Patch12:	%{name}-force_detect.patch
URL:		http://alpha.greenie.net/mgetty/
BuildRequires:	XFree86-devel
BuildRequires:	groff
BuildRequires:	tetex
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		viewfax_version		2.5

%description
The mgetty package contains a "smart" getty which allows logins over a
serial line (i.e., through a modem). If you're using a Class 2 or 2.0
modem, mgetty can receive faxes. If you also need to send faxes,
you'll need to install the sendfax program.

If you'll be dialing in to your system using a modem, you should
install the mgetty package. If you'd like to send faxes using mgetty
and your modem, you'll need to install the mgetty-sendfax program. If
you need a viewer for faxes, you'll also need to install the
mgetty-viewfax package.

%description -l es
Este paquete contiene el programa inteligente 'getty' que permite logins a
través de una línea serial (usadas con un módem por ejemplo). El programa
permite el uso automático de callback y incluye soporte a FAX (el paquete
mgetty-sendfax necesita ser instalado para hacer uso total del soporte a FAX).

%description -l de
Dieses Paket enthält ein intelligentes getty, das das Anmelden über
eine serielle Leitung, z.B. ein Modem, zuläßt. Es unterstützt
automatischen Rückruf und Fax (für vollständige Fax-Unterstützung muß
jedoch mgetty-sendfax installiert werden.

%description -l fr
Ce paquetage contient un getty intelligent permettant les logins sur
une ligne série (via un modem, par exemple). Il autorise le rappel
automatique et contient une gestion fax (mgetty-sendfax doit être
installé pour utiliser pleinement cette gestion fax).

%description -l pl
Pakiet mgetty zawiera "m±dry" getty, który pozwala na po³±czenia przez
linie szeregowe (tj. przez modem). Je¶li twój modem obs³uguje standard
Class 2 lub 2.0, mgetty mo¿e odbieraæ faksy. Je¶li potrzebujesz
równie¿ wysy³aæ faksy, musisz zainstalowaæ program sendfax.

Je¶li bêdziesz siê ³±czy³ ze swoim systemem u¿ywaj±c modemu,
powiniene¶ zainstalowaæ pakiet mgetty. Je¶li chcesz wysy³aæ faksy
u¿ywaj±c mgetty, musisz zainstalowaæ pakiet mgetty-sendfax. Je¶li
potrzebujesz przegl±darki otrzymanych faksów, musisz równie¿
zainstalowaæ pakiet mgetty-viewfax.

%description -l pt_BR
Este pacote contém o programa inteligente 'getty' que permite logins através de
uma linha serial (usadas com um modem por exemplo). O programa permite o uso
automático de callback e inclui suporte a FAX (o pacote mgetty-sendfax precisa
ser instalado para fazer uso total de seu suporte a FAX).

%description -l tr
Bu pakette seri baðlantý üzerinden sisteme giriþe olanak veren, akýllý
bir getty sürümü bulunur. Otomatik arama ve faks desteði içerir
(saðladýðý fax desteðinin tam olarak kullanýlabilmesi için
mgetty-sendfax paketi gerekir).

%package sendfax
Summary:	Provides support for sending faxes over a modem
Summary(de):	Unterstützung zum Versand und Empfang von Faxnachrichten über ein Faxmodem
Summary(es):	Soporte a envío y recepción de faxes vía faxmódem
Summary(fr):	Gestion de l'envoi et de la réception de fax via un faxmodem
Summary(pl):	Umo¿liwia wysy³anie faksów przez modem
Summary(pt_BR):	Suporte ao envio e recepção de faxes via faxmodem
Summary(tr):	1 veya 2 sýnýfý modemler üzerinden fax gönderme desteði
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	netpbm-progs

%description sendfax
Sendfax is a standalone backend program for sending fax files. The
mgetty program (a getty replacement for handling logins over a serial
line) plus sendfax will allow you to send faxes through a Class 2
modem.

If you'd like to send faxes over a Class 2 modem, you'll need to
install the mgetty-sendfax and the mgetty packages.

%description sendfax -l de
Dieses Paket schließt Unterstützung für den Versand und Empfang durch
Modems der FAX Class 2 ein. Ebenfalls enthalten ist der Support für
eine einfache FAX-Warteschlange.

%description sendfax -l es
Este paquete incluye soporte al envío y recepción de faxes en fax-módems clase
2. También incluye soporte sencillo a encadenamiento de faxes.

%description sendfax -l fr
Ce paquetage contient la gestion des modems FAX Classe 2 pour émettre
et recevoir des faxs. Il contient aussi une gestion simple des
attentes de fax.

%description sendfax -l pl
Sendfax jest samodzielnym programem do wysy³ania faksów. Program
mgetty (zamiennik getty dla przyjmowania po³±czeñ przez linie
szeregowe) + sendfax pozwol± na wysy³anie faksów w standardzie
Class 2.

Je¶li chcemy wysy³aæ faksy przez modem obs³uguj±cy standard Class 2,
musimy zainstalowaæ pakiety: mgetty-sendfax i mgetty.

%description sendfax -l pt_BR
Este pacote inclui suporte para o envio e recepção de faxes em fax-modems
classe 2. Também inclui suporte simples a enfileiramento de faxes.

%description sendfax -l tr
Bu paket 'FAX Class 2' modemleri için faks gönderme ve alma desteði
içerir. Ayný zamanda basit bir faks kuyruðu desteði vardýr.

%package voice
Summary:	A program for using your modem and mgetty as an answering machine
Summary(de):	Support für Modems, die Voice-Mail unterstützen
Summary(es):	Soporte para módems con capacidad de mail por voz
Summary(fr):	Gestionnaire pour les modems vocaux
Summary(pl):	Program pozwalaj±cy na wykorzystanie mgetty i modemu jako automatycznej sekretarki
Summary(pt_BR):	Suporte para modems com capacidade de mail por voz
Summary(tr):	Sesli mektup gönderebilen modemlere destek
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description voice
The mgetty-voice package contains the vgetty system, which enables
mgetty and your modem to support voice capabilities. In simple terms,
vgetty lets your modem act as an answering machine. How well the
system will work depends upon your modem, which may or may not be able
to handle this kind of implementation.

Install mgetty-voice along with mgetty if you'd like to try having
your modem act as an answering machine.

%description voice -l de
Dieses Paket unterstützt bestimmte Modems mit Voice-Mail- Erweiterung.

%description voice -l es
Este paquete incluye soporte a algunos módems que tiene extensiones de voice
mail.

%description voice -l fr
Ce paquetage contient les gestionnaires de certains modems disposant
des extensions voice mail.

%description voice -l pl
Pakiet mgetty-voice zawiera system vgetty, który zezwala mgetty i
modemowi na obs³ugê g³osu. Mówi±c krótko, vgetty pozwala modemowi
pracowaæ jako automatyczna sekretarka. To, jak dobrze bêdzie ten
system dzia³a³, zale¿y od tego, czy modem obs³uguje tego rodzaju
funkcje.

Nale¿y zainstalowaæ mgetty-voice razem z mgetty, je¶li chcemy
przemieniæ swój modem w automatyczn± sekretarkê.

%description voice -l pt_BR
Este pacote inclui suporte a alguns modems que têm extensões de voice mail.

%description voice -l tr
Bu paket sesli mektup uzantýsý olan bazý modemler için destek içerir.

%package viewfax
Summary:	An X Window System fax viewer
Summary(es):	Visualizador de faxes para X11
Summary(pl):	Przegl±darka faksów dla X Window System
Summary(pt_BR):	Visualizador de faxes para X11
Epoch:		1
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description viewfax
Viewfax displays the fax files received using mgetty in an X11 window.
Viewfax is capable of zooming in and out on the displayed fax.

%description viewfax -l es
Este paquete ofrece un visor de faxes para X11 con capacidad de zoom.

%description viewfax -l pl
Viewfax jest narzêdziem dla X11, którym mo¿na przegl±daæ otrzymane
przy pomocy mgetty faksy.

%description viewfax -l pt_BR
Este pacote fornece um visualizador de faxes para X11 com capacidade
de zoom.

%prep
%setup -q
cp -f policy.h-dist policy.h

%patch0 -p0
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p0
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
%{__make} \
	LDFLAGS="%{rpmldflags}"
cd voice
%{__make} \
	LDFLAGS="%{rpmldflags}"

cd ../frontends/X11/viewfax-%{viewfax_version}
xmkmf
%{__make} depend
%{__make} \
	CDEBUGFLAGS="%{rpmcflags}" \
	EXTRA_LDOPTIONS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/var/spool/voice/{messages,incoming},/sbin,/etc/logrotate.d} \
	$RPM_BUILD_ROOT%{_libdir}/mgetty+sendfax

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	spool=$RPM_BUILD_ROOT/var/spool \
	MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	INFODIR=$RPM_BUILD_ROOT%{_infodir} \
	CONFDIR=$RPM_BUILD_ROOT%{_sysconfdir}/mgetty+sendfax

install callback/callback $RPM_BUILD_ROOT%{_sbindir}
install callback/ct $RPM_BUILD_ROOT%{_bindir}

mv -f $RPM_BUILD_ROOT%{_sbindir}/mgetty $RPM_BUILD_ROOT/sbin

# this conflicts with efax
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/fax.1 \
	$RPM_BUILD_ROOT%{_mandir}/man1/mgetty_fax.1

# voice mail extensions
%{__make} install -C voice \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	spool=$RPM_BUILD_ROOT/var/spool \
	MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	INFODIR=$RPM_BUILD_ROOT%{_infodir} \
	CONFDIR=$RPM_BUILD_ROOT%{_sysconfdir}/mgetty+sendfax

mv -f $RPM_BUILD_ROOT%{_sbindir}/vgetty $RPM_BUILD_ROOT/sbin
install voice/voice.conf-dist $RPM_BUILD_ROOT%{_sysconfdir}/mgetty+sendfax/voice.conf

%{__make} install -C frontends/X11/viewfax-%{viewfax_version} \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} install.man -C frontends/X11/viewfax-%{viewfax_version} \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/logrotate.d/sendfax
install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/vm
install %{SOURCE3} $RPM_BUILD_ROOT/etc/logrotate.d/ttyS

mv $RPM_BUILD_ROOT%{_sysconfdir}/mgetty+sendfax/faxspool.rules.sample \
	$RPM_BUILD_ROOT%{_sysconfdir}/mgetty+sendfax/faxspool.rules

# make the html documenatation
texi2html -monolithic doc/mgetty.texi

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc BUGS ChangeLog README.1st THANKS doc/modems.db
%doc samples doc/*.txt mgetty.html faq/SGML/FAQ.sgml
%attr(700,root,root) /sbin/mgetty
%{_mandir}/man8/mgetty.8*
%{_mandir}/man4/mgettydefs.4*
%{_infodir}/mgetty.info*
%dir %{_sysconfdir}/mgetty+sendfax
%attr(600,root,root) %config %{_sysconfdir}/mgetty+sendfax/login.config
%attr(600,root,root) %config %{_sysconfdir}/mgetty+sendfax/mgetty.config
%attr(600,root,root) %config %{_sysconfdir}/mgetty+sendfax/dialin.config
/etc/logrotate.d/ttyS

%files sendfax
%defattr(644,root,root,755)
%dir /var/spool/fax
%dir /var/spool/fax/incoming
%attr(1777,root,root) %dir /var/spool/fax/outgoing
#%attr(777,root,root) %dir /var/spool/fax/outgoing/locks
%attr(600,root,root) %config %{_sysconfdir}/mgetty+sendfax/faxspool.rules

%attr(755,root,root) %{_bindir}/kvg
%attr(755,root,root) %{_bindir}/newslock
%attr(755,root,root) %{_bindir}/g3cat
%attr(755,root,root) %{_bindir}/g32pbm
%attr(755,root,root) %{_bindir}/pbm2g3
%attr(755,root,root) %{_bindir}/faxspool
%attr(700,root,root) %{_bindir}/faxrunq
%attr(755,root,root) %{_bindir}/faxq
%attr(755,root,root) %{_bindir}/faxrm
%attr(755,root,root) %{_bindir}/ct
%attr(755,root,root) %{_sbindir}/sendfax
%attr(755,root,root) %{_sbindir}/faxrunqd
%attr(755,root,root) %{_sbindir}/callback
%dir %{_libdir}/mgetty+sendfax
%{_prefix}/lib/mgetty+sendfax/cour25.pbm
%{_prefix}/lib/mgetty+sendfax/cour25n.pbm
%{_prefix}/lib/mgetty+sendfax/faxq-helper
%{_mandir}/man1/g32pbm.1*
%{_mandir}/man1/pbm2g3.1*
%{_mandir}/man1/g3cat.1*
%{_mandir}/man1/mgetty_fax.1*
%{_mandir}/man1/faxspool.1*
%{_mandir}/man1/faxrunq.1*
%{_mandir}/man1/faxq.1*
%{_mandir}/man1/faxrm.1*
%{_mandir}/man1/coverpg.1*
%{_mandir}/man5/faxqueue.5*
%{_mandir}/man8/sendfax.8*
%{_mandir}/man8/callback.8*
%{_mandir}/man8/faxrunqd.8*
%config %{_sysconfdir}/mgetty+sendfax/sendfax.config
%attr(600,root,root) %config %{_sysconfdir}/mgetty+sendfax/faxrunq.config
%config %{_sysconfdir}/mgetty+sendfax/faxheader
/etc/logrotate.d/sendfax

%files voice
%defattr(644,root,root,755)
%doc voice/doc/* voice/scripts
%dir /var/spool/voice
%dir /var/spool/voice/incoming
%dir /var/spool/voice/messages

%attr(700,root,root) /sbin/vgetty
%attr(755,root,root) %{_bindir}/vm
%attr(755,root,root) %{_bindir}/pvfamp
%attr(755,root,root) %{_bindir}/pvfcut
%attr(755,root,root) %{_bindir}/pvfecho
%attr(755,root,root) %{_bindir}/pvffile
%attr(755,root,root) %{_bindir}/pvffft
%attr(755,root,root) %{_bindir}/pvfmix
%attr(755,root,root) %{_bindir}/pvfreverse
%attr(755,root,root) %{_bindir}/pvfsine
%attr(755,root,root) %{_bindir}/pvfspeed
%attr(755,root,root) %{_bindir}/pvftormd
%attr(755,root,root) %{_bindir}/rmdtopvf
%attr(755,root,root) %{_bindir}/rmdfile
%attr(755,root,root) %{_bindir}/pvftovoc
%attr(755,root,root) %{_bindir}/voctopvf
%attr(755,root,root) %{_bindir}/pvftolin
%attr(755,root,root) %{_bindir}/lintopvf
%attr(755,root,root) %{_bindir}/pvftobasic
%attr(755,root,root) %{_bindir}/basictopvf
%attr(755,root,root) %{_bindir}/pvftoau
%attr(755,root,root) %{_bindir}/autopvf
%attr(755,root,root) %{_bindir}/pvftowav
%attr(755,root,root) %{_bindir}/wavtopvf
%attr(755,root,root) %{_bindir}/cutbl
%attr(755,root,root) %{_bindir}/pvffilter
%attr(755,root,root) %{_bindir}/pvfnoise

%{_mandir}/man1/zplay.1*
%{_mandir}/man1/pvf.1*
%{_mandir}/man1/pvfamp.1*
%{_mandir}/man1/pvfcut.1*
%{_mandir}/man1/pvfecho.1*
%{_mandir}/man1/pvffile.1*
%{_mandir}/man1/pvffft.1*
%{_mandir}/man1/pvfmix.1*
%{_mandir}/man1/pvfreverse.1*
%{_mandir}/man1/pvfsine.1*
%{_mandir}/man1/pvfspeed.1*
%{_mandir}/man1/pvftormd.1*
%{_mandir}/man1/rmdtopvf.1*
%{_mandir}/man1/rmdfile.1*
%{_mandir}/man1/pvftovoc.1*
%{_mandir}/man1/voctopvf.1*
%{_mandir}/man1/pvftolin.1*
%{_mandir}/man1/lintopvf.1*
%{_mandir}/man1/pvftobasic.1*
%{_mandir}/man1/basictopvf.1*
%{_mandir}/man1/pvftoau.1*
%{_mandir}/man1/autopvf.1*
%{_mandir}/man1/pvftowav.1*
%{_mandir}/man1/wavtopvf.1*
%{_mandir}/man1/pvffilter.1*
%{_mandir}/man1/pvfnoise.1*
%{_mandir}/man8/vgetty.8*
%attr(600,root,root) %config %{_sysconfdir}/mgetty+sendfax/voice.conf
/etc/logrotate.d/vm

%files viewfax
%defattr(644,root,root,755)
%doc frontends/X11/viewfax-%{viewfax_version}/C* frontends/X11/viewfax-%{viewfax_version}/README
%attr(755,root,root) %{_bindir}/viewfax
%dir %{_libdir}/mgetty+sendfax
%{_libdir}/mgetty+sendfax/viewfax.tif
%{_mandir}/man1/viewfax.1x*
