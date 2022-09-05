Lloyd's mirror effect
#####################
:date: 2013-11-15 18:12

:category: Blog
:tags: acoustics, sonorus
:slug: lloyds-mirror-effect

When two waves are superimposed on each other it is possible that the
resultant wave has a higher or lower amplitude at certain moments in
time. This phenomenon is called interference. One classical experiment
related to interference is Lloyd's mirror. In the classical experiment,
light from a monochromatic slit source reflects from a glass surface at
a small angle. The reflected light then interferes with the direct light
from the source, forming interference fringes. This pattern is called
Lloyd's mirror effect.

In the classical experiment light is used but the same result can be
obtained using sound waves. When a sound wave is reflected from a
surface the reflected sound wave will also interfere with the direct
sound wave. This phenomenon can also be experienced with aircraft noise
due to the ground reflection. However, because an aircraft generally
(hopefully?) moves in the sky, the interference pattern changes over the
time.

Today I managed to include this effect in my aircraft auralisation
tool. The figure below shows a spectrogram of a synthesized aircraft
passage. In the spectrogram the Doppler shift can be seen as well as
many curves which represent interference fringes, the Lloyd's mirror
effect. The mirror effect is in this case solely due to the ground. Now,
since my implementation supports reflections from buildings as well, the
effect will also be obtained due to these reflections from facades,
although far less pronounced.

.. figure:: {static}/images/2013/11/mirror_effect-300x226.png
    :align: center
    :target: {static}/images/2013/11/mirror_effect.png
    
    Spectrogram of a synthesized aircraft passage showing the Doppler effect and Lloyd's mirror effect. The x-axis shows time and y-axis frequency. The color indicates sound pressure.
