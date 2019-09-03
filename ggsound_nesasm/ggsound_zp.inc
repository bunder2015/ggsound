sound_region: .ds 1
sound_disable_update: .ds 1
sound_local_byte_0: .ds 1
sound_local_byte_1: .ds 1
sound_local_byte_2: .ds 1

sound_local_word_0: .ds 2
sound_local_word_1: .ds 2
sound_local_word_2: .ds 2

sound_param_byte_0: .ds 1
sound_param_byte_1: .ds 1
sound_param_byte_2: .ds 1

sound_param_word_0: .ds 2
sound_param_word_1: .ds 2
sound_param_word_2: .ds 2
sound_param_word_3: .ds 2

addr_instruments: .ds 2
addr_note_table_lo:  .ds 2
addr_note_table_hi:  .ds 2
  ifdef FEATURE_DPCM
addr_dpcm_sample_table: .ds 2
addr_dpcm_note_to_sample_index: .ds 2
addr_dpcm_note_to_sample_length: .ds 2
addr_dpcm_note_to_loop_pitch_index: .ds 2
  endif

apu_data_ready: .ds 1
apu_square_1_old: .ds 1
apu_square_2_old: .ds 1
  ifdef FEATURE_DPCM
apu_dpcm_state: .ds 1
  endif

song_list_address: .ds 2
sfx_list_address: .ds 2
song_address: .ds 2
apu_register_sets: .ds 20
