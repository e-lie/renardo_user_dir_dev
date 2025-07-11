sccode = """
SynthDef.new(\play1,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=1.0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, buf=0, pos=0, room=0.1|
var osc, env;
sus = sus * blur;
rate = In.kr(bus, 1);
osc=PlayBuf.ar(1, buf, (BufRateScale.ir(buf) * rate), startPos: (BufSampleRate.kr(buf) * pos));
osc=(osc * amp);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;
"""


synth = SCInstrument(
    shortname="play1",
    fullname="Play sampler mode mono",
    description="FoxDot rhytmic sampler 'play'",
    code=sccode,
    arguments={
        "dur": .5,
    }
)
