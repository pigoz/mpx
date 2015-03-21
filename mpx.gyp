{
  'variables': {
    'PKG_CONFIG':  'pkg-config',
    'MPV_CFLAGS':  '<!(<(PKG_CONFIG) --cflags mpv)',
    'MPV_LDFLAGS': '<!(<(PKG_CONFIG) --libs mpv)',
    'MPV_INCLUDE_PATH': '<!(echo "<(MPV_CFLAGS)" | cut -c 3-)',
  },
  'targets': [
    {
      'target_name': 'mpx',
      'product_name': 'mpx',
      'type': 'executable',
      'xcode_settings': {

        'GCC_TREAT_WARNINGS_AS_ERRORS': 'YES',
        'GCC_WARN_PEDANTIC': 'YES',
        'GCC_C_LANGUAGE_STANDARD': 'c11',
        'CODE_SIGNING_REQUIRED': 'NO',

        'CONFIGURATION_BUILD_DIR': 'build/Default',
        'SWIFT_OBJC_BRIDGING_HEADER': 'src/bridge.h',

        'HEADER_SEARCH_PATHS': [
          '$(inherited)',
          '<(MPV_INCLUDE_PATH)',
        ],

        'OTHER_CFLAGS': [
          '<@(MPV_CFLAGS)',
        ],

        'OTHER_LDFLAGS': [
          '<@(MPV_LDFLAGS)',
        ]
      },

      'sources': [
        'src/ctest.c',
        'src/main.swift',
      ],
    },
  ],
}
