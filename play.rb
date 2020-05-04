# Playing the music with a live hollow

live_loop :hollow do
    use_real_time
    a, b = sync "/osc*/trigger/hollow"
    #  adding 50 to ensure that music stays within the audible range
    d= a.to_f + 50
    puts d
    synth :hollow, note: d, sustain: b
  end