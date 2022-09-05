Modelling a turbulent atmosphere
################################
:date: 2013-12-11 10:35

:category: Blog
:tags: acoustics, sonorus
:slug: modelling-a-turbulent-atmosphere

When listening to an aircraft flying over, you can hear that the level
and spectral contents fluctuate somewhat. These fluctuations are due to
turbulence in the atmosphere, affecting the sound generation (variable
load on engines) and the sound propagation. In order to create a
plausible auralisation of aircraft noise these fluctuations have to be
accounted for.

Turbulent flow can be modeled as a superposition of a spectrum of
fluctuations and eddies upon a mean flow. A common approach for noise
predictions methods to include the effects of atmospheric turbulence is
to use a statistical approach; generate many random 'frozen' turbulence
fields, calculate for each of these how sound propagates through them
and then average your results. The 'frozen' fields represent snapshots
in time of how the atmosphere could look like. These snapshots are
calculated based on a spectrum of fluctuations. Well known descriptions
of these spectra are the Gaussian and von Karman spectra.

The figure belows shows a portion of two turbulence spectra.

.. figure:: {static}/images/2013/12/Gaussian2DTempWind_and_VonKarman2DTempWind_spectral_density-300x225.png
    :align: center
    :target: {static}/images/2013/12/Gaussian2DTempWind_and_VonKarman2DTempWind_spectral_density.png
    
    Gaussian and Von Karman spectral densities as function of wavenumber.

A random turbulence field is created by the superposition of modes. The
figure below shows the amplitude of these modes as function of
wavenumber.

.. figure:: {static}/images/2013/12/salomons_figure_J1-300x225.png
    :align: center
    :target: {static}/images/2013/12/salomons_figure_J1.png
    
    Gaussian and Von Karman mode amplitudes as function of wavenumber.

And finally a figure showing the refractive-index fluctuation. The field
is generated using a Von Karman spectrum and 200 modes.

.. figure:: {static}/images/2013/12/VonKarman2DTempWind_field-300x225.png
    :align: center
    :target: {static}/images/2013/12/VonKarman2DTempWind_field.png
    
    Von Karmann refractive-index field.
