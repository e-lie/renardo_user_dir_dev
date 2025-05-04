sccode = """
SynthDef.new(\\mySynth,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0|
var osc, env;
freq = In.kr(bus, 1);
freq = [freq, freq+fmod];
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;

"""

synth = SCInstrument(
    shortname="mysynth",
    fullname="Mysynth",
    description="Mysynth synth",
    code=sccode,
    arguments={}
)
