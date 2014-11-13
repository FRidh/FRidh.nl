Auralisation of aircraft noise
##############################
:date: 2013-09-26 22:59

:category: Blog
:tags: acoustics, sonorus
:slug: auralisation-of-aircraft-noise

Almost two months ago I started working at the Swiss research institute
Empa in Dübendorf, Switzerland, as part of a European Seventh Framework
project called `Sonorus`_. The project is about urban sound planning and
my task is to develop an aircraft noise simulator.  The first two months
passed really fast. It's a great place to work, and the type of work
really fits me. Obviously I began with reading a bit about the topic and
thinking how I would tackle the issues at hand. But very soon I began
with implementing the first bits and mainly prototyping what I think it
should become.

The idea is that I develop an aircraft noise simulator capable of
simulating how an aircraft pass-by sounds at a stationary receiver while
in an urban environment. This means effects like spherical spreading,
Doppler shift and reflections at the ground and facades have to be
included in the propagation model. But first it is important to obtain a
good time-frequency representation of an aircraft, and obviously these
depend on the make or type of the aircraft as well as the conditions.
Finally, the aircraft noise has to be reproduced using for example an
Ambisonics setup.

Now, there are quite some challenges here and 'unknowns' to be solved .
While I have a good idea of how I will build such a tool for
auralisation, there are many details requiring attention. An example is
how much does turbulence in the atmosphere influence the propagation?
How to simulate decorrelation? How to reproduce correct over-head
information? And quite some more questions that need answering the
coming three years :-)

.. _Sonorus: http://www.fp7sonorus.eu/
