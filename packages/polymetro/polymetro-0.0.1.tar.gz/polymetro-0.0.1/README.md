# polymetro

A polyrhythmic metronome with CLI and Jack audio server connectivity.

## Installation

Install `polymetro` using pip:

```bash
pip install polymetro
```

## Basic Usage

To use `polymetro`, follow the format:

```bash
polymetro -p JACK_MIDI_PORT_NAME -t TEMPO -d <int> [int int ...]
```

### Parameters:

- `-p JACK_MIDI_PORT_NAME`: The port name as shown by `jack_lsp`. For example: `fluidsynth:midi_00`.
- `-t TEMPO`: Set the tempo in measures per minute (main beat tempo).
- `-d`: Beat subdivisions. Can be one or multiple values, such as `-d 4` for 4 beats per measure. If multiple values are given, like `-d 3 4`, a 3-against-4 polyrhythm will be generated. In this scenario, the metronome will play two separate MIDI tracks, each with its own output, besides the main MIDI output.

## Example:

To generate a 3-against-4 polyrhythm at a measure tempo of 30 per minute on the port `fluidsynth:midi_00`, you'd run:

```bash
polymetro -p fluidsynth:midi_00 -t 30 -d 3 4
```

## Feedback and Contributions

Feel free to open issues or pull requests if you have suggestions, bug reports, or contributions. Your feedback is highly appreciated!

## LICENSE

This project is licensed under the terms of the LICENSE included in this repository. You can view the full license text by [clicking here](LICENSE).
