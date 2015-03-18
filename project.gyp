{
  'targets': [
    {
      'target_name': 'pureia',
      'product_name': 'pureia',
      'type': 'executable',
      # 'mac_bundle': 1,
      'xcode_settings': {
        # 'INFOPLIST_FILE': 'resources/Info.plist',
        'CODE_SIGNING_REQUIRED': 'NO',
        'CONFIGURATION_BUILD_DIR':'build/Default',
      },
      'sources': [
        'src/main.swift',
      ],
    },
  ],
}
