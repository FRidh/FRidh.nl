Environmental sound recognition
###############################
:date: 2012-07-21 22:05

:slug: environmental-sound-recognition
:status: hidden

Laws exist regulating the amount of noise permitted in for example
residential areas. Usually, noise models are made to predict whether the
expected emissions are within regulations, and sometimes measurements
are conducted to test whether they are indeed within the limits.
However, such measurements are not always representable, sometimes
requiring long-term measurements. Besides determing whether these
immissions are within the limits, these long-term monitors could
potentially give far more useful information.

The goal of this project was to develop a system capable of classifying
sounds like aircraft, trains and cars. This could give the possibility
to determine how much the contribution is of certain classes of sounds,
e.g. how much does aircraft noise contribute to the overall noise level.

The project consisted of a literature study to machine learning
techniques and several implementations of these methods. The final
implementation was based on One-Class Support Vector Machines and was
capable of accurately classifying aircraft and trains sounds.
