#!/usr/bin/env python27

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()

from mplayer.models import Group, Artist, Member
g1 = Group(name="Nirvana",formed="1987")
g2 = Group(name="Foo Fighters",formed="1995")

g1.save()
g2.save()

a1 = Artist(artist="Krist Novoselic")
a2 = Artist(artist="Kurt Cobain")
a3 = Artist(artist="Dave Grohl")
a4 = Artist(artist="Chris Shiflett")
a5 = Artist(artist="Nate Mendel")
a6 = Artist(artist="Taylor Hawkins")
a7 = Artist(artist="Pat Smear")

a1.save()
a2.save()
a3.save()
a4.save()
a5.save()
a6.save()
a7.save()

m1 = Member(group="1",artist="1")
m2 = Member(group="1",artist="2")
m3 = Member(group="1",artist="3")
m4 = Member(group="2",artist="3")
m5 = Member(group="2",artist="4")
m6 = Member(group="2",artist="5")
m7 = Member(group="2",artist="6")
m8 = Member(group="2",artist="7")

m1.save()
m2.save()
m3.save()
m4.save()
m5.save()
m6.save()
m7.save()
m8.save()

