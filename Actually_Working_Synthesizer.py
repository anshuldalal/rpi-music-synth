# IMPORTING LIBRARIES
import RPi.GPIO as GPIO
from gpiozero import PWMLED, MCP3008
import pygame
import time

# INITIALIZING
GPIO.setmode(GPIO.BCM)
pygame.mixer.init()
pygame.mixer.get_init()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# ORGANIZING SAMPLE FILE PATHS

sax_oct1 = [
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_3/AltoSax.F3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_3/AltoSax.Gb3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_3/AltoSax.G3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_3/AltoSax.Ab3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_3/AltoSax.A3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_3/AltoSax.Bb3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_3/AltoSax.B3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_4/AltoSax.C4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_4/AltoSax.Db4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_4/AltoSax.D4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_4/AltoSax.Eb4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_4/AltoSax.E4.wav"
    ]

sax_oct2 = [
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_4/AltoSax.F4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_4/AltoSax.Gb4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_4/AltoSax.G4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_4/AltoSax.Ab4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_4/AltoSax.A4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_4/AltoSax.Bb4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_4/AltoSax.B4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_5/AltoSax.C5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_5/AltoSax.Db5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_5/AltoSax.D5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_5/AltoSax.Eb5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Alto_Sax_WAV/AltoSax_Oct_5/AltoSax.E5.wav"
    ]

bells_oct1 = [
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_5/bells.F5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_5/bells.Gb5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_5/bells.G5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_5/bells.Ab5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_5/bells.A5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_5/bells.Bb5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_5/bells.B5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_6/bells.C6.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_6/bells.Db6.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_6/bells.D6.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_6/bells.Eb6.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_6/bells.E6.wav"
    ]


bells_oct2 = [
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_6/bells.F6.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_6/bells.Gb6.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_6/bells.G6.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_6/bells.Ab6.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_6/bells.A6.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_6/bells.Bb6.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_6/bells.B6.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_7/bells.C7.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_7/bells.Db7.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_7/bells.D7.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_7/bells.Eb7.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Bells_WAV/Bells_Oct_7/bells.E7.wav"
    ]


clarinet_oct1 = [
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_3/BbClarinet.F3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_3/BbClarinet.Gb3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_3/BbClarinet.G3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_3/BbClarinet.Ab3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_3/BbClarinet.A3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_3/BbClarinet.Bb3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_3/BbClarinet.B3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_4/BbClarinet.C4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_4/BbClarinet.Db4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_4/BbClarinet.D4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_4/BbClarinet.Eb4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_4/BbClarinet.E4.wav"
                  ]

clarinet_oct2 = [
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_4/BbClarinet.F4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_4/BbClarinet.Gb4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_4/BbClarinet.G4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_4/BbClarinet.Ab4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_4/BbClarinet.A4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_4/BbClarinet.Bb4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_4/BbClarinet.B4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_5/BbClarinet.C5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_5/BbClarinet.Db5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_5/BbClarinet.D5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_5/BbClarinet.Eb5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Clarinet_WAV/BbClarinet_Oct_5/BbClarinet.E5.wav"
    ]

flute_oct1 = [
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_4/Flute.F4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_4/Flute.Gb4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_4/Flute.G4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_4/Flute.Ab4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_4/Flute.A4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_4/Flute.Bb4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_4/Flute.B4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_5/Flute.C5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_5/Flute.Db5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_5/Flute.D5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_5/Flute.Eb5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_5/Flute.E5.wav"
    ]

flute_oct2 = [
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_5/Flute.F5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_5/Flute.Gb5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_5/Flute.G5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_5/Flute.Ab5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_5/Flute.A5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_5/Flute.Bb5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_5/Flute.B5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_6/Flute.C6.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_6/Flute.Db6.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_6/Flute.D6.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_6/Flute.Eb6.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Flute_WAV/Flute_Oct_6/Flute.E6.wav"
    ]

marimba_oct1 = [
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_3/Marimba.F3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_3/Marimba.Gb3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_3/Marimba.G3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_3/Marimba.Ab3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_3/Marimba.A3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_3/Marimba.Bb3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_3/Marimba.B3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_4/Marimba.C4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_4/Marimba.Db4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_4/Marimba.D4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_4/Marimba.Eb4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_4/Marimba.E4.wav"
    ]

marimba_oct2 = [
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_4/Marimba.F4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_4/Marimba.Gb4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_4/Marimba.G4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_4/Marimba.Ab4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_4/Marimba.A4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_4/Marimba.Bb4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_4/Marimba.B4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_5/Marimba.C5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_5/Marimba.Db5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_5/Marimba.D5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_5/Marimba.Eb5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Marimba_WAV/Marimba_Oct_5/Marimba.E5.wav"
    ]


trumpet_oct1 = [
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_3/Trumpet.F3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_3/Trumpet.Gb3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_3/Trumpet.G3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_3/Trumpet.Ab3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_3/Trumpet.A3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_3/Trumpet.Bb3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_3/Trumpet.B3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_4/Trumpet.C4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_4/Trumpet.Db4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_4/Trumpet.D4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_4/Trumpet.Eb4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_4/Trumpet.E4.wav"
    ]

trumpet_oct2 = [
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_4/Trumpet.F4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_4/Trumpet.Gb4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_4/Trumpet.G4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_4/Trumpet.Ab4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_4/Trumpet.A4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_4/Trumpet.Bb4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_4/Trumpet.B4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_5/Trumpet.C5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_5/Trumpet.Db5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_5/Trumpet.D5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_5/Trumpet.Eb5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Trumpet_WAV/Trumpet_Oct_5/Trumpet.E5.wav"
    ]

tuba_oct1 = [
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_1/Tuba.F1.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_1/Tuba.Gb1.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_1/Tuba.G1.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_1/Tuba.Ab1.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_1/Tuba.A1.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_1/Tuba.Bb1.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_1/Tuba.B1.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_2/Tuba.C2.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_2/Tuba.Db2.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_2/Tuba.D2.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_2/Tuba.Eb2.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_2/Tuba.E2.wav"
    ]

tuba_oct2 = [
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_2/Tuba.F2.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_2/Tuba.Gb2.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_2/Tuba.G2.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_2/Tuba.Ab2.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_2/Tuba.A2.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_2/Tuba.Bb2.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_2/Tuba.B2.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_3/Tuba.C3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_3/Tuba.Db3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_3/Tuba.D3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_3/Tuba.Eb3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Tuba_WAV/Tuba_Oct_3/Tuba.E3.wav",
    ]

vibes_oct1 = [
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_3/Vibraphone.F3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_3/Vibraphone.Gb3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_3/Vibraphone.G3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_3/Vibraphone.Ab3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_3/Vibraphone.A3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_3/Vibraphone.Bb3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_3/Vibraphone.B3.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_4/Vibraphone.C4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_4/Vibraphone.Db4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_4/Vibraphone.D4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_4/Vibraphone.Eb4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_4/Vibraphone.E4.wav"
    ]

vibes_oct2 = [
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_4/Vibraphone.F4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_4/Vibraphone.Gb4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_4/Vibraphone.G4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_4/Vibraphone.Ab4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_4/Vibraphone.A4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_4/Vibraphone.Bb4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_4/Vibraphone.B4.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_5/Vibraphone.C5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_5/Vibraphone.Db5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_5/Vibraphone.D5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_5/Vibraphone.Eb5.wav",
    "/home/cobbler/synth_samples/Samples_WAV/Vibraphone_WAV/Vibraphone_Oct_5/Vibraphone.E5.wav"
    ]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# list nesting: index by octave (0-1), then note (0-11), then instrument (0-7)

oct1_list = [
    [sax_oct1[0], bells_oct1[0], clarinet_oct1[0], flute_oct1[0], marimba_oct1[0], trumpet_oct1[0], tuba_oct1[0], vibes_oct1[0]],
    [sax_oct1[1], bells_oct1[1], clarinet_oct1[1], flute_oct1[1], marimba_oct1[1], trumpet_oct1[1], tuba_oct1[1], vibes_oct1[1]],
    [sax_oct1[2], bells_oct1[2], clarinet_oct1[2], flute_oct1[2], marimba_oct1[2], trumpet_oct1[2], tuba_oct1[2], vibes_oct1[2]],
    [sax_oct1[3], bells_oct1[3], clarinet_oct1[3], flute_oct1[3], marimba_oct1[3], trumpet_oct1[3], tuba_oct1[3], vibes_oct1[3]],
    [sax_oct1[4], bells_oct1[4], clarinet_oct1[4], flute_oct1[4], marimba_oct1[4], trumpet_oct1[4], tuba_oct1[4], vibes_oct1[4]],
    [sax_oct1[5], bells_oct1[5], clarinet_oct1[5], flute_oct1[5], marimba_oct1[5], trumpet_oct1[5], tuba_oct1[5], vibes_oct1[5]],
    [sax_oct1[6], bells_oct1[6], clarinet_oct1[6], flute_oct1[6], marimba_oct1[6], trumpet_oct1[6], tuba_oct1[6], vibes_oct1[6]],
    [sax_oct1[7], bells_oct1[7], clarinet_oct1[7], flute_oct1[7], marimba_oct1[7], trumpet_oct1[7], tuba_oct1[7], vibes_oct1[7]],
    [sax_oct1[8], bells_oct1[8], clarinet_oct1[8], flute_oct1[8], marimba_oct1[8], trumpet_oct1[8], tuba_oct1[8], vibes_oct1[8]],
    [sax_oct1[9], bells_oct1[9], clarinet_oct1[9], flute_oct1[9], marimba_oct1[9], trumpet_oct1[9], tuba_oct1[9], vibes_oct1[9]],
    [sax_oct1[10], bells_oct1[10], clarinet_oct1[10], flute_oct1[10], marimba_oct1[10], trumpet_oct1[10], tuba_oct1[10], vibes_oct1[10]],
    [sax_oct1[11], bells_oct1[11], clarinet_oct1[11], flute_oct1[11], marimba_oct1[11], trumpet_oct1[11], tuba_oct1[11], vibes_oct1[11]],
    ]

oct2_list = [
    [sax_oct2[0], bells_oct2[0], clarinet_oct2[0], flute_oct2[0], marimba_oct2[0], trumpet_oct2[0], tuba_oct2[0], vibes_oct2[0]],
    [sax_oct2[1], bells_oct2[1], clarinet_oct2[1], flute_oct2[1], marimba_oct2[1], trumpet_oct2[1], tuba_oct2[1], vibes_oct2[1]],
    [sax_oct2[2], bells_oct2[2], clarinet_oct2[2], flute_oct2[2], marimba_oct2[2], trumpet_oct2[2], tuba_oct2[2], vibes_oct2[2]],
    [sax_oct2[3], bells_oct2[3], clarinet_oct2[3], flute_oct2[3], marimba_oct2[3], trumpet_oct2[3], tuba_oct2[3], vibes_oct2[3]],
    [sax_oct2[4], bells_oct2[4], clarinet_oct2[4], flute_oct2[4], marimba_oct2[4], trumpet_oct2[4], tuba_oct2[4], vibes_oct2[4]],
    [sax_oct2[5], bells_oct2[5], clarinet_oct2[5], flute_oct2[5], marimba_oct2[5], trumpet_oct2[5], tuba_oct2[5], vibes_oct2[5]],
    [sax_oct2[6], bells_oct2[6], clarinet_oct2[6], flute_oct2[6], marimba_oct2[6], trumpet_oct2[6], tuba_oct2[6], vibes_oct2[6]],
    [sax_oct2[7], bells_oct2[7], clarinet_oct2[7], flute_oct2[7], marimba_oct2[7], trumpet_oct2[7], tuba_oct2[7], vibes_oct2[7]],
    [sax_oct2[8], bells_oct2[8], clarinet_oct2[8], flute_oct2[8], marimba_oct2[8], trumpet_oct2[8], tuba_oct2[8], vibes_oct2[8]],
    [sax_oct2[9], bells_oct2[9], clarinet_oct2[9], flute_oct2[9], marimba_oct2[9], trumpet_oct2[9], tuba_oct2[9], vibes_oct2[9]],
    [sax_oct2[10], bells_oct2[10], clarinet_oct2[10], flute_oct2[10], marimba_oct2[10], trumpet_oct2[10], tuba_oct2[10], vibes_oct2[10]],
    [sax_oct2[11], bells_oct2[11], clarinet_oct2[11], flute_oct2[11], marimba_oct2[11], trumpet_oct2[11], tuba_oct2[11], vibes_oct2[11]],
    ]

sample_list = [oct1_list, oct2_list] # combines the octave lists for indexing

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# CREATING CUSTOM CLASSES

# lists GPIO port numbers for the 12 push buttons, which will be referenced by each object
Push_Button_List = [7, 1, 4, 17, 27, 22, 14, 15, 18, 23, 24, 25]

for i in Push_Button_List:	# turn each port for momentary push buttons into an input
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


class Push_Button(object):	# creating a special class for push buttons to instance
    
    def __init__(self, name, pin, current_state, old_state):
        """
        Creates the attribute spaces for the pin number, GPIO input state, and old GPIO state.
        Each will apply to all future instances.
    
        attr:
        'name' gives the string name of the instance.
        'pin' gives its GPIO pin number.
        'current_state' shows its current 1/0 value.
        'old_state' shows this value from the previous pass.
        """
        self.name = name
        self.pin = pin
        self.current_state = current_state
        self.old_state = old_state


# creating all 12 push button instances
push_1 = Push_Button("push_1", Push_Button_List[0], 0, 0)
push_2 = Push_Button("push_2", Push_Button_List[1], 0, 0)
push_3 = Push_Button("push_3", Push_Button_List[2], 0, 0)
push_4 = Push_Button("push_4", Push_Button_List[3], 0, 0)
push_5 = Push_Button("push_5", Push_Button_List[4], 0, 0)
push_6 = Push_Button("push_6", Push_Button_List[5], 0, 0)
push_7 = Push_Button("push_7", Push_Button_List[6], 0, 0)
push_8 = Push_Button("push_8", Push_Button_List[7], 0, 0)
push_9 = Push_Button("push_9", Push_Button_List[8], 0, 0)
push_10 = Push_Button("push_10", Push_Button_List[9], 0, 0)
push_11 = Push_Button("push_11", Push_Button_List[10], 0, 0)
push_12 = Push_Button("push_12", Push_Button_List[11],0, 0)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Rot_Switch_List = [0, 5, 6, 13, 26, 19, 20, 21]

for j in Rot_Switch_List:	# turn each port for the rotary switch into an input
    GPIO.setup(j, GPIO.IN)

class Rot_Spot(object):	# creating a special class for position of the rotary switch to instance
    
    def __init__(self, name, pin, current_state, old_state):
        
        self.name = name
        self.pin = pin
        self.current_state = current_state
        self.old_state = old_state


rot_pos_1 = Rot_Spot("rot_pos_1", Rot_Switch_List[0], 0, 0)
rot_pos_2 = Rot_Spot("rot_pos_2", Rot_Switch_List[1], 0, 0)
rot_pos_3 = Rot_Spot("rot_pos_3", Rot_Switch_List[2], 0, 0)
rot_pos_4 = Rot_Spot("rot_pos_4", Rot_Switch_List[3], 0, 0)
rot_pos_5 = Rot_Spot("rot_pos_5", Rot_Switch_List[4], 0, 0)
rot_pos_6 = Rot_Spot("rot_pos_6", Rot_Switch_List[5], 0, 0)
rot_pos_7 = Rot_Spot("rot_pos_7", Rot_Switch_List[6], 0, 0)
rot_pos_8 = Rot_Spot("rot_pos_8", Rot_Switch_List[7], 0, 0)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Tog_Switch_List = [16, 12]	# GPIO Number for each side of the momentary toggle switch

for k in Tog_Switch_List:	# turn each port for the toggle switch into an input
    GPIO.setup(k, GPIO.IN)
    
class Tog_Switch(object):	# creating a special class for each side of the toggle to instance
    
    def __init__(self, name, pin, current_state, old_state):
        self.name = name
        self.pin = pin
        self.current_state = current_state
        self.old_state = old_state


tog_up = Tog_Switch("tog_up", Tog_Switch_List[0], 0, 0)
tog_down = Tog_Switch("tog_down", Tog_Switch_List[1], 0, 0)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# assigns the channel for the Analog-to-Digital Converter for each slide (0-3) and the rotary (4)
pot_channel_0 = MCP3008(0)
pot_channel_1 = MCP3008(1)
pot_channel_2 = MCP3008(2)
pot_channel_3 = MCP3008(3)
pot_channel_4 = MCP3008(4)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# COMPONENT SCANNING

def Check_Switch(button):	# defines a function to check a digital part
    """
    Takes the custom pushbutton class to pull variables from.
    Updates 'current_state' from GPIO Input.
    Debounces (only returns value if 'current_state' does NOT match 'old_state').
    
    : param button: contains the button name, pin, current, and old state.
    """
    # print(button.pin)
    button.current_state = GPIO.input(button.pin)
    # print(button.current_state)
    if button.current_state != button.old_state:
        # print("old: {}".format(button.old_state))
        button.old_state = button.current_state	# update old state
        return button.current_state
        # print("{}: currently {}".format(button.name, button.current_state))
        # print("old state  is now: {}".format(button.old_state))
        # print("{}: currently {}".format(button.name, button.current_state))


def Check_Potentiometer(pot, pot_nbr):	# defines a function to check either a rotary or slide potentiometer
    """
    Updates 'pot_value' from the value outputted by the MCP3008 from 0-1.
    Drops values under 0.01 down to 0 and lifts values above 0.99 up to 1.
    Returns the 'pot_value' from 0-1; does NOT flip the value.
    
    :param pot: The potentiometer channel number.
    :param pot_nbr: The identifying counter for the potentiometer.
    """
    pot_value = pot.value
    if (pot_value < 0.01):	# display that the pot is off when channel 0 is close to "off"
        # print("Pot #{} value: 0".format(pot_nbr))
        pot_value = 0.000
        return pot_value
    elif (pot_value > 0.99):
        pot_value = 1.000
        return pot_value
    else:
        return pot_value


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# DECLARATIONS

octave = 0
octave_min = 0
octave_max = 1

instrument = 1

volume = 0.5
pot_loops = 0
loops = 0
maxtime = 1000
fade_in = 0
fade_out = 0


pygame.mixer.set_num_channels(12)

# creates channels 0-11
channel0 = pygame.mixer.Channel(0)
channel1 = pygame.mixer.Channel(1)
channel2 = pygame.mixer.Channel(2)
channel3 = pygame.mixer.Channel(3)
channel4 = pygame.mixer.Channel(4)
channel5 = pygame.mixer.Channel(5)
channel6 = pygame.mixer.Channel(6)
channel7 = pygame.mixer.Channel(7)
channel8 = pygame.mixer.Channel(8)
channel9 = pygame.mixer.Channel(9)
channel10 = pygame.mixer.Channel(10)
channel11 = pygame.mixer.Channel(11)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# OUTPUT FUNCTION

def play_sound(octave: int, note: int, instrument: int, channel, loops: int, maxtime: int, fade_in: int, fade_out: int, volume: float):
    """
    Takes arguments given when called or as global variables.
    Finds the sample file path; narrows by octave, then note, then instrument using earlier nested lists.
    Applies sample path to local variable 'sound'.
    Sets the channel volume. Sets the fade-out time of the sample.
    Plays the sound with the integer number of loops, integer maxtime of the sample in ms, and the integer fade-in time in ms.
    
    :param octave: Takes the octave number selected by the toggle as a global variable.
    :param note: Takes the note based on which button is pushed.
    :param instrument: Takes the instrument counter from the rotary switch as a global variable.
    :param channel: Takes the assigned channel number, between 1 and 12.
    :param loops: Takes the integer count of sampling loops between 1 and 5 from Potentiometer 0.
    :param maxtime: Takes the integer max time of the sample from Potentiometer 1.
    :param fade_in: Takes the integer fade-in time from Potentiometer 2.
    :param fade_out: Takes the integer fade-out time from Potentiometer 3.
    :param volume: Takes the floating volume between 0 and 1 from Potentiometer 4.
    """
    print("oct: {}, note: {}, instrument: {}".format(octave, note, instrument))
    path = sample_list[octave][note][instrument]
    print(path)
    sound = pygame.mixer.Sound(path)
    channel.set_volume(volume)
    print(channel.get_volume())
    channel.fadeout(fade_out)
    channel.play(sound, loops, maxtime, fade_in)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# MAIN ROUTINE

try:	# continue until exception of Keyboard Interrupt, Ctrl + C
    while True: # loop the routine continuously
        # """
        if Check_Switch(push_1) == 1:
            play_sound(octave, 0, instrument, channel0, loops, maxtime, fade_in, fade_out, volume)
        if Check_Switch(push_2) == 1:
            play_sound(octave, 1, instrument, channel1, loops, maxtime, fade_in, fade_out, volume)
        if Check_Switch(push_3) == 1:
            play_sound(octave, 2, instrument, channel2, loops, maxtime, fade_in, fade_out, volume)
        if Check_Switch(push_4) == 1:
            play_sound(octave, 3, instrument, channel3, loops, maxtime, fade_in, fade_out, volume)
        if Check_Switch(push_5) == 1:
            play_sound(octave, 4, instrument, channel4, loops, maxtime, fade_in, fade_out, volume)
        if Check_Switch(push_6) == 1:
            play_sound(octave, 5, instrument, channel5, loops, maxtime, fade_in, fade_out, volume)
        if Check_Switch(push_7) == 1:
            play_sound(octave, 6, instrument, channel6, loops, maxtime, fade_in, fade_out, volume)
        if Check_Switch(push_8) == 1:
            play_sound(octave, 7, instrument, channel7, loops, maxtime, fade_in, fade_out, volume)
        if Check_Switch(push_9) == 1:
            play_sound(octave, 8, instrument, channel8, loops, maxtime, fade_in, fade_out, volume)
        if Check_Switch(push_10) == 1:
            play_sound(octave, 9, instrument, channel9, loops, maxtime, fade_in, fade_out, volume)
        if Check_Switch(push_11) == 1:
            play_sound(octave, 10, instrument, channel10, loops, maxtime, fade_in, fade_out, volume)
        if Check_Switch(push_12) == 1:
            play_sound(octave, 11, instrument, channel11, loops, maxtime, fade_in, fade_out, volume)
        # """
        # """
        if Check_Switch(rot_pos_1) == 1:	# if position 1 is up, update 'instrument'
            instrument = 0
        if Check_Switch(rot_pos_2) == 1:
            instrument = 1
        if Check_Switch(rot_pos_3) == 1:
            instrument = 2
        if Check_Switch(rot_pos_4) == 1:
            instrument = 3
        if Check_Switch(rot_pos_5) == 1:
            instrument = 4
        if Check_Switch(rot_pos_6) == 1:
            instrument = 5
        if Check_Switch(rot_pos_7) == 1:
            instrument = 6
        if Check_Switch(rot_pos_8) == 1:
            instrument = 7
        # """
        # """
        if Check_Switch(tog_up) == 1: # Check if the switch is toggled up
            if octave < octave_max:	# if the octave is less than the maximum octave, add 1
                octave += 1
        if Check_Switch(tog_down) == 1:	# Check if the switch is toggled down
            if octave > octave_min:	# if the octave is more than the minimum octave, subtract 1
                octave -= 1
        # """

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        # """
        pot_loops = Check_Potentiometer(pot_channel_0, 0) * 5	# takes 1-0 from pot 4 and flips it; multiply by 5
        # print("floating loops: {}".format(pot_loops))
        loops = int(pot_loops)	# turn floating 'pot_loops' into integer 'loops'
        # print("loops: {}".format(loops))

        maxtime = int(Check_Potentiometer(pot_channel_1, 1) * 1000)	# takes 1-0 from pot 2 and flips it; multiply by 1000 ms
        # print("maxtime: {}".format(maxtime))

        fade_in = int(Check_Potentiometer(pot_channel_2, 2) * 1000)
        # print("fade in: {}".format(fade_in))
        
        fade_out = int(Check_Potentiometer(pot_channel_3, 3) * 1000)
        # print("fade out: {}".format(fade_out))
        
        volume = Check_Potentiometer(pot_channel_4, 4)	# takes volume from 0 to 1 from rotary pot
        # print("volume: {}".format(volume))
        # """

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        time.sleep(0.1)	# short delay between cycles
        
except KeyboardInterrupt:	# jumps out of the loop when Ctrl + C is hit.
    pygame.mixer.music.stop()	# stops all channels and quits out of pygame mixer
    pygame.mixer.quit()
    GPIO.cleanup	#resets all GPIOs for safety