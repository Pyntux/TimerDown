install:
	install -d '$(DESTDIR)'/usr/bin/
	install -m755 TimerDown.py '$(DESTDIR)'/usr/bin/timerdown
	install -d '$(DESTDIR)'/usr/share/timerdown/
	cp -r icons/ timerdown.ico '$(DESTDIR)'/usr/share/timerdown/
	cp -r gui.py '$(DESTDIR)'/usr/share/timerdown/
	install -d '$(DESTDIR)'/usr/share/applications/
	cp TimerDown.desktop '$(DESTDIR)'/usr/share/applications/timerdown.desktop 
