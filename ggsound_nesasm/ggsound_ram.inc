stream_flags:                  .ds MAX_STREAMS
stream_note:                   .ds MAX_STREAMS
stream_note_length_lo:         .ds MAX_STREAMS
stream_note_length_hi:         .ds MAX_STREAMS
stream_note_length_counter_lo: .ds MAX_STREAMS
stream_note_length_counter_hi: .ds MAX_STREAMS
stream_instrument_index:       .ds MAX_STREAMS
stream_volume_offset:          .ds MAX_STREAMS
  ifdef FEATURE_ARPEGGIOS
stream_arpeggio_index:         .ds MAX_STREAMS
stream_arpeggio_offset:        .ds MAX_STREAMS
  endif
stream_pitch_offset:           .ds MAX_STREAMS
stream_duty_offset:            .ds MAX_STREAMS

stream_channel:                .ds MAX_STREAMS
stream_channel_register_1:     .ds MAX_STREAMS
stream_channel_register_2:     .ds MAX_STREAMS
stream_channel_register_3:     .ds MAX_STREAMS
stream_channel_register_4:     .ds MAX_STREAMS

stream_read_address_lo:        .ds MAX_STREAMS
stream_read_address_hi:        .ds MAX_STREAMS
stream_return_address_lo:      .ds MAX_STREAMS
stream_return_address_hi:      .ds MAX_STREAMS

stream_tempo_counter_lo:       .ds MAX_STREAMS
stream_tempo_counter_hi:       .ds MAX_STREAMS
stream_tempo_lo:               .ds MAX_STREAMS
stream_tempo_hi:               .ds MAX_STREAMS
