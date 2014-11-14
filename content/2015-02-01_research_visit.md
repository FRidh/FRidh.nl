Title: Research visit to Chalmers
Date: 2015-02-01
Tags: acoustics, work, sonorus

After the ASA meeting in Indianapolis I went to Gothenburg again for a research 
visit. As I wrote in my previous post it was strange to be there again. Last 
spring I visited Gothenburg for just a couple of days, but now, staying for 
seven weeks again is quite different. You start noticing quite a lot of things 
have changed. Many people I knew there have moved away and I also noticed a 
couple of restaurants I visited have closed since. Despite those things it was nice meeting old friends again.

So, as I wrote in the title I went there on a research visit. The main reason 
for my visit was to attend some courses at Chalmers but to also work on my 
research. Initially the idea was to investigate further the model we're 
developing to deal with atmospheric turbulence in aircraft auralisations. 
However, in the end the courses took more time then I expected, so I didn't 
really get to work on the turbulence model anymore. However, I did manage to 
implement one nice part of the auralisation tool, namely support for Ambisonics. 

Besides Chalmers I also visited SP in Borås. SP was a familar place for me as 
well since I did an 
[internship]({filename}/pages/thermoacoustic-refrigerator.rst) there in 2010. 
Earlier I had made recordings with a SoundField microphone, however, at Empa we 
do not have an Ambisonics setup. SP has a listening room with a third order 
Ambisonics system, giving me the possibility to listen to the first order 
recording as well as to higher order auralisations. 

One visit I met up with Peter Lundén who installed the system. After some problem solving we managed to 
get both the recordings and auralisations working. Unfortunately there was one 
problem with the auralisations, somehow halfway the aircraft makes a U-turn. 
While I haven't checked it any further, I think it is due to 
the inclusion of the [Condon-Shortley phase](http://en.wikipedia.org/wiki/Ambisonic_data_exchange_formats#Polarity) 
in the [function](http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.special.sph_harm.html) I used to calculate the spherical harmonics.
