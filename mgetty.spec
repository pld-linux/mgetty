Summary: 	A getty replacement for use with data and fax modems.
Summary(pl):	Zamiennik getty dla modemów i faxmodemów.
Name: 		mgetty
Version:	1.1.20
Release:	2
Group: 		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Copyright:      distributable
Source:		ftp://ftp.leo.org/pub/comp/os/unix/networking/mgetty/mgetty1.1.20-Jan17.tar.gz
Patch0: 	mgetty-config.patch
Patch1: 	mgetty-makekvg.patch
Patch2: 	mgetty-policy.patch
Patch3: 	mgetty-echo.patch
Patch4: 	mgetty-logrotate.patch
Patch5: 	mgetty-imakefile.patch
Patch6: 	mgetty-xref.patch
Patch7: 	mgetty-install.patch
Patch8:		mgetty-manpages.patch
Patch9:		mgetty-info.patch
BuildPrereq:	tetex
BuildPrereq:	texinfo
BuildPrereq:	groff
Prereq:		/sbin/install-info
Requires: 	libgr-progs
Buildroot: 	/tmp/%{name}-%{version}-root

%description
The mgetty package contains a "smart" getty which allows logins over a
serial line (i.e., through a modem).  If you're using a Class 2 or 2.0
modem, mgetty can receive faxes.  If you also need to send faxes, you'll
need to install the sendfax program.

If you'll be dialing in to your system using a modem, you should install
the mgetty package.  If you'd like to send faxes using mgetty and your
modem, you'll need to install the mgetty-sendfax program.  If you need a
viewer for faxes, you'll also need to install the mgetty-viewfax package.

%description -l pl
Pakiet mgetty zawiera "m±dry" getty, który pozwala na po³±czenia przez
linie szeregowe (tj. przez modem). Je¶li twój modem obs³uguje standard
Class 2 lub 2.0, mgetty mo¿e odbieraæ faksy. Je¶li potrzebujesz równie¿ 
wysy³aæ faksy, musisz zainstalowaæ program sendfax.

Je¶li bêdziesz siê ³±czy³ ze swoim systemem u¿ywaj±c modemu, powiniene¶
zainstalowaæ pakiet mgetty. Je¶li chcesz wysy³aæ faksy u¿ywaj±c mgetty,
musisz zainstalowaæ pakiet mgetty-sendfax. Je¶li potrzebujesz przegl±darki 
otrzymanych faksów, musisz równie¿ zainstalowaæ pakiet mgetty-viewfax.

%package sendfax
Summary: 	Provides support for sending faxes over a modem.
Summary(pl):	Umozliwia wysy³anie faksów przez modem.
Group:          Applications/Communications
Group(pl):      Aplikacje/Komunikacja
Requires:       %{name} = %{version}

%description sendfax
Sendfax is a standalone backend program for sending fax files.  The
mgetty program (a getty replacement for handling logins over a serial
line) plus sendfax will allow you to send faxes through a Class 2 modem.

If you'd like to send faxes over a Class 2 modem, you'll need to install
the mgetty-sendfax and the mgetty packages.

%description -l pl sendfax
Sendfax jest samodzielnym programem do wysy³ania faksów. Program mgetty 
(zamiennik getty dla przyjmowania po³±czeñ przez linie szeregowe) + sendfax
pozwol± ci na wysy³anie faksów w standardzie Class 2.

Je¶li chcia³by¶ wysy³aæ faksy przez modem obs³uguj±cy standard Class 2, 
musisz zainstalowaæ pakiety: mgetty-sendfax i mgetty.

%package voice
Summary: 	A program for using your modem and mgetty as an answering machine.
Summary(pl):	Program pozwalaj±cy na wykorzystanie mgetty i modemu jako automatycznej sekretarki.
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

%description -l pl voice
Pakiet mgetty-voice zawiera system vgetty, który zezwala mgetty i twojemu
modemowi na obs³ugê g³osu. Mówi±c krótko, vgetty pozwala twojemu modemowi 
pracowaæ jako automatyczna sekretarka. To, jak dobrze bêdzie ten system 
dzia³a³, zale¿y od tego, czy twój modem obs³uguje tego rodzaju funkcje.

Zainstaluj mgetty-voice razem z mgetty, je¶li chcia³by¶ przemieniæ swój
modem w automatyczn± sekretarkê.

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

%patch0 -p1 
%patch1 -p1 
%patch2 -p1
%patch3 -p1 
%patch4 -p1 
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
make "RPM_OPT_FLAGS=$RPM_OPT_FLAGS"
cd voice
make "RPM_OPT_FLAGS=$RPM_OPT_FLAGS"

cd ../frontends/X11/viewfax-2.4
xmkmf
make depend
make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{var/spool,sbin}

make prefix=$RPM_BUILD_ROOT/usr spool=$RPM_BUILD_ROOT/var/spool \
	CONFDIR=$RPM_BUILD_ROOT/etc/mgetty+sendfax install

install -s callback/callback $RPM_BUILD_ROOT/usr/sbin
install -s callback/ct $RPM_BUILD_ROOT/usr/bin

mv -f $RPM_BUILD_ROOT/usr/sbin/mgetty $RPM_BUILD_ROOT/sbin

# this conflicts with efax
mv -f $RPM_BUILD_ROOT/usr/man/man1/fax.1 $RPM_BUILD_ROOT/usr/man/man1/mgetty_fax.1

# voice mail extensions
install -d $RPM_BUILD_ROOT/var/spool/voice/{messages,incoming}

make prefix=$RPM_BUILD_ROOT/usr spool=$RPM_BUILD_ROOT/var/spool \
	CONFDIR=$RPM_BUILD_ROOT/etc/mgetty+sendfax install -C voice

mv -f $RPM_BUILD_ROOT/usr/sbin/vgetty $RPM_BUILD_ROOT/sbin
install voice/voice.conf-dist $RPM_BUILD_ROOT/etc/mgetty+sendfax/voice.conf

make DESTDIR=$RPM_BUILD_ROOT install -C frontends/X11/viewfax-2.4
make DESTDIR=$RPM_BUILD_ROOT install.man -C frontends/X11/viewfax-2.4

install -d $RPM_BUILD_ROOT/etc/logrotate.d
install logrotate.mgetty $RPM_BUILD_ROOT/etc/logrotate.d/mgetty
install logrotate.sendfax $RPM_BUILD_ROOT/etc/logrotate.d/sendfax

# make the html documenatation
texi2html -monolithic doc/mgetty.texi


gzip -9nf $RPM_BUILD_ROOT/usr/man/{man1,man4,man5,man8}/* \
	$RPM_BUILD_ROOT/usr/info/* \
	FAQ BUGS ChangeLog README.1st THANKS doc/*.txt mgetty.html \
	frontends/X11/viewfax-2.4/C* frontends/X11/viewfax-2.4/README \
	voice/doc/* doc/modems.db
gzip -9rnf samples/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/mgetty.info.gz /etc/info-dir

%preun
if [ "$1" = 0 ]; then
	/sbin/install-info --delete /usr/info/mgetty.info.gz /etc/info-dir
fi

%files
%defattr(644,root,root,755)
%doc {FAQ,BUGS,ChangeLog,README.1st,THANKS}.gz doc/modems.db.gz
%doc samples doc/*.txt.gz mgetty.html.gz
%attr(700,root,root) /sbin/mgetty
/usr/man/man8/mgetty.8.gz
/usr/man/man8/callback.8.gz
/usr/man/man8/faxrunqd.8.gz
/usr/man/man4/mgettydefs.4.gz
/usr/info/mgetty.info-2.gz
/usr/info/mgetty.info-3.gz
/usr/info/mgetty.info-4.gz
/usr/info/mgetty.info.gz
/usr/info/mgetty.info-1.gz
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

%attr(755,root,root) /usr/bin/kvg
%attr(755,root,root) /usr/bin/newslock
%attr(755,root,root) /usr/bin/g3cat
%attr(755,root,root) /usr/bin/g32pbm
%attr(755,root,root) /usr/bin/pbm2g3
%attr(755,root,root) /usr/bin/faxspool
%attr(700,root,root) /usr/bin/faxrunq
%attr(755,root,root) /usr/bin/faxq
%attr(755,root,root) /usr/bin/faxrm
%attr(4711,root,root) /usr/bin/ct
%attr(700,root,root) /usr/sbin/sendfax
%attr(700,root,root) /usr/sbin/faxrunqd
%attr(700,root,root) /usr/sbin/callback
%dir /usr/lib/mgetty+sendfax
/usr/lib/mgetty+sendfax/cour25.pbm
/usr/lib/mgetty+sendfax/cour25n.pbm
/usr/man/man1/g32pbm.1.gz
/usr/man/man1/pbm2g3.1.gz
/usr/man/man1/g3cat.1.gz
/usr/man/man1/mgetty_fax.1.gz
/usr/man/man1/faxspool.1.gz
/usr/man/man1/faxrunq.1.gz
/usr/man/man1/faxq.1.gz
/usr/man/man1/faxrm.1.gz
/usr/man/man1/coverpg.1.gz
/usr/man/man5/faxqueue.5.gz
/usr/man/man8/sendfax.8.gz
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
%attr(755,root,root) /usr/bin/vm
%attr(755,root,root) /usr/bin/pvfamp
%attr(755,root,root) /usr/bin/pvfcut
%attr(755,root,root) /usr/bin/pvfecho
%attr(755,root,root) /usr/bin/pvffile
%attr(755,root,root) /usr/bin/pvffft
%attr(755,root,root) /usr/bin/pvfmix
%attr(755,root,root) /usr/bin/pvfreverse
%attr(755,root,root) /usr/bin/pvfsine
%attr(755,root,root) /usr/bin/pvfspeed
%attr(755,root,root) /usr/bin/pvftormd
%attr(755,root,root) /usr/bin/rmdtopvf
%attr(755,root,root) /usr/bin/rmdfile
%attr(755,root,root) /usr/bin/pvftovoc
%attr(755,root,root) /usr/bin/voctopvf
%attr(755,root,root) /usr/bin/pvftolin
%attr(755,root,root) /usr/bin/lintopvf
%attr(755,root,root) /usr/bin/pvftobasic
%attr(755,root,root) /usr/bin/basictopvf
%attr(755,root,root) /usr/bin/pvftoau
%attr(755,root,root) /usr/bin/autopvf
%attr(755,root,root) /usr/bin/pvftowav
%attr(755,root,root) /usr/bin/wavtopvf

/usr/man/man1/zplay.1.gz
/usr/man/man1/pvf.1.gz
/usr/man/man1/pvfamp.1.gz
/usr/man/man1/pvfcut.1.gz
/usr/man/man1/pvfecho.1.gz
/usr/man/man1/pvffile.1.gz
/usr/man/man1/pvffft.1.gz
/usr/man/man1/pvfmix.1.gz
/usr/man/man1/pvfreverse.1.gz
/usr/man/man1/pvfsine.1.gz
/usr/man/man1/pvfspeed.1.gz
/usr/man/man1/pvftormd.1.gz
/usr/man/man1/rmdtopvf.1.gz
/usr/man/man1/rmdfile.1.gz
/usr/man/man1/pvftovoc.1.gz
/usr/man/man1/voctopvf.1.gz
/usr/man/man1/pvftolin.1.gz
/usr/man/man1/lintopvf.1.gz
/usr/man/man1/pvftobasic.1.gz
/usr/man/man1/basictopvf.1.gz
/usr/man/man1/pvftoau.1.gz
/usr/man/man1/autopvf.1.gz
/usr/man/man1/pvftowav.1.gz
/usr/man/man1/wavtopvf.1.gz
%attr(600,root,root) %config /etc/mgetty+sendfax/voice.conf

%files viewfax
%defattr(644,root,root,755)
%doc frontends/X11/viewfax-2.4/C* frontends/X11/viewfax-2.4/README.gz
%attr(755,root,root) /usr/bin/viewfax
%dir /usr/lib/mgetty+sendfax
/usr/lib/mgetty+sendfax/viewfax.tif
/usr/man/man1/viewfax.1x.gz

%changelog
* Sun Apr  4 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.1.20-2]
- removed mgetty-strip.patch,
- changed install procedure to allow building from non-root account
  (mgetty-install.patch),
- removed "strip $RPM_BUILD_ROOT/usr/bin/*" in %install (binary files 
  are already striped during installation and we don't want to strip 
  shell scripts, do we?),
- removed "find samples -type f -exec chmod 644 {} \;" in %install
  (permissions are set in %files now),
- added full %defattr description and %attr macros in %files,
- simplifications in %install,
- added gzipping documentation and man pages,
- added -f (and -r) to gzip parameters,
- fixed creating man pages (mgetty-manpages.patch),
- added info entry (mgetty-info.patch),
- standarized {un}registering info pages,
- added pl translation,
- changed Buildoot to /tmp/%%{name}-%%{version}-root,
- added BuildPrereq: tetex, texinfo, groff (needed to build manuals 
  and documentation),
- cosmetic changes for common l&f.

* Thu Mar 18 1999 Cristian Gafton <gafton@redhat.com>
- version 1.1.20
- cleaned the spec file of subshells
- updated spec file

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- rebuild for glibc 2.1

* Sat Aug 22 1998 Jos Vos <jos@xos.nl>
- Use a patch for creating policy.h using policy.h-dist.
- Add viewfax subpackage (X11 fax viewing program).
- Add logrotate config files for mgetty and sendfax log files.
- Properly define ECHO in Makefile for use with bash.
- Add optional use of dialin.config (for modems supporting this).
- Change default notification address to "root" (was "faxadmin").
- Change log file names according to better defaults.
- Change default notify program to /etc/mgetty+sendfax/new_fax (was
  /usr/local/bin/new_fax).

* Fri Aug 21 1998 Jeff Johnson <jbj@redhat.com>
- add faxrunqd man page (problem #850)
- add missing pbm2g3 (and man page); remove unnecessary "rm -f pbmtog3"
- delete redundant ( cd tools; make ... )

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- updated to 1.1.14
- AutoPPP patch
 
* Thu Dec 18 1997 Mike Wangsmo <wanger@redhat.com>
- added more of the documentation files to the rpm

* Wed Oct 29 1997 Otto Hammersmith <otto@redhat.com>
- added install-info support

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- updated version

* Wed Oct 15 1997 Erik Troan <ewt@redhat.com>
- now requires libgr-progs instead of netpbm

* Mon Aug 25 1997 Erik Troan <ewt@redhat.com>
- built against glibc
