Summary: 	A getty replacement for use with data and fax modems.
Summary(de):	Intelligenter Ersatz für Daten- und Faxmodems 
Summary(fr):	Remplacement de getty pour les modems données et fax
Summary(pl):	Zamiennik getty dla modemów i faxmodemów.
Summary(tr):	Veri ve faks modemleri için yeni ve akýllý bir getty
Name: 		mgetty
Version:	1.1.21
Release:	4
Copyright:      distributable
Group: 		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Source:		ftp://ftp.leo.org/pub/comp/os/unix/networking/mgetty/mgetty1.1.21-Jul24.tar.gz
Patch0: 	mgetty-config.patch
Patch1: 	mgetty-makekvg.patch
Patch2: 	mgetty-policy.patch
Patch3: 	mgetty-logrotate.patch
Patch4: 	mgetty-imakefile.patch
Patch5: 	mgetty-install.patch
Patch6:		mgetty-manpages.patch
Patch7:		mgetty-info.patch
Patch8:		mgetty-makedoc.patch
Patch9:		mgetty-faxprint.patch
BuildRequires:	XFree86-devel
BuildRequires:	tetex
BuildRequires:	texinfo
BuildRequires:	groff
Prereq:		/usr/sbin/fix-info-dir
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The mgetty package contains a "smart" getty which allows logins over a
serial line (i.e., through a modem).  If you're using a Class 2 or 2.0
modem, mgetty can receive faxes.  If you also need to send faxes, you'll
need to install the sendfax program.

If you'll be dialing in to your system using a modem, you should install
the mgetty package.  If you'd like to send faxes using mgetty and your
modem, you'll need to install the mgetty-sendfax program.  If you need a
viewer for faxes, you'll also need to install the mgetty-viewfax package.

%description -l de
Dieses Paket enthält ein intelligentes getty, das das Anmelden über eine
serielle Leitung, z.B. ein Modem, zuläßt. Es unterstützt automatischen
Rückruf und Fax (für vollständige Fax-Unterstützung muß jedoch
mgetty-sendfax installiert werden.

%description -l fr
Ce paquetage contient un getty intelligent permettant les logins sur une
ligne série (via un modem, par exemple). Il autorise le rappel automatique
et contient une gestion fax (mgetty-sendfax doit être installé pour utiliser
pleinement cette gestion fax).

%description -l pl
Pakiet mgetty zawiera "m±dry" getty, który pozwala na po³±czenia przez
linie szeregowe (tj. przez modem). Je¶li twój modem obs³uguje standard
Class 2 lub 2.0, mgetty mo¿e odbieraæ faksy. Je¶li potrzebujesz równie¿ 
wysy³aæ faksy, musisz zainstalowaæ program sendfax.

Je¶li bêdziesz siê ³±czy³ ze swoim systemem u¿ywaj±c modemu, powiniene¶
zainstalowaæ pakiet mgetty. Je¶li chcesz wysy³aæ faksy u¿ywaj±c mgetty,
musisz zainstalowaæ pakiet mgetty-sendfax. Je¶li potrzebujesz przegl±darki 
otrzymanych faksów, musisz równie¿ zainstalowaæ pakiet mgetty-viewfax.

%description -l tr
Bu pakette seri baðlantý üzerinden sisteme giriþe olanak veren, akýllý bir
getty sürümü bulunur. Otomatik arama ve faks desteði içerir (saðladýðý fax
desteðinin tam olarak kullanýlabilmesi için mgetty-sendfax paketi gerekir).

%package sendfax
Summary: 	Provides support for sending faxes over a modem.
Summary(de):	Unterstützung zum Versand und Empfang von Faxnachrichten über ein Faxmodem 
Summary(fr):	Gestion de l'envoi et de la réception de fax via un faxmodem
Summary(pl):	Umo¿liwia wysy³anie faksów przez modem
Summary(tr):	1 veya 2 sýnýfý modemler üzerinden fax gönderme desteði
Group:          Applications/Communications
Group(pl):      Aplikacje/Komunikacja
Requires:       libgr-progs
Requires:       %{name} = %{version}

%description sendfax
Sendfax is a standalone backend program for sending fax files.  The
mgetty program (a getty replacement for handling logins over a serial
line) plus sendfax will allow you to send faxes through a Class 2 modem.

If you'd like to send faxes over a Class 2 modem, you'll need to install
the mgetty-sendfax and the mgetty packages.

%description -l de sendfax
Dieses Paket schließt Unterstützung für den Versand und Empfang durch 
Modems der FAX Class 2 ein. Ebenfalls enthalten ist der Support für 
eine einfache FAX-Warteschlange. 

%description -l fr sendfax
Ce paquetage contient la gestion des modems FAX Classe 2 pour émettre et
recevoir des faxs. Il contient aussi une gestion simple des attentes de fax.

%description -l pl sendfax
Sendfax jest samodzielnym programem do wysy³ania faksów. Program mgetty 
(zamiennik getty dla przyjmowania po³±czeñ przez linie szeregowe) + sendfax
pozwol± ci na wysy³anie faksów w standardzie Class 2.

Je¶li chcia³by¶ wysy³aæ faksy przez modem obs³uguj±cy standard Class 2, 
musisz zainstalowaæ pakiety: mgetty-sendfax i mgetty.

%description -l tr sendfax
Bu paket 'FAX Class 2' modemleri için faks gönderme ve alma desteði içerir.
Ayný zamanda basit bir faks kuyruðu desteði vardýr.

%package voice
Summary: 	A program for using your modem and mgetty as an answering machine.
Summary(de):	Support für Modems, die Voice-Mail unterstützen 
Summary(fr):	Gestionnaire pour les modems vocaux
Summary(pl):	Program pozwalaj±cy na wykorzystanie mgetty i modemu jako automatycznej sekretarki.
Summary(tr):	Sesli mektup gönderebilen modemlere destek
Group: 		Applications/Communications
Group(pl):      Aplikacje/Komunikacja
Requires:       %{name} = %{version}

%description voice
The mgetty-voice package contains the vgetty system, which enables
mgetty and your modem to support voice capabilities.  In simple terms,
vgetty lets your modem act as an answering machine.  How well the system
will work depends upon your modem, which may or may not be able to handle
this kind of implementation.

Install mgetty-voice along with mgetty if you'd like to try having your
modem act as an answering machine.

%description -l de voice
Dieses Paket unterstützt bestimmte Modems mit Voice-Mail- Erweiterung.

%description -l fr voice
Ce paquetage contient les gestionnaires de certains modems disposant des
extensions voice mail.

%description -l pl voice
Pakiet mgetty-voice zawiera system vgetty, który zezwala mgetty i twojemu
modemowi na obs³ugê g³osu. Mówi±c krótko, vgetty pozwala twojemu modemowi 
pracowaæ jako automatyczna sekretarka. To, jak dobrze bêdzie ten system 
dzia³a³, zale¿y od tego, czy twój modem obs³uguje tego rodzaju funkcje.

Zainstaluj mgetty-voice razem z mgetty, je¶li chcia³by¶ przemieniæ swój
modem w automatyczn± sekretarkê.

%description -l tr voice
Bu paket sesli mektup uzantýsý olan bazý modemler için destek içerir.

%package viewfax
Summary: 	An X Window System fax viewer.
Summary(pl):	Przegl±darka faksów dla X Window System.
Group: 		Applications/Communications
Group(pl):      Aplikacje/Komunikacja
Requires:       %{name} = %{version}

%description viewfax
Viewfax displays the fax files received using mgetty in an X11 window.
Viewfax is capable of zooming in and out on the displayed fax.

If you're installing the mgetty-viewfax package, you'll also need to
install mgetty.

%description -l pl viewfax
Viewfax jest narzêdziem dla X11, którym mo¿esz przegl±daæ otrzymane 
przy pomocy mgetty faksy. 

Je¶li instalujesz pakiet mgetty-viewfax musisz równie¿ zainstalowaæ mgetty.

%prep
%setup -q
cp policy.h-dist policy.h

%patch0 -p0
%patch1 -p0 
%patch2 -p1
%patch3 -p1 
%patch4 -p1 
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p0
%patch9 -p1

%build
make LDFLAGS="-s"
cd voice
make LDFLAGS="-s"

cd ../frontends/X11/viewfax-2.4
xmkmf
make depend
make CDEBUGFLAGS="$RPM_OPT_FLAGS" EXTRA_LDOPTIONS="-s"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{var/spool,sbin}

make install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	spool=$RPM_BUILD_ROOT/var/spool \
	MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	INFODIR=$RPM_BUILD_ROOT%{_infodir} \
	CONFDIR=$RPM_BUILD_ROOT/etc/mgetty+sendfax

install callback/callback $RPM_BUILD_ROOT%{_sbindir}
install callback/ct $RPM_BUILD_ROOT%{_bindir}

mv -f $RPM_BUILD_ROOT%{_sbindir}/mgetty $RPM_BUILD_ROOT/sbin

# this conflicts with efax
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/fax.1 \
	$RPM_BUILD_ROOT%{_mandir}/man1/mgetty_fax.1

# voice mail extensions
install -d $RPM_BUILD_ROOT/var/spool/voice/{messages,incoming}

make install -C voice \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	spool=$RPM_BUILD_ROOT/var/spool \
        MANDIR=$RPM_BUILD_ROOT%{_mandir} \
        INFODIR=$RPM_BUILD_ROOT%{_infodir} \
	CONFDIR=$RPM_BUILD_ROOT/etc/mgetty+sendfax

mv -f $RPM_BUILD_ROOT%{_sbindir}/vgetty $RPM_BUILD_ROOT/sbin
install voice/voice.conf-dist $RPM_BUILD_ROOT/etc/mgetty+sendfax/voice.conf

make install -C frontends/X11/viewfax-2.4 \
	DESTDIR=$RPM_BUILD_ROOT
make install.man -C frontends/X11/viewfax-2.4 \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/logrotate.d
install logrotate.mgetty $RPM_BUILD_ROOT/etc/logrotate.d/mgetty
install logrotate.sendfax $RPM_BUILD_ROOT/etc/logrotate.d/sendfax

# make the html documenatation
texi2html -monolithic doc/mgetty.texi

gzip -9nf $RPM_BUILD_ROOT{%{_mandir}/man?/*,%{_infodir}/*} \
	FAQ BUGS ChangeLog README.1st THANKS doc/*.txt \
	frontends/X11/viewfax-2.4/C* frontends/X11/viewfax-2.4/README \
	voice/doc/* doc/modems.db
find samples -type f -exec gzip -9nf {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc {FAQ,BUGS,ChangeLog,README.1st,THANKS}.gz doc/modems.db.gz
%doc samples doc/*.txt.gz mgetty.html
%attr(700,root,root) /sbin/mgetty
%{_mandir}/man8/mgetty.8*
%{_mandir}/man4/mgettydefs.4*
%{_infodir}/mgetty.info*
%dir /etc/mgetty+sendfax
%attr(600,root,root) %config /etc/mgetty+sendfax/login.config
%attr(600,root,root) %config /etc/mgetty+sendfax/mgetty.config
%attr(600,root,root) %config /etc/mgetty+sendfax/dialin.config
%config /etc/logrotate.d/mgetty
 
%files sendfax
%defattr(644,root,root,755)
%dir /var/spool/fax
%dir /var/spool/fax/incoming
%attr(1777,root,root) %dir /var/spool/fax/outgoing
%attr(777,root,root) %dir /var/spool/fax/outgoing/locks

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
%{_libdir}/mgetty+sendfax/cour25.pbm
%{_libdir}/mgetty+sendfax/cour25n.pbm
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
%config /etc/mgetty+sendfax/sendfax.config
%attr(600,root,root) %config /etc/mgetty+sendfax/faxrunq.config
%config /etc/mgetty+sendfax/faxheader
%config /etc/logrotate.d/sendfax

%files voice
%defattr(644,root,root,755)
%doc voice/doc/*
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
%attr(600,root,root) %config /etc/mgetty+sendfax/voice.conf

%files viewfax
%defattr(644,root,root,755)
%doc frontends/X11/viewfax-2.4/C* frontends/X11/viewfax-2.4/README.gz
%attr(755,root,root) %{_bindir}/viewfax
%dir %{_libdir}/mgetty+sendfax
%{_libdir}/mgetty+sendfax/viewfax.tif
%{_mandir}/man1/viewfax.1x*
