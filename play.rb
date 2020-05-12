# Playing the music with a live hollow
# To be pasted on sonic-pi

live_loop :hollow do
  use_real_time
  midi1, midi2, midi3, i= sync "/osc*/trigger/hollow"
  puts midi1
  synth :hollow, note: midi1, attack: 5, release: 5 - i
  sleep rrand(0.5, 1.5, 1, 2)
  synth :hollow, note: midi2, attack: 3, release: 5 - i
  sleep rrand(0.5, 1.5, 1, 2)
  synth :hollow, note: midi3, attack: 3, release: 5
  sleep rrand(0.5, 1.5, 1, 2)
  if one_in(3)
    synth :hollow, note: midi1 - 3, attack: 3, release: 3
  end
end