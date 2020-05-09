# Playing the music with a live hollow
# To be pasted on sonic-pi

live_loop :hollow do
  use_real_time
  a, b, c= sync "/osc*/trigger/hollow"
  puts a
  synth :hollow, note: a, attack: 5, release: 5 - c
  sleep rrand(0.5, 1.5, 1, 2)
  synth :hollow, note: a + 3, attack: 3, release: 6 - c
  sleep rrand(0.5, 1.5, 1, 2)
  if one_in(3)
    synth :hollow, note: a + 6, attack: 3, release: 3
  end
end