# wav-cutter

Wav-cutter is a simple python script to cut `*.wav` files.

When you want cut footage, but only from start to duration, you can use this.

## Usage

Usage: `wav-cutter <file path> <duration in seconds>`

You can push output to other file with option `--footage_dest`.

## Example

When you asterisk confbridge footage is too long, then you can cut like:

`wav-cutter confbridge-15541-1254788256.wav 2000`

Now, in working directory exist file confbridge-15541-1254788256.wav.new, duration is 2000 secends.

When you want another file name, the use --footage_dest option, like:

`wav-cutter confbridge-15541-1254788256.wav 2000 --footage_dest new.wav`
