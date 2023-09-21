#!/usr/bin/env python3
import jack
import argparse
import time

class MetronomeTrack:

    NOTEON = 0x9
    NOTEOFF = 0x8
    CHANNEL = 9  # MIDI channels are 0-indexed in the protocol, so channel 10 is represented as 9

    ACCENTED_VELOCITY = 127
    UNACCENTED_VELOCITY = 90

    def __init__(self, client, note, divisions, bpm, track_number):
        self.note = note
        self.divisions = divisions
        self.bpm = bpm
        self.fs = client.samplerate
        self.offset = 0
        self.current_division = 1
        self.outport = client.midi_outports.register(f'track_{track_number}')
        self.frames_per_beat = int(self.fs * 60 / self.bpm)
        self.frames_per_division = int(self.frames_per_beat / self.divisions)
        self.frames_per_note = self.frames_per_beat // 2
        self.note_off_frame = self.frames_per_beat

    def _send_note_on(self, main_outport):
        velocity = self.ACCENTED_VELOCITY if self.current_division == 1 else self.UNACCENTED_VELOCITY
        status_byte_on = (self.NOTEON << 4) + self.CHANNEL
        data_on = bytearray([status_byte_on, self.note, velocity])
        try:
            main_outport.write_midi_event(0, data_on)
        except jack.JackErrorCode as e:
            print(f"Failed to write MIDI note on event: {e}")
        self.current_division = self.current_division % self.divisions + 1

    def _send_note_off(self, main_outport):
        status_byte_off = (self.NOTEOFF << 4) + self.CHANNEL  # NOTE OFF status byte
        data_off = bytearray([status_byte_off, self.note, 0])  # Velocity for NOTE OFF is typically 0
        try:
            main_outport.write_midi_event(0, data_off)
        except jack.JackErrorCode as e:
            print(f"Failed to write MIDI note off event: {e}")

    def process(self, global_frame, frames, main_outport):
        self.outport.clear_buffer()
        for frame in range(frames):
            abs_frame = frame + global_frame
            if (frame + global_frame) % self.frames_per_division == 0:
                self._send_note_on(main_outport)
                self._send_note_on(self.outport)
            elif abs_frame == self.note_off_frame:
                self._send_note_off(main_outport)
                self._send_note_off(self.outport)

class Metronome:

    DRUM_NOTES = [
        36,  # Kick
        42,  # Closed hat
        38,  # Snare
        46,  # Open hat
        50,  # Tom (highest)
        48,  # Tom
        47,  # Tom
        45,  # Tom
        43,  # Tom
        41,  # Tom
        39   # Tom (lowest)
    ]

    def __init__(self, bpm, divisions_list):
        self.client = jack.Client('Metronome')
        self.main_outport = self.client.midi_outports.register('out')
        self.tracks = [ ]
        for idx, division in enumerate(divisions_list):
            tr = MetronomeTrack(self.client, self.DRUM_NOTES[idx], division, bpm, idx)
            self.tracks.append(tr)

        # Setting the callbacks
        self.client.set_process_callback(self.process)
        self.client.set_shutdown_callback(self.shutdown)
        self.global_frame = 0

    def process(self, frames):
        self.main_outport.clear_buffer()
        for track in self.tracks:
            track.process(self.global_frame, frames, self.main_outport)
        self.global_frame += frames

    def shutdown(self, status, reason):
        """Callback for JACK shutdown."""
        print('JACK shutdown:', reason, status)

    def start(self, port_name):
        """Start the Metronome."""
        with self.client:
            self.main_outport.connect(port_name)
            print(f'Starting metronome at {self.tracks[0].bpm} BPM on main port {port_name}. Press Ctrl+C to stop.')
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print('\nInterrupted by user')

def main():
    parser = argparse.ArgumentParser(description='polymetro: a polyrhythmic metronome with CLI and Jack server connectivity.')

    parser.add_argument('-p', '--port', dest='port_name', required=True, help='Name of the JACK MIDI output port for the main metronome')
    parser.add_argument('-b', '--bpm', type=int, required=True, help='Beats per minute')

    # Modify this line to accept between 1 and 8 values, each between 1 and 8
    parser.add_argument('-d', '--divisions', type=int, nargs='+', required=True, choices=range(1, 17), help='Divisions per beat for each track. Accepts up to 8 integers, each between 1 and 16.')

    args = parser.parse_args()

    # Ensure divisions contains no more than 8 values
    if len(args.divisions) > 8:
        parser.error("--divisions accepts a maximum of 8 values.")

    metronome = Metronome(args.bpm, args.divisions)
    metronome.start(args.port_name)

if __name__ == "__main__":
    main()